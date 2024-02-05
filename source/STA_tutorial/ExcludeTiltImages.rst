.. _sec_sta_excludetiltimages:

Exclude Tilt Images
===================

Each tilt series can contain images which are not suitable for tomogram reconstruction or further image processing. 
This can be due to several factors including very low or no signal at higher tilts and contamination or grid bars blocking the field of view. 
We can exclude these images from further processing using  :jobtype:`Exclude tilt-images` job.

Start by selecting the :guitab:`I/O` tab.

:Input tilt series: CtfFind/job[Number]/tilt_series_ctf.star

:Number of cached tilt series: 5
(This will store 5 tilt series in memory and minimise loading times between tilt series. 
If your computer is struggling with loading the tilt series, you can change this to 1 later.)

Clicking the :runbutton:`Run!` button will launch the Napari.

Before doing anything, wait for the tilt series to load. The loading of the tilt series is indicated in the bottom left corner. 
Once loading is finished, we can examine the first tilt series. 
In the :guitab:`Images` panel on the far right of the GUI, click the top image and scroll through the tilt series using the arrow key on your keyboard. 
If your tilt series is like ours (TS_01), the first image (TS_01_039_-60.mrc) will be blank but the rest of the tilt series will look good. 
The first image should be deleted from the tilt series. We can do this by unticking the box next to its name and then clicking :guitab:`Save tilt-series STAR file` in the bottom right corner. 
We can now move onto the next tilt series (TS_03) by clicking Session_1_TS_03 in the tilt series panel in the bottom right. 
Before doing anything, wait for the tilt series to load. Again, go through the tilt series and remove or keep images as you see fit. 
Repeat for all tilt series. We recommend clicking :guitab:`Save tilt-series STAR file` after each tilt series just in case Napari crashes. 
If Napari does crash, you can continue the job by running a new :jobtype:`Exclude tilt-images` job where the input tilt series in the :guitab:`I/O` tab is the ``tilt_series.star`` from the directory of the crashed job. 
When finished, click :guitab:`Save tilt-series STAR file` and close Napari. 