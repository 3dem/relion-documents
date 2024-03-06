.. _sec_sta_ini3d:

De novo 3D model generation
===============================

**Changes have been made for relion-5 up to this point; Please bear with us, as we modify the rest of the tutorial for relion-5!**

**[TODO: update the exact parameters after finishing all the VDAM runs]**

|RELION|-5.0 uses a gradient-driven algorithm to generate a *de novo* :jobtype:`3D initial reference` from the pseudo-subtomograms.
This algorithm is different from the SGD algorithm in the CryoSPARC program :cite:`punjani_cryosparc:_2017`.
Provided you have a reasonable distribution of angular directions, this algorithm is likely to yield a suitable, low-resolution model that can subsequently be used for :jobtype:`3D classification` or :jobtype:`3D auto-refine`.

The sample and the sphere picking procedure used in this tutorial make it possible to obtain initial orientations normal to the spheroidal surface during the picking process, which can be used to obtain an initial reference using the :jobtype:`Reconstruct particle` job, as explained in the :ref:`sec_sta_reconstructpart` section. The map obtained this way will be used as a reference for the first :jobtype:`3D auto refine` job at bin 6, which will be explained in the :ref:`sec_sta_refine3d_ini` section.

However, here we will show how to obtain a *de novo* model without any prior knowledge, using the VDAM algorithm. We have noticed that in some cases VDAM generates better initial models using 3D pseudo-sobtomograms rather than 2D stacks, so you may want to try both for your own dataset. To generate 3D stacks, a new :jobtype:`Extract subtomos` job should be run with the **Write output as 2D stacks?** option set to ``No`` (see the :ref:`sec_sta_makepseudosubtomo` section).

Running the job
---------------

Select the ``Extract/job009/optimisation_set.star`` file on the :guitab:`I/O` tab of the :jobtype:`3D initial reference` jobtype.
Everything is already in order on the :guitab:`CTF`.
Fill in the :guitab:`Optimisation` tab as follows:

:Number of VDAM mini-batches: 100

     (The number of iterations of VDAM. The algorithm will loop over mini-batches, which contain only hundreds to thousands of particles.)

:Regularisation parameter T: 4

    (Values greater than 1 for this regularisation parameter (T in the JMB2011 paper) put more weight on the experimental data. Values around 2-4 have been observed to be useful for 3D initial model calculations.)

:Number of classes: 1

     (Sometimes, using more than one class may help in providing a 'sink' for sub-optimal particles that may still exist in the data set.
     In this case, which is quite homogeneous, a single class should work just fine.)

:Mask diameter (A): 230

     (The same as before).

:Flatten and enforce non-negative solvent: Yes

:Symmetry: C6

:Run in C1 and apply symmetry later: No

     (If set to yes, the actual refinement will be run in C1, which has been observed to converge better than performing it in higher symmetry groups.
     After the refinement, the ``relion_align_symmetry`` program is run to automatically detect the symmetry axes and the symmetry will be applied.)

:Prior width on tilt angle (deg): 10
    
    (Since the picking gives tilt angles so that the particles are normal to surface of the pseudo-spheres, we enforce this prior knowledge here.)

On the :guitab:`Compute` tab, set:

:Use parallel disc I/O?: Yes

:Number of pooled particles:: 30

:Pre-read all particles into RAM?: No

:Copy particles to scratch directory: ""


:Combine iterations through disc?: No

:Use GPU acceleration?: Yes

:Which GPUs to use: 0

On the :guitab:`Running` tab, set:

:Number of MPI procs: 1

     (Remember that the gradient-driven algorithm does not scale well with MPI.)

:Number of threads: 8

Using the settings above, this job took 90 minutes on our system.
If you didn't get that coffee before, perhaps now is a good time too...


Analysing the results
---------------------

You could look at the output map from the gradient-driven algorithm (``InitialModel/job010/run_it100_class001.mrc``) with a 3D viewer like UCSF :textsc:`chimera`.
If **Run in C1 and apply symmetry later** was set to ``yes``, 
you should probably confirm that the symmetry point group was correct and that the symmetry axes were identified correctly.
If so, the symmetrised output map (``InitialModel/job010/initial_model.mrc``) should look similar to the output map from the gradient-driven algorithm.

