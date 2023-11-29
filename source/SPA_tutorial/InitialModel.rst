.. _sec_ini3d:

De novo 3D model generation
===============================

|RELION|-4.0 uses a gradient-driven algorithm to generate a *de novo* :jobtype:`3D initial reference` from the 2D particles.
As of release 4.0, this algorithm is different from the SGD algorithm in the CryoSPARC program :cite:`punjani_cryosparc:_2017`.
Provided you have a reasonable distribution of viewing directions, and your data were good enough to yield detailed class averages in :jobtype:`2D classification`, this algorithm is likely to yield a suitable, low-resolution model that can subsequently be used for :jobtype:`3D classification` or :jobtype:`3D auto-refine`.


Running the job
---------------

Select the ``Select/job014/particles.star`` file on the :guitab:`I/O` tab of the :jobtype:`3D initial reference` jobtype.
Everything is aready in order on the :guitab:`CTF`.
Fill in the :guitab:`Optimisation` tab as follows (leave the defaults for the angular and offset sampling):

:Number of VDAM mini-batches: 100

     (The VDAM algorithm will loop over mini-batches, which contain only hundreds to thousands of particles each.)

:Regularisation parameter T: 4

     (The default is 4 for 3D runs.)

:Number of classes: 1

     (Sometimes, using more than one class may help in providing a 'sink' for sub-optimal particles that may still exist in the data set.
     In this case, which is quite homogeneous, a single class should work just fine.)

:Mask diameter (A): 200

     (The same as before).

:Flatten and enforce non-negative solvent: Yes

:Symmetry: D2

:Run in C1 and apply symmetry later?: Yes
				      
     (The actual refinement will be run in C1, which has been observed to converge better than running VDAM in higher symmetry groups.
     After the refinement, the ``relion_align_symmetry`` program is run automatically to detect the symmetry axes and the symmetry will be applied.)


On the :guitab:`Compute` tab, set:

:Use parallel disc I/O?: Yes

:Number of pooled particles: 30


:Pre-read all particles into RAM?: Yes

     (Again, this is only possible here because the data set is small. For your own data, you would like write the particles to a scratch disk instead, see below.)

:Copy particles to scratch directory: \ 

:Combine iterations through disc?: No

:Use GPU acceleration?: Yes

:Which GPUs to use: 0,1,2,3

On the :guitab:`Running` tab, set:

:Number of MPI procs: 1

     (Remember that the gradient-driven algorithm cannot be run with multiple MPI processes.)

:Number of threads: 12

Using the settings above, this job took 2 minutes on our system.


Analysing the results
---------------------

You can look at the output map in 2D slices through the 3D map by selecting ``InitialModel/job015/initial_model.mrc`` from the :button:`Display:` button. We like looking at 3D maps in 2D slices, as it is a good way to assess artifacts, for example streaks in the solvent region. You may also want to look at your map in 3D, with a 3D viewer like UCSF :textsc:`chimera`.

