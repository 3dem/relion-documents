DynaMight: fitting motions
==========================

As of release 5.0, |RELION| comes with a machine-learning approach for the analysis of molecular motions and flexibility called ``DynaMight`` :cite:`schwab_dynamight_2023`. DynaMight will fit molecular motions for each experimental particle image as a 3D deformation field, which is learnt using a variational auto-encoder. It also implements functionality to calculate a pseudo-inverse 3D deformation field that can then be used in a deformed weighted backprojection algorithm to obtain an improved 3D reconstruction of the consensus structure.

Beta-galactosidase is not a floppy protein, therefore running DynaMight on this data set will not be exciting! The below just walks you through the steps, so you learn how to run DynaMight jobs for your own data set.


Estimating the motions
----------------------

 We will use the :jobtype:`DynaMight flexibility` job type. On the :guitab:`I/O` tab set:

:Input images STAR file:: Refine3D/job029/run\_data.star

:Consensus map:: Refine3D/job029/run\_class001.mrc

:Number of Gaussian:: 8000	       

     (Describing flexibility at higher resolutions will require more Gaussians. As a rule of thumb, use 1-2 Gaussians per amino acid or nucleotide in your complex. The beta-galactosidase tetramer has just over 4x1042 amino acids, so we will use 8000 Gaussians here. The more Gaussians you use, the longer this will take... so you may want to run smaller tests too. Note that running with more than 30,000 Gaussians will be difficult in terms of memory unless you have a very large GPU.)

:Initial map threshold (optional):: 0.015

     (This is a threshold at which flexible regions still show in 3D visualisation tools like UCSF :textsc:`chimera`, but you should avoid the appearance of noisy density islands in the solvent region at this threshold.)

:Regularization factor:: 1

:Which (single) GPU to use:: 0

     (For now, DynaMight only uses one GPU at a time.)

:Preload images in RAM?: Yes
			 
     (As we only have a few thousand, we can read all particles in RAM and save time.)

     
For nowm ignore the :guitab:`Tasks` tab; on the :guitab:`Running` tab set:

     :Number of threads:: 4
			

Visualising the deformations
----------------------------

On our, relatively old, 1080 GPU, estimating the deformations took xxx hours.

Running with 8 MPI processes, this job took approximately 7 minutes.
The output is a file called ``LocalRes/job031/relion_locres.mrc`` that may be used in UCSF :textsc:`chimera` to color the `Postprocess/job030/postprocess.mrc` map according to local resolution.
This is done using ``[Tools]-[Volume data]-[Surface color]``, and then select ``by volume data value`` and browse to the ``resmap`` file.

Unique to the |RELION| option is the additional output of a locally-filtered (and sharpened map), which may be useful to describe the overall variations in map quality in a single map.
This map is saved as ``LocalRes/job031/relion_locres_filtered.mrc`` and can be visualised directly in UCSF :textsc:`chimera` (and optionally also coloured by local resolution as before).

