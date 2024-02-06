.. _sec_sta_particlepicking:

Picking Particles
=====================

Particle picking is probably the most difficult part of the subtomogram averaging pipeline. 
It is important that you pick particles as accurately as possible so RELION is not trying to align and average particles which are completely different. 
We have provided a Napari plug in to pick particles directly in your tomograms either individually or based on geometric shapes within your tomograms such as membranes or vesicles. 
It will then output a STAR file with the particle coordinates saved. This tutorial will use the Napari plugin for particle picking.

Click on the :jobtype:`Pick tomograms` job from the job types.

On the :guitab:`I/O` tab

:Input tomograms.star: ReconstructTomograms/job[Number]/tomograms.star

If you have denoised tomograms make sure to choose the tomograms.star from the DenoiseTomo/job[Number] job.

:Picking mode: spheres

Napari tool has 4 modes of picking: particles, spheres, filaments and surfaces(?). For tutorial data we use
spheres mode because HIV-VLPs are more-or-less like spheres. By picking on spheres we can
assign Euler angles to the particles to give an approximate particle orientation.

:Particle spacing (A): 75

This is the interparticle distance and it determines the number of particles on the sphere. For tutorial data
we know this distance is ca. 75 A.

On the :guitab:`Running` tab 

:Submit to queue: No

By clicking on the :runbutton:`Run!` button will launch the Napari GUI.


Picking in Napari GUI
---------------------

Napari will automatically open the first tomogram on the GUI. To move along the Z xis (normal to plane)
use 'Shift' + click + drag. 

Individual particle picking:
    To pick indiviual particles 'Alt' + click or 'Alt' + 'Ctrl' + click on some linux flavours. By default
    Napari will open the middle section of the tomogram. But for picking we found gradual navigation from
    either top or bottom is easy. Locate the particles on each Z-section and click on the particle
    when it is centered on the Z axis while pressing the 'Alt' key. Napri will show this location
    with a small blue sphere centered around the particle. In case, if you want to move or delete any particle picked
    select that particle by clicking on it (just left mouse click), go the the 'n3d points' layer on the Napari GUI and 
    choose the approximate action button (x - delete, arrow- move).
    Once you finished picking all the particles in one tomogram click on the 'save particles' button
    at the lower-left corner of the GUI. Then choose the next tomogram from the tomograms list in the GUI. Once you finished
    picking all the tomograms just close the Napari GUI.

Sphere annotation: 
    The first step is to locate the centre of the sphere-like object in the tomogram. In tutorial data,
    HIV-VLPs are more-or-less distorted spheres. Move along the Z-dim of a chosen capsid to find the
    maximum diameter and locate the middle of that capsid. Then 'Ctrl' + 'Alt' + click in that centre to
    place a small sphere. To resize the sphere press letter 'r'. Oftentimes just one press will not be sufficent.
    The strategy worked for us was zooming in and out combined with pressing 'r'. We have noticed that
    pressing 'r' after every zoom out makes the radius bigger. You'll need to play a bit to get the right
    radius of the sphere. The right sphere size is when the surface of the sphere cuts through the middle of
    the capsid membrane. Then go to a new capsid and repeat the above process. To move on to a new capsid
    press the letter 'n'. Once you finished annotating all the sphere in one tomogram press the button
    'save spheres'. Next you can choose the second tomogram and so on. Once you finished annotating all
    the tomograms close the Napari window.

filaments annotation: 
    TODO

surface annotation: 
    TODO


The results from picking will be output to PickTomo/job[Number]/particles.star file. 
This star file should contain the coordinates of your particles in 3 dimensions under the headers 
rlnCoordinate<X/Y/Z> and the name of the tomogram each particle is contained in under the header rlnTomoName. 
Also, note that the particle positions are given in unbinned coordinates. 

For your own data, you may want to try other particle pickers such as TomoTwin, DeePiCt, DeepFinder, CrYOLO, or many more. 
We strongly recommend only picking in tomograms generated in ReconstructTomograms or DenoiseTomo jobs unless you can verify 
that the coordinates that you picked in tomograms generated outside of RELION match the coordinates of the RELION tomograms perfectly. 
The only requirement to continue in the RELION pipeline is that the coordinates of your picked particles are contained in a particles.star.
In such cases, make sure that particle positions are given in unbinned coordinates.
