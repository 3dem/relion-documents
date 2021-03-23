.. _sec_sta_preprocessing:

Preprocessing
=============


Getting organised
-----------------

We recommend to create a single directory per project, i.e. per structure you want to determine.
We'll call this the project directory. **It is important to always launch the RELION graphical user-interface (GUI) from the project directory.** Inside the project directory you should make a separate directory to store all your Imod reconstructed tomograms folder.
We like to call this directory ``tomograms/``. Inside, we should find the different tomograms in folders like ``TS_1`` or ``TS_01``.
If for some reason you do not want to place your movies inside the |RELION| project directory, then inside the project directory you can also make a symbolic link to the directory where your reconstructed tomograms are stored.

|RELION| uses the original tilt series stack prior to tilt axis alignment and imports the alignment data from Imod. The tomogram folder should contain: a stack file, with extension ``.st``, ``.mrc`` or ``mrcs``; a ``newst.com`` and ``tilt.com`` script files, where the transformation and tilt angles filenames are obtained from, together with tomogram dimensions, offsets and excluded views.

When you unpacked the tutorial test data, the (``Movies/``) directory was created.
It should contain 24 movies in compressed TIFF format, a gain-reference file (``gain.mrc``) and a ``NOTES`` file with information about the experiment.

We will start by launching the |RELION| GUI.
As said before, this GUI always needs to be launched from the project directory.
To prevent errors with this, the GUI will ask for confirmation the first time you launch it in a new directory.
Make sure you are inside the project directory, and launch the GUI by typing:

::

    relion --tomo&


and answer ``Yes`` when prompted to set up a new |RELION| project here.

The first thing to do is to import the set of recorded micrograph movies into the pipeline.
Select ``Import`` from the job-type browser on the left, and fill in the following parameters on the :guitab:`Movies/mics` tab:

:Import raw movies/micrographs?: Yes

:Raw input files:: Movies/\*.tiff

:Are these multi-frame movies?: Yes

     (Set this to ``No`` if these are single-frame micrographs)

:Optics group name:: opticsGroup1

     (This field can be used to divide the data set into multiple optics groups: separately import each optics group with its own name, and then use the ``Join star files`` jobtype to combine the groups.

:MTF of the detector:: mtf\_k2\_200kV.star

:Pixel size (Angstrom):: 0.885

:Voltage (kV):: 200

:Spherical aberration (mm):: 1.4

:Amplitude contrast:: 0.1

:Beamtilt in X (mrad):: 0

:Beamtilt in Y (mrad):: 0


On the :guitab:`Others` tab, make sure the following is set:

:Import other node types?: No


You may provide a meaningful alias (for example: `movies`) for this job in the white field named ``Current job: Give_alias_here``.
Clicking the :runbutton:`Run!` button will launch the job.
A directory called ``Import/job001/`` will be created, together with a symbolic link to this directory that is called ``Import/movies``.
Inside the newly created directory a :textsc:`star` file with all the movies is created.
Have a look at it using:

::

    less Import/job001/movies.star


If you had extracted your particles in a different software package, then instead of going through the Preprocessing steps below, you would use the same :jobtype:`Import` job-type to import particles :textsc:`star` file, 3D references, 3D masks, etc.
Note that this is NOT the recommended way to run |RELION|, and that the user is responsible for generating correct :textsc:`star` files.

.. _sec_motioncorrection:

Beam-induced motion correction
------------------------------

The :jobtype:`Motion correction` job-type implements |RELION|'s own (CPU-based) implementation of the UCSF |MotionCor2| program for convenient whole-frame movie alignment, as well as a wrapper to the (GPU-based) |MotionCor2| program itself :cite:`zheng_motioncor2:_2017`.
Besides executing the calculations on the CPU/GPU, there are three other differences between the two implementations:

- :jobtype:`Bayesian polishing` (for per-particle motion-correction; see :ref:`this section <sec_bayesian_polishing>`) can only read local motion tracks from our own implementation;
- The |MotionCor2| program performs outlier-pixel detection on-the-fly, and this information is not conveyed to :jobtype:`Bayesian polishing`, which may result in unexpectedly bad particles after polishing;
- Our own implementation can write out the sum of power spectra over several movie frames, which can be passed directly into |CTFFIND4.1| for faster CTF-estimation.

For these three reasons, we now favour running our own implementation.

On the :guitab:`I/O` tab set:

:Input movies STAR file:: Import/job001/movies.star

     (Note that the :button:`Browse` button will only list movie :textsc:`star` files.)

:First frame for corrected sum:: 1

:Last frame for corrected sum:: 0

     (This will result in using all movie frames.)

:Dose per frame (e/A2): 1.277

:Pre-exposure (e/A2): 0

:EER fractionation: 32

    (This option will be ignored for TIFF files.)

:Do dose-weighting?: Yes

:Save non-dose-weighted as well?: No

     (In some cases non-dose-weighted micrographs give better CTF estimates.
     To save disk space, we're not using this option here as the data are very good anyway.)

:Save sum of power spectra?: Yes

:Sum of power spectra every e/A2:: 4

     (This seems to be a good value according to measurements by Greg McMullan and Richard Henderson.)


Fill in the :guitab:`Motion` tab as follows:

:Bfactor:: 150

     (use larger values for super-resolution movies)

:Number of patches X,Y: 5 5

:Group frames:: 1

:Binning factor:: 1

     (we often use 2 for super-resolution movies)

:Gain-reference image:: Movies/gain.mrc

     (This can be used to provide a gain-reference file for on-the-fly gain-reference correction.
     This is necessary in this case, as these movies are not yet gain-corrected.)

:Gain rotation:: No rotation (0)

:Gain flip:: No flipping (0)

:Defect file:: \

     (This can be used to mask away broken pixels on the detector.
     Formats supported in our own implementation and in UCSF |MotionCor2| are either a text file in UCSF |MotionCor2| format (each line contains four numbers: x, y, width and height of a defect region); or a defect map (an image in MRC or TIFF format, where 0=good and 1=bad pixels).
     The coordinate system is the same as the input movie before application of binning, rotation and/or flipping. **Note that defect text files produced by SerialEM are NOT supported!** However, one can convert a SerialEM-style defect file into a defect map using :textsc:`imod`.)

:Use RELION's own implementation?: Yes

     (this reduces the requirement to install the UCSF implementation.
     If you have the UCSF program installed anyway, you could also use that one.
     In that case, you also need to fill in the options below.)


Fill in the :guitab:`Running` tab as follows:

:Number of MPI procs:: 1

     (Assuming you're running this tutorial on a local computer)

:Number of threads:: 12

     (As these movies are 24 frames, each thread will do two movie frames)

:Submit to queue?: No

     (Again, assuming you're running this tutorial on a local computer)


Executing this program takes approximately 5 minutes when using 12 threads on a reasonably modern machine.
Note that our own implementation of the |MotionCor2| algorithm does not use a GPU.
It is however multi-threaded.
As each thread will work independently on a movie frame, it is optimal to use a number of threads such that the number of movie frames divided by the number threads is an integer number.
As these movies have 24 frames, using 12 threads will result in 2 frames being processed by each thread.
You can look at the estimated beam-induced shifts, and their statistics over the entire data set, by selecting the ``out: logfile.pdf`` from the :button:`Display:` button below the run buttons, or you can look at the summed micrographs by selecting `out: corrected_micrographs.star`.
Depending on the size of your screen, you should probably downscale the micrographs (``Scale: 0.3``) and use ``Sigma contrast: 3`` and few columns (something like ``Number of columns: 3``) for convenient visualisation.
Note that you cannot select any micrographs from this display.
If you want to exclude micrographs at this point (which we will not do, because they are all fine), you could use the :jobtype:`Subset selection` job-type.


CTF estimation
--------------

Next, we will estimate the CTF parameters for each corrected micrograph.
You can use the :jobtype:`CTF estimation` job-type as a wrapper to Kai Zhang's :textsc:`gctf` to execute on the GPU, or you can also use Alexis Rohou and Niko Grigorieff's |CTFFIND4.1| to execute efficiently on the CPU.
We now prefer |CTFFIND4.1|, as it is the only open-source option, and because it allows reading in the movie-averaged power spectra calculation by |RELION|'s own implementation of the |MotionCor2| algorithm.
Fill in the settings as follows:

On the :guitab:`I/O`:

:Input micrographs STAR file:: Motioncorr/job002/corrected_micrographs.star

     (You can again use the :button:`Browse` button to select the `corrected_micrographs.star` file of the :jobtype:`Motion correction` job.)

:Use micrograph without dose-weighting?: No

     (These may have better Thon rings than the dose-weighted ones, but we decided in the previous step not to write these out)

:Estimate phase shifts?: No

     (This is only useful for phase-plate data)

:Amount of astigmatism (A):: 100

     (Assuming your scope was reasonably well aligned, this value will be suitable for many data sets.)


On the :guitab:`CTFFIND-4.1` tab, set:

:Use CTFFIND-4.1?: Yes

:CTFFIND-4.1 executable:: /wherever/it/is/ctffind.exe

:Use power spectra from MotionCorr job?: Yes

     (We can use these, as we told |RELION|'s own implementation of the |MotionCor2| algorithm to write these out in the previous section.)

:Use exhaustive search?: No

     (In difficult cases, the slower exhaustive searches may yield better results.
     For these data, this is not necessary.)

:Estimate CTF on window size (pix): -1

     (If a positive value is given, a squared window of this size at the center of the micrograph will be used to estimate the CTF.
     This may be useful to exclude parts of the micrograph that are unsuitable for CTF estimation, e.g. the labels at the edge of photographic film. )

:FFT box size (pix):: 512

:Minimum resolution (A):: 30

:Maximum resolution (A):: 5

:Minimum defocus cvalue (A):: 5000

:Maximum defocus cvalue (A):: 50000

:Defocus step size (A):: 500


On the :guitab:`Gctf` tab, make sure the option to use :textsc:`gctf` instead is set to No.
On the :guitab:`Running` tab, use six MPI processes to process the 24 micrographs in parallel.
This took less than 10 seconds on our machine.
Once the job finishes there are additional files for each micrograph inside the output ``CtfFind/job003/Movies`` directory: the ``.ctf`` file contains an image in `MRC` format with the computed power spectrum and the fitted CTF model; the ``.log`` file contains the output from :textsc:`ctffind` or :textsc:`gctf`; (only in case of using :textsc:`ctffind`, the `.com` file contains the script that was used to launch :textsc:`ctffind`).

You can visualise all the Thon-ring images using the :button:`Display` button, selecting ``out: micrographs_ctf.star``.
The zeros between the Thon rings in the experimental images should coincide with the ones in the model.
Note that you can sort the display in order of defocus, maximum resolution, figure-of-merit, etc.
The ``logfile.pdf`` file contains plots of useful parameters, such as defocus, astigmatism, estimated resolution, etc for all micrographs, and histograms of these values over the entire data set.
Analysing these plots may be useful to spot problems in your data acquisition.

If you see CTF models that are not a satisfactory fit to the experimental Thon rings, you can delete the ``.log`` files for those micrographs, select the ``CtfFind/job003`` entry from the :joblist:`Finished jobs` list, alter the parameters in the parameter-panel, and then re-run the job by clicking the :button:`Continue!` button.
Only those micrographs for which a ``.log`` file does not exist will be re-processed.
You can do this until all CTF models are satisfactory.
If this is not possible, or if you decide to discard micrographs because they have unsatisfactory Thon rins, you can use the :jobtype:`Subset selection` job-type to do this.


