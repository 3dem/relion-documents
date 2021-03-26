.. _sec_sta_optimisation_set:

Optimisation set
================

The optimisation set is the central data type in a |RELION| tomography project, and it only contains paths to other files.
It is usually named ``optimisation_set.star``.

.. image:: optimisation_set.svg
    :align: center

Specifically, it can point to the following data files:

- A |tomogram_set| listing all tomograms.
- A |particle_set| listing all particles.
- A |trajectory_set| describing the motion of all particles.
- A |manifold_set| listing all manifolds (e.g. spheres or blobs).
- A pair of reference half maps.
- The FSC corresponding to the reference maps.
- A mask to be used with the reference maps.

All of those entries are optional, and different programs require different inputs.
All programs take an optimisation set as input, and most of them also write one out.
If a data file is created or updated by a program, it is added to the optimisation set that the program writes out.
This frees the user from having to track which programs update which data files.
For example, :ref:`program_tomo_refine_ctf` will only update the |tomogram_set|, because the defoci are only defined once for each tilt image, while :ref:`program_tomo_align` will update the |tomogram_set|, the |particle_set| and the |trajectory_set|.
		
When running a program, the input optimisation set is always specified with the ``--i`` argument.
In addition, the individual data files can also be specified separately, in which case the individual files will override the ones listed in the optimisation set.
This allows the user to easily perform the same procedure with specific data files exchanged.
If all data files required by a program have been specified individually, then an optimisation set is not required at all.
The input arguments for the individual data files are always named as follows:

- ``--t`` |nbsp| for the tomogram set
- ``--p`` |nbsp| for the particle set
- ``--mot`` |nbsp| for the trajectory set
- ``--man`` |nbsp| for the manifold set.
- ``--ref<1/2>`` |nbsp| for the respective reference map
- ``--mask`` |nbsp| for the reference mask
- ``--fsc`` |nbsp| for the reference FSC

There are 3 ways to create an initial optimisation set:

- Use the utility program :ref:`program_tomo_make_optimisation_set`.
- Run any program and specify the individual data files. The program will then output a new optimisation set.
- Write one manually.

.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |manifold_set| replace:: :ref:`manifold set <sec_sta_manifold_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
.. |nbsp| unicode:: 0xA0