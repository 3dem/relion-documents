.. _sec_sta_class3d:

Duplicate removal and 3D classification
=================

Having obtained a bin 2 map, now is a good time to remove from our dataset any unwanted particles that will prevent us from correctly estimating the resolution of the structure or from obtaining a higher resolution structure.

Discarding duplicate particles
----------------------------------

**[TODO: add explanation]**

Select the :jobtype:`Subset selection` job-type, and on the :guitab:`I/O` tab, write the path of the previous job's particles file in the appropriate field:

:Select classes from job:: ""
:OR select from micrographs.star:: ""
:OR select from particles.star:: Refine3D/job013/run_data.star

Leave all the other fields at their default values, except on the :guitab:`Duplicates` tab:

:OR remove duplicates?: Yes
:Minimum inter-particle distance(A): 30

      (Since the distance between two adjacent hexamers is approximately 75Å, we can reasonably assume that any particles closer than 30Å will eventually converge to the same particle, and therefore should be considered to be duplicates.)

We give this job the alias ``remove-dups``
Running the job will lead to the duplicated particles being removed, and the resulting duplicate-free particle set is in ``Select/job018/particles.star``.

Discarding bad particles through 3D classification
----------------------------------

**[TODO: add explanation]**

On the :guitab:`I/O` tab, input the appropriate files as follows:

:Input optimisation set:: ""

:OR use direct entries?: Yes

:Input particle set: Select/job018/particles.star





The procedure to perform a 3D classification using pseudo-subtomograms is strictly the same as described in :ref:`SPA tutorial<sec_class3d>`.

