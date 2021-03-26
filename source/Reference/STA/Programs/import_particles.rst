.. _program_tomo_import_particles:

relion_tomo_import_particles
============================

This program imports a set of 3D coordinates and (optionally) Euler angles to construct a new :ref:`particle set <sec_sta_particle_set>`

The 3D coordinates can be provided either in one big .star file, or as a set of shorter files, one for each tomogram.

If all the coordinates are provided as one .star file, it has to contain at least the following columns:

- **rlnTomoName**: name of the tomogram to which a particle belongs.
- **rlnCoordinate<X/Y/Z>**: the 3D coordinates within that tomogram.

If the input file also contains the particle angle columns **rlnAngle<Rot/Tilt/Psi>**, or any other column, they are also kept.

In case the other format is chosen, then the input file only needs to contain the following columns: **rlnTomoName** and **rlnTomoImportParticleFile**.
The latter column points to a set of files (one for each tomogram) that contain the coordinates (**rlnCoordinate<X/Y/Z>**) and (optionally) angles (**rlnAngle<Rot/Tilt/Psi>**).

Program arguments:
------------------

- ``--i``: Input ``.star`` file containing a set of particle coordinates or a set of names of files containing those.
- ``--t``: Input :ref:`tomogram set <sec_sta_tomogram_set>` which particles belong.
- ``--o``: Output directory.


