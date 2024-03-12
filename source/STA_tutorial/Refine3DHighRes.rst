.. _sec_sta_refine3d:

High-resolution 3D refinement
=============================

At this point in the tutorial, we have obtained a refined map at binning factor 2, we have removed any duplicate particles, as well as any bad particles that do not align well with our map.
We are now ready to perform 3D refinement at binning factor 1.

.. _sec_sta_refine3d_subtomo:

Pseudo-subtomograms and reference map at bin 1
----------------------------------------------

First, we need to generate new pseudo-subtomograms and a reference map at binning factor 1. 
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


.. _sec_sta_refine3d_mask:

Masks for high-resolution refinement and FSC estimation
--------------------------------------------------------------------------

Next, we need to generate appropriate masks to help the refinement process and FSC assessment. In the particular case of the HIV capsid, we provide the following masks: 

 1. ``mask_align.mrc``, which we will use in the ``Reference mask`` field of the :jobtype:`3D auto-refine` job: Since the refined region in our structure so far contains both the HIV capsid and the matrix, we need to make sure that we only focus on the capsid. Moreover, this mask is nearly as wide as the 230Å diameter mask applied to the images during refinement, ensuring that we use as much of the information available in the volume as possible to align the particles. 

 2. ``msk_fsc.mrc``, which we will use in the ``Solvent mask`` field of the :jobtype:`Post-processing` job (see :ref:`sec_sta_refine3d_postprocess` below). Since we use a wide mask to improve the alignment of particles during refinement, the volume we refine will consist of more than one hexamer. In order to asssess the reconstruction quality of the central hexamer only, we use a tighter mask around it for FSC calculations.

The above masks can be created externally using tools like UCSF :textsc:`chimera` or `dynamo_mask_GUI` from the :textsc:`dynamo` package.
For general mask creation, refer to SPA tutorial :ref:`mask description<sec_mask>`.

In order to use the provided masks, we suggest recentering the reference map to ensure that the masks and the reference are aligned (so that the masks focus on the capsid).
You could look at the output reference map from the previous step (``Reconstruct/job025/merged.mrc``) and the mask (``masks/mask_align.mrc``) with a 3D viewer like IMOD :textsc:`3dmod` to estimate the Z offset between both maps, in pixels. 
In our case, it is 2.75 pixels but this could be different as it depends on the initial *de novo* model. 
Thus, recentering the particles can be done from the command-line:

::

    relion_star_handler --i Extract/job024/particles.star \
    --o Extract/job024/particles2.75.star --center --center_Z 2.75

To check that the capsid within the reference map is aligned with the mask, we can reconstruct it using the :jobtype:`Reconstruct particle` job-type, described in :ref:`Reconstruct particle <sec_sta_reconstructpart>`.


.. _sec_sta_refine3d_refinebin1:

Running the auto-refine job at bin 1
-------------------------------------



On the :guitab:`I/O` tab of the :jobtype:`3D auto-refine` job-type set:

:Input optimisation set:: Extract/job024/optimisation_set.star

:OR\: use direct entries:: No

      (If a new particles file has been generated in the previous step during recentering, this option should be set to ``Yes`` and the correct input particle set and tomogram set files should be used.)

:Reference map:: Reconstruct/job025/half1.mrc

      (Once we reach a high enough resolution in the refinement process, it is important to keep the two halfsets entirely separate in order to obtain a gold-standard reconstruction. 
      Halfmap files should be used as reference maps for each halfset processed by `relion_refine`, keeping the 3D refinement of both halfsets independent along the whole workflow. 
      To that end, when the reference map file name contains either ``*half?*.mrc`` template, each halfmap is automatically assigned to its halfset.)

:Reference mask (optional):: masks/mask_align.mrc

On the :guitab:`Reference` tab, set:

:Ref. map is on absolute greyscale?: Yes

:Resize reference if needed?: Yes

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

	(This option enables the computation of the resolution during refinement using masked halfmaps using the provided ``mask_align.mrc`` mask file.)

:Use Blush regularisation?: No

On the :guitab:`Auto-sampling` tab set:

:Initial angular sampling:: 1.8 degrees

On our system, using 2 GPU cards, it took just under two hours.

We now remove duplicates again by running :jobtype:`Subset selection` with a minimum inter-particle distance of 50Å to ensure that no other particles converged to the same positions, and then generate a new reference map  with :jobtype:`Reconstruct particle`.

.. _sec_sta_refine3d_postprocess:

Post-processing
---------------

Finally, the procedure to sharpen a 3D reference map and estimate the gold-standard FSC curves for subtomogram averaging is strictly the same as described in the :ref:`SPA tutorial<sec_postprocess>`.

Select the :jobtype:'Post-processing` jobtype, and on the :guitab:`I/O` tab, set:

:One of the 2 unfiltered half-maps:: Reconstruct/job036/half1.mrc

:Solvent mask:: mask_fsc.mrc

	(This is the tight mask that only includes the central hexamer.)

We leave the other fields as they are and run the job. The resulting final resolution we see in our workspace is 3.93Å.

At this moment, this is the best alignment we could reach without applying any specific tomo refinement, as shown in :ref:`sec_sta_ctfrefine` and :ref:`sec_sta_framealign` sections.


.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
