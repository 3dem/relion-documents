.. _sec_sta_particlepicking:

Particle picking
================

Particle picking is probably the most difficult part of the subtomogram averaging pipeline. 
It is important that you pick particles as accurately as possible, so RELION is not trying to align and average particles without the appropriate signal.
Alister Burt has written a Napari plug-in to pick particles directly in your tomograms. His picker can be used to pick individual particles, or particles that are randomly sampled from geometric shapes (curved lines for filaments, spheres for capsids or vesicles, or surfaces for membranes or other larger objects. (Please not the surface picker is not functional yet). 

To launch the Napari picker, **again make sure you are working on the computer you are actually sitting behind as Napari performs poorly over remote connections**, and select the :jobtype:`Pick tomograms` job type. On the :guitab:`I/O` tab, set:

:Input tomograms.star: ReconstructTomograms/job006/tomograms.star

:Picking mode: spheres

    (The Napari picker has 4 modes of picking: particles, spheres, filaments and surfaces. For the tutorial data we use spheres, because HIV-VLPs are more-or-less that shape. Besides randomly picking particles with the distance specified them below, this mode of picking also provides prior angles on the particles that will mean that with a tilt angle of 90 degrees, they will be oriented with their Z-axis along the normal to the sphere surface. In what follows, this prior information will be used in refinements and classification of the subtomograms. Filaments are picked as multiple points forming a (curved) line; with priors that result in tilt=90 angles orienting particles with their Z-axis along the helical axis. Individual particle picking does not provide any priors. Surface picking is not functional yet.)

:Particle spacing (A): 60

    (This is the inter-particle distance with which particle positions will be randomly sampled from on the sphere. HIV capsid hexamers are approximately 75 Angstroms apart. By over-sampling the sphere we reduce the number of missed particles.)

On the :guitab:`Running` tab set:

:Submit to queue: No

And click on the :runbutton:`Run!` button to launch the Napari GUI.



Picking in Napari GUI
---------------------

Napari will automatically open the first tomogram on the GUI. Keep down (drag) the left mouse button (``lef-mouse + drag``) to rotate the scene; use the scroll wheel to zoom in/out; use ``Shift + lef-mouse + drag`` to move the visualised plane along the Z axis (normal to plane). [We should mention the problem of the viewer getting stuck in perspective mode and what to here...] 

Sphere annotation: 
    The first step is to locate the centre of the sphere-like object in the tomogram. In the tutorial data,
    HIV-VLPs are more-or-less distorted spheres. Move along the Z-dim of a chosen capsid to find the
    maximum diameter and locate the middle of that capsid. Then use ``Alt + left-click`` or (``Ctrl + Alt + left-click`` on some Linux flavours) at that centre to
    place a small sphere. To resize the sphere press letter ``r`` and the sphere will be resized to point where the mouse is pointing.
    You'll need to play a bit to get the right radius of the sphere. The right sphere size is when the surface of the sphere cuts through the middle of
    the capsid membrane. Then go to a new capsid and repeat the above process. To move on to a new capsid
    press the letter ``n``. Once you finished annotating all the spheres in one tomogram press the button
    ``save spheres``. Next you can choose the second tomogram and so on. Once you finished annotating all
    the tomograms close the Napari window.

filaments annotation: 
    If you're picking filaments, find the start of one and use ``(Ctrl +) Alt + left-click`` to add a point to its (curved) line;
    keep adding as many points as you need to describe the curvature.  To move on to a new filament press the letter ``n``. Once you finished annotating all the filaments in one tomogram press the button
    ``save filaments`` and move to the next tomogram. 

surface annotation: 
    This is not functional yet. Please stay tuned.

Individual particle picking:
    To pick indiviual particles use ``(Ctrl +) Alt + left-click`` on some linux flavours. Napari will show this location with a small blue sphere. 
    To delete any particle picked select that particle by left-clicking on it, go the the ``n3d points`` layer on the Napari GUI and choose the approximate action button (``x`` = delete, ``arrow`` = move). [This is not clear at all!]
    Once you finished picking all the particles in one tomogram click on the ``save particles`` button and move to the next tomogram.
    picking all the tomograms just close the Napari GUI.


After the Napari picker is closed, a python script will convert the picked coordinates from each tomogram, which are saved in the directory ``Picks/job007/annotations`` to individual particle picks (in case spheres, filaments or surfaces were picked), and then write out a file called ``PickTomo/job007/particles.star`` with all particles from all tomograms. This star file contains the coordinates of your particles in 3 dimensions under the headers ``rlnCoordinate<X/Y/Z>``, which are in (unbinned) pixels starting from (1,1,1) in the top corner of the tomogram. We are currently working to write out these coordinates as ``rlnCenteredCoordinate<X/Y/Z>Angst``, which wil be in Angstroms from the centre of the tomogram. Please bear with us as this work is being finished during beta-code development.

For your own data, you may also want to try other particle pickers such as TomoTwin, DeePiCt, DeepFinder, CrYOLO, or others. We strongly recommend only picking in tomograms generated in ``ReconstructTomograms`` (or ``Denoise``) jobs, unless you can verify that the coordinates that you picked in tomograms generated outside of RELION match the coordinates of the RELION tomograms perfectly. Future developments in the ccp-em tomography pipeline will hopefully make using third-party pickers easier.
