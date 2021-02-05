.. _sec_ini3d:

De novo 3D model generation
===============================

|RELION|-3.2 uses a gradient-driven algorithm to generate a *de novo* :jobtype:`3D initial model` from the 2D particles. 
As of release 3.2, this algorithm is different from the SGD algorithm in the CryoSPARC program :cite:`punjani_cryosparc:_2017`.
Provided you have a reasonable distribution of viewing directions, and your data were good enough to yield detailed class averages in :jobtype:`2D classification`, this algorithm is likely to yield a suitable, low-resolution model that can subsequently be used for :jobtype:`3D classification` or :jobtype:`3D auto-refine`.


Running the job
---------------

Select the ``Select/job014/particles.star`` file on the :guitab:`I/O` tab of the :jobtype:`3D initial model` jobtype.
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
     However, to illustrate how to proceed from C1 to D2, we will run the gradient-driven algorithm in C1.)

Typically, in first instance one would not change anything on the :guitab:`Optimisation` tab, as the default are suitable for many cases.
Just make sure that the mask diameter is adequate for your particle:

:Mask diameter (A):: 200

On the :guitab:`Compute` tab, set:

:Use parallel disc I/O?: Yes

:Number of pooled particles:: 3

:Skip padding?: Yes

:Skip gridding?: Yes

:Pre-read all particles into RAM?: Yes

     (Again, this is only possible here because the data set is small. For your own data, you would like write the particles to a scratch disk instead, see below.)

:Copy particles to scratch directory: \ 

:Combine iterations through disc?: No

:Use GPU acceleration?: Yes

:Which GPUs to use: 0

On the :guitab:`Running` tab, set:

:Number of MPI procs: 1

     (Remember that the gradient-driven algorithm does not scale well with MPI.)

:Number of threads: 12

Using the settings above, this job took xx minutes on our system.
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
