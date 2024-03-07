.. _sec_sta_particlepicking:

Particle picking
================

Particle picking is probably the most difficult part of the subtomogram averaging pipeline. 
It is important that you pick particles as accurately as possible, so RELION is not trying to align and average particles without the appropriate signal.
Alister Burt has written a Napari plug-in to pick particles directly in your tomograms. His picker can be used to pick individual particles, or particles that are randomly sampled from geometric shapes (curved lines for filaments, spheres for capsids or vesicles, or surfaces for membranes or other larger objects. (Please do not use the surface picker -- it is not functional yet). 

To launch the Napari picker, **again make sure you are working on the computer you are actually sitting behind, as Napari performs poorly over remote connections**, and select the :jobtype:`Pick tomograms` job type. On the :guitab:`I/O` tab, set:

:Input tomograms.star: Tomograms/job006/tomograms.star

:Picking mode: spheres

    (The Napari picker has 4 modes of picking: particles, spheres, filaments and surfaces. For the tutorial data we use spheres, because HIV-VLPs are more-or-less that shape. Besides randomly picking particles with the distance specified below, this mode of picking also provides prior angles on the particles that will mean that with a tilt angle of 90 degrees, they will be oriented with their Z-axis along the normal to the sphere surface. In what follows, this prior information will be used in refinements and classification of the subtomograms. Filaments are picked as multiple points forming a (curved) line, with priors that result in tilt=90 angles orienting particles with their Z-axis along the helical axis. Individual particle picking does not provide any priors. Surface picking is not functional yet.)

:Particle spacing (A): 60

    (This is the inter-particle distance with which particle positions will be randomly sampled from on the sphere. HIV capsid hexamers are approximately 75Å apart. By over-sampling the sphere we reduce the number of missed particles.)

:Input particles.star (optional): ""

    (We do not use this field at this point in the pipeline. It can be used to load the particles in a given star file as annotations on the tomogram by providing such a star file in this field together with setting **Picking mode** to ``particles``.)

On the :guitab:`Running` tab set:

:Submit to queue: No

And click on the :runbutton:`Run!` button to launch the Napari GUI.



Napari will automatically open the first tomogram on the GUI. Keep down (drag) the left mouse button (``lef-mouse + drag``) to rotate the scene; use the scroll wheel to zoom in/out; use ``Shift + lef-mouse + drag`` on the tomogram plane to move the visualised plane along the Z axis (normal to plane). [We should mention the problem of the viewer getting stuck in perspective mode and what to here...] The ``contrast limits`` slide bar in the top left side of the screen can be used to adjust contrast in the visualised tomogram plane.

Sphere annotation: 
    The first step is to locate the centre of the sphere-like object in the tomogram. In the tutorial data,
    HIV-VLPs are more-or-less distorted spheres. Move along the Z-dim of a chosen capsid to find the
    maximum diameter and locate the middle plane of that capsid. Then use ``Alt + left-click`` or (``Ctrl + Alt + left-click`` on some Linux flavours) at that centre to
    place a small sphere. To resize the sphere press letter ``r`` and the sphere will be resized to point where the mouse is pointing.
    You'll need to play a bit to get the right radius of the sphere. The right sphere size is when the surface of the sphere cuts through the middle of
    the capsid membrane. Then go to a new capsid and repeat the above process. To move on to a new capsid
    press the letter ``n``. 
    To delete or move an existing sphere, select the ``n3d spheres`` layer on the left side of the screen, then left-click
    on the centre of the sphere. The sphere can then be moved by drag-and-drop of its centre, or deleted by pressing the ``x`` button on the top-left of the screen (under ``layer controls``). 
    Once you finished annotating all the spheres in one tomogram, press the ``save spheres`` button. 
    Next you can choose the second tomogram and so on. Once you finished annotating all the tomograms, close the Napari window.

Filaments annotation: 
    If you're picking filaments, find the start of one and use ``(Ctrl +) Alt + left-click`` to add a point to its (curved) line;
    keep adding as many points as you need to describe the curvature.  To move on to a new filament press the letter ``n``. Once you finished annotating all the filaments in one tomogram press the button
    ``save filaments`` and move to the next tomogram. 

Surface annotation: 
    This is not functional yet. Please stay tuned.

Individual particle annotation:
    To pick a new indiviual particle, use ``(Ctrl +) Alt + left-click``. Napari will show this location with a small blue sphere. 
    To delete or move any particle picked, first select the ``n3d points`` layer on the Napari GUI (the layer list is on the left of the screen), then select the particle by left-clicking on it. Pressing the ``x`` button on the top left side of the screen (under ``layer controls``) deletes the particle, while pressing the third button (``Select points``) allows you to select a new particle, which can be deleted in the same way, or moved by drag-and-drop.
    Once you finished picking all the particles in one tomogram, click on the ``save particles`` button and move to the next tomogram.
    picking all the tomograms just close the Napari GUI.


After the Napari picker is closed, a python script will save the selected annotations to individual annotation files ``*_spheres.star``, ``*_filaments.star`` or ``*_particles.star``, one per tomogram, to the ``Picks/job008/annotations`` directory, and then write out a file called ``Picks/job008/particles.star`` with all particles from all tomograms. This star file contains the coordinates of your particles in 3 dimensions under the headers ``rlnCoordinate<X/Y/Z>``, which are in (unbinned) pixels starting from (1,1,1) in the top corner of the tomogram. We are currently working to write out these coordinates as ``rlnCenteredCoordinate<X/Y/Z>Angst``, which wil be in Angstroms from the centre of the tomogram. Please bear with us as this work is being finished during beta-code development.

For your own data, you may also want to try other particle pickers such as TomoTwin, DeePiCt, DeepFinder, CrYOLO, or others. We strongly recommend only picking in tomograms generated in ``ReconstructTomograms`` (or ``Denoise``) jobs, unless you can verify that the coordinates that you picked in tomograms generated outside of RELION match the coordinates of the RELION tomograms perfectly. Future developments in the ccp-em tomography pipeline will hopefully make using third-party pickers easier.
