.. _sec_sta_tomorefine:

Tomo refinement cycle
==========================

We will now describe the specific tomo refinement steps that will refine the particle-specific CTF parameters, tilt angles and beam-induced deformations, which will lead to higher resolution in our subtomogram-averaged structure.

The tomo refinement jobs are :jobtype:`CTF refinement` and :jobtype:`Bayesian polishing`, and one tomo refinement cycle would include both. 
Moreover, for better improvements, we recommend running multiple tomo refinement cycles.

In the current section, we give an overview of how such a tomo refinement cycle would look.


.. _sec_sta_ctfrefine_refmap:

Reference map and FSC data
-----------------------------------

Before running each of the tomo refinement jobs (:jobtype:`CTF refinement` and :jobtype:`Bayesian polishing`), the following are required:

    1. Reference halfmaps obtained by running :jobtype:`Reconstruct particle`. The implementation of the :jobtype:`Reconstruct particle` job is consistent with the the implementation of the tomo refinement jobs (e.g. range of the intensities), so it is important to use this reference map rather than maps obtained from :jobtype:`3D auto-refine`.

    2. Post-processed FSC data for the reference halfmaps obtained by running :jobtype:`Post-processing`. This is required to estimate the SNR. If not provided, these programs internally calculate it without phase randomization, so SNR will be slightly optimistic. 

    3. Alignment mask file at binning facor 1 

    4. |Optimisation_set| 

Note that, independently of the binning factor of the data in the previous steps, :jobtype:`CTF refinement` and :jobtype:`Bayesian polishing` protocols process data in the original pixel size (binning 1).
Therefore, the reference map should always be reconstructed at this binning level and proper reference and FSC masks should be used.


Running the jobs
----------------

The order of :jobtype:`CTF refinement` and :jobtype:`Bayesian polishing` is not important, as long as we keep track of the optimisation set file. 
In our workspace, in each cycle we ran the two jobs as follows:

1. :jobtype:`CTF refinement`, described in detail in the :ref:`sec_sta_ctfrefine` section, and

2. :jobtype:`Bayesian polishing`, described in detail in the :ref:`sec_sta_bayesian_polishing` section.


3D refinement 
----------------------

After running both tomo specific refinement steps, it is still recommended to run a new :jobtype:`3D auto-refine` job to take advantage of the improved tomograms and particles.
To this end, we need to construct a new set of pseudo-subtomos and reference maps as described in the :ref:`sec_sta_refine3d_subtomo` subsection.
For the new :jobtype:`3D auto-refine` job, the same parameters as in the :ref:`sec_sta_refine3d_refinebin1` section apply, except for:

On the :guitab:`Reference` tab, set:

:Initial low-pass filter (A):: 4

On the :guitab:`Auto-sampling` tab set:

:Initial angular sampling:: 0.9 degrees


This new 3D refinement step took just under 2 hours on our system (2 GPU cards) and, after :jobtype:`Reconstruct particle` and :jobtype:`Post-processing` with the tight mask, we reached a resolution of 3.6Å, completing the first tomo refinement cycle.
After another four full tomo refine cycles, we reached 3.3Å, and depending on the quality of the picked particles, it is also possible to obtain 3.2Å.


.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
