.. _sec_sta_ctfestimation:

CTF Estimation
=================

Next, we will estimate the CTF parameters for each corrected micrograph. 
We will use Alexis Rohou and Niko Grigorieff’s CTFFIND-4.1 because it allows reading in the movie-averaged power spectra calculation by RELION’s own implementation of the MotionCor2 algorithm. 

Select the :jobtype:`CTF estimation` job type in the job-type browser and fill in the following parameters on the :guitab:`I/O` tab:

:Input tilt series: MotionCorr/job[Number]/corrected_tilt_series.star

:Estimate phase shifts?: No
(Estimate phase shifts option is only useful for phase plate data)

:Amount of astigmatism (A): 100
(This number is suitable for most data sets on reasonably well aligned microscopes.)


On the :guitab:`CTFFIND-4.1` tab:

:CTFFIND-4.1 executable: path/to/ctffind

:Use power spectra from MotionCorr job?: Yes
(as we have saved our images in float16. If you didn’t use float16 and/or your images were already motion corrected, select No.)

:Minimum resolution (A): 30

:Maximum resolution (A): 5
(For you own data, you may need to change these values)

:Minimum defocus value (A): 5000

:Maximum defocus value (A): 50000

:Defocus step size (A): 500

Keep other parameters to their default values.

On the :guitab:`Running` tab:

Set your desired compational setting including

:Number of MPI procs: xx


Clicking the :runbutton:`Run!` button will launch the job.
The output will be saved in the ``CtfFind/job[number]/`` directory. The output star file containing all necessary metadata for input into other jobs is saved as ``tilt_series_ctf.star``.
Check the defocus values for a few tilt series by examining their star files in the tilt_series directory of the CtfFind job. 
Look in the rlnDefocusU column. Tilt series tend to have low SNR, particularly at higher tilts. 
Consequently, the defocus values may wildly vary at higher tilts. This can be prevented by narrowing the maximum and minimum defocus range (provided you are not cropping the defocus of other tilt series out of range) and adjusting the minimum and maximum resolution that will be used to plot the CTF. 
For some datasets, particularly for thick samples, we find setting the maximum resolution as high as 20 Å and the minimum resolution at 40 Å can yield much more consistent results. 
Furthermore, later in the pipeline during subtomogram averaging we will carry out defocus refinement in which we can regularise the defocus in each tilt series which should minimise the effect of incorrect defocus estimates at this stage. 
Finally, the logfile.pdf file contains plots of useful parameters, such as defocus, astigmatism, estimated resolution, etc for all micrographs, and histograms of these values over the entire data set. Analysing these plots may be useful to spot problems in your data acquisition.
