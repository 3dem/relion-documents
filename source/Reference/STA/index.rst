.. _sec_sta_programs:

Subtomogram Averaging
=====================

Data Types
----------

The custom data types used in tomography programs in |RELION|:

.. toctree::

   Datatypes/tomogram_set
   Datatypes/particle_set
   Datatypes/trajectory_set
   Datatypes/manifold_set
   Datatypes/optimisation_set


Programs
--------

These are the most relevant tomography-related programs in |RELION|


Core programs
:::::::::::::

.. toctree::
   :hidden:

   Programs/reconstruct_particle
   Programs/subtomo
   Programs/import_tomograms
   Programs/find_fiducials

- :ref:`program_tomo_reconstruct_particle` : creates high-resolution 3D maps from a given data set.
- :ref:`program_tomo_subtomo` : creates pseudo subtomograms that can be fed into ``relion_refine``.



Refinement programs
:::::::::::::::::::

These programs use an existing particle set and a pair of high-resolution 3D reference maps to estimate or improve different properties:




Utility programs
::::::::::::::::

- :ref:`program_tomo_import_tomograms` : imports new tilt series to create or extend a tomogram set.
- :ref:`program_tomo_find_fiducials` : detects the fiducial markers in a given data set.
