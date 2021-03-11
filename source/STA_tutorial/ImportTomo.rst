.. _sec_sta_importomo:

Import tomograms
================


Getting organised
-----------------

This section shows how to import a data set whose tomograms have already been aligned using Imod and the CTF estimated with ctffind or ctfplotter.

We recommend to create a single directory per project, i.e. per structure you want to determine.
We'll call this the project directory. **It is important to always launch the RELION graphical user-interface (GUI) from the project directory.** Inside the project directory you should make a separate directory to store all your Imod reconstructed tomograms folder.
We like to call this directory ``tomograms/``. Inside, we should find the different tomograms in folders like ``TS_1`` or ``TS_01``.
If for some reason you do not want to place your movies inside the |RELION| project directory, then inside the project directory you can also make a symbolic link to the directory where your reconstructed tomograms are stored.

|RELION| uses the original tilt series stack prior to tilt axis alignment and imports the alignment data from Imod. The tomogram folder should contain: a stack file, with extension ``.st``, ``.mrc`` or ``mrcs``; the ``newst.com`` and ``tilt.com`` script files, where the transformation and tilt angles filenames are obtained from, together with tomogram dimensions, offsets and excluded views. Particle coordinates should refer to tomograms reconstructed using this information.

The first step to do is to import the set of tomograms into the pipeline. To do that, we must first create a description ``.star`` file containing the required information, one row per tomogram. The basic fields are the tilt series stack filename, CTF estimated data filename and Imod project folder. The ``rlnTomoName`` label is a unique identifier per tomogram, automatically created if not provided (More information can be found in `relion_tomo_import_tomograms`_ program help). An example of ``tomograms_descr.star`` to use in this tutorial:

::

    # tomograms_input.star

    data_global

    loop_
    _rlnTomoName
    _rlnTomoTiltSeriesName
    _rlnTomoImportCtfPlotterFile
    _rlnTomoImportImodDir

     TS_1    tomograms/TS_1/TS_1_aligned.st:mrc  tomograms/TS_1/ctfplotter/TS_1_output.txt    tomograms/TS_1
     TS_2    tomograms/TS_2/TS_2_aligned.st:mrc  tomograms/TS_2/ctfplotter/TS_2_output.txt    tomograms/TS_2
     TS_3    tomograms/TS_3/TS_3_aligned.st:mrc  tomograms/TS_3/ctfplotter/TS_3_output.txt    tomograms/TS_3
     ...


We can now launch the |RELION| GUI.
As said before, this GUI always needs to be launched from the project directory.
To prevent errors with this, the GUI will ask for confirmation the first time you launch it in a new directory.
Make sure you are inside the project directory, and launch the GUI by typing:

::

    relion --tomo&


and answer ``Yes`` when prompted to set up a new |RELION| project here.

Select ``Tomo import`` from the jobt-type browser on the left and fill in the following parameters on the :guitab:`Tomograms` tab:

:Import tomograms?: Yes

:STAR file with tomograms description:: tomograms_descr.star

:Append to tomograms set: [empty]

     (This field can be used to add new tomograms to an existing ``tomograms.star``. This is usefull when subsets of tomograms have different values for pixel size, voltage ... )

:Pixel size (Angstrom):: 0.834

:Voltage (kV):: 300

:Spherical aberration (mm):: 2.7

:Amplitude contrast:: 0.07

:Frame dose (e/A^2):: 3

    (If this values varies among the input tomograms, then specify it using its own column in the description input STAR file.)

:Ordered list:: tomograms/orderlist.txt

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
Inside the newly created directory a :textsc:`tomogram set` ``tomograms.star`` file is created. It contains a table with the properties for each tomogram and the projection matrices, astigmatic defocus and cumulative radiation dose per tilt frame in a table for each tomogram (See `relion_tomo_import_tomograms`_ program help).

Have a look at it using:

::

    less ImportTomo/job001/tomograms.star

