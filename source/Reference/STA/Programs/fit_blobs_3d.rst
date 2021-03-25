.. _program_tomo_fit_blobs_3d:

relion_tomo_fit_blobs_3d
========================

This program refines spherical manifolds to better fit the double membranes of vesicles, producing spheroidal manifolds.
The resulting manifold will run along the outer interface of the outer membrane, where the signal is the strongest.
These spheroidal manifolds can then be used to sample random particles at a specific depth and with an appropriate initial orientation using the program :ref:`program_tomo_sample_manifold`.

The initial spherical manifolds need to be part of the input |manifold_set| that can be created using the program :ref:`program_tomo_add_spheres`.
The estimated spheroids are written into the output manifold set which replaces the given one in the output |optimisation_set|.
Note: the user is recommended to first detect all fiducials in the input tomograms, since their strong signal can disturb the membrane estimation.
This can be done using the program :ref:`program_tomo_find_fiducials`.

Relevant program arguments:
---------------------------

- ``--i`` and/or  ``--t`` and ``--man``: input optimisation-set and/or its components (see |optimisation_set|).
- ``--ms``: approximate membrane separation in Å.
- ``--rr``: the expected variation of the vesicle radius as a multiple of the initial sphere radius.
- ``--frad``: approximate radius of the fiducial markers (required for their deletion).
- ``--bin``: binning level at which to perform the membrane estimation. This needs to allow multiple pixels of separation between the two membranes.
- ``--n``: number of `Spherical Harmonics <https://en.wikipedia.org/wiki/Spherical_harmonics>`_ bands used to represent the spheroids. A greater number will allow for a more precise membrane fit, but it will also make overfitting more likey. A value between 5 and 9 is recommended.
- ``--j``: number of threads to be used. This should be set to the number of CPU cores available.
- ``--o``: name of the output directory (that will be created).


Program output:
---------------

After running the program, the output directory (``--o`` argument) will contain the following items:

- **manifolds.star**: a new |manifold_set| containing the spheroidal membranes. It will *not* contain the initial spheres, nor any other initial manifolds.
- **optimisation_set.star**: a new |optimisation_set| pointing to the new manifold set.
- **Meshes/<** ``tomogram_name`` **>.ply**: visualisations showing the fitted spheroids for each tomogram in `ply format <https://en.wikipedia.org/wiki/PLY_(file_format).ply>`_. They can be viewed in relation to (low-magnification) tomograms as produced by :ref:`program_tomo_reconstruct_tomogram` in a viewer that supports both meshes and 3D images (such as e.g. `Paraview <https://www.paraview.org/>`_).
- **note.txt**: a text file containing the command issued to run the program.


.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |manifold_set| replace:: :ref:`manifold set <sec_sta_manifold_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
