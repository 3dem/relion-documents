.. _sec_sta_refine3d:

High-resolution 3D refinement
=============================

Once we have obtained a refined map in high binning factor (low resolution) we can proceed to refine this dataset to higher resolution.

At this point in the tutorial, the 3D refinement could be directly processed using the original pixel size (binning factor 1).
However, it's recommended to sequentially process 3D refinements through decreasing binning factors to speed up calculations as we don't longer need to setup a large valued low-pass filter for the initial reference.
This initial low-pass filter prevents bias towards high-frequency components in the map and maintains the `gold-standard` of completely independent refinements at resolutions higher than the initial one.
To overcome this, halfmap files can be used as reference maps for each halfset processed by `relion_refine`, keeping the 3D refinement independent along the whole worflow.
To that end, when the reference map filename contains either ``*half?*.mrc`` template, each halfmap is automatically assigned to its halfset.


Pseudo-subtomograms at bin 2
----------------------------

In the previous :ref:`reconstruct particle <sec_sta_reconstructpart>` step, we showed how to obtain the 3D refined reference map and halfmaps at binning factor 2.
Now, we also need to construct the pseudo-subtomogram files at that same binning factor.
To do this, go to the :jobtype:`Make pseudo-subtomos` jobtype on the GUI, and on the :guitab:`I/O` tab give:

:Input optimisation set:: ReconstructParticleTomo/job013/optimisation_set.star

On the :guitab:`Reconstruct` tab, make sure the following is set to reconstruct particles with a binning factor of 2:

:Box size (pix):: 256
:Cropped box size (pix):: 128
:Binning factor:: 2

Note we're using the :jobtype:`Tomo reconstruct particle` output |optimisation_set| file.
Therefore, the output optimisation set file after constructing the pseudo-subtomos will contain both particles and references at the same binning factor.


Running the auto-refine job at bin 2
-----------------------------------------------

On the :guitab:`I/O` tab of the :jobtype:`3D auto-refine` job-type set:

:Input optimisation set:: PseudoSubtomo/job014/optimisation_set.star

:Input images STAR file:: \

    (Note this is blank as it is extracted from the optimisation set file.)

:Reference map:: \

    (Note this is blank as a halfmap is extracted from the optimisation set file.)

:Reference mask (optional):: masks/mask_align_bin2.mrc

On the :guitab:`Reference` tab, set:

:Ref. map is on absolute greyscale?: Yes

:Initial low-pass filter (A): 12

     (We set the low-pass filter slightly below the achieved resolution in the previous step. In this case, it's Nyquist resolution at binning factor 4.)

:Symmetry: C6

On the :guitab:`CTF` tab set:

:Do CTF correction?: Yes

:Ignore CTFs until first peak?: No

On the :guitab:`Optimisation` tab set:

:Mask diameter (A):: 230

:Mask individual particles with zeros?: Yes

:Use solvent-flattened FSCs?: Yes

On the :guitab:`Auto-sampling` tab, to resume the refinement from the current resolution, we could adjust the angular sampling below the angular resolution given the initial low-pass filter argument and mask diameter.
A coarse estimation can be obtained by :math:`\arctan{\frac{resolution*2}{diameter}}`. In our case:

:Initial angular sampling:: 3.7 degrees

We leave the rest of arguments at their default values, except for:

:Use finer angular sampling faster?: Yes

On our computer with 4 GPUs, we used 5 MPIs and 8 threads, and this calculation took approximately 6 hours.


Again, the 3D refinement will have achieved Nyquist resolution so we can finally proceed to process using the original pixel size at binning factor 1.


Pseudo-subtomograms and reference map at bin 1
----------------------------------------------

The order to process :jobtype:`Make pseudo-subtomos` and :jobtype:`Tomo reconstruct particle` jobtypes is irrelevant as long as they are done consecutively to keep track in the |optimisation_set| file.
For 3D refinement at binning factor 1, make sure the following options are properly set on :jobtype:`Make pseudo-subtomos` :guitab:`Reconstruct` tab and :jobtype:`Tomo reconstruct particle` :guitab:`Average` tab:

:Box size (pix):: 512
:Cropped box size (pix):: 192
:Binning factor:: 1

We could also set the solvent mask in the :jobtype:`Tomo reconstruct particle` case to estimate current resolution:

:FSC Solvent mask:: masks/mask_fsc.mrc


Running the auto-refine job at bin 1
-------------------------------------

On the :guitab:`I/O` tab of the :jobtype:`3D auto-refine` job-type set:

:Input optimisation set:: ReconstructParticleTomo/job018/optimisation_set.star

:Reference mask (optional):: masks/mask_align.mrc

On the :guitab:`Reference` tab, set:

:Ref. map is on absolute greyscale?: Yes

:Initial low-pass filter (A): 5.5

     (We set the low-pass filter slightly below the achieved resolution in the previous step. In this case, it's Nyquist resolution at binning factor 2.)

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








.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`