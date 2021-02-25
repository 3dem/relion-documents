Movie Compression
=================

This page describes how to compress CryoEM movies to save disk spaces and reduce I/O loads.


Falcon3 / Falcon4
-----------------

Falcon3 and Falcon4 output images in 16-bit integers.
Gain normalization is always applied and cannot be disabled.

In the counting mode, an electron is not rendered as a single 1 but seems to be placed as a blob of 3x3 pixels that sum to 100.
This is probably to reduce noise aliasing from frequencies higher than the Nyquist frequency.

Below is an example from Falcon3.
You can see three electrons.
Two electrons have overlapping tails::

    0  0  0  0  0  0  0  0  0  0  0
    0  0  3  7  1  0  0  0  0  0  0
    0  0 15 42 11 16  4  0  0  0  0
    0  0  6 15 14 44 11  3  7  1  0
    0  0  0  0  2  7  2 15 42  7  0
    0  0  0  0  0  0  0  6 15  3  0
    0  0  0  0  0  0  0  0  0  0  0


Because of this feature, Falcon3 and Falcon4 movies do not compress well.
Typically, one can reduce the size to about 50 to 60 % of the original movie by TIFF with the **deflate filter** (also called zip filter).
The LZW filter is faster but gives larger files.


Falcon4 EER
-----------

EER (Electron Event Representation) is a new movie format for Falcon4.
It records electron events at the detector's physical frame rate (248 Hz).
The file size is typically smaller than MRC, but can be larger than fractionated TIFF from Falcon4.

The location of events is stored in a 4x super-resolution grid (i.e.
16K x 16K pixels).
RELION renders an electron as a single dot in a 4K or 8K grid.
By rendering in a 8K grid and then Fourier cropping to a 4K grid, you can remove noise beyond the (physical) Nyquist frequency.
If you directly render in a 4K grid, the noise aliases back and slightly lowers the DQE.
However, this effect is very tiny in practice and the resolution rarely changes.
One possibility is to start processing at 4K and coarse slicing and then switch to 8K and finer slicing in Polish to save processing time and memory (see below).

.. note::
    As of RELION 3.1.1, 8K rendering can create artifacts around defect lines.
    Thus, we do not recommend 8K rendering.


To process an EER dataset, proceed as follows.
This feature needs RELION >= 3.1.1.

1.  Decide how many (internal) frames to group into a fraction.

    For example, if you have 1000 internal frames and group them by 30, you will get 33 fractions.
    The remaining 10 (= 1000 - 30 * 33) frames will be ignored.
    Too fine slicing leads to very slow processing and out of memory errors.

2.  Calculate how many e/A2 each fraction has.

    Fractionate such that each fraction has about 0.5 to 1.25 e/A2.
    You can change this later.

3.  Import EER files as usual.

    Use the physical pixel size for 4K rendering. **For 8K rendering, the pixel size should be half of the physical size.**


4.  Run motion correction.

    - Specify the value decided in the step 1 to ``EER fractionation``.
    - Specify the dose rate calculated in step 2.
    - Specify the gain reference.
    - ``Group frames`` in the GUI **must be 1** regardless of what you choose in step 1.
    - ``Binning factor`` should be 2 to bring a 8K super resolution grid into a 4K physical grid by Fourier cropping.
        Otherwise, set it to 1.
    - Add ``--eer_upsampling 2`` if you work in a 8K grid.
      The default is 4K, that is, ``--eer_upsampling 1``.


If you want to change the rendering mode (4K or 8K) and/or the fractionation before Polish, you have to modify the trajectory STAR files produced by a MotionCorr job.
Use ``scripts/eer_trajectory_handler.py``::

    python3 /path/to/eer_trajectory_handler.py --i MotionCorr/job002/corrected_micrographs.star --o up2_gr8 --resample 2 --regroup 8

will change the sampling to 8K and the fractionation to 8 frames.
The output will be ``MotionCorr/job002/corrected_micrographs_up2_gr8.star``, which should be specified to a Polish job.
Note that the extraction box size for Polish is in pixels of the rendered movie.

The gain reference for EER is different from multiplicative gain references for K2/K3.
When the movie is in EER format, RELION will **divide** raw pixel values with the provided gain.
When the gain is zero, the pixel is considered as defective.
The gain reference can be 8K x 8K or 4K x 4K.
If the size of the gain reference and the size requested by ``--eer_upsampling`` do not match, the gain reference is upsampled / downsampled.

If memory usage is a concern, consider building RELION in CPU single precision (``cmake -DDoublePrec_CPU=OFF``).

Another useful tool is ``relion_convert_to_tiff``, which renders an EER movie into a compressed integer TIFF.
You can render in 4K or 8K (``--eer_upsampling``) with specified fractionation (``--eer_grouping``).
Due to the different meanings of the gain reference for EER and TIFF, you have to take the inverse of the EER gain reference before processing the resulting TIFF files.
The tool performs this conversion when the EER gain reference is specified in the ``--gain`` option.


Gatan K2 / K3 in counting or super-resolution mode
--------------------------------------------------

Gain non-normalised movies
^^^^^^^^^^^^^^^^^^^^^^^^^^

Always use the gain **non-normalised** mode.
Then the images represent electron counts and consist of mostly 0s, a few 1s, fewer 2s, even fewer 3s and so on.
Below is an example::

    1  0  0  0  0  0  0  0
    0  1  0  3  1  1  0  2
    1  0  0  1  0  1  0  0
    2  1  0  0  0  0  0  1
    0  2  0  1  0  0  0  0


Such images compress extremely well by TIFF with the **LZW filter**.
The deflate filter is much slower and gives larger files.

SerialEM can directly write compressed TIFF movies.
EPU cannot write movies in TIFF but in integer (8 bit for counting mode, 4 bit for super-resolution mode) MRC, which can be converted to TIFF later.

Update: According to Grigory Sharov at MRC-LMB, TIFF output is available in EPU >=2.4 for K3 and EPU >=2.9 with TEM server >=7.6 (requires Windows 10) for K2.

Gain normalised movies
^^^^^^^^^^^^^^^^^^^^^^

The gain reference looks like below::

    1.149962  1.083618  1.198896  1.140650  1.159426  1.063172  1.204020  1.145287
    1.075346  1.122473  1.173919  1.149962  1.159426  1.051271  1.178831  1.071257
    1.043484  1.009823  1.109215  1.100549  1.183784  1.100549  1.126962  0.978266
    1.193816  1.047363  1.246640  1.214399  1.193816  1.067199  1.051271  0.999080
    1.131488  1.159426  1.304355  1.051271  1.035811  1.131488  0.974881  0.988563


If you save movies in the gain normalised mode, the electron counts are multiplied by this to yield::

    1.149962  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000
    0.000000  1.122473  0.000000  3.449886  1.159426  1.051271  0.000000  2.142514
    1.043484  0.000000  0.000000  1.100549  0.000000  1.100549  0.000000  0.000000
    2.387632  1.047363  0.000000  0.000000  0.000000  0.000000  0.000000  0.999080
    0.000000  2.318852  0.000000  1.051271  0.000000  0.000000  0.000000  0.000000


Now, values are 32-bit floating points, which hardly compress.

If we *knew* the gain reference, we could divide pixel values by the gain to bring them back to integers.
However, the gain reference is not written in the gain normalised mode.
Fortunately, there is a way to reliably estimate the gain reference.

Consider a particular pixel and look at the values over many frames.
The values should be integer multiples of its gain, for example::

    0.000000  2.21843  0.0000000  1.109215  0.000000  0.000000  1.109215  3.327645  0.000000 ...


Thus, we can estimate the gain by finding the greatest common divisor among these values.
Since the dose rate of counting mode movies is very low (otherwise, you will have coincidence losses), it is highly probable that the list contains an observation corresponding to one electron.
Thus, one simply needs to find the smallest **positive** value and use it as the gain for this pixel.
In this case, it is 1.109215.

There is one complication.
Digital Micrograph applies defect correction when working in the gain normalised mode.
Values of such pixels are no longer integer multiples of their gain and the above trick does not work.
For such pixels, one can keep the original values and set the gain to 1.000000.
Then gain multiplication does not modify such pixels.
The output remains 32bit floating point numbers, not integers, but since most values are 0.000000, 1.000000, 2.000000, 3.000000, etc except for defect pixels, the entropy is smaller than the input and compression is more efficient.

relion_convert_to_tiff
----------------------

The command ``relion_convert_to_tiff`` implements above compression schemes.

For Falcon3, Falcon4, gain non-normalised K2/K3 images, the usage is very simple::

    relion_convert_to_tiff --i movies.star --o Converted/

The STAR file needs only the ``rlnMicrographMovieName`` column.
You can also specify a list file ``.lst`` that contains movie names without any STAR headers.

When the input is from Falcon detectors, judged by the width being 4096 pixels, it applies deflate compression at level 6.
Otherwise, LZW compression is performed.
This default can be overridden by ``--compression`` and ``--deflate_level`` arguments.
By default, ``relion_convert_to_tiff`` treats all rows in a frame as one TIFF strip to improve the compression ratio.
This can be disabled by ``--line_by_line`` option.

``--only_do_unfinished`` allows conversion of only new files.
The program writes to a temporary file and renames it to ``.tif`` only after all frames have been written.
Thus, killing a program in the middle is safe.

In contrast to `mrc2tif <https://bio3d.colorado.edu/imod/doc/man/mrc2tif.html>`_ command from the IMOD suite, ``relion_convert_to_tiff`` does not support thread parallelization to compress one movie with many cores.
However, one can use MPI parallelization as::

    mpirun -np 24 relion_convert_to_tiff_mpi --i movies.star --o Converted/ # 24 processes

to process many movies simultaneously.

.. note::
    In MRC-LMB computer cluster, you should run the above command after booking a full CPU node by ``qlogin -l dedicated=24``.
    Note that our cluster nodes cannot access ``/teraraid*``.
    If your movies are there, you have to run conversion on ``max``, ``hex`` or ``hal`` (be considerate to others by reducing the number of processes!).


Gain estimation
^^^^^^^^^^^^^^^

To compress gain normalised K2 movies, one has to first estimate the gain *used during data collection*.
Note that this gain is different from what ``relion_estimate_gain`` estimates.

::

    relion_convert_to_tiff --i movies.star --o Converted/ --estimate_gain

This prints a row per frame::


    Processing Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 000 #Changed    7673083 #Mismatch          0, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 001 #Changed    4549992 #Mismatch      80676, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 002 #Changed    2743457 #Mismatch      89580, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 003 #Changed    1670936 #Mismatch      77997, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 004 #Changed    1028044 #Mismatch      59783, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 005 #Changed     638637 #Mismatch      44309, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 006 #Changed     399216 #Mismatch      30629, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 007 #Changed     251807 #Mismatch      21201, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 008 #Changed     159379 #Mismatch      15021, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 009 #Changed     101211 #Mismatch      10315, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 010 #Changed      64619 #Mismatch       7191, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 011 #Changed      41322 #Mismatch       5089, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 012 #Changed      26191 #Mismatch       3789, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 013 #Changed      16901 #Mismatch       2901, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 014 #Changed      10994 #Mismatch       2284, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 015 #Changed       7170 #Mismatch       1885, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 016 #Changed       4538 #Mismatch       1613, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 017 #Changed       2980 #Mismatch       1446, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 018 #Changed       1913 #Mismatch       1349, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 019 #Changed       1273 #Mismatch       1293, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 020 #Changed        859 #Mismatch       1256, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 021 #Changed        554 #Mismatch       1206, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 022 #Changed        344 #Mismatch       1232, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 023 #Changed        243 #Mismatch       1188, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 024 #Changed        169 #Mismatch       1189, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 025 #Changed        107 #Mismatch       1195, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 026 #Changed         79 #Mismatch       1182, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 027 #Changed         60 #Mismatch       1206, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 028 #Changed         53 #Mismatch       1187, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 029 #Changed         39 #Mismatch       1177, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 030 #Changed         37 #Mismatch       1165, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 031 #Changed         30 #Mismatch       1199, #Negative          0, #Unreliable   14238980 /   14238980
     Original/FoilHole_7230495_Data_7226082_7226083_20181209_0240-40759.mrc Frame 032 #Changed         23 #Mismatch       1185, #Negative          0, #Unreliable   14238980 /   14238980

As explained above, the program finds smallest positive numbers for each pixel over many frames.
``#Changed`` is the number of pixels whose minimum value is updated.
``#Mismatch`` is the number of pixels whose value in the frame is not an integer multiple of the current gain estimate.
This happens when (1) the pixel is defective and Digital Micrograph applied correction or (2) the estimated gain is not correct (for example, the current minimum corresponds to two electrons and the frame contains three electrons).

``#Unreliable`` is the number of pixels whose gain estimate is still unreliable.
A pixel is considered to be reliable when values which are integer multiples of the current gain estimate were observed at least ``--thresh`` times (default 50) without being interrupted by mismatch.

After processing several hundreds frames, the values should become stable.
The number of mismatches fluctuates.
The number of unreliable pixels is usually 1000 to 5000 in most K2 detectors.

::

    Processing Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 000 #Changed          0 #Mismatch       1216, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 001 #Changed          0 #Mismatch       1203, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 002 #Changed          0 #Mismatch       1199, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 003 #Changed          0 #Mismatch       1199, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 004 #Changed          0 #Mismatch       1192, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 005 #Changed          0 #Mismatch       1210, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 006 #Changed          0 #Mismatch       1186, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 007 #Changed          0 #Mismatch       1219, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 008 #Changed          0 #Mismatch       1224, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 009 #Changed          0 #Mismatch       1197, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 010 #Changed          0 #Mismatch       1202, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 011 #Changed          0 #Mismatch       1176, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 012 #Changed          0 #Mismatch       1197, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 013 #Changed          0 #Mismatch       1196, #Negative          0, #Unreliable       1346 /   14238980
     Original/FoilHole_7232574_Data_7226091_7226092_20181209_2221-42294.mrc Frame 014 #Changed          0 #Mismatch       1204, #Negative          0, #Unreliable       1346 /   14238980

Now you can stop the program by pressing ``Ctrl-C``.
The program updates ``gain_estimate.bin`` and ``gain_estimate_reliability.bin`` every movie.

To perform actual compression, specify ``gain_estimate.bin`` as ``--gain`` option::

    relion_convert_to_tiff --i movies.star --o Converted/ --gain Converted/gain_estimate.bin

The program writes not only TIFF movies but also ``gain-reference.mrc``, which should be used for subsequent data processing.


Practical considerations
^^^^^^^^^^^^^^^^^^^^^^^^

If you updated the gain reference in Digital Micrograph during data collection, you have to divide your dataset into two and estimate gain separately.

Some pixels are cold pixels and emit 0 most of the time.
Thus, it is very rare to observe values corresponding to one electron.
If you terminate gain estimation too early, such pixels are flagged as unreliable.
This is safe, because values of unreliable pixels are always written as they are with the gain value of 1.0000.

If the program never observes an event corresponding to one electron but only events corresponding to two or four electrons during gain estimation, the program mistakenly considers the value for two electrons as the gain and still flags the pixel as reliable.
If the program encounters an event corresponding to one or three electrons during compression, which is not multiple of the estimated gain, the program emits an error and terminates.
In this case, you have to re-run gain estimation from more frames and repeat compression **from the beginning**.
Fortunately, such situation is highly unlikely; because the pixel values are Poisson distributed and the dose rate is low, you observes an event corresponding to one electron frequently.
When the dose rate is high, the probability for one-electron events is lower, but the distribution becomes also wider.
This means that you observe neighbouring values (e.g.
two-, three- and four-electron events) with similar frequencies.
In other words, it is unlikely to observe many two- and four-electron events without observing any three-electron events.
Because three is not divisible by two, this pixel remains flagged as unreliable.
The ``--ignore_error`` option forces the program to continue by rounding non-conforming values but this leads to change of pixel values.

Defective pixels do not carry much information.
If we round them to nearest integers, the output can be saved as integers, not floating point numbers, and the compression ratio will improve.
Since the number of defects are very small (1000 to 5000 out of 14 million pixels in K2) and their values are not very accurate anyway, such a slightly-lossy compression scheme probably do not hurt the resolution.
Implementation and verification of such a strategy is on our TODO list.

Examples
--------

Compression rates depend on dose.
Fewer electrons typically lead to better compression.

Falcon 3 counting
^^^^^^^^^^^^^^^^^

`FoilHole_24156969_Data_24154827_24154828_20170425_0847_Fractions.tif <ftp://ftp.ebi.ac.uk/empiar/world_availability/10309/data/Movies/FoilHole_24156969_Data_24154827_24154828_20170425_0847_Fractions.tif>`_ from `EMPIAR-10309 <https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10309/>`_ (A2a receptor).
The deposited file is already in TIFF, but decompressed to 16 bit integer MRC for testing.
4096 x 4096 pixels, 75 frames, 16 bit integer, mean = 36.644 (e.g. 0.36 e/px/frame)

*   16 bit integer MRC: 2,516,583,424
*   IMOD mrc2tif, lzw: 1,583,972,550 (62.9 %)
*   IMOD mrc2tif, zip level 6: 1,432,846,496 (56.9 %)
*   IMOD mrc2tif, zip level 9: 1,432,820,192 (56.9 %)
*   relion_convert_to_tiff, auto = zip level 6: 1,337,873,325 (53.2 %)
*   bzip2: 1,067,277,634 (42.4 %)

Note that bzip2 gives a smaller file but you cannot process them directly in RELION; you have to decompress them before processing.

K2 counting, gain normalised from EPU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`FoilHole_12404830_Data_12400523_12400524_20181213_1058-251321.mrc <ftp://ftp.ebi.ac.uk/empiar/world_availability/10317/data/Micrographs/FoilHole_12404830_Data_12400523_12400524_20181213_1058-251321.mrc>`_ from `EMPIAR-10317 <https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10317/>`_ (ABC transporter).
3838 x 3710 pixels, 40 frames, 32 bit floating point from EPU, mean = 1.45

*   32 bit floating point MRC: 2,278,237,824
*   IMOD mrc2tif, lzw: 1,554,985,144 (68.3 %)
*   IMOD mrc2tif, zip level 6: 1,274,226,678 (55.9 %)
*   bzip2: 739,204,755 (32.4 %)
*   relion_convert_to_tiff after gain estimation: 270,856,741 (11.9 %)

1502 pixels were marked as unreliable.

Also note that it would have been 569560224 bytes (25 %) in gain non-normalised 8-bit integer MRC even before compression.

K2 counting, gain non-normalised from EPU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`FoilHole_2491648_Data_2484494_2484495_20190505_2224-167458.mrc <ftp://ftp.ebi.ac.uk/empiar/world_availability/10340/data/Movies/Case3/FoilHole_2491648_Data_2484494_2484495_20190505_2224-167458.tif>`_ from `EMPIAR-10340 <https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10340/>`_ (tau filaments).
3838 x 3710 pixels, 48 frames, 8 bit integers from EPU, mean = 0.96

*   8 bit integer MRC: 683,472,064
*   IMOD mrc2tif, zip level 6: 205,103,218 (30.0 %)
*   IMOD mrc2tif, lzw: 193,826,068 (28.4 %)
*   relion_convert_to_tiff, auto = lzw: 190,200,465 (27.8 %)
*   bzip2: 189,773,107 (27.8 %)

By saving in the gain non-normalised mode, the integer MRC file is one forth the size of the floating point MRC file (32 / 8 = 4).
LZW compression further reduces the size.
