.. _program_tomo_subtomo:

relion_tomo_subtomo
===================

This program creates *pseudo subtomograms* that can be fed into ``relion_refine`` to perform subtomogram alignment.
Those pseudo subtomograms are not meant to represent the actual density distributions of the particles, but instead abstract 3D image terms that allow ``relion_refine`` to approximate the cost function that would arise if the alignment were to be performed on the stack of corresponding 2D images instead.
Specifically, each pseudo subtomogram consists of a sum of CTF-weighted observations (data term) as well as the corresponding sum of CTF² terms (weight term).
In addition, the output weight term also contains - concatenated along the Z axis - a 3D multiplicity-image (number of Fourier slices contributing to each Fourier voxel) that allows ``relion_refine`` to estimate a spherically symmetrical noise distribution.

The reconstructed pseudo subtomograms consider the motion of the particles as well as higher-order aberrations, if either have been estimated.
The program will output a new |particle_set|, as well as a new |optimisation_set| in which the initial particle set has been replaced by the newly generated one.
That particle set can be fed into ``relion_refine``.

If a subtomogram orientation has been defined (see |particle_set|), then the subtomogram will be constructed in that coordinate system. If the approximate orientation of the particle is known a-priori from the surrounding geometry, this allows angle priors to be used in ``relion_refine`` to avoid searching through implausible orientations. In particular, for particles sampled from a manifold (using :ref:`program_tomo_sample_manifold`), the Z axis of the subtomogram coordinate-system is always perpendicular to the local manifold. A strong tilt-angle prior can then be applied to only search through orientations that do not tilt the particle too far away from that orientation, while leaving the remaining two angles unconstrained (i.e. the direction of tilt and the rotation around the Z axis).

Relevant program arguments:
---------------------------

- ``--i`` and/or ``--p``, ``--t`` and ``--mot``: input optimisation-set and/or its components (see |optimisation_set|).
- ``--b``: initial box size of the reconstruction. A sufficiently large box size allows more of the high-frequency signal to be captured that has been delocalised by the CTF.
- ``--crop``: cropped output box size. After construction, the resulting pseudo subtomograms are cropped to this size. A smaller box size allows the (generally expensive) refinement using ``relion_refine`` to proceed more rapidly.
- ``--bin``: downsampling (binning) factor. Note that this does not alter the initial or the cropped box size. The reconstructed region instead becomes larger.
- ``--cone_weight``: downweight a cone in Fourier space along the Z axis (as defined by the coordinate system of the particle). This is useful for particles embedded in a membrane, as it can prevent the alignment from being driven by the membrane signal (the signal of a planar membrane is localised within one line in 3D Fourier space). Note that the coordinate system of a particle is given by both the subtomogram orientation (if defined) *and* the particle orientation (see |particle_set|). This allows the user to first obtain a membrane-driven alignment, and to then specifically suppress the signal in that direction.
- ``--cone_angle``: the (full) opening angle of the cone to be suppressed, given in degrees. This angle should include both the uncertainty about the membrane orientation and its variation across the region represented in the subtomogram.
- ``--j``: number of threads used to reconstruct pseudo subtomograms in parallel. Each thread will require additional memory, so this should be set to the number of CPU cores available, unless the memory requirements become prohibitive.
- ``--o``: name of the output directory (that will be created).

Program output:
---------------

After running the program, the output directory (``--o`` argument) will contain the following items:

- **particles.star**: a new |particle_set| containing the file names of the reconstructed subtomograms. This file can be understood by ``relion_refine``
- **optimisation_set.star**: a new |optimisation_set| pointing to the new particle set.
- **Subtomograms/<**`particle_name`**>_data.mrc**: 3D images representing the data terms of all subtomograms.
- **Subtomograms/<** ``particle_name`` **>_weights.mrc**: the weight terms of all subtomograms. Each 3D image contains, concatenated along Z, an image describing the sums over all CTF² and an image describing the multiplicities.
- **note.txt**: a text file containing the command issued to run the program.

.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`