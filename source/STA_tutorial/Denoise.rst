.. _sec_sta_denoise:
  
Denoise tomograms
=================

For denoising tomorgams, the :jobtype:`Denoise tomograms` is a wrapper of ``Cryo-CARE`` :cite:`buchholz_cryo-care_2019`. 

The first step is to train a neural network on patches from the odd and even frame tomograms using the NOISE2NOISE approach. Therefore, denoising only works if both ``Save images for denoising?`` in the :jobtype:`Motion correction` job and ``Generate tomograms for denoising?`` in the :jobtype:`Reconstruct tomograms` were both set to ``Yes``.
The second step is to apply the trained neural network to patches in the noisy tomograms to obtained the denoised versions.
Each of the two steps will be carried out as a separate :jobtype:`Denoise tomograms` job, as described below.




Train
-----

For the training step, select the :jobtype:`Denoise tomograms` job type, and on the :guitab:`I/O` tab, set:

:Input tomograms.star:: Tomograms/job006/tomograms.star

:Directory with cryoCARE execuables:: "..."

      (The path to the cryoCARE directory on your local machine)

:Which GPU to use:: 0


On the :guitab:`CryoCARE: Train` tab, set:

:Train denoising model:: Yes

:Tomograms for model training:: TS_01:TS_03:TS_43:TS_45:TS_54

:Number of sub-volumes per tomogram:: 1200

:Sub-volume dimensions (px):: 72

On the :guitab:`CryoCARE: Predict` tab, set:

:Generate denoised tomograms:: No

and press the :runbutton:`Run` button to run the job.

On our machine, this job took under 1.5 hours to run.

Predict
-------

For the actual denoising step, select a new :jobtype:`Denoise tomograms` job, and set the fields on the :guitab:`I/O` tab to the same values as in the previous :jobtype:`Denoise tomograms` job. On the :guitab:`CryoCARE: Train` tab, set:

:Train denoising model:: No

and on the :jobtype:`CryoCARE: Predict` tab, set:

:Generate denoised tomograms:: Yes

:Path to denoising model:: Denoise/job007/denoising_model.tar.gz

	(The model trained in the previous Denoise job.)

and leave the other fields set to their default values. Running this job is much faster than the training job and in our workspace it took around one minute.

Analysing the results
---------------------

The |tomogram_set| resulting from the ``Predict`` step (in our case the file ``Denoise/job008/tomograms.star``) contains the additional column ``rlnTomoReconstructedTomogramDenoised`` pointing to the denoised tomograms, which can be visualised, for example, using IMOD or Napari. 
As mentioned in the :ref:`sec_sta_reconstructtomo` section, the denoised tomograms, just like the initial reconstructed odd/even frame tomograms, are used for visualisation and particle picking only, and will not be used for further processing in the sub-tomogram averaging pipeline once the particles have been annotated.


.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
