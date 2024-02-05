.. _sec_sta_importomo:

Import Raw Data
================

We will now import the raw data into RELION. In the GUI, select :jobtype:`Tomo import` from the jobt-type browser on the left and fill in the following parameters on the :guitab:`General` tab:

:Pixel size (Angstrom):: 1.35

:Voltage (kV):: 300

:Spherical aberration (mm):: 2.7

:Amplitude contrast:: 0.07

On the :guitab:`Tilt series` tab:

:Import tilt-series?: Yes

:Tilt image files: frames/*.tif

:mdoc files: mdoc/*.mdoc

:Dose rate per tile-image: 3

:Is dose rate per movie frame?: No

:Tilt axis angle (deg): 85

:Invert defocus handedness?: Yes

:Movies already motion corrected?: No

On the :guitab:`Tomograms` tab:

:Import tomograms?: No

On the :guitab:`Coordinates` tab:

:Import coordinates?: No

On the :guitab:`Others` tab:

:Import other node types?: No

On the :guitab:`Running` tab:

:Submit to queue?: No

Keep all other parameters to default values.

You may provide a meaningful alias (for example: `images`) for this job in the white field named ``Current job: Give_alias_here``.
Clicking the :runbutton:`Run!` button will launch the job.
A directory called ``ImportTomo/job001/`` will be created, together with a symbolic link to this directory that is called ``ImportTomo/images``.
Inside the newly created directory a |tomogram_set| ``tilt_series.star`` file is created. It contains a table with general tilt-series properties per tilt series.