.. _sec_sta_importomo:

Import tomograms
================

This section shows how to import a data set whose tomograms have already been aligned using IMOD_ and the CTF estimated with CTFFind_ or CtfPlotter_.

The first step to do is to import the |tomogram_set| into the pipeline.
To do that, we must first create a description ``.star`` file containing the required information, one row per tomogram.
The basic fields are the tilt series stack filename, CTF estimated data filename and IMOD_ project folder. As an example, the ``tomograms_descr.star`` file used in this tutorial contains the following fields:

::

    # tomograms_descr.star

    data_

    loop_
    _rlnTomoName
    _rlnTomoTiltSeriesName
    _rlnTomoImportCtfFindFile
    _rlnTomoImportImodDir
    _rlnTomoImportFractionalDose

     TS_01   tomograms/TS_01/01.mrc   tomograms/TS_01/01_output.txt   tomograms/TS_01   3.0
     TS_03   tomograms/TS_03/03.mrc   tomograms/TS_03/03_output.txt   tomograms/TS_03   3.0
     TS_43   tomograms/TS_43/43.mrc   tomograms/TS_43/43_output.txt   tomograms/TS_43   3.1
     TS_45   tomograms/TS_45/45.mrc   tomograms/TS_45/45_output.txt   tomograms/TS_45   3.1
     TS_54   tomograms/TS_54/54.mrc   tomograms/TS_54/54_output.txt   tomograms/TS_54   3.0

The ``rlnTomoName`` label is a unique identifier per tomogram, automatically created if not provided in this description file (More information can be found in :ref:`program_tomo_import_tomograms` program help). Note that in this dataset the electron dose is not constant so it should be provided in the description file instead of as a global parameter when importing tomograms.

In the GUI, select :jobtype:`Tomo import` from the jobt-type browser on the left and fill in the following parameters on the :guitab:`Tomograms` tab:

:Import tomograms?: Yes

:STAR file with tomograms description:: input/tomograms_descr.star

:Append to tomograms set: \

     (This field can be used to add new tomograms to an existing ``tomograms.star``. This is usefull when subsets of tomograms have different values for pixel size, voltage ... )

:Pixel size (Angstrom):: 1.35

:Voltage (kV):: 300

:Spherical aberration (mm):: 2.7

:Amplitude contrast:: 0.07

:Frame dose (e/A^2):: \

    (If this values varies among the input tomograms, then specify it using its own column in the description input STAR file.)

:Ordered list:: input/order_list.csv

    (A 2-column, comma-separated file with the frame-order list of the tilt series, where the first column is the frame (image) number (starting at 1) and the second column is the tilt angle (in degrees). If this values varies among the input tomograms, then specify it using its own column in the description input STAR file.)

:Flip YZ?: Yes

:Flip Z?: Yes

:Tilt handedness:: -1

On the :guitab:`Coordinates` tab, make sure the following is set:

:Import coordinates?: No

On the :guitab:`Others` tab, make sure the following is set:

:Import other node types?: No


You may provide a meaningful alias (for example: `tomograms`) for this job in the white field named ``Current job: Give_alias_here``.
Clicking the :runbutton:`Run!` button will launch the job.
A directory called ``ImportTomo/job001/`` will be created, together with a symbolic link to this directory that is called ``ImportTomo/tomograms``.
Inside the newly created directory a |tomogram_set| ``tomograms.star`` file is created. It contains a table with general tomogram properties and a specific table for each tomogram including projection matrices, astigmatic defocus, cumulative radiation dose and deformations per tilt frame. (See :ref:`program_tomo_import_tomograms` program help).



.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. _IMOD: https://bio3d.colorado.edu/imod
.. _CTFFind: https://grigoriefflab.umassmed.edu/ctffind4
.. _CtfPlotter: https://bio3d.colorado.edu/imod/doc/man/ctfplotter.html