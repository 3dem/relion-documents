.. _program_tomo_local_particle_refine:

relion_tomo_local_particle_refine
=================================

This program optimises the viewing angles and 3D positions of all particles. 
This is done by following the local gradient of the L2 error function downhill, so it is significantly faster than a full refinement using ``relion_refine``. 
Currently, the results are slightly worse than those from ``relion_refine``, though.

The estimated particle angles and positions are written into the output |particle_set| which replaces the given particle set in the output |optimisation_set|.


Relevant program arguments:
---------------------------

- ``--i`` and/or ``--p``, ``--t``, ``--mot``, ``--ref<1/2>``, ``--mask`` and ``--fsc``: input optimisation-set and/or its components (see |optimisation_set|).
- ``--b``: box size to be used for the estimation. Note that this can be larger than the box size of the reference map. A sufficiently large box size allows more of the high-frequency signal to be captured that has been delocalised by the CTF.
- ``--j``: number of threads to be used. This should be set to the number of CPU cores available.
- ``--o``: name of the output directory (that will be created).


Program output:
---------------

After running the program, the output directory (``--o`` argument) will contain the following items:

- **particles.star**: a new |particle_set|  containing the newly estimated angles and positions.
- **optimisation_set.star**: a new |tomogram_set| pointing to the new particle set.
- **note.txt**: a text file containing the command issued to run the program.



.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
