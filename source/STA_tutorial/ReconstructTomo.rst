.. _sec_sta_reconstructtomo:

Reconstruct Tomograms
=====================

We can now generate our tomograms. Click on the :jobtype:`Reconstruct tomograms` job from the job types, and on the :guitab:`I/O` tab set:

:Input tilt series: AlignTiltSeries/job005/aligned_tilt_series.star

On the :guitab:`Reconstruct` tab:

:Unbinned tomogram width (Xdim): 4000

    (This is the X-dimension of the reconstructed tomogram, in voxels. We're using a slightly larger tomogram volume than the actual size of the images (which is 3710 x 3838) so that if they rotate, all pixels will still be in the tomogram. Because we use a large pixel below, the costs on disk space are not too large, but you could tweak this to have a bit smaller tomograms.)				 

:Unbinned tomogram height (Ydim): 4000

    (As above for the Y-dimension.)

:Unbinned tomogram thickness (Zdim): 2000

    (This is the Z-dimension of the tomogram, in voxels. For the tutorial data, 2000 voxels encapsulates the signal for all five tomograms. For your own data, you may want to test a few values here to make sure the tomogram thickness is not too small to contain your entire sample. If you intend to denoise your tomograms later, it is better not to pick a tomogram thickness that is much greater than the thickness of your sample, because the denoising protocol randomly extracts subtomograms from your tomograms and you don't want too many without signal.)

:Binned pixel size (A): 10

    (A binned pixel size of 10 Angstrom will suffice for particle picking and denoising. Typically, the larger the pixel size, the faster the tomogram reconstruction and the less space they occupy on disk.) 

:Generate tomograms for denoising?: No

    (The quality of the tutorial tomograms is very good and they don’t need to be denoised; however, for your own data, you may select Yes if you plan to denoise them.)

:Tilt angle offset (deg): 0

    (This option allows you to reconstruct all your tomograms according to a pre-set offset for the tilt angle. This may be useful, for example when you have FIB-milled all you lamella under a know tilt angle.)			  
:Reconstruct only this tomogram: \"\"

    (This option allows you to reconstruct only one tomogram from the input series, for example because you have tweaked its alignment parameters or because you want to run a quick test. Just specify  the rlnTomoName, e.g. TS_01)

On the :guitab:`Running` tab choose the approriate number of MPIs and Threads and then click on the :runbutton:`Run!` button. 
With 1 MPI and 12 threads this step took less than 2 minutes on our computer. But denoising tomograms will take more time.

The output tomograms are called ``Tomograms/job006/tomograms/rec_TS_01.mrc`` etc. You can visualise them in your favourite viewer, including IMOD's 3dmod or Napari.
The main objectives of these tomograms are to assess the quality of your sample and to allow particle picking. They do not need to contain high-resolution information at this point.



