Mask creation & Postprocessing
===============================

After performing a 3D auto-refinement, the map needs to be sharpened.
Also, the gold-standard FSC curves inside the auto-refine procedures only use unmasked maps (unless you've used the option `Use solvent-flattened FSCs`).
This means that the actual resolution is under-estimated during the actual refinement, because noise in the solvent region will lower the FSC curve. |RELION|'s procedure for B-factor sharpening and calculating masked FSC curves :cite:`chen_high-resolution_2013` is called ``post-processing``.
First however, we'll need to make a mask to define where the protein ends and the solvent region starts.
This is done using the :jobtype:`Mask Creation` job-type.


Making a mask
-------------

On the :guitab:`I/O` tab, select the output map from the finished 3D auto-refine job: ``Refine3D/first3dref/run_class001.mrc``.

On the :guitab:`Mask` tab set:

:Lowpass filter map (A):: 15

     (A 15 Å low-pass filter seems to be a good choice for smooth solvent masks for many proteins.)

:Pixel size (A):: -1

     (This value will be taken automatically from the header of the input map.)

:Initial binarisation threshold:: 0.005

     (This should be a threshold at which rendering of the low-pass filtered map in for example :textsc:`chimera` shows absolutely no noisy spots outside the protein area.
     Move the threshold up and down to find a suitable spot.
     Remember that one can use the command-line program called ``relion_image_handler`` with the options ``--lowpass 15 --angpix 1.244`` to get a low-pass filtered version of an input map.
     Often good values for the initial threshold are around 0.01-0.04.)

:Extend binary map this many pixels:: 0

     (The threshold above is used to generate a black-and-white mask.
     The white volume in this map will be grown this many pixels in all directions.
     Use this to make your initial binary mask less tight.)

:Add a soft-edge of this many pixels:: 6

     (This will put a cosine-shaped soft edge on your masks.
     This is important, as the correction procedure that measures the effect of the mask on the FSC curve may be quite sensitive to too sharp masks.
     As the mask generation is relatively quick, we often play with the mask parameters to get the best resolution estimate.)


Ignore the :guitab:`Helix` tab and use an alias like `first3dref`.
Note that you can run the ``relion_mask_create`` program with multiple threads to accelerate this step.
You can look at slices through the resulting mask using the :button:`Display:` button, or you can load the mask into UCSF :textsc:`chimera`.
The latter may be a good idea, together with the map from the auto-refine procedure, to confirm that the masks encapsulates the entire structure, but does not leave a lot of solvent inside the mask.
You can continue the same job with new settings for the mask generation until you have found a mask you like.


Postprocessing
--------------

Now select the :jobtype:`Post-processing` job-type, and on the :guitab:`I/O` tab, set:

:One of the 2 unfiltered half-maps:: Refine3D/first3dref/run\_half1\_class001\_unfil.mrc

:Solvent mask:: MaskCreate/first3dref/mask.mrc

:Calibrated pixel size (A):: 1.244

    (Sometimes you find out when you start building a model that what you thought was the correct pixel size, in fact was off by several percent.
     Inside |RELION|, everything up until this point was still consistent. so you do not need to re-refine your map and/or re-classify your data.
     All you need to do is provide the correct pixel size here for your correct map and final resolution estimation.)


On the :guitab:`Sharpen` tab, set:

:Estimate B-factor automatically:: Yes

     (This procedure is based on the classic Rosenthal and Henderson paper :cite:`rosenthal_optimal_2003`, and will need the final resolution to extend significantly beyond 10 Å.
     If your map does not reach that resolution, you may want to use your own ``ad-hoc`` B-factor instead.)

:Lowest resolution for auto-B fit (A):: 10

     (This is usually not changed.)

:Use your own B-factor?: No

:Perform MTF correction?: No

     (As we provided an MTF file when we imported the movies, MTF correction has already been performed inside the refinement.)


On the :guitab:`Filter` tab, set:

:Skip FSC-weighting?: No

     (This option is sometimes useful to analyse regions of the map in which the resolution extends **beyond** the overall resolution of the map.
     This is not the case now.)


Run the job (no need for a cluster, as this job will run very quickly) and use an alias like ``first3dref``.
Using the :button:`Display` button, you can display slizes through the postprocessed map and a PDF with the FSC curves and the Guinier plots for this structure.
You can also open the ``PostProcess/first3dref/postprocess.mrc`` map in :textsc:`chimera`, where you will see that it is much easier to see where all the alpha-helices are then in the converged map of the 3D auto-refine procedure.
The resolution estimate is based on the phase-randomization procedure as published previously :cite:`chen_high-resolution_2013`.
Make sure that the FSC of the phase-randomized maps (the red curve) is more-or-less zero at the estimated resolution of the postprocessed map.
If it is not, then your mask is too sharp or has too many details.
In that case use a stronger low-pass filter and/or a wider and more softer mask in the :jobtype:`Mask creation` step above, and repeat the postprocessing.