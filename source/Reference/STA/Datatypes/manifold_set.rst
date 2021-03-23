.. _sec_sta_manifold_set:

Manifold set
============

The manifold set is typically named ``manifolds.star``, and it lists all the manifolds defined in all tomograms.
In this context, all manifolds are 2D surfaces embedded in 3D space.
Currently, only *spheres* and *spheroids* are supported.
Spheroids are sphere-like surfaces (blobs) whose deviation from a sphere is expressed using the `Spherical Harmonics <https://en.wikipedia.org/wiki/Spherical_harmonics>`_ basis.
Spheres can be imported by using the program :ref:`program_tomo_add_sphere`, while spheroids can be fitted to membrane vesicles from initial spheres using the program :ref:`program_tomo_fit_blobs_3d`.
	
The manifolds file contains one table for each tomogram, each named after the corresponding *tomogram name* (see :ref:`tomogram set <sec_sta_tomogram_set>`).
Each row of a table corresponds to one manifold, listing its:

- number (``rlnTomoManifoldIndex``),
- type (``rlnTomoManifoldType``),
- and parameters (``rlnTomoManifoldParams``).

The parameter set varies depending on the manifold type: for spheres, the first 3 coefficients describe the position of the centre of the sphere, while the fourth describes its radius. For spheroids, the first 3 coefficients also describe the position, while the remaining ones are coefficients that describe the contribution of each Spherical Harmonics basis function. Please note that for spheroids, the fourth parameter is *not* equal to the radius, but to the radius multiplied by :math:`{2\sqrt \pi}`.
Every consecutive parameter then distorts the sphere of that radius by applying higher-order Spherical Hamonics functions.

Given a set of manifolds, the program :ref:`program_tomo_sample_manifold` allows the user to sample particles along each manifold, generating a novel :ref:`tomogram set <sec_sta_particle_set>`.
Those particles are aligned such that their Z direction points perpendicularly to the surface normal of the manifold.
This allows strong tilt priors to be applied during refinement in order to save time.
