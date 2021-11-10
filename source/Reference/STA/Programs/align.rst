.. _program_tomo_align:

relion_tomo_align
=================

This program refines the projections that map 3D space onto the images of the tilt series, as well as (optionally) also the beam-induced motion trajectories of the particles. 
Each projection is optimised using the full 5 degrees of freedom: the assumption of a common tilt axis is abandoned. 
Even if no beam-induced motion is estimated, the (in that case static) 3D particle-positions are also optimised by the program.
This is because those 3D positions cannot be assumed to be known in advance, since they have only been inferred from the observed 2D particle-positions in the individual tilt images.
Therefore, this program always looks for the optimal set of 3D positions *and* projections.

If the particle motion is also being estimated (using the ``--motion`` argument), then the 3D positions of the particles are allowed to differ between tilt images, albeit only in a limited and spatially smooth manner.
This is done analogously to `Bayesian polishing <https://journals.iucr.org/m/issues/2019/01/00/fq5003>`_ in 2D (implemented in ``relion_motion_refine``), except that the trajectories are estimated in 3D, and that no acceleration constraint is imposed.
Because part of the particle motion is rigid, the motion estimation also always includes a rigid alignment of the frames.

Please note that estimating beam-induced motion significantly increases the runtime of the program, so it should only be done in the final rounds of optimisation.

The estimated particle trajectories are written into the output |trajectory_set|, the projection matrices (containing the rigid part of the motion as well as the alignment of the tilt series - these cannot be distinguished) into the output |tomogram_set| and the estimated (initial) particle positions into the output |particle_set| which replace the given trajectory, tomogram and particle sets in the output |optimisation_set|.

General program arguments:
--------------------------

- ``--i`` and/or ``--p``, ``--t``, ``--mot``, ``--ref<1/2>``, ``--mask`` and ``--fsc``: input optimisation-set and/or its components (see |optimisation_set|).
- ``--b``: box size to be used for the estimation. Note that this can be larger than the box size of the reference map. A sufficiently large box size allows more of the high-frequency signal to be captured that has been delocalised by the CTF.
- ``--r``: maximal assumed error in the initial 2D particle-positions (distances between the projected 3D positions and their true positions in the images), given in pixels.
- ``--j``: number of threads to be used. This should be set to the number of CPU cores available.
- ``--o``: name of the output directory (that will be created).


Motion-related arguments:
-------------------------

- ``--motion``: perform motion estimation simultaneously with the tilt-image alignment.
- ``--s_vel``: the expected amount of motion (i.e. the std. deviation of particle positions in Å after 1 electron per Å² of radiation).
- ``--s_div``: the expected spatial smoothness of the particle trajectories (a greater value means spatially smoother motion).
- ``--sq_exp_ker``: assume that the correlation of the velocities of two particles decays as a Gaussian over their distance, instead of as an exponential. This will produce spatially smoother motion and result in a shorter program runtime.

Deformation-related arguments:
------------------------------

- ``--deformation``: perform 2D deformation estimation for each tilt-image.
- ``--def_w``: Number of horizontal sampling points for the deformation grid.
- ``--def_h``: Number of vertical sampling points for the deformation grid.
- ``--def_model``: Type of model to estimate deformations (linear, spline or Fourier).
- ``--def_reg (0.0)``: Value of the deformation regulariser
- ``--per_frame_deformation``: Model separate 2D deformations for each tilt-image instead of the whole tilt series.

Program output:
---------------

After running the program, the output directory (``--o`` argument) will contain the following items:

- **motion.star**: a new trajectory set
- **tomograms.star**: a new |tomogram_set| containing the newly estimated projection matrices (``rlnTomoProj<X/Y/Z/W>``)
- **particles.star**: a new |particle_set| containing the newly estimated particle positions in 3D (``rlnCoordinate<X/Y/Z>``)
- **optimisation_set.star**: a |optimisation_set| pointing to the new trajectory, tomogram and particle sets.
- **Trajectories/<** ``tomogram_name`` **>_x<1/8>.ply**: meshes of 3D trajectories in `ply format <https://en.wikipedia.org/wiki/PLY_(file_format).ply>`_, scaled by a factor of 1 or 8, respectively. Note that only the trajectories themselves are scaled - their positions are those of the particles. They can be viewed in relation to (low-magnification) tomograms as produced by :ref:`program_tomo_reconstruct_tomogram` in a viewer that supports both meshes and 3D images (such as e.g. `Paraview <https://www.paraview.org>`_).
- **note.txt**: a text file containing the command issued to run the program.

.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
