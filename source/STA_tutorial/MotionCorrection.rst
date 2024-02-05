.. _sec_sta_motioncor:

Motion Correction
=================

As the raw data in EMPIAR-10164 are movies, we need to carry out motion correction. If your own raw data are not movies, and therefore are likely already motion corrected, you can skip this section provided you have selected ‘Yes’ under ‘Movies already motion corrected?’ in the :jobtype:`Tomo import`
To start, click the :jobtype:`Motion correction`` job type in the job-type browser and fill in the following parameters on the :guitab:`I/O` tab:

:Input tilt series: ImportTomo/job001/tilt_series.star
(RELION will use this star file to locate the movies for each tilt series.)

:EER fractionation: 32
(This dataset was not collected using a Falcon 4 detector and therefore the raw data are not found in the EER format. Therefore, we can ignore the EER fractionation field and you should not delete the value in this field. If your own data are collected in the EER format, the fractionation should be adjusted as described here)

:Write output in float16?:: Yes
(We recommend selecting ‘Yes’ to ‘Write output in float16?’ to save hard drive space.
If you select ‘Yes’ to writing in float16, you must selected ‘Yes’ to ‘Save sum of power spectra?’ otherwise CTF estimation will not work later on.)

:Save sum of power spectra?: Yes

:Sum power spectra every n frames: 1

:Save images for denoising?: Yes
(The tutorial dataset is very high quality with good contrast and, consequently, the tomograms produced probably do not need to be denoised. However, to demonstrate RELION’s denoising protocol later, we will select ‘Yes’ in the ‘Save images for denoising?’ field. If, for your own data, you have limited hard drive space and you are confident your tomograms will be high contrast and easily interpreted, you can select ‘No’. However, for most datasets we recommend saving images for denoising, just in case it may be needed at a later stage. )

On the :guitab:`Motion` tab:

:Bfactor: 150
(For your own data, this can be reduced if the SNR is particularly low. For super resolution movies, increasing the B factor may help.)

Keep the ‘Number of patches X,Y’ as 1 and 1. We do not advise this number is increased unless you have exceptionally high SNR. 

:Group frames: 1

:Binning factor: 2
(The raw images were collected in super resolution mode and have not yet been binned. This will bin the images to 1.35 Å.)

The tutorial data has already been gain corrected so does not need a ‘Gain reference image’ and so this field should be left blank.

‘Gain rotation’ and ‘Gain flip’ can be left as any value as they will be ignored. 
For your own data, if gain correction is necessary, enter the path to the gain reference under ‘Gain reference image’ and specify how the reference should be transformed in ‘Gain flip’ and ‘Gain rotation’, if necessary. 

No ‘Defect file’ is provided for the tutorial dataset, so this field can be ignored. 
For your own data, the defect file can be used to mask away broken pixels on the detector. Formats supported in our own implementation and in UCSF motioncor2 are either a text file in UCSF motioncor2 format (each line contains four numbers: x, y, width and height of a defect region); or a defect map (an image in MRC or TIFF format, where 0=good and 1=bad pixels). 
The coordinate system is the same as the input movie before application of binning, rotation and/or flipping. Note that defect text files produced by SerialEM are NOT supported! However, one can convert a SerialEM-style defect file into a defect map using imod.

:Use RELION's own implementation: Yes
If you prefer to use MotionCor2, select No, provide the path the executable, the GPU ID(s) of the GPUs you wish to use, and any other MotionCor2 arguments in their respective fields. 
Note that MotionCor2 cannot save images in float16 yet.

On the :guitab:`Running` tab:

:Submit to queue?: Yes

:Number of MPI procs: xx

:Number of threads: xx


Clicking the :runbutton:`Run!` button will launch the job.
Your motion corrected particles will be output into the ``MotionCorr/job[number]/`` directory. 
The output star file containing all necessary metadata for input into other jobs is saved as ``corrected_tilt_series.star``. 