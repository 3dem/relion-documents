
.. _sec_sta_importcoord:

Import coordinates
==================


The minimum required data to construct pseudo-subtomos is the set of 3D coordinates and tomograms name for each particle. Coordinates should be in bin1 and related to the dimensions and offsets given by ``tilt.com`` file (See :ref:`sec_sta_importomo`) During the import coordinates process, it checks the tomogram name of each particle exists in the tomogram set ``tomograms.star`` file and adds the corresponding ``data_optics`` table to the ``particles.star`` file.

Select ``Tomo import`` from the jobt-type browser on the left and fill in the following parameters on the :guitab:`Coordinates` tab:

:Import coordinates?: Yes

:STAR file with coordinates:: coordinates.star

:Tomograms set:: Tomo/job001/tomograms.star

    (Note that the :button:`Browse` button will only list tomogram set :textsc:`star` files.)

On the :guitab:`Tomograms` tab, make sure the following is set:

:Import tomograms?: No

On the :guitab:`Others` tab, make sure the following is set:

:Import other node types?: No

Inside the newly created directory, together with the :textsc:`particle set` ``particles.star`` file, an :textsc:`optimiser_set.star` is also created. It contains a table with the properties for each tomogram and the projection matrices, astigmatic defocus and cumulative radiation dose per tilt frame in a table for each tomogram (See `relion_tomo_import_tomograms`_ program help).

Have a look at it using:

::

    less ImportTomo/job001/tomograms.star


If you had preprocessed your particles in a different project, you would use the same :jobtype:`ImportTomo` job-type to import particles :textsc:`star` file, 3D references, 3D masks, etc, on the :guitab:`Others` tab.
Note that this is NOT the recommended way to run |RELION|, and that the user is responsible for generating correct :textsc:`star` files.
