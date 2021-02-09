.. _sec_bayesian_polishing:

Bayesian polishing
==================

|RELION| also implements a Bayesian approach to per-particle, reference-based beam-induced motion correction.
This approachs aims to optimise a regularised likelihood, which allows us to associate with each hypothetical set of particle trajectories a prior likelihood that favors spatially coherent and temporally smooth motion without imposing any hard constraints.
The smoothness prior term requires three parameters that describe the statistics of the observed motion.
To estimate the prior that yields the best motion tracks for this particular data set, we can first run the program in 'training mode'.
Once the estimates have been obtained, one can then run the program again to fit tracks for the motion of all particles in the data set and to produce adequately weighted averages of the aligned movie frames.


Running in training mode
------------------------

Using 16 threads in parallel, this job took almost 2 hours on our computer...
If you do not want to wait for this, you can just proceed to `the next section <sec_polish>`_ and use the sigma-values from our precalculated results, which are already given in that section.
For many data sets the default parameters on the GUI (:math:`\sigma_{\text{vel}}=0.2; \sigma_{\text{div}}=5000; \sigma_{\text{acc}}=2`) will also perform well, so people often skip training for :jobtype:`Bayesian polishing`.

If you do want to run the training job yourself, on the :guitab:`I/O` tab of the :jobtype:`Bayesian polishing` job-type set:

:Micrographs (from MotionCorr):: MotionCorr/job002/corrected\_micrographs.star

:Particles (from Refine3D or CtfRefine):: Refine3D/job025/run\_data.star

     (These particles will be polished)

:Postprocess STAR file: PostProcess/job026/postprocess.star

     (the mask and FSC curve from this job will be used in the polishing procedure.)

:First movie frame:: 1

:Last movie frame:: -1

     (Some people throw away the first or last frames from their movies.
     Note that this is **not recommended** when performing Bayesian polishing in |RELION|.
     The B-factor weighting of the movie frames will automatically optimise the signal-to-noise ratio in the shiny particles, so it is best to include all movie frames.)

:Extraction size (pix in unbinned movie): -1

     (This option can be used to extract polished particles in a box with a different size than the ones from the input refinement above.
     It is irrelevant for a training job.)

:Re-scaled size (pixels): -1

     (This option can be used to re-scale the polished particles to a different size than the ones from the input refinement above.
     It is irrelevant for a training job.)

On the :guitab:`Train` tab set:

:Train optimal parameters?: Yes

:Fraction of Fourier pixels for testing:: 0.5

     (Just leave the default here)

:Use this many particles:: 3500

     (That's almost all we have anyway.
     Note that the more particles, the more RAM this program will take.
     If you run out of memory, try training with fewer particles.
     Using much fewer than 4000 particles is not recommended.)


On the :guitab:`Polish` tab make sure you set:

:Perform particle polishing?: No


Note that the training step of this program has not been MPI-parallelised.
Therefore, make sure you use only a single MPI process.
We ran the program with 16 threads to speed it up.
Still, the calculation took more than 1 hour.


.. _sec_polish:

Running in polishing mode
-------------------------

Once the training step is finished, the program will write out a text file called ``Polish/job027/opt_params.txt``.
To use these parameters to polish your particles, click on the job-type menu on the left to select a new :jobtype:`Bayesian polishing` job.
Keep the parameters on the :guitab:`I/O` tab the same as before, and on the :guitab:`Train` tab, make sure you switch the training off.
Then, on the :guitab:`Polish` tab set:

:Perform particle polishing?: Yes

:Optimised parameter file:: Polish/job027/opt\_params.txt

:OR use your own parameters?: No

:Minimum resolution for B-factor fit (A):: 20

:Maximum resolution for B-factor fit (A):: -1

     (just leave the defaults for these last two parameters)


Alternatively, if you decided to skip the training set, then you can fill in the :guitab:`Polish` tab with the sigma-parameters that we obtained in our run:

:Perform particle polishing?: Yes

:Optimised parameter file:: \

     (leave this empty to use the optimal parameters we got as per below.)

:OR use your own parameters?: Yes

:Sigma for velocity (A/dose): 0.474

:Sigma for divergence (A): 1770

:Sigma for acceleration (A/dose): 3.21

:Minimum resolution for B-factor fit (A):: 20

:Maximum resolution for B-factor fit (A):: -1

     (just leave the defaults for these last two parameters)


This part of the program is MPI-parallelised.
Using 3 MPI processes, each with 16 threads, our run finished in eight minutes.


Analysing the results
---------------------

The :jobtype:`Bayesian polishing` job outputs a STAR file with the polished particles called `shiny.star` and a PDF logfile.
The latter contains plots of the scale and B-factors used for the radiation-damage weighting, plus plots of the refined particle tracks for all included particles on all micrographs.
Looking at the plots for this data set, it appeared that the stage was a bit drifty: almost all particles move from the top right to the bottom left during the movies.

Re-running refinement and post-processing
-----------------------------------------

After polishing, the signal-to-noise ratio in the particles has improved, and one should submit a new :jobtype:`3D auto-refine` job and a corrsponding :jobtype:`Post-processing` job.
We chose to run the :jobtype:`3D auto-refine` job with the shiny particles using the following option on the :guitab:`I/O` tab:

:Reference mask (optional):: MaskCreate/job020/mask.mrc

     (this is the mask we made for the first :jobtype:`Post-processing` job.
     Using this option, the solvent will be set to zero for all pixels outside the mask.
     This reduces noise in the reference, and thus lead to better orientation assignments and thus reconstructions.)


and this option on the :guitab:`Optmisation` tab:

:Use solvent-flattened FSCs?: Yes

     (Using this option, the refinement will use a solvent-correction on the gold-standard FSC curve at every iteration, very much like the one used in the :jobtype:`Post-processing` job-type.
     This option is particularly useful when the protein occupies a relatively small volume inside the particle box, e.g. with very elongated molecules, or when one focusses refinement on a small part using a mask.
     The default way of calculating FSCs in the 3D auto-refinement is without masking the (gold-standard) half-maps, which systematically under-estimates the resolution during refinement.
     This is remediated by calculating phase-randomised solvent-corrected FSC curves at every iteration, and this generally leads to a noticeable improvement in resolution.)

Also, on the :guitab:`Auto-sampling` tab, we now set:

:Use finer angular sampling faster?: No

As you can see in the pre-calculated results, we obtained a final resolution just beyond 2.8 Å.
Not bad for 3GB of data, right?


When and how to run CTF refinement and Bayesian polishing
---------------------------------------------------------

Both :jobtype:`Bayesian polishing` and :jobtype:`CTF refinement`, which comprises per-particle defocus, magnification and higher-order aberration estimation, may improve the resolution of the reconstruction.
This raises a question of which one to apply first.
In this example, we first refined the aberrations, the magnification, and then the per-particle defocus values.
We then followed up with polishing, but we could have also performed the polishing before any of the CTF refinements.
Both approaches benefit from higher resolution models, so an iterative procedure may be beneficial.
For example, one could repeat the CTF refinement after the Bayesian polishing.
In general, it is probably best to tackle the biggest problem first, and some trial and error may be necessary.

Moreover, we have seen for some cases that the training prodcedure of Bayesian polishing yields inconsistent results: i.e. multiple runs yield very different sigma values.
However, we have also observed that often the actual sigma values used for the polishing do not matter much for the resolution of the map after re-refining the shiny particles.
Therefore, and also because the training is computationally expensive, it may be just as well to run the polishing directly with the default parameters (:math:`\sigma_{\text{vel}}=0.2; \sigma_{\text{div}}=5000; \sigma_{\text{acc}}=2`), i.e. without training for your specific data set.
