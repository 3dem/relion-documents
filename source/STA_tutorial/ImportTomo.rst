.. _sec_sta_importomo:

Import
======

We will now import the raw data into RELION. In the GUI, select :jobtype:`Import` from the jobt-type browser on the top left and fill in the following parameters on the :guitab:`General` tab:

:Tilt image files: frames/*.mrc


:Movies already motion corrected?: No
				   
	(These are 8-frame movies that have not yet been motion-corrected.)	   

:mdoc files: mdoc/*.mdoc

:Optics group name: optics1

	(All imported tomograms will belong to the same optics group with this name. When left empty, each tomogram will be its own optics group, with the tomogram name as the optics group name.)

:Prefix: \"\" 

:Pixel size (Angstrom):: 0.675

:Voltage (kV):: 300

:Spherical aberration (mm):: 2.7

:Amplitude contrast:: 0.1


On the :guitab:`Tilt series` tab:


:Dose rate per tile-image: 3

:Is dose rate per movie frame?: No

:Tilt axis angle (deg): 85

			(This is the nominal value for the tilt-axis orientation wrt to the Y-axis (positive is CCW from Y))

:Invert defocus handedness?: Yes

		(Specify Yes to flip the handedness of the defocus geometry; the default, Yes, leads to a value of -1 in the STAR file, which is the correct one for the tutorial dataset.)
	 

On the :guitab:`Running` tab:

:Submit to queue?: No

You may provide a meaningful alias (for example: `tilt_series`) for this job in the white field named ``Current job: Give_alias_here``.
Clicking the :runbutton:`Run!` button will launch the job.

A directory called ``ImportTomo/job001/`` will be created, together with a symbolic link to this directory that is called ``ImportTomo/tilt_series``.
Inside the newly created directory a ``tilt_series.star`` file is created. It contains a table with an entry for each tilt series.
For each tilt series, a separate starfile contains relevant metadata that has been extracted from the input images and mdoc files.
Have a look at these by typing:

::

    less Import/job001/tilt_series.star
    less Import/job001/TS_01/tilt_series.star

