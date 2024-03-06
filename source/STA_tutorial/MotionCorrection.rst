.. _sec_sta_motioncor:

Motion correction
=================

As the raw data in EMPIAR-10164 are movies, we need to carry out motion correction. If your own raw data are already motion-corrected, you can skip this section provided you have selected ‘Yes’ under ‘Movies already motion corrected?’ in the :jobtype:`Import`

To start, click the :jobtype:`Motion correction` job type in the job-type browser and fill in the following parameters on the :guitab:`I/O` tab:

:Input tilt series: ImportTomo/job001/tilt_series.star

		    (RELION will use this star file to locate the movies for each tilt series.)

:EER fractionation: 32

		    (This dataset was not saved in the EER format. Therefore, we can ignore the EER fractionation field; but don't leave it empty. If your own data are collected in the EER format, the fractionation should be adjusted as described here)

:Write output in float16?: Yes

   (We recommend writing images in float16 format to save disk space. If you select ‘Yes’ to writing in float16, you must also select ‘Yes’ to ‘Save sum of power spectra?’, because CtfFind4 will not be able to read float16 images.)

:Save images for denoising?: Yes

	(The tutorial dataset is very high quality with good contrast and, consequently, the tomograms produced probably do not need to be denoised. However, to demonstrate RELION’s denoising protocol later, we will select ‘Yes’ in the ‘Save images for denoising?’ field. If, for your own data, you have limited hard drive space and you are confident your tomograms will be high contrast and easily interpreted, you can select ‘No’. However, for most datasets we recommend saving images for denoising, just in case it may be needed at a later stage. )

:Save sum of power spectra?: Yes

    (Sums of non-dose weighted power spectra provide better signal for CTF estimation. The power spectra can be used by CTFFIND4. This option is not available for UCSF MotionCor2. You must use this option when writing in float16, as CtfFind4 cannot read images in float16 format.)

:Sum power spectra every n frames: 1

    (McMullan et al. Ultramicroscopy, 2015 suggest that summing power spectra every 4.0 e/A2 gives optimal Thon rings. One frame will be 3 e/A2.)				   

On the :guitab:`Motion` tab:

:Bfactor: 150

	  (For your own data, you may need to increase this value, if the SNR is particularly low. For super resolution movies, increasing the B factor may also help.)

:Number of patches: 1    1

	(As there is so little dose in each movie frame, it is better not to use patch-based motion correction.)
	
:Group frames: 1

:Binning factor: 2

	(The raw images were collected in super-resolution mode and have not yet been binned. This will bin the images to 1.35 Å.)

:Gain-reference image: ""

	(The tutorial data has already been gain corrected so does not need a ‘Gain reference image’ and so this field should be left blank.)

:Gain rotation: No rotation (0)

	(This will be ignored as we are not doing gain correction.)
		
:Gain flip: No flip (0)

	(This will be ignored as we are not doing gain correction.)

:Defect file: ""

	(We don't have a file that describes the camera defects for this data set. For your own data, the defect file can be used to mask away broken pixels on the detector. Formats supported in our own implementation and in UCSF motioncor2 are either a text file in UCSF motioncor2 format (each line contains four numbers: x, y, width and height of a defect region); or a defect map (an image in MRC or TIFF format, where 0=good and 1=bad pixels. The coordinate system is the same as the input movie before application of binning, rotation and/or flipping. Note that defect text files produced by SerialEM are NOT supported! However, one can convert a SerialEM-style defect file into a defect map using imod.). 

:Use RELION's own implementation: Yes
If you prefer to use UCSF MotionCor2, select No, provide the path to the executable, the GPU ID(s) of the GPUs you wish to use, and any other MotionCor2 arguments in their respective fields. 
Note that MotionCor2 cannot save images in float16 yet, nor does it write out summed power spectra of movie frames for subsequent CTF estimation.

On the :guitab:`Running` tab:

:Submit to queue?: Yes

:Number of MPI procs: 32

   (We used 32 parallel processes on our computer.)

:Submit to queue?: No

   (We used a local machine, but this will depend on your setup.)


Clicking the :runbutton:`Run!` button will launch the job.
Your motion corrected particles will be output into the ``MotionCorr/job002/`` directory. 
The output star file containing all necessary metadata for input into other jobs is saved as ``MotionCorr/job002/corrected_tilt_series.star``. You can again have a look at the star files it refers to, to see accumulated metadata about the motion correction by typing:

::

    less MotionCorr/job002/tilt_series/TS_01.star


    
