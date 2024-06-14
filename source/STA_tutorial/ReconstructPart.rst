.. _sec_sta_reconstructpart:

Reconstruct particle
====================

The :jobtype:`Reconstruct particle` job generates a reference map from a particle set by averaging the particles using positions and orientations given in the input particles file. This reference map will then be used for further processing in :jobtype:`3D auto-refne`, :jobtype:`3D classification`, :jobtype:`CTF refinement` or :jobtype:`Bayesian polishing`.

Continuing the tutorial, we will now generate a first 3D reference map using the particles obtained by the previous :jobtype:`Extract subtomos` job at bin 6.

Running the job
---------------

Select the :guitab:`IO` tab from the :jobtype:`Reconstruct particle` jobtype.

:Input optimisation set:: Extract/job010/optimisation_set.star
:OR\: use direct entries:: No
:Input particle set:: \ 
:Input tomogram set:: \
:Input trajectory set:: \

On the :guitab:`Average` tab, make sure the following is set to reconstruct particles with a binning factor of 6:

:Binning factor:: 6
:Box size (binned pix):: 192
:Cropped box size (binned pix):: 96
:Wiener SNR constant:: 0

:Symmetry:: C6

On the :guitab:`Running` tab, set:

:Number of MPI procs:: 5
:Number of threads:: 12 

Note that reconstructing from 2D tilt series :ref:`program_tomo_reconstruct_particle` program has 3 thread arguments.
The number of threads provided here sets both ``--j`` and ``--j_out`` arguments so, to avoid exceeding the available memory resources, the ``--mem`` argument should also be set using around 80-90% to keep a safety margin.
In our system, we ran 1 MPI process per cluster node (64Gb) so we added:

:Additional arguments:: \--mem 50

Using the settings above, this job took less than 5 minutes on our system.


Analysing the results
---------------------

You can look at the output map ``Reconstruct/job011/merged.mrc`` with a 3D viewer like UCSF :textsc:`chimera`.
When random halfsets are specified in the input particles file via the ``rlnRandomSubset`` field, the two halfmaps ``half1.mrc`` and ``half2.mrc`` are also generated.


.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
