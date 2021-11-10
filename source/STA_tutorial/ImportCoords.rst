.. _sec_sta_importcoord:

Import coordinates
------------------

The minimum required data to construct pseudo-subtomos is the set of 3D coordinates and corresponding tomogram name for each particle.
Pixel coordinates should be related to dimensions and offsets given by ``newst.com`` ``tilt.com`` files for original pixel size (Bin1) (See :ref:`sec_sta_importomo`).
During the import coordinates process, it checks if the tomogram names of all particles exist in the related |tomogram_set| ``tomograms.star`` file and adds the corresponding ``data_optics`` table to the output ``particles.star`` file (More information in :ref:`program_tomo_import_particles` program help and :ref:`sec_sta_particle_set` description).

Select :jobtype:`Tomo import` from the jobt-type browser on the left and fill in the following parameters on the :guitab:`Coordinates` tab:

:Import coordinates?: Yes

:STAR file with coordinates:: input/coords_5tomos.star

:Tomograms set:: ImportTomo/job001/tomograms.star

    (Note that the :button:`Browse` button will only list tomogram set :textsc:`star` files.)

On the :guitab:`Tomograms` tab, make sure the following is set:

:Import tomograms?: No

On the :guitab:`Others` tab, make sure the following is set:

:Import other node types?: No

Inside the newly created directory, you will find the imported |particle_set| ``particles.star`` file along with an ``optimiser_set.star`` file.

If you had preprocessed your particles in a different project, you would use the same :jobtype:`Tomo import` job-type to import particles :textsc:`star` file, 3D references, 3D masks, etc, on the :guitab:`Others` tab.
Note that this is NOT the recommended way to run |RELION|, and that the user is responsible for generating correct :textsc:`star` files.

.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`