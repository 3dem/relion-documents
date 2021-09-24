.. _program_tomo_refine_ctf:

relion_tomo_refine_ctf
======================

This program estimates the astigmatic defoci of the individual tilt images, the ice thickness (which determines the overall signal intensity) and higher-order optical aberrations. 

**Defocus**: In tomography, the relative depth distances between particles are known from the 3D positions of the particles. 
Therefore, only one defocus value is estimated for all the particles in each tilt image.
Because of the often large number of particles in each tomogram, this value can typically be estimated to greater precision than in single-particle analysis, where the defocus of each particle has to be estimated independently.

**Ice-thickness**: A thicker sample permits fewer electrons to pass through, which reduces the scale of the signal.
In addition to the actual variation in sample thickness, the effective thickness of the ice also increases as the sample is tilted.
This program allows the user to estimate the signal intensity either independently for each tilt image, or by fitting the base thickness, the initial beam luminance and the surface normal of the sample assuming `Beer-Lambert's Law <https://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law>`_.
In the latter case, only one surface normal and base thickness are estimated for an entire tilt series, which allows for a more stable fit from tomograms with fewer particles.

**Higher-order optical aberrations**: This algorithm works analogously to ``relion_ctf_refine`` for single-particle analysis.
As in single-particle analysis, the aberrations are estimated per optics group.
This allows the user to group particles that are expected to share the same aberrations, either by image region or by subset of tilt series, or both.
Both symmetrical (even) and antisymmetrical (odd) aberrations are supported.
A detailed description of the aberrations estimation algorithm can be found in the |RELION| `aberrations paper <https://journals.iucr.org/m/issues/2020/02/00/fq5009/>`_.

The estimated defocus and ice-thickness values are written into the output |tomogram_set| and the aberrations into the |particle_set|, both of which replace the given sets in the output |optimisation_set|.


General program arguments:
--------------------------

- ``--i`` and/or ``--p``, ``--t``, ``--mot``, ``--ref<1/2>``, ``--mask`` and ``--fsc``: input optimisation-set and/or its components (see |optimisation_set|).
- ``--b``: box size to be used for the estimation. Note that this can be larger than the box size of the reference map. A sufficiently large box size allows more of the high-frequency signal to be captured that has been delocalised by the CTF.
- ``--j``: number of threads to be used. This should be set to the number of CPU cores available.
- ``--o``: name of the output directory (that will be created).


Defocus-estimation arguments:
-----------------------------

- ``--do_defocus``: instructs the program to estimate the defoci.
- ``--do_reg_defocus``: applies defocus regularisation. High-tilt images do not offer enough signal to recover the defocus value precisely. The regularisation forces the estimated defoci to assume similar values within a given tilt series, which prevents those high-tilt images from overfitting.
- ``--lambda``: defocus regularisation strength.
- ``--d0`` and ``--d1``: minimal and maximal defocus offset (from the initial value) to scan in the initial part of the defocus estimation. This scan allows the algorithm to escape a local minimum in case it has been intialised in one. Afterwards, a local astigmatic-defocus refinement is performed. Both values are assumed to be given in Å.
- ``--ds``: number of steps between ``--d0`` and ``--d1``.
- ``--kmin``: Lowest spatial frequency to consider, in Å.
- ``--reset_to_common``: Reset the CTFs of all tilts to a common one prior to local refinement.


Ice-thickness estimation arguments:
-----------------------------------

- ``--do_scale``: instructs the program to estimate the signal scale or ice thickness.
- ``--per_frame_scale``: estimate the signal-scale parameter independently for each tilt. If not specified, the ice thickness, beam luminance and surface normal are estimated instead. Those three parameters then imply the signal intensity for each frame. Due to the smaller number of parameters, the ice thickness model is more robust to noise. By default, the ice thickness and surface normal will be estimated per tilt-series, and the beam luminance globally.
- ``--per_tomogram_scale``: estimate the beam luminance separately for each tilt series. This is not recommended.


Aberrations-estimation arguments:
---------------------------------

- ``--do_even_aberrations``: instructs the program to estimate the even (i.e. symmetrical) aberrations. These deform the shape of the CTF.
- ``--do_odd_aberrations``: instructs the program to estimate the odd (i.e. anti-symmetrical) aberrations. These rotate the phases of the observed images.
- ``--ne``: number of Zernike bands used to fit the even aberrations. A greater number can quickly lead to overfitting. The user is advised to keep this value at 4 - this will allow for a correction to the spherical aberration term, as well as four-fold and first- and second-order two-fold astigmatism.
- ``--no``: number of odd Zernike bands. The user is advised to keep this value at 3 - this will allow for beam tilt and three-fold astigmatism.


Program output:
---------------

After running the program, the output directory (``--o`` argument) will contain the following items:

- **tomograms.star**: a new |tomogram_set| containing the newly estimated defoci (``rlnDefocus<U/V>`` and ``rlnDefocusAngle``) and ice thickness values. Note that only the signal scale (``rlnCtfScalefactor``) implied by the ice thickness is used by other programs.
- **particles.star**: a new |particle_set| containing the estimated aberrations.
- **optimisation_set.star**: a new |optimisation_set| pointing to the new tomogram and particle sets.
- **note.txt**: a text file containing the command issued to run the program.
- **group_<** ``optics_group`` **>_<even/odd>_phase_per-pixel.mrc**: visualisations showing the optimal phase-shift for each pixel. Inspecting this allows the user to ensure that the estimated pattern is not mere noise.
- **group_<** ``optics_group`` **>_<even/odd>_phase_nonlinear-fit.mrc**: visualisations of the fits using Zernike polynomials, which will be used by the other programs.


.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
