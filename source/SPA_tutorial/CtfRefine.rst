CTF and aberration refinement
=============================

Next, we'll use the :jobtype:`CTF refinement` job-type to estimate the asymmetrical and symmetrical aberrations in the dataset; whether there is any anisotropic magnification; and we'll re-estimate per-particle defocus values for the entire data set.
Running this job-type can lead to further improvements in resolution at a relatively minor computational cost, but it all depends on how flat your ice was (for per-particle defocus estimates), and how well you had aligned your scope (for the aberrations).
It runs from a previous :jobtype:`3D auto-refine` job as well as a corresponding :jobtype:`Post-processing` job.
Let's start with the higher-order aberrations, to see whether this data suffered from beamtilt or trefoil (which are asymmetric aberrations), or from tetrafoil or an error in spherical aberration (which are symmetric aberrations).


Higher-order aberrations
------------------------

On the :guitab:`I/O` tab of :jobtype:`CTF refinement` job-type on the GUI the set:

:Particles (from Refine3D): Refine3D/job019/run\_data.star

:Postprocess STAR file:: PostProcess/job021/postprocess.star


On the :guitab:`Fit` tab set:

:Estimate (anisotropic magnification: No

     (We will do this later, see below.)

:Perform CTF parameter fitting?: No

     (We will do this later, see below.)

:Estimate beamtilt?: Yes

     (Despite the observation that most microscopists perform coma-free alignment schemes prior to data acquisition, there are still many data sets with a significant amount of beamtilt.
     That's why in this example we're first looking for beamtilt, and do the anisotropic magnification and the per-particle defocus later.
     In general, one would try to first estimate the source of the largest errors.)

:Also estimate trefoil?: Yes

     (This will allow more higher-order Zernike polynomials in the fitting of the asymmetric aberrations.)

:estimate 4th order aberrations?: Yes

     (This is done mostly for illustrative purposes here.
     One would not expect a big improvement at the current resolution of 3 Å.)

:Minimum resolution for fits (A):: 30

     (Just leave the default.)


This program is only implemented on the CPU.
Using 1 MPI and 12 threads, on our computer, this job finished in approximately one minute.

You can analyse the accumulated averages for the asymmetrical and symmetrical aberrations, as well as their models, by selecting the ``logfile.pdf`` file from the :button:`Display:` button on the GUI.
You'll see that this data actually suffered from some beamtilt: one side of the asymmetrical aberration images is blue, whereas the other side is red.
You can find the values (approximately -0.2 mrad of beamtilt in the Y-direction) in the optics table of the output STAR file:

::

     less CtfRefine/job022/particles_ctf_refine.star


There was also a small error in the spherical aberration, as the symmetrical aberration image shows a significant, circularly symmetric difference (the image is blue at higher spatial frequencies, i.e. away from the center of the image).
Importantly, for both the asymmetric and the symmetric aberaations, the model seems to capture the aberrations well.

If the data had suffered from trefoil, then the asymmetric aberration plot would have shown 3-fold symmetric blue/red deviations.
If the data had suffered from tetrafoil, then the symmetric aberration plot would have shown 4-fold symmetric blue/red deviations.
Examples of those are shown in the supplement of our 2019 publication on Tau filaments from the brain of individuals with chronic traumatic encephalopathy (CTE).


Anisotropic magnification
-------------------------

Next, let's see whether these data suffer from anisotropic magnification.
On the :guitab:`I/O` tab of :jobtype:`CTF refinement` job-type on the GUI, use the output from the previous CTF refinement job as input to this one:

:Particles (from Refine3D): CtfRefine/job022/particles\_ctf\_refine.star

:Postprocess STAR file:: PostProcess/job021/postprocess.star


And this time, on the :guitab:`Fit` tab set:

:Estimate (anisotropic magnification: Yes

     (This will deactivate most of the other options, as simultaneous magnification and aberration refinement is unstable.)

:Minimum resolution for fits (A):: 30

     (Just leave the default.)


Using 1 MPI and 12 threads, on our computer, this job finished in approximately one minute.

Again, the relevant images to analyse are in the ``logfile.pdf``.
There seem to be some blue-red trends, but the actual anisotropy is very small, as assessed from the ``_rlnMagMat??`` elements of the (2x2) transformation matrix in the optics table of the output STAR file:

::

     less CtfRefine/job023/particles_ctf_refine.star


Per-particle defocus values
---------------------------

Lastly, let's re-estimate the defocus values for each particle.
Again, use the output from the previous job as input for this one (although we could have just as well kept using the output from the aberration correction, as the magnification anisotropy was very small):

:Particles (from Refine3D): CtfRefine/job023/particles\_ctf\_refine.star

:Postprocess STAR file:: PostProcess/job021/postprocess.star


And this time, on the :guitab:`Fit` tab set:

:Estimate (anisotropic magnification: No

:Perform CTF parameter fitting?: Yes

:Fit defocus?: Per-particle

     (Provided the resolution of the reference extends well beyond 4 Å, per-particle defocus estimation seems to be relatively stable.
     It will account for non-horizontal ice layers, and particles at the top or bottom of the ice layer.)

:Fit astigmatism?: Per-micrograph

     (Provided the resolution of the reference extends well beyond 4 Å, and there are enough particles on each micrograph, estimating astigmatism on a per-micrograph basis seems to be relatively stable.
     Doing this on a pre-particle basis would require particles with very strong signal.)

:Fit B-factor?: No

:Fit phase-shift?: No

     (This is useful for phase-plate data.)

:Estimate beamtilt?: No

:estimate 4th order aberrations?: No

:Minimum resolution for fits (A):: 30

     (Just leave the default.)


Using 1 MPI and 12 threads, on our computer, this job finished in four minutes on our computer.

Per-particle defocus values are plotted by colour for each micrograph in the ``logfile.pdf``.
Can you spot micrographs with a tilted ice layer?

It is probably a good idea to re-run :jobtype:`3D auto-refine` and :jobtype:`Post-processing` at this stage, so we can confirm that the new particle STAR file actually gives better results.

For the :jobtype:`3D auto-refine`, we left all options as before, except on the :guitab:`I/O` tab:

:Input images STAR file: CtfRefine/job024/particles_ctf_refine.star

:Reference map: Refine3D/job019/run_class001.mrc

and on the :guitab:`Reference` tab:

:Ref. map is on absolute greyscale?: Yes

After another :jobtype:`Post-processing` job, the resolution didn't actually improve from 3.15 Å...
