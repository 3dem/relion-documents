.. note::

    |RELION| is distributed under a GPLv2 license, i.e. it is completely free, open-source software for both academia and industry.


Installation
============

The sections below explain how to download and install |RELION| on your computer. 

Note that |RELION| depends on and uses several external programs and libraries.

C++ compiler:
    RELION 5.0 requires a C++ compiler that fully supports the C++14 standard.
    For GCC, this means `version 5.0 or later <https://gcc.gnu.org/projects/cxx-status.html#cxx14>`_.
    Note that GCC 4.8, which comes with RedHat Enterprise Linux / Cent OS 7.x, is too old.
    You can obtain newer GCC via devtoolset or use free Intel compiler that comes with oneAPI toolkit (see below).

MPI:
    Your system will need `MPI <https://en.wikipedia.org/wiki/Message_Passing_Interface>`_ runtime (most flavours will do).
    If you don't have an MPI installation already on your system, we recommend installing `OpenMPI <http://www.open-mpi.org/>`_.

CUDA, HIP/ROCm, SYCL or oneAPI intel compilers:
    If you have GPUs from :textsc:`nvidia`, AMD or Intel, you can accelerate many jobs considerably.

    By default, |RELION| will build with GPU-acceleration support, for which you'll need :textsc:`cuda`.
    Download it from `NVIDIA website <https://developer.nvidia.com/cuda-downloads>`_.
    Note that CUDA toolkits support only a limited range of C compilers.
    Also note that a newer CUDA toolkit requires a newer GPU driver.
    Carefully read the release note and make sure you have a compatible set of GPU driver, C compiler and CUDA toolkit.

    If you want to compile with HIP/ROCm, you will need
        - `AMD ROCm <https://docs.amd.com/en/docs-5.7.1/deploy/linux/index.html>`_
    
    If you want to compile with SYCL, you will need
        - `Intel oneAPI Base Toolkit and HPC Toolkit <https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html>`_ (All components recommended; this is also recommended if you want to build the CPU acceleration path, see below)
	- `Intel software for general purpose GPU capabilities <https://dgpu-docs.intel.com>`_
	- `Intel CPU Runtime for OpenCL(TM) Applications <https://www.intel.com/content/www/us/en/developer/articles/technical/intel-cpu-runtime-for-opencl-applications-with-sycl-support.html>`_ (optional)
	- `Codeplay oneAPI for NVIDIA GPU <https://developer.codeplay.com/products/oneapi/nvidia>`_ (optional)
	- `Codeplay oneAPI for AMD GPU <https://developer.codeplay.com/products/oneapi/amd>`_ (optional)

CTFFIND-4.1:
    CTF estimation is not part of |RELION|.
    Instead, |RELION| provides a wrapper to Alexis Rohou and Niko Grigorieff's :textsc:`ctffind` 4 :cite:`rohou_ctffind4:_2015`.
    Alternatively, you may also use (the closed-source) :textsc:`gctf` by Kai Zhang :cite:`zhang_gctf:_2016`, which may be downloaded from `Kai's website <http://www.mrc-lmb.cam.ac.uk/kzhang/>`_.

Ghostscript:
    RELION uses `Ghostscript <https://www.ghostscript.com/>`_ to generate PDF files.

FLTK (only for GUI):
    RELION uses `FLTK <https://www.fltk.org/>`_ as a GUI tool kit.
    This will be installed automatically (see below).

X Window system libraries (only for GUI):
    RELION needs basic X11 libraries together with `Xft <https://www.freedesktop.org/wiki/Software/Xft/>`_ for the GUI.
    Most Linux distributions have packages called ``libxft-dev`` or ``libXft-devel`` and ``libX11-devel``.
    Note that you need developer packages if you build your own FLTK.

FFT libraries:
    RELION needs an FFT library.
    The default is `FFTW <https://www.fftw.org/>`_.
    This will be installed automatically (see below).
    Depending on your CPU, `Intel MKL FFT <https://software.intel.com/mkl>`_ or `AMD optimised FFTW <https://developer.amd.com/amd-aocl/fftw/>`_ might run faster.
    See below how to use them.

libtiff:
    RELION needs `libtiff <http://www.libtiff.org/>`_ version >= 4.0.
    Most Linux distributions have packages called ``libtiff-dev`` or ``libtiff-devel``.
    Note that you need a developer package.

libpng:
    RELION needs `libpng <http://www.libpng.org/pub/png/libpng.html>`_.
    Most Linux distributions have packages called ``libpng-dev`` or ``libpng-devel``.
    Note that you need a developer package.

pbzip2, xz, zstd:
    RELION needs these commands in the ``PATH`` to read MRC movies compressed by bzip2, xz or ZStandard, respectively.
    Note that RELION uses ``pbzip2``, not ``bzip2``.
    Most Linux distributions provide packages for these utilities.

UCSF MotionCor2 (optional):
    |RELION| implements its own (CPU-only) implementation of the UCSF |MotionCor2| algorithm for whole-frame micrograph movie-alignment :cite:`zheng_motioncor2:_2017`.
    If you want, you can still use the (GPU-accelerated) UCSF program.
    You can download it from `David Agard's page <http://msg.ucsf.edu/em/software/motioncor2.html>`_ and follow his installation instructions.
    Note that using the UCSF program does not make full advantage of the opportunities provided in Bayesian polishing.

ResMap (optional):
    Local-resolution estimation may be performed inside |RELION|'s own postprocessing program.
    Alternatively, one can also use Alp Kucukelbir's :textsc:`resmap` :cite:`kucukelbir_quantifying_2014`.
    Download it from `Alp's ResMap website <http://resmap.sourceforge.net/>`_  and follow his installation instructions.


In practice, most of these dependencies can be installed by system's package manager if you have the root priviledge.

In Debian or Ubuntu::

    sudo apt install cmake git build-essential mpi-default-bin mpi-default-dev libfftw3-dev libtiff-dev libpng-dev ghostscript libxft-dev
 

In RHEL, Cent OS, Scientific Linux::

    sudo yum install cmake git gcc gcc-c++ openmpi-devel fftw-devel libtiff-devel libpng-devel ghostscript libXft-devel libX11-devel


Download RELION
---------------

We store the public release versions of |RELION| on `GitHub <https://github.com/3dem/relion>`_, a site that provides code-development with version control and issue tracking through the use of ``git``.
We will not describe the use of git in general, as you will not need more than very basic features.
Below we outline the few commands needed on a UNIX-system, please refer to general git descriptions and tutorials to suit your system.
To get the code, you clone or download the repository.
We recommend cloning, because it allows you very easily update the code when new versions are released.
To do so, use the shell command-line::

    git clone https://github.com/3dem/relion.git

This will create a local Git repository.
All subsequent git-commands should be run inside this directory.

The `master` branch (default) contains the stable release of |RELION|-4.0.
By performing::

    git checkout ver5.0

you can access the latest (developmental) updates for RELION 5.0x.

The code will be intermittently updated to amend issues.
To incorporate these changes, use the command-line::

    git pull

inside you local repository (the source-code directory downloaded).
If you have changed the code in some way, this will force you to commit a local merge.
You are free to do so, but we will assume you have not changed the code.
Refer to external instructions regarding git and merging so-called conflicts if you have changed the code an need to keep those changes.

Setup a conda environment
-------------------------

To add support for Python modules (e.g. Blush, ModelAngelo and DynaMight) you will have to setup a Python environment with dependencies.
We recommend installing via `Miniconda3 <https://docs.conda.io/en/latest/miniconda.html>`_.

Once you have conda setup, you can install all the RELION Python dependencies into a new environment by running::

    conda env create -f environment.yml

Also code in this environment will be updated intermittently. You can incorporate the latest changes by running::

    conda env update -f environment.yml

.. warning::
    You should **NOT** activate this ``relion-5.0`` conda environment when compiling and using RELION;
    RELION activates it automatically only when necessary.
    Otherwise, system-wide installation of compilers/libraries/MPI runtime might get mixed up with those provided by conda, leading to compilation failures or runtime errors.
    The same applies to other software packages that provide their own libraries/MPI runtime, such as CCPEM, CCP4, EMAN2, DIALS, PHENIX.

The ``cmake`` command should automatically detect the ``relion-5.0`` conda environment created above.
If it does not, you can specify ``-DPYTHON_EXE_PATH=path/to/your/conda/python``.
Additionally, if you intend to make use of automatically downloaded pretrained model weights (used in e.g. Blush, ModelAngelo and class_ranker), it's recommended to set the ``TORCH_HOME`` directory by include the flag ``-DTORCH_HOME_PATH=path/to/torch/home``.
Otherwise, it will be downloaded to the default location (usually ``~/.cache/torch``).

At the moment, the model weights for Blush are stored on MRC-LMB's FTP server.
If your network blocks FTP, please follow `instructions here <https://github.com/3dem/relion/issues/1003#issuecomment-1786280151>`_.

Compilation
-----------

|RELION| has an installation procedure which relies on ``cmake``.
You will need to have this program installed, but most UNIX-systems have this by default.
You will need to make a build-directory in which the code will be compiled.
This can be placed inside the repository::

     cd relion
     mkdir build
     cd build

You then invoke ``cmake`` inside the build-directoy, but point to the source-directoy to configure the installation.
This will not install |RELION|, just configure the build::

     cmake ..

The output will notify you of what was detected and what type of build will be installed.
Because |RELION| is rich in terms of the possible configurations, it is important to check this output.
For instance:

*   The path to the MPI library.
*   GPU-capability will only be included if a CUDA SDK is detected.
    If not, the program will install, but without support for GPUs.
*   The path to the Python interpreter.
*   If FFTW is not detected, instructions are included to download and install it in a local directory known to the |RELION| installation.
*   As above, regarding FLTK (required for GUI).
    If a GUI is not desired, this can be escaped as explained in the following section.

The MPI library must be the one you intend to use |RELION| with.
Compiling |RELION| with one version of MPI and running the resulting binary with ``mpirun`` from another version can cause crash.
Note that some software packages (e.g. CCPEM, crYOLO, EMAN2) come with their own MPI runtime.
Sourcing/activating their environment might update ``PATH`` and ``LD_LIBRARY_PATH`` environmental variables and put their MPI runtime into the highest priority.

The MPI C++ compiler (``mpicxx``) and CUDA compiler (``nvcc``) internally calls a C++ compiler.
This must match the compiler ``cmake`` picked up.
Otherwise, the compilation might fail at the linking step.

Following the completion of cmake-configuration without errors, ``make`` is used to install the program::

     make -j N

, where ``N`` is the number of processes to use during installation.
Using a higher number simply means that it will compile faster.

Take note of any warnings or errors reported.
|RELION| will be installed in the ``build`` directory's sub-directory called ``bin``.
To make the installation system-wide, see below.

Wherever you install |RELION|, make sure your ``PATH`` environmental variable points to the directory containing relion binaries.
Launching |RELION| with a path like ``/path/to/relion`` is not the right way;
this starts the right GUI, but the GUI might invoke other versions of |RELION| in the ``PATH``.

General configuration
---------------------

`CMake <https://cmake.org/>`_ allows configuration of many aspects of the installation, some of which are outlined here.
Note that by default, |RELION| is configured to build with CUA acceleration on NVidia GPUs. Instructions for building with CPU, HIP/Rocm (AMD) SYCL (Intel et al) acceleration are given in the next section below.

Most options can be set by adding options to the ``cmake`` configuration.
Under the below subheadings, some example replacement commands are given to substitute the original configuration command.
It is also recommended to clean or purge your build-directory between builds, since CMake caches some of previous configurations::

     cd build
     rm -fr *

And of course, any of the below options can be combined.

Omitting the GUI:
     ``cmake -DGUI=OFF ..`` (default is ON)

     With this option, GUI programs (e.g. ``relion``, ``relion_manualpick``, ``relion_display``) are not be built and FLTK becomes unnecessary.

Using single-precision on the CPU:
    ``cmake -DDoublePrec_CPU=OFF ..`` (default is ON)

    This will reduce (CPU but not GPU) memory consumption to about half.
    This is useful when memory hungry tasks such as motion correction and Polishing run out of memory.
    This is safe in most cases but please use the default double precision build if CtfRefine produces NaNs.

Using double-precision on the GPU:
    ``cmake -DDoublePrec_GPU=ON ..`` (default is OFF)

    This will slow down GPU-execution considerably, while this does *NOT* improve the resolution.
    Thus, this option is not recommended.

Compiling NVIDIA GPU codes for your architecture:
    ``cmake -DCUDA_ARCH=52 ..`` (default is 35, meaning compute capability 3.5, which is the lowest supported by |RELION|)

    CUDA-capable NVIDIA devices have a so-called compute capability, which code can be compiled against for optimal performance.
    The compute capability of your card can be looked up at `the table in NVIDIA website <https://developer.nvidia.com/cuda-gpus>`_.
    WARNING: If you use a wrong number, compilation might succeed but the resulting binary can fail at the runtime.

Forcing build and use of local FFTW:
    ``cmake -DFORCE_OWN_FFTW=ON ..``

    This will download, verify and install FFTW during the installation process.

Forcing build and use of AMD optimized FFTW:
    ``cmake -DFORCE_OWN_FFTW=ON -DAMDFFTW=ON ..``

    This will download, verify and install AMD optimized version of FFTW during the installation process.
    This is recommended for AMD CPUs (e.g. Ryzen, Threadripper, EPYC).

Forcing build and use of Intel MKL FFT:
    ``cmake -DMKLFFT=ON ..``

    This will use FFT library from Intel MKL.
    In contrast to the FFTW options above, this will *not* download MKL automatically.
    You have to install MKL and set relevants paths (usually by sourcing the ``mkl_vars.sh`` script).

Forcing build and use of local FLTK:
    ``cmake -DFORCE_OWN_FLTK=ON ..``

    This will download, verify and install FLTK during the installation process.
    If any of these are not detected during configuration, this will happen automatically anyway, and you should not have to specify the below options manually.

Specify location of libtiff:
    ``cmake -DTIFF_INCLUDE_DIR=/path/to/include -DTIFF_LIBRARY=/path/to/libtiff.so.5``

    This option is to use libtiff installed in non-standard location.

Specifying an installation location:
    To allow |RELION| a system-wide installation use::

        cmake -DCMAKE_INSTALL_PREFIX=/path/to/install/dir/ ..
        make -j N
        make install

.. warning::
    Do not specify the ``build`` directory itself as ``CMAKE_INSTALL_PREFIX``.
    This does not work!
    If you are happy with binaries in the build directory, leave ``CMAKE_INSTALL_PREFIX`` as default and omit the ``make install`` step.

Configuration with CPU acceleration
-----------------------------------

Enable accelerated CPU code path:
    ``cmake -DALTCPU=ON``

    Note that this is mutually exclusive with GPU acceleration (``-DCUDA=ON``).
    Intel Classic compilers are recommended for this option (see below).

Use Intel Classic compilers:
    Intel Classic compilers often generate faster binaries for Intel CPUs, especially when combined with the accelerated CPU code path above.
    Intel Classic compilers are available free of chage as part of `Intel oneAPI HPC toolkit <https://software.intel.com/content/www/us/en/develop/tools/oneapi/hpc-toolkit.html>`_.
    Note that Intel Classic compilers are being deprecated in favour of LLVM-based new Intel compilers.
    As of 2023 October, the classic compilers generate faster binaries than newer compilers.
    We recommend you to keep oneAPI toolkit installers, in case Intel stops the distribution of classic compilers.

    To use Intel Classic compilers, run below after sourcing the initialization script (`setvars.sh`)::

        mkdir build-cpu
        cd build-cpu
        cmake .. -DMKLFFT=ON \
        -DCMAKE_C_COMPILER=icc -DCMAKE_CXX_COMPILER=icpc -DMPI_C_COMPILER=mpiicc -DMPI_CXX_COMPILER=mpiicpc \
        -DCMAKE_C_FLAGS="-O3 -ip -g -xCOMMON-AVX512 -restrict " \
        -DCMAKE_CXX_FLAGS="-O3 -ip -g -xCOMMON-AVX512 -restrict "
	make -j 24

    This generates binaries optimized with AVX512 instructions.
    If your CPU supports only up to AVX256, use ``-xCORE-AVX2`` instead of ``-xCOMMON-AVX512``.

    If you don't want to use Intel MPI, change ``mpiicc`` and ``mpiicpc`` accordingly.
    For example, to use OpenMPI with Intel compilers, specify ``mpicc`` and ``mpicxx`` after setting environmental variables ``OMPI_CC=icc`` and ``OMPI_CXX=icpc``.
    If `cmake` still picks up Intel MPI, specify `MPI_HOME`.
    See `OpenMPI FAQ <https://www.open-mpi.org/faq/?category=mpi-apps#override-wrappers-after-v1.0>`_ and `FindMPI manual <https://cmake.org/cmake/help/latest/module/FindMPI.html#variables-for-locating-mpi>`_ for details.


Configuration with HIP/ROCm acceleration for AMD GPUs
-----------------------------------------------------

Enable the accelerated HIP/ROCm code path with:
    ``cmake -DHIP=ON``

Note that this is mutually exclusive with other accelerated code paths (e.g. CUDA, ALTCPU and SYCL).
On our system, we build with HIP/ROCm acceleration to use AMD GPUs with the following commands::

        export LD_LIBRARY_PATH=/opt/rocm/lib:$LD_LIBRARY_PATH
        export PATH=/opt/rocm/:$PATH
        export ROCM_PATH=/opt/rocm/
        mkdir build-amd
        cd build-amd
        cmake -DCMAKE_BUILD_TYPE=Release -DHIP=ON -DHIP_ARCH="gfx90a,gfx908" -DFORCE_OWN_FFTW=ON  -DAMDFFTW=on ..
        make -j 24

If you get problems finding ``omp.h``, make sure you have ``openmp-extras-devel`` installed on your system too.

Configuration with SYCL acceleration (Intel GPUs)
-------------------------------------------------

Enable accelerated the SYCL code path with:
    ``cmake -DSYCL=ON``

Note that this is mutually exclusive with other accelerated code paths (e.g. CUDA, ALTCPU and HIP/ROCm).
Technically speaking, you can build SYCL for AMD and NVIDIA GPUs to make a single binary that runs on NVIDIA, AMD and Intel GPUs,
but this is highly experimental and not tested well.

For now, this way of building RELION is `explained here: <https://github.com/3dem/relion/blob/ver5.0/README_sycl.md>`_.


Set-up queue job submission
---------------------------

The GUI allows the user to submit jobs to a job queueing system with a single click.
For this to work, a template job submission script needs to be provided for the queueing system at hand (e.g. TORQUE, PBS, SGE).
In this script a set of strings (variables) in the template script is replaced by the values given in the GUI.
The following table contains all defined variables:

.. list-table::
   :widths: 25 15 65
   :header-rows: 1

   * - String
     - Variable
     - Meaning
   * - ``XXXoutfileXXX``
     - string
     - The standard output log file RELION GUI displays.
   * - ``XXXerrfileXXX``
     - string
     - The standard error log file RELION GUI displays.
   * - ``XXXcommandXXX``
     - string
     - relion command + arguments
   * - ``XXXqueueXXX``
     - string
     - Name of the queue to submit job to
   * - ``XXXmpinodesXXX``
     - integer
     - The number of MPI processes to use
   * - ``XXXthreadsXXX``
     - integer
     - The number of threads to use on each MPI process
   * - ``XXXcoresXXX``
     - integer
     - The number of MPI processes times the number of threads
   * - ``XXXdedicatedXXX``
     - integer
     - The minimum number of cores on each node (use this to fill entire nodes)
   * - ``XXXnodesXXX``
     - integer
     - The total number of nodes to be requested
   * - ``XXXextra1XXX``
     - string
     - Installation-specific, see below
   * - ``XXXextra2XXX``
     - string
     - Installation-specific, see below

The ``XXXcommandXXX`` variable needs a special care.
For non-MPI commands (e.g. ``relion_refine``) not only the variable but the whole line is replaced.
Thus, ``mpirun XXXcommandXXX`` will be ``mpirun relion_refine_mpi`` for an MPI job but ``relion_refine`` for a non-MPI job.
Also note that some jobs consist of multiple lines of commands.
See CCPEM threads (`1 <https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?A2=ind2205&L=CCPEM&O=D&P=38145>`_ and `2 <https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?A2=ind2204&L=CCPEM&D=0&O=D&P=61014>`_) for typical pitfalls.

There are two environment variables that control the use of the entry of the 'Minimum number of dedicated cores per node' on the Running tabs of the GUI: ``RELION_MINIMUM_DEDICATED`` sets its default value (1 if not set); ``RELION_ALLOW_CHANGE_MINIMUM_DEDICATED`` sets whether the user will be able to change this entry. At LMB, we set the default to 24 and do not allow users to change it. In this way, we enforce that our hyper-threaded 12-core nodes get filled up entirely by individual |RELION| jobs.

By default, the ``XXXextra1XXX``, ``XXXextra2XXX``, ... variables are not used.
They provide additional flexibility for queueing systems that require additional variables.
They may be activated by first setting ``RELION_QSUB_EXTRA_COUNT`` to the number of fields you need (e.g.
2) and then setting the ``RELION_QSUB_EXTRA1``, ``RELION_QSUB_EXTRA2``, ... environment variables, respectively. This will result in extra input fields in the GUI, with the label text being equal to the value of the environment variable.
Likewise, their default values (upon starting the GUI) can be set through environment variables ``RELION_QSUB_EXTRA1_DEFAULT``, ``RELION_QSUB_EXTRA2_DEFAULT``, etc and their help messages can be set through environmental variables ``RELION_QSUB_EXTRA1_HELP``, ``RELION_QSUB_EXTRA2_HELP`` and so on.
But note that (unlike all other entries in the GUI) the extra values are not remembered from one run to the other.

The template job submission script may be saved in any location.
By default, the one used at the LMB is present as ``gui/qsub.csh`` in the |RELION| tar-ball.
Upon installation this file is copied to the bin directory.
It is convenient for the user if he does not have to select this file each time he opens the |RELION| GUI in a new directory.
Therefore, one may set the environment variable ``RELION_QSUB_TEMPLATE`` to point to the location of the script for the system at hand.
This value will be pre-set as default in the GUI.
(Note the user still has the liberty to define and use his own template!)

.. note::

     If somehow the job queue submission cannot be set up, |RELION| may still be run in parallel and on a job queueing system.
     The GUI comprises a Print command button that prints the entire |RELION| command, including all arguments, to the screen.
     Pasting of this command to a job queue submission script, and manual submission of this script may then be used to submit the parallel job to a queueing system.

..
    COMMENTED OUT FOR NOW.
    For illustrative purposes, have a look at the following examples:
    * [[SGE template script example]] used at the LMB
    * [[TORQUE template script example]] used at the CNB-CSIC
    * [[manual machinefile script example]] used at Columbia (no queueing system involved)


Edit the environment set-up
---------------------------

For |RELION|, we source the following C-shell setup in our ``.cshrc`` file.
You'll need to change all the paths for your own system, and translate the script in case you use a bash shell (which uses `export` instead of `setenv` etc).

::

     #!/bin/csh -f
     
     # Setup openMPI if not already done so
     if ("" == "`echo $path | grep /public/EM/OpenMPI/openmpi/bin`") then
             set path=(/public/EM/OpenMPI/openmpi/bin $path)
     endif
     if ("1" == "$?LD_LIBRARY_PATH") then
             if ("$LD_LIBRARY_PATH" !~ */public/EM/OpenMPI/openmpi/lib*) then
                     setenv LD_LIBRARY_PATH /public/EM/OpenMPI/openmpi/lib:$LD_LIBRARY_PATH
             endif
     else
             setenv LD_LIBRARY_PATH /public/EM/OpenMPI/openmpi/lib
     endif
     
     # Setup |RELION| if not already done so
     if ("" == "`echo $path | grep /public/EM/RELION/relion/bin`") then
     	set path=(/public/EM/RELION/relion/bin $path)
     endif
     if ("1" == "$?LD_LIBRARY_PATH") then
             if ("$LD_LIBRARY_PATH" !~ */public/EM/RELION/relion/lib*) then
                     setenv LD_LIBRARY_PATH /public/EM/RELION/relion/lib:$LD_LIBRARY_PATH
             endif
     else
             setenv LD_LIBRARY_PATH /public/EM/RELION/relion/lib
     endif
     
     # CUDA for RELION
     setenv PATH /public/EM/CUDA/Cuda11.4/bin:$PATH
     setenv LD_LIBRARY_PATH /public/EM/CUDA/Cuda11.4/lib64:$LD_LIBRARY_PATH
     setenv CUDA_HOME /public/EM/CUDA/Cuda11.4
     
     # Where is qsub template script stored
     setenv RELION_QSUB_TEMPLATE /public/EM/RELION/relion-devel/bin/qsub.csh
     
     # Default PDF viewer
     setenv RELION_PDFVIEWER_EXECUTABLE evince
     
     # Default MOTIONCOR2 executable
     setenv RELION_MOTIONCOR2_EXECUTABLE /public/EM/MOTIONCOR2/bin/MotionCor2_1.0.4
     
     # Default CTFFIND-4.1+ executable
     setenv RELION_CTFFIND_EXECUTABLE /public/EM/ctffind/ctffind.exe
     
     # Default Gctf executable
     setenv RELION_GCTF_EXECUTABLE /public/EM/Gctf/bin/Gctf
 
     # Default ResMap executable
     setenv RELION_RESMAP_EXECUTABLE /public/EM/ResMap/ResMap-1.1.4-linux64
     
     # Enforce cluster jobs to occupy entire nodes with 24 hyperthreads
     setenv RELION_MINIMUM_DEDICATED 24
     # Do not allow the user to change the enforcement of entire nodes
     setenv RELION_ALLOW_CHANGE_MINIMUM_DEDICATED 0
     
     # Ask for confirmation if users try to submit local jobs with more than 12 MPI nodes
     setenv RELION_WARNING_LOCAL_MPI 12
     
     # Other useful variables
     # RELION_MPI_RUN: The mpi runtime ('mpirun' by default)
     # RELION_QSUB_NRMPI: The default for 'Number of MPI procs'
     # RELION_MPI_MAX: The maximum number of MPI processes available from the GUI
     # RELION_QSUB_NRTHREADS: The default for 'Number of threads'
     # RELION_THREAD_MAX: The maximum number of threads per MPI process available from the GUI
     # RELION_QUEUE_USE: The default for 'Submit to queue?'. "yes" or "no".
     # RELION_QUEUE_NAME: The default for 'Queue Name"
     # RELION_QSUB_COMMAND: The default for 'Queue submit command'
     # RELION_MINIMUM_DEDICATED: The default for 'Minimum dedicated cores per node'
     # RELION_ALLOW_CHANGE_MINIMUM_DEDICATED: Whether to allow a user to change the 'Minimum dedicated cores per node' field in the GUI
     # RELION_SHELL: A shell used to launch CTFFIND/GCTF in CtfFind jobs ('csh' by default; only available from 3.1)
     # RELION_SCRATCH_DIR: The default scratch directory in the GUI
     # RELION_STACK_BUFFER: The buffer size used for MRC(S) file I/O, potentially useful on GPFS or Lustre file system. See https://github.com/3dem/relion/pull/783 for details.
