.. _sec_sta_aligntiltseries:

Align tilt-series
=================

Before tomogram reconstruction, each tilt series must be aligned. 
To do this, RELION 5 implements a wrapper to IMOD or AreTomo. For the tutorial dataset, we will use IMOD’s fiducial-based alignment as the raw data contains (10 nm) gold beads as fiducial markers. 
For your own data, you may want to use various tilt series alignment methods and then compare the quality of the tomograms that each method produces (see next step).
 
Start by selecting the :jobtype:`Align tilt-series` job, and in the :guitab:`I/O` tab set:

:Input tilt series: ExcludeTiltImages/job004/selected_tilt_series.star

On the :guitab:`IMOD` tab, set:

:Use IMOD's fiducial based alignment?: Yes

:Fiducal diameter (nm): 10

:Use IMOD's patch-tracking for alignment?: No

   (For your own data, select Yes if you want to use IMOD’s patch-tracking instead of fiducial-based alignment.)

On the :guitab:`AreTomo` tab, make sure this is still set:

:Use AreTomo: No

Then, run the job, which has not been parallelised (yet), by clicking the :runbutton:`Run!` button.

You can again view the accumulated metadata for each tilt series by typing:


::

    less AlignTiltSeries/job005/tilt_series/TS_01.star

The tutorial data is very good and automated alignment is not a problem. This may not be the case for your own data. You can however go into each of the individual IMOD directories (e.g. ``AlignTiltSeries/job005/external/TS_01``) and re-run IMOD for individual tilt series by tweaking the parameter files. This will obviously require some skills in IMOD, which may be useful to acquire anyway. You can find the `IMOD documentation here <https://bio3d.colorado.edu/imod/doc/guide.html>`_. First delete the corresponding ``AlignTiltSeries/job005/tilt_series/TS_XX.star`` file (if it exists in the first place) and then continue the :jobtype:`Align tilt-series` job from the GUI. The job will then read in the new results and generate an updated star file. 
