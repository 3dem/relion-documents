.. _sec_ini3d:

De novo 3D model generation
===============================

|RELION| uses a Stochastic Gradient Descent (SGD) algorithm, as was first introduced in the CryoSPARC program :cite:`punjani_cryosparc:_2017`, to generate a *de novo* :jobtype:`3D initial model` from the 2D particles.
Provided you have a reasonable distribution of viewing directions, and your data were good enough to yield detailed class averages in :jobtype:`2D classification`, this algorithm is likely to yield a suitable, low-resolution model that can subsequently be used for :jobtype:`3D classification` or :jobtype:`3D auto-refine`.


Running the job
---------------

Select the ``Select/class2d_template/particles.star`` file on the :guitab:`I/O` tab of the :jobtype:`3D initial model` jobtype.
Everything is aready in order on the :guitab:`CTF`.
Fill in the :guitab:`optimisation` tab as follows (leave the defaults for the angular and offset sampling):

:Number of classes: 1

     (Sometimes, using more than one class may help in providing a 'sink' for sub-optimal particles that may still exist in the data set.
     The additional argument ``--sgd_skip_anneal`` may then also be useful.  In this case, we will just use a single class in order to speed up things).

:Mask diameter (A): 200

     (The same as before).

:Flatten and enforce non-negative solvent: Yes

:Symmetry: C1

     (If you don't know what the symmetry is, it is probably best to start with a C1 reconstruction.
     Also, some higher-symmetry objects may be easier to solve by SGD in C1 than in their correct space group.
     This data set is great data, and would also work in the correct point group D2.
     However, to illustrate how to proceed from C1 to D2, we will run the SGD in C1.)

Typically, in first instance one would not change anything on the :guitab:`SGD` tab, as the default are suitable for many cases.
However, in order to speed things up for this tutorial, we will only perform half the default number of iterations.
Therefore change:

:Number of initial iterations: 25

:Number of in-between iterations: 100

:Number of final iterations: 25

On the :guitab:`Compute` tab, optimise things for your system.
You may well be able to pre-read the few thousand particles into RAM again.
GPU acceleration will also yield speedups, though multiple maximisation steps during each iteration will slow things down compared to standard 2D or 3D refinements or classifications.
We used an alias of `symC1` for this job.
Using 4 GPU cards, 5 MPI processes and 6 threads per MPI process, this run took approximately 15 minutes on our system.
If you didn't get that coffee before, perhaps now is a good time too...


Analysing the results
---------------------

Look at the output volume (``InitialModel/job015/run_it150_class001.mrc``) with a 3D viewer like UCSF :textsc:`chimera`.
If you recognise additional point group symmetry at this point, then you will need to align the symmetry axes with the main X,Y,Z axes of the coordinate system, according to |RELION|'s conventions.
Use the following command line instruction to do this:

::

    relion_align_symmetry --i InitialModel/job015/run_it150_class001.mrc \
      --o InitialModel/job015/run_it150_class001_alignD2.mrc --sym D2


And after confirming in UCSF :textsc:`chimera` or `relion_display` that the symmetry axes in the map are now indeed aligned with the X, Y and Z-axes, we can now impose D2 symmetry using:

::

    relion_image_handler --i InitialModel/job015/run_it150_class001_alignD2.mrc \
      --o InitialModel/job015/run_it150_class001_symD2.mrc --sym D2


The output map of the latter command should be similar to the input map.
You could check this by:

::

    relion_display --i InitialModel/job015/run_it150_class001_alignD2.mrc &
    relion_display --i InitialModel/job015/run_it150_class001_symD2.mrc &