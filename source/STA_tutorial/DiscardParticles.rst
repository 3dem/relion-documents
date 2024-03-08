.. _sec_sta_discardparticles:

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

Running 3D classification
----------------------------------

**[TODO: add explanation]**

On the :guitab:`I/O` tab, input the appropriate files as follows:

:Input optimisation set:: ""

:OR use direct entries?: Yes

:Input particle set:: Select/job018/particles.star

:Input tomogram set:: Tomograms/job007/particles.star

:Reference map:: Refine3D/job013/run_class001.mrc

On the :guitab:`Reference` tab, change the following two fields:

:Initial low-pass filter (A):: 60

:Symmetry:: C1

Leave the fields on the :guitab:`CTF` tab with their default values, then in the :guitab:`Optimisation` tab leave the default values for all fields except:

:Number of classes:: 9

:Mask diameter (A):: 230

On the :guitab:`Sampling` tab, change the fields:

:Peform image alignment?: Yes

:Angular sampling interval:: 1.8 degrees

:Perform local angular searches?: Yes

:Prior width on tilt angle (deg): 10

Ignore the :guitab:`Helix` tab and set the fields on the :guitab:`Compute` and :guitab:`Running` tabs to the same values as in the :jobtype:`3D auto-refine` jobs in the :ref:`sec_sta_refine3d_ini` section:

:Number of pooled particles:: 30

:Use GPU acceleration?: Yes

:Number of MPI procs:: 5

:Number of threads:: 6

On our computer with 2 GPUs, this job took around 3 hours.


Analysing the results of the 3D classification
----------------------------------






The procedure to perform 3D classification using pseudo-subtomograms is the same as in the single particle analysis pipeline, so you may find it useful to also read the description in :ref:`SPA tutorial<sec_class3d>`.


Discarding the bad classes
----------------------------------

