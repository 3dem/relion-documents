Installation
=====================


Install MPI
-----------

Note that you'll need a computing cluster (or a multi-core desktop machine with :textsc:`nvidia` GPUs) with an MPI (message passing interface) installation.
To compile |RELION|, you'll need a mpi-devel package.
The exact flavour (OpenMPI, MPICH, LAM-MPI, etc) or version will probably not matter much.
If you don't have an mpi-devel installation already on your system, we recommend installing `OpenMPI <http://www.open-mpi.org/>`_.


Install CUDA
------------

If you have a relatively modern GPU from :textsc:`nvidia` (with compute capability 3.5+), then you can accelerate your autopicking, classification and refinement jobs considerably.
In order to compile |RELION| with GPU-acceleration support, you'll need to install :textsc:`cuda`.
We used :textsc:`cuda`-8.0 to prepare this tutorial.
Download it from `NVIDIA website <https://developer.nvidia.com/cuda-downloads>`_.


Install RELION
--------------

|RELION| is open-source software.
Download it for free from `RELION wiki <http://www2.mrc-lmb.cam.ac.uk/relion/index.php/Download_%26_install>`_ and follow the installation instructions.
If you're not familiar with your job submission system (e.g.
Sun Grid Engine, PBS/TORQUE, etc), then ask your system administrator for help in setting up the qsub.csh script as explained in the installation instructions.
Note that you will probably want to run so-called hybridly-parallel jobs, i.e. calculations that use both MPI for distributed-memory parallelization AND pthreads for shared-memory parallelization.
Your job submission queueing system may require some tweaking to allow this.
Again, ask your sysadmin for assistance.

.. attention::

    TODO: This section should be updated!


Install motion-correction software
----------------------------------

|RELION|-3.0 provides a wrapper to the UCSF program |MotionCor2|, which is used for whole-frame micrograph movie-alignment :cite:`zheng_motioncor2:_2017`.
Download the program from `David Agard's page <http://msg.ucsf.edu/em/software/motioncor2.html>`_ and follow his installation instructions.
Alternatively, you may also use RELION's own (CPU-only) implementation of |MotionCor2|, so don't worry if you have trouble installing the UCSF implementation.
Note that, as of version 3.0, the wrapper to :textsc:`unblur` :cite:`grant_measuring_2015` from Niko grigorieff's group has been discontinued from the GUI.


Install CTF-estimation software
-------------------------------

CTF estimation is not part of |RELION|.
Instead, |RELION| provides a wrapper to Alexis Rohou and Niko Grigorieff's :textsc:`ctffind` 4 :cite:`rohou_ctffind4:_2015`.
Please download this from `Niko's CTFFIND website <http://grigoriefflab.janelia.org/ctf>`_ and follow his installation instructions.
Alternatively, if you have :textsc:`nvidia` graphics cards (GPUs) in your machine, you may also use Kai Zhang's :textsc:`gctf` :cite:`zhang_gctf:_2016`, which may be downloaded from `Kai's website at LMB <http://www.mrc-lmb.cam.ac.uk/kzhang/>`_.

Install ResMap
--------------

Local-resolution estimation may be performed inside |RELION|'s own postprocessing program, or through a wrapper to Alp Kucukelbir's :textsc:`resmap` :cite:`kucukelbir_quantifying_2014`.
Please download it from `Alp's ResMap website <http://resmap.sourceforge.net/>`_  and follow his installation instructions.