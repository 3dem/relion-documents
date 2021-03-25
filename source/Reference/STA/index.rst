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

.. toctree::
   :hidden:

   Programs/reconstruct_particle
   Programs/subtomo
   Programs/align
   Programs/refine_ctf
   Programs/local_particle_refine
   Programs/fit_blobs_3d
   Programs/reconstruct_tomogram
   Programs/import_tomograms
   Programs/import_particles
   Programs/find_fiducials


Core programs
:::::::::::::

- :ref:`program_tomo_reconstruct_particle` : creates high-resolution 3D maps from a given data set.
- :ref:`program_tomo_subtomo` : creates pseudo subtomograms that can be fed into ``relion_refine``.


Refinement programs
:::::::::::::::::::

These programs use an existing particle set and a pair of high-resolution 3D reference maps to estimate or improve different properties:

- :ref:`program_tomo_align` : aligns the images of a tilt series and estimates beam-induced motion to better fit a set of particles.
- :ref:`program_tomo_refine_ctf` : refines the astigmatic defocus, signal intensity (i.e. ice thickness) and higher-order aberrations.
- :ref:`program_tomo_local_particle_refine` : offers a rapid way to refine the angles and positions of individual particles.
- :ref:`program_tomo_fit_blobs_3d` : fits a set of spherical manifolds representing vesicles to the observed membranes.


Utility programs
::::::::::::::::

- :ref:`program_tomo_reconstruct_tomogram` : creates a (typically low-magnification) tomogram.
- :ref:`program_tomo_import_tomograms` : imports new tilt series to create or extend a tomogram set.
- :ref:`program_tomo_import_particles` : imports new particles.

- :ref:`program_tomo_find_fiducials` : detects the fiducial markers in a given data set.
