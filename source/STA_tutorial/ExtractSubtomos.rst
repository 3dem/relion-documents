.. _sec_sta_makepseudosubtomo:

Extract subtomos
================

Now that we have 3D particle coordinates, the :jobtype:`Extract` job extracts the relevant cropped areas of the tilt series images for each individual particle and saves them as CTF-premultiplied extracted 2D image stacks (or as 3D volumes) on the disk for further processing using the `relion_refine` program. As these are not really boxed out of a 3D tomogram, we call these particles pseudo-subtomograms. 

The pseudo-subtomograms can be either 2D stacks or 3D volumes (where Fourier slices of the 2D images are combined in 3D). While both options are available in :jobtype:`Extract`, we strongly recommend working with 2D stacks, as they take less disk space and, in the case of reconstruction and refinement, this saves an interpolation step and therefore avoids artifacts related to pseudo-subtomogram construction.

Pseudo-subtomogram particles are described by a |particle_set| star file, as well as a |tomogram_set| star file. In addition, if :jobtype:`Bayesian polishing` has been performed, the pseudo-subtomograms are also described by a |trajectory_set| star file. For convenience, a single |optimisation_set| star file provides links to the corresponding three star files. After a :jobtype:`Bayesian polishing` and/or :jobtype:`CTF refinement` job, a new set of updated pseudo-subtomos particles should be extracted prior to further refinement or classification by `relion_refine`.

We will start by extracting pseudo-subtomograms in relatively large boxes with a large (binned) pixel size to speed up the initial calculations for obtaining a *de novo* initial model. Select the :jobtype:`Extract subtomos` jobtype, and on the :guitab:`IO` tab set:


:Input optimisation set: Picks/job008/optimisation_set.star
			
    (You can see how this file refers to the inidividual |particle_set| and |tomogram_set| star files using ``cat Picks/job008/optimisation_set.star``.)

:OR use direct entries?: No
			 
:Input particle set: ""
		     
:Input tomogram set: ""
		     
:Input trajectory set: ""

On the :guitab:`Reconstruct` tab, we set:

:Binning factor: 6

    (This will result in a pixel size of 8.1 Angstroms...)
    
:Box size (binned pix): 192 

    (This is the box size for the original cropping of the particle from the tilt series images. This box is often set larger than the cropped box size below, because a larger box will allow more of the high-frequency signal to be captured by pre-multiplication of the CTF.)
    
:Cropped box size (binned pix): 96

    (This is the final box size of the particles. If this value is smaller than the original box size above, then a second cropping operation is performed after the CTF pre-multiplication.) 
				
:Maximum dose (2/A^2): 50

	(Tilt series frames with a dose higher than this maximum dose (in electrons per squared Angstroms) will not be included in the 3D pseudo-subtomogram, or in the 2D stack. For 2D stacks, this will reduce disc I/O operations and increase speed.)
	
:Minimum nr. frames: 1

	(Some particles are outside the field of view (i.e. invisible) in high-tilt images. When set to a positive value, each particle needs to be visible in at least this number of tilt series frames with doses below the maximum dose to be written out as a pseudo-subtomogram.)

:Write output as 2D stacks?: Yes

    (This is new as of relion-5 and the preferred way of generating pseudo-subtomograms. If set to No, then relion-4 3D pseudo-subtomograms will be written out. Either can be used in subsequent refinements and classifications, but 2D stacks take up less disk space and give slightly better results in 3D refinements. In some cases, we have noticed that 3D pseudo-subtomograms behave better in the VDAM algorithm of :jobtype:`3D initial reference` jobs, which is why one can still write in this format too.)
			     
:Write output in float16?: Yes

	(This will save a factor of 2 in disk space.)

On the :guitab:`Running` tab, we aim to saturate the processes on our 112-core CPU node by setting:

:Number of MPI procs: 5
:Number of threads: 24

Note that the MPI versions of this program (and those of :jobtype:`Reconstruct particle`, :jobtype:`CTF refinement` and :jobtype:`Bayesian polishing` are parallelized at the level of individual tomograms. Therefore, the ``Number of MPI processes`` should not exceed the number of tomograms.

Using the settings above, this job took around 13 minutes on our system.

Your pseudo-subtomogram 2D stacks will be stored into MRC files in a new directory called ``Extract/job009/Subtomograms/TS_01/1_stack2d.mrcs`` etc. The program will also write out an updated |particle_set| as ``Extract/job009/particles.star`` and a new |optimisation_set| as ``Extract/job009/optimisation_set.star``.







.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
