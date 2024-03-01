.. _sec_sta_trajectory_set:

Trajectory set
==============

The trajectory set (typically named ``motion.star``) contains the motion trajectories of all particles in a corresponding :ref:`particle set <sec_sta_particle_set>`.
The trajectories can be estimated using the program :ref:`program_tomo_align`, and they will be considered by any |RELION| tomography program that requires particle positions.

The trajectory file consists of ``P+1`` tables, where ``P`` is the number of particles in the corresponding particle set.
The first table only contains the number of particles, while every successive table, named using the particle name (the same as the value of ``rlnTomoParticleName`` in the :ref:`particle set <sec_sta_particle_set>` file) lists the trajectory of each particle.
The trajectories are given in Å, and they are relative to the position of the particle in the chronologically first tilt image (i.e. the image with the lowest cumulative dose). 
