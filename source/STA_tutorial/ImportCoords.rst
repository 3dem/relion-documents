.. _sec_sta_importcoord:

Import coordinates
------------------

While we will not use this functionality in this tutorial, here we describe briefly how one can import coordinates of particles picked outside RELION, for example by using picking software such as ``crYOLO`` :cite:`wagner_sphire-cryolo_2019`.

We assume, for illustration purpose, that the coordinate files are one text file per tomogram, containing particle coordinates that have been picked in the tomograms obtained from a :jobtype:`Reconstruct tomograms` or :jobtype:`Denoise tomgorams` job, with the file names containing the tomogram name (e.g. ``rec_TS_01.coords``) and are located in a directory ``PARTICLE_COORDS``.


Select :jobtype:`Import` from the jobt-type browser on the left and fill in the following parameters on the :guitab:`Coordinates` tab:

:Or Import coordinates instead?: Yes

:Input coordinates?: PARTICLE_COORDS/rec_TS_*

    (Alternatively, if the particle files are in RELION STAR file format, then the input coordinate file should be a 2-column STAR file with columns ``rlnTomoName`` and ``rlnTomoImportParticleFile`` for the tomogram names and their corrsesponding particle coordinate files.)

:Remove substring from filenames:: rec\_

    (This field and the one below allow the import program to find the tomogram name in the file name.)

:Second substring to remove: .coords

:Text files contain centered coordinates?: No

:Multiply coords in text files with:: 7.407407 

    (If the coordinates are with respect to the binning/voxel size in the tomograms in ``Denoise/job008/tomograms/``, this is the number that they will be multiplied with so that the resulting coordinates correspond to the pixel size in the motion-corrected tilt series. In this case, this is found in the ``rlnTomoTomogramBinning`` column of the ``Denoise/job008/tomograms.star`` file.)

:Add this to coords in text files:: 0


Inside the newly created directory, you will find the imported |particle_set| ``particles.star`` file. 
This should then be used as input to a new :jobtype:`Extract subtomos` job together with the |tomogram_set| ``tomograms.star`` file containing the details of the tomograms used for picking outside RELION:

:Input optimisation set:: ""

:OR\: use direct entries?: Yes

:Input particle set:: Import/jobXX/particles.star

:Input tomogram set:: Denoise/job008/tomograms.star

This will generate new 2D stacks or 3D pseudo-subtomograms that can be used in the next refinement steps. 
The resulting particles can be visualised using the Napari plugin in a new :jobtype:`Pick tomograms` job with ``Picking mode`` set to ``particles``, as explained in the :ref:`sec_sta_class3d_visualising` section.


.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
