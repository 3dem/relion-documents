.. _sec_sta_reconstructtomo:

Reconstruct Tomograms
=====================

We can now generate our tomograms. Click on the :jobtype:`Reconstruct tomograms` job from the job types.
On the :guitab:`I/O` tab

:Input tilt series: AlignTiltSeries/job[Number]/aligned_tilt_series.star

On the :guitab:`Reconstruct` tab:

:Unbinned tomogram width (Xdim): 3710

:Unbinned tomogram height (Ydim): 3838

Xdim and Ydim correspond to the X and Y dimensions of your motion corrected images, adjusted by your tilt axis angle. 
[does this need more explanation].

:Unbinned tomogram thickness (Zdim): 2500

Zdim is the thickness of your tomogram in voxels. For your own data, you may want to test a few values here to make sure 
the tomogram thickness is not too small to contain your entire sample. 
If you intend to denoise your tomograms later, we strongly recommend that you do not pick a tomogram thickness 
which is significantly greater than the thickness of your sample. 
This is because the denoising protocol randomly extracts subtomograms from your tomograms and if too much of 
your tomogram is noise above and below the sample, the training of the denoising neural network will be suboptimal. 

:Binned pixel size (A): 10

A binned pixel size of 10 Å will suffice for particle picking and denoising. 
Typically, the larger the pixel size, the faster the tomogram reconstruction. 
Therefore, if the tomograms are taking too long to reconstruct, increase the pixel size. 

:Generate tomograms for denoising?: No

The quality of the tutorial tomograms is very good and don’t need to be denoised; 
however, for your own data, you may select Yes if you plan to denoise them.

:Tilt angle offset (deg): 0

:Reconstruct only this tomogram:

This option allows you to reconstruct only one tomogram from multiple alignment jobs. 
In that case, you can specify the rlnTomoName (i.e. the name of the individual tilt series .star files like Session_1_TS_01) of the tomogram you wish to reconstruct. 
In the tutorial, we will use all tilt series.

On the :guitab:`Running` tab choose the approriate number of MPIs and Threads and then click on the :runbutton:`Run!` button. 
With 6 MPIs and 14 threads this step tool ca. 5 mins in our system. Note that generating tomograms for
denoising can take significant time. Also, you can speed up this step by choosing a larger value for binned pixel size.

Tomograms from this step can be found in ReconstructTomograms/job[Number]/tomograms/ directory. 
If you have selected Yes to denoising, two tomograms per tilt series will have been generated (half1 and half2). 
You can visualise the tomograms using IMOD (3dmod) or Napari. Later, these tomograms will then be used for denoising and particle picking. 
The quality of the tomogram is important for visualisation during the particle picking process and in assessment of your sample. 
However, RELION does not perform averaging on subtomograms extracted directly from these tomograms. 
Instead, it extracts particles from motion corrected 2D images. 
Consequently, you do not have to worry too much about the quality of these tomograms beyond visualisation purposes unless you intend to perform subtomogram averaging on these tomograms using different software.


