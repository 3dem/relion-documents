.. _sec_sta_excludetiltimages:

Exclude tilt-images
===================

Often, tilt series contain some images that are not suitable for tomogram reconstruction or further image processing, for example because they are partially or all black because of grid bars blocking the field of view.  We can exclude these images from further processing using the :jobtype:`Exclude tilt-images` job.

On the :guitab:`I/O` tab, set:

:Input tilt series: CtfFind/job003/tilt_series_ctf.star

:Number of cached tilt series: 5

	(This will store 5 tilt series in memory and minimise loading times between tilt series. If your computer struggles with loading so many, you can change this to 1.)

Clicking the :runbutton:`Run!` button will launch the Napari. **Note that Napari is notoriously slow when displaying over a network, so make sure you are running this job from the same computer as you are sitting behind!**

Before doing anything, wait for the tilt series to load. The loading of the tilt series is indicated in the bottom left corner. Once loading is finished, we can examine the first tilt series. 
In the :guitab:`Images` panel on the far right of the GUI, click the top image and scroll through the tilt series using the arrow key on your keyboard. 
For ``TS_01``, the first image (``TS_01_039_-60_0.mrc``) is blank but the rest of the tilt series looks good. 
Therefore, that first image should be excluded from further calculations. Do this by unticking the box next to its name and then clicking :guitab:`Save tilt-series STAR file` in the bottom right corner. 
Then, move onto the next tilt series (``TS_03``) by clicking :guitab:`Session_1_TS_03` in the tilt series panel in the bottom right. Repeat the same for all tilt series. We recommend clicking :guitab:`Save tilt-series STAR file` after each tilt series, just in case Napari crashes. If Napari does crash, you can start a new :jobtype:`Exclude tilt-images` job, where the input tilt series file on the :guitab:`I/O` tab is the ``selected_tilt_series.star`` from the ``ExcludeTiltImages/`` directory of the crashed job. 

When finished, click :guitab:`Save tilt-series STAR file` and close Napari. 
