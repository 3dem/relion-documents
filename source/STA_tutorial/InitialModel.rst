.. _sec_sta_ini3d:

De novo 3D model generation
===============================

|RELION|-4.0 uses a gradient-driven algorithm to generate a *de novo* :jobtype:`3D initial model` from the pseudo-subtomograms.
As of release 4.0, this algorithm is different from the SGD algorithm in the CryoSPARC program :cite:`punjani_cryosparc:_2017`.
Provided you have a reasonable distribution of angular directions, this algorithm is likely to yield a suitable, low-resolution model that can subsequently be used for :jobtype:`3D classification` or :jobtype:`3D auto-refine`.

The sample used in is tutorial usually allows for obtaining initial orientations, normal to the spheroidal surface, during the picking process which could be used as initial reference.
However, here we will show how to obtain a *de novo* model without any prior knowledge.

Running the job
---------------

Select the ``PseudoSubtomo/job007/particles.star`` file on the :guitab:`I/O` tab of the :jobtype:`3D initial model` jobtype.
Everything is already in order on the :guitab:`CTF`.
Fill in the :guitab:`Optimisation` tab as follows (leave the defaults for the angular and offset sampling):

:Number of iterations: 100

     (The algorithm will loop over mini-batches, which contain only hundreds to thousands of particles.)

:Number of classes: 1

     (Sometimes, using more than one class may help in providing a 'sink' for sub-optimal particles that may still exist in the data set.
     In this case, which is quite homogeneous, a single class should work just fine.)

:Mask diameter (A): 230

     (The same as before).

:Flatten and enforce non-negative solvent: Yes

:Symmetry: C6

     (The actual refinement will be run in C1, which has been observed to converge better than performing it in higher symmetry groups.
     After the refinement, the ``relion_align_symmetry`` program is run to automatically detect the symmetry axes and the symmetry will be applied.)

:Initial angular sampling:: 15 degrees

     (The default angular and offset samplings should be fine for most cases, perhaps with the exception of highly symmetric particles like viruses, which may require finer samplings.)

:Offset search range (pix):: 6

:Offset search step (pix):: 2


On the :guitab:`Compute` tab, set:

:Use parallel disc I/O?: Yes

:Number of pooled particles:: 16

:Skip gridding?: Yes

:Pre-read all particles into RAM?: No

:Copy particles to scratch directory: \


:Combine iterations through disc?: No

:Use GPU acceleration?: Yes

:Which GPUs to use: 0

On the :guitab:`Running` tab, set:

:Number of MPI procs: 1

     (Remember that the gradient-driven algorithm does not scale well with MPI.)

:Number of threads: 8

Using the settings above, this job took 45 minutes on our system.
If you didn't get that coffee before, perhaps now is a good time too...


Analysing the results
---------------------

You could look at the output map from the gradient-driven algorithm (``InitialModel/job008/run_it100_class001.mrc``) with a 3D viewer like UCSF :textsc:`chimera`.
You should probably conform that the symmetry point group was correct and that the symmetry axes were identified correctly.
If so, the symmetrised output map (``InitialModel/job008/initial_model.mrc``) should look similar to the output map from the gradient-driven algorithm.

