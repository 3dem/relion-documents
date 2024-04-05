.. _sec_sta_duplicateparticles:

Duplicate particles removal 
=================

Before continuing with higher-resolution refinement of the structure we have so far, now is a good time to discard any unwanted particles, which are either duplicates or low quality.
In this section, we address the problem of duplicate particles. 

As the initial particle picking consists of random sampling of positions on the annotated spheres, these positions are gradually refined into positions of particles in the tilt series that resemble projections of the structure being subtomogram averaged. 
Consequently, it is likely that multiple particle positions converge to the same, or very close, positions in the tilt series (and equivalently in the tomogram). 
This is problematic because, in addition to unnecessarily refining the same particle multiple times in each refinement cycle (and therefore wasting time and computational resources), the same particle can appear in both random halfsets during refinemt, which leads to overestimated resolution estimates, since the gold-standard FSC criterion is no longer satisfied. Therefore, duplicate particles must be removed from the particle set.

To do this, go to the :jobtype:`Subset selection` job-type, and on the :guitab:`I/O` tab, write the path of the previous job's output particles file in the appropriate field:

:Select classes from job:: ""
:OR select from micrographs.star:: ""
:OR select from particles.star:: Refine3D/job015/run_data.star

Leave all the other fields at their default values, except on the :guitab:`Duplicates` tab:

:OR\: remove duplicates?: Yes
:Minimum inter-particle distance(A): 30

      (Since the distance between two adjacent hexamers is approximately 75Å, we can reasonably assume that any particles closer than 30Å will eventually converge to the same particle, and therefore should be considered duplicates.)

We give this job the alias ``remove-dups`` and press the :runbutton:`Run!` button.
The duplicated particles are then removed and the resulting duplicate-free particle set is in ``Select/remove-dups/particles.star``.

In our workspace, this job removed 8937 duplicated particles from the initial 30596 particles.
