DynaMight: exploring motions
============================

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

On our, relatively old, 1080 GPU, estimating the deformations took xxx hours. To visualise the flexibility in the beta-galactosidase complex, we use a continuation of the :jobtype:`DynaMight flexibility` job, where on the :guitab:`Tasks` tab we set:

:Checkpoint file:: DynaMight/job034/forward_deformations/checkpoints/checkpoint\_final.pth

:Do visualization?: Yes

:Half-set to visualize:: 1

     (You can visualize either halfset 1 or halfset 2. There is another option where you visualize halfset 0. In that case, you can visualize error estimates on the 3D deformations for a validation set of 10% of your particles)

:Do inverse-deformation estimation?: No

:Do deformed backprojection?: No

Running this by pressing the :runbutton:`Continue!` button will launch a viewer that was written in ``napari``. It is quite a heavy-handed tool, so you will need to run this viewer locally, while also needing a GPU (specified on the :guitab:`I/O` tab, to perform some of the calculations...

By clicking on the colourful representation of latent space on the right, the 3D viewer will display the corresponding deformed state of the consensus structure. On the bottom right, by selecting ``trajectory`` under the ``action`` menu, one can draw a line through latent space using the middle-mouse button. This will create a movie of the states in the 3D viewer, which you can play with the triangle button underneath the 3D viewer. As said before, this looks underwhelming for beta-galactosidase, which basically has very little flexibility. You can use the right-mouse to zoom in on the tips, where perhaps you can see some imnute movements?

You can save maps or movies using the button on the bottom right. The individual states of such a movie would be saved as maps in MRC format here: ``DynaMight/job138/movies/movie01_half1/``. You can then load all these maps into a 3D visualisation program, like UCSF |chimera|, and recreate the movie there. 


Estimating inverse deformations
-------------------------------

The 3D deformations are defined from the consensus positions of the Gaussians to their new position. For use in deformed weighted backprojection, we first need estimates for the inverse deformations at every point in the 3D Cartesian space. For this, DynaMight also uses a neural network. We can train it by using another continuation of the same :jobtype:`DynaMight flexibility` job, where on the :guitab:`Tasks` tab we now set:

:Checkpoint file:: DynaMight/job034/forward_deformations/checkpoints/checkpoint\_final.pth

:Do visualization?: No

:Do inverse-deformation estimation?: Yes

:Number of epochs to perform: 200

:Store deformations in RAM?: No

     (If set to Yes, dynamight will store all deformations in the GPU memory, which will speed up the calculations, but you need to have enough GPU memory to do this. We could not do this on our small 1080s.)
     
:Do deformed backprojection?: No

Running this by pressing the :runbutton:`Continue!` button took xxx hours on one of our 1080s. 

Deformed backprojection
-----------------------

Finally, the resulting inverse deformations can then be used for a deformed backprojection that attempts to reconstruct an improved version of the consensus map, where densities for each particle are warped into non-straight lines in the backprojection in an attempt to "un-do" their deformations. Again, we use a continuation of the same :jobtype:`DynaMight flexibility` job, where on the :guitab:`Tasks` tab we set:


:Checkpoint file:: DynaMight/job034/forward_deformations/checkpoints/checkpoint\_final.pth

:Do visualization?: No

:Do inverse-deformation estimation?: No
    
:Do deformed backprojection?: Yes

:Backprojection batchsize:: 2

     (Batches are processes in parallel on the GPU. Again, because our 1080s don't have a lot of memory, we could only run with a batchsize of 2. If you have a larger GPU, you could try and use more, e.g. 5 or 10.)

This took xxx hours on our system. The resulting half-maps can be used for a standard :jobtype:`Post-processing` job. In this case, nothing really interesting happens as there are hardly any deformations. The resolution actually decreases by about 0.5 Angstrom, probably because the deformed backprojection algorithm is not as good as good as the Fourier inversion algorithm for structurally homogeneous data sets. More interesting examples of deformed backprojection reconstructions are in the DynaMight paper :cite:`schwab_dynamight_2023`.



     
