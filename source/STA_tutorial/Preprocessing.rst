.. _sec_sta_preprocessing:

Preprocessing
=============

At this moment, |RELION| requires tomograms to be preprocessed externally.
It is user responsability to perform the initial steps of movie frames alignment, tilt series alignment and particle picking.

In summary, the required information to start processing in |RELION| is:

- **Tilt series alignment**: It should be done using IMOD_ package. Standard IMOD pipeline is typically accepted but note that not all IMOD options are supported.
- **Initial CTF parameters**: They can be estimated by either CTFFind_ or CtfPlotter_.
- **Order list**: Chronological order of the tilt series acquisition.
- **Fractional electron dose**: electron dose per tilt image.

In this tutorial, we provide the files after computing these previous steps. For a full description of the preprocessing requirement, see :ref:`program_tomo_import_tomograms` program.


Getting organised
-----------------

We recommend to create a single directory per project, i.e. per structure you want to determine.
We'll call this the project directory. **It is important to always launch the RELION graphical user-interface (GUI) from the project directory.** Inside the project directory you should make a separate directory to store all your IMOD_ reconstructed tomograms folder.
We like to call this directory ``tomograms/``. Inside, we should find the different tomograms in folders like ``TS_1`` or ``TS_01``.
If for some reason you do not want to place your tomograms inside the |RELION| project directory, then inside the project directory you can also make a symbolic link to the directory where your reconstructed tomograms are stored.

|RELION| uses the original tilt series stack prior to tilt axis alignment and imports the alignment data from IMOD_. The tomogram folder should contain: a stack file, with extension ``.st``, ``.mrc`` or ``mrcs``; the ``newst.com`` and ``tilt.com`` script files, where the transformation and tilt angles filenames are obtained from together with tomogram dimensions, offsets and excluded views. Particle coordinates should refer to tomograms reconstructed using this information.

When you unpacked the tutorial test data, the ``tomograms/`` directory was created.
It should contain 5 tomogram folders. You should also find the ``masks/`` and ``input/`` folders. The last one should contains the files required to import tomograms data and coordinates.

We will start by launching the |RELION| GUI.
This GUI always needs to be launched from the project directory.
To prevent errors with this, the GUI will ask for confirmation the first time you launch it in a new directory.
Make sure you are inside the project directory, and launch the GUI by typing:

::

    relion --tomo&

and answer ``Yes`` when prompted to set up a new |RELION| project here.


.. _sec_sta_importomo:

Import tomograms
----------------

This section shows how to import a data set whose tomograms have already been aligned using IMOD_ and the CTF estimated with CTFFind_ or CtfPlotter_.

The first step to do is to import the |tomogram_set| into the pipeline.
To do that, we must first create a description ``.star`` file containing the required information, one row per tomogram.
The basic fields are the tilt series stack filename, CTF estimated data filename and IMOD_ project folder. As an example, the ``tomograms_descr.star`` file used in this tutorial contains the following fields:

::

    # tomograms_descr.star

    data_global

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

In the GUI, select ``Tomo import`` from the jobt-type browser on the left and fill in the following parameters on the :guitab:`Tomograms` tab:

:Import tomograms?: Yes

:STAR file with tomograms description:: tomograms_descr.star

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
Inside the newly created directory a |tomogram_set| ``tomograms.star`` file is created. It contains a table with the properties for each tomogram and the projection matrices, astigmatic defocus and cumulative radiation dose per tilt frame in a table for each tomogram (See :ref:`program_tomo_import_tomograms` program help).


.. _sec_sta_importcoord:

Import coordinates
------------------

The minimum required data to construct pseudo-subtomos is the set of 3D coordinates and corresponding tomogram name for each particle.
Pixel coordinates should be related to dimensions and offsets given by ``newst.com`` ``tilt.com`` files for original pixel size (Bin1) (See :ref:`sec_sta_importomo`).
During the import coordinates process, it checks if the tomogram names of all particles exist in the related |tomogram_set| ``tomograms.star`` file and adds the corresponding ``data_optics`` table to the output ``particles.star`` file.

Select ``Tomo import`` from the jobt-type browser on the left and fill in the following parameters on the :guitab:`Coordinates` tab:

:Import coordinates?: Yes

:STAR file with coordinates:: input/coords_5tomos.star

:Tomograms set:: ImportTomo/job001/tomograms.star

    (Note that the :button:`Browse` button will only list tomogram set :textsc:`star` files.)

On the :guitab:`Tomograms` tab, make sure the following is set:

:Import tomograms?: No

On the :guitab:`Others` tab, make sure the following is set:

:Import other node types?: No

Inside the newly created directory, together with the |particle_set| ``particles.star`` file, an :ref:`optimisation set <sec_sta_optimisation_set>` ``optimiser_set.star`` is also created.

If you had preprocessed your particles in a different project, you would use the same :jobtype:`ImportTomo` job-type to import particles :textsc:`star` file, 3D references, 3D masks, etc, on the :guitab:`Others` tab.
Note that this is NOT the recommended way to run |RELION|, and that the user is responsible for generating correct :textsc:`star` files.





.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. _IMOD: https://bio3d.colorado.edu/imod
.. _CTFFind: https://grigoriefflab.umassmed.edu/ctffind4
.. _CtfPlotter: https://bio3d.colorado.edu/imod/doc/man/ctfplotter.html