.. _program_tomo_reconstruct_tomogram:

relion_tomo_reconstruct_tomogram
================================

This program creates a tomogram (i.e. a 3D image approximating the scattering potential within a cryo-EM sample) from a tilt series defined in a given |tomogram_set|.
Please note that these tomograms are *not* intended for further processing.
Instead, their purpose is only to allow for the inspection of the sample and the detection of specific structures, such as manifolds or individual particles.
In order to perform subtomogram averaging, the detected particles should be written into a|particle_set|, from which *pseudo subtomograms* should be constructed using the program :ref:`program_subtomo`.
These pseudo subtomograms can then be refined using ``relion_refine``.

This program is also not intended for the reconstruction of full-size tomograms, since the resulting 3D image needs to fit into memory.

Relevant program arguments:
---------------------------

- ``--i`` or ``--t``: input optimisation-set or tomogram set (see |optimisation_set|).
- ``--tn``: ``tomogram_name`` of the tomogram to reconstruct (see |tomogram_set|).
- ``--no_weight``: reconstruct an unweighted tomogram, as opposed to applying a weighting in 3D using a `Wiener filter <https://en.wikipedia.org/wiki/Wiener_filter>`_. If the purpose of the tomogram is for a human to slice through it along the viewing direction, then an unweighted tomogram offers the most contrast. It will introduce streaking artifacts along the viewing direction, however.
- ``--pre_weight``: apply a pre-weighting in 2D instead of a 3D weighting. This is significantly more efficient for large tomograms.
- ``--SNR``: the signal-to-noise ratio assumed by the Wiener filter. Note: a realistic SNR might lead to an excessive dampening of the high frequencies. If the purpose of the tomogram is only for humans to inspect it, then this dampening might make the image clearer.
- ``--noctf``: do not modulate the input images by a (spatially constant) CTF.
- ``--keep_mean``: do not subtract the mean from (i.e. do not zero the DC component of) every 2D image prior to reconstruction.
- ``--td``: taper distance. Do not backproject image regions closer than this to the edge of a 2D image.
- ``--tf``: taper falloff. Fade out the contribution of each 2D image along this distance to the edge of the effective image. If a value has been specified for the ``--td`` argument, then this falloff begins at that edge. These two options are useful if the images show artifacts near the edge, and the resulting tomogram is to be used for automated detection.	
- ``--<x0/y0/z0>``: the origin of the 3D region to be reconstructed. Note: to maintain consistency with other processing software, the default origin (corresponding to the one used by IMOD_) is equal to 1. Therefore, 1 is also the default value for these arguments.
- ``--<w/h/d>``: the size of the 3D region to be reconstructed (in bin-1 pixels). If not specified, the size indicated in the tomogram set will be used, which should correspond to the region defined in IMOD_.
- ``--bin``: the binning level of the reconstruction. Note: the default value for this is 8, in order to prevent accidentally reconstructing a bin-1 tomogram.
- ``--j``: number of threads to be used. This should be set to the number of CPU cores available.
- ``--o``: name of the output 3D image. This is the only file created by this program. If the file name contains subdirectories, then those will also be created.


.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
.. _IMOD: https://bio3d.colorado.edu/imod
