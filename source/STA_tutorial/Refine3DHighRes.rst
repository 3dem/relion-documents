.. _sec_sta_refine3d:

High-resolution 3D refinement
=============================

**NOTE: The Relion 5 Tomo tutorial has been revised up to this point. For the next steps, use at your own risk.**

At this point in the tutorial, we have obtained a refined map at binning factor 2, we have removed any duplicate particles, as well as any bad particles that do not align well with our map.
We are now ready to perform 3D refinement at binning factor 1.

.. _sec_sta_refine3d_subtomo:

Pseudo-subtomograms and reference map at bin 1
----------------------------------------------

Before running the :jobtype:`3D auto-refine` job, we need to generate new pseudo-subtomograms and a reference map at binning factor 1. 
The order of running the :jobtype:`Extract subtomos` and :jobtype:`Reconstruct particle` jobtypes is irrelevant as long as they are run consecutively to keep track of the |optimisation_set| file. 
In addition, since the previous job we ran was a :jobtype:`Subset selection` job, we must use its output particles file as the input particle set to the next job (either :jobtype:`Extract subtomos` or :jobtype:`Reconstruct particle`):

:Input optimisation set:: ""
:OR\: use direct entries?: Yes
:Input particle set: Select/job023/particles.star
:Input tomgoram set: Tomograms/job007/tomograms.star
:Input trajectory set: ""

For 3D refinement at binning factor 1, make sure the following options are properly set on :jobtype:`Extract subtomos` :guitab:`Reconstruct` tab and :jobtype:`Reconstruct particle` :guitab:`Average` tab:

:Binning factor:: 1
:Box size (binned pix):: 512
:Cropped box size (binned pix):: 192



.. _sec_sta_refine3d_refinebin1:

Running the auto-refine job at bin 1
-------------------------------------

**[TODO: edit paragraph]**
To overcome this, halfmap files can be used as reference maps for each halfset processed by `relion_refine`, keeping the 3D refinement of both halfsets independent along the whole workflow.
To that end, when the reference map filename contains either ``*half?*.mrc`` template, each halfmap is automatically assigned to its halfset.


On the :guitab:`I/O` tab of the :jobtype:`3D auto-refine` job-type set:

:Input optimisation set:: ReconstructParticleTomo/job018/optimisation_set.star

:Reference mask (optional):: masks/mask_align.mrc

On the :guitab:`Reference` tab, set:

:Ref. map is on absolute greyscale?: Yes

:Initial low-pass filter (A): 5.5

     (We set the low-pass filter slightly below the reached resolution in the previous step. In this case, it's Nyquist resolution at binning factor 2.)

:Symmetry: C6

On the :guitab:`CTF` tab set:

:Do CTF correction?: Yes

:Ignore CTFs until first peak?: No

On the :guitab:`Optimisation` tab set:

:Mask diameter (A):: 230

:Mask individual particles with zeros?: Yes

:Use solvent-flattened FSCs?: Yes

On the :guitab:`Auto-sampling` tab set:

:Initial angular sampling:: 1.8 degrees

In our system, using 4 GPU cards, it took around half a day to finish.

Thereafter, running a :jobtype:`Post-processing` job with the tight mask ``masks/mask_fsc.com`` you should obtain a resolution around 3.6Å. At this moment, this is the best alignment we could reach without applying any specific tomo refinement, as shown in :ref:`sec_sta_ctfrefine` and :ref:`sec_sta_framealign` sections.


-------------------------------


**[TODO: Integrate the below paragraph into this page]**

Before this, since the refined map we obtained in this initial 3D refinement covers the HIV capsid and matrix, we need to make sure the mask we will be using in the next refinement is aligned and focused on the capsid only.
We suggest to recenter the reference as masks provided in ``masks/`` folder are already centered.
You could look at the output refined map (``Refine3D/job009/run_class001.mrc``) and mask (``masks/mask_align_bin4.mrc``) with a 3D viewer like IMOD :textsc:`3dmod` to estimate the Z offset between both maps, in pixels. In our case, it is 2.75 pixels but this could be different as it depends on the initial *de novo* model. Thus, recentering the particles can be done from the command-line:

::

    relion_star_handler --i Refine3D/job009/run_data.star \
    --o Refine3D/job009/run_data_z2.75.star --center --center_Z 2.75


To assess the capsid within the reference map is aligned with the mask, we could reconstruct it using the :jobtype:`Tomo reconstruct particle` job-type, described in the next step :ref:`reconstruct particle <sec_sta_reconstructpart>`.

.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
