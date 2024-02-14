.. _sec_sta_ctfestimation:

CTF Estimation
=================

Next, we will estimate the CTF parameters for each motion-corrected image of the five tilt series.
We will use Alexis Rohou and Niko Grigorieff’s CTFFIND-4.1 because it gives excellent results and allows reading in the movie-averaged power spectra calculation by RELION’s own implementation of the MotionCor2 algorithm. 

Select the :jobtype:`CTF estimation` job type in the job-type browser and fill in the following parameters on the :guitab:`I/O` tab:

:Input tilt series: MotionCorr/job002/corrected_tilt_series.star

:Estimate phase shifts?: No

   (Estimating phase shifts option is only useful for phase plate data)

:Amount of astigmatism (A): 100

   (This number is suitable for most data sets on reasonably well aligned microscopes.)


On the :guitab:`CTFFIND-4.1` tab:

:CTFFIND-4.1 executable: path/to/ctffind

	(You will need to have CTFFIND-4.1 installed somewhere. Copy the filename of the executable here.)

:Use power spectra from MotionCorr job?: Yes

	(This estimates the CTF parameters using the power spectra that were saved during motion correction.)

:Minimum resolution (A): 30

	(This is the lowest resolution that is used for CTF estimation. For you own data, you may need to change these values.)
	
:Maximum resolution (A): 5

	(This is the highest resolution that is used for CTF estimation, in the image with the least dose. For you own data, you may need to change these values.)

:Minimum defocus value (A): 5000

	(Note that this value will be ignored as long as we use the 'Nominal defocus search range' field below.)

:Maximum defocus value (A): 50000

	(Note that this value will be ignored as long as we use the 'Nominal defocus search range' field below.)

:Defocus step size (A): 500

:Nominal defocus search range (A): 10000

	(If a positive value is given, the defocus search range will be set to +/- this value (in A) around the nominal defocus value from the input STAR file. The nominal defocus would have been extracted from the mdoc files. When using this option make sure that the correct values are present in the input star files for each tilt series. If a zero or negative value is given for this field, then the overall min-max defocus search ranges above will be used instead.)

:Dose-dependent Thon ring fading (e/A2): 100

    (If a positive value is given, then the maximum resolution for CTF estimation is lowerered by exp(dose/this_factor) times the original maximum resolution specified above. Remember that exp(1)~=2.7, so a value of 100 e/A^2 for this factor will yield 2.7x higher maxres for an accumulated dose of 100 e/A^2; Smaller values will lead to faster decay of the maxres. If zero or a negative value is given, the maximum value specified above will be used for all images.)


On the :guitab:`Running` tab:

Make sure you use a suitable number of parallel MPI processes for your computational setup, possibly submit to a queue, and click the :runbutton:`Run!` button to launch the job.

The output will be saved in the ``CtfFind/job003/`` directory. The output star file containing all necessary metadata for input into other jobs is saved as ``CtfFind/job003/tilt_series_ctf.star``.
You can again have a look at added metadata for each tilt series image by looking into their star files:

::

    less CtfFind/job003/tilt_series/TS_01.star

Check the defocus values for a few tilt series by examining their star files in the tilt_series directory of the CtfFind job. 
The ``rlnDefocusU`` and ``rlnDefocusV`` columns specify the estimated defocus values.

In addition, the ``logfile.pdf`` file contains plots of useful parameters, such as defocus, astigmatism, estimated resolution, etc for all micrographs, and histograms of these values over the entire data set. Analysing these plots may be useful to spot problems in your data acquisition.

Compared to single-particle data, tilt series images tend to have low SNR, particularly at higher tilts. Consequently, the defocus values may vary at higher tilts. 
Later in this tutorial, we will perform reference-based CTF refinement, during which we can determine better defoci, so as long as the estimated values aren't too far off, we can hope to improve of them later on and we need not worry too much at this stage.

