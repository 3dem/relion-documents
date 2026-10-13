
Command Line Reference
======================

``relion_ctf_mask_test``
-------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input particle *.star file
                                    --s : Image size
                                    --r : Particle radius
                                    --t : Frequency step
                                   --tw : Filter step width
                                    --o : Output path
                                --j (1) : Number of threads
                               --mg (0) : Micrograph index
                              --version : Print RELION version and exit

``relion_particle_select``
---------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file containing the source particles
                                --i_ref : Input STAR file containing reference particles
                       --angles (false) : Copy particle viewing angles from reference
                      --offsets (false) : Copy particle offsets from reference
                    --o (selected.star) : Output path
                              --version : Print RELION version and exit

``relion_demodulate``
----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file with a list of particles
                                  --out : Output path
                                --j (6) : Number of OMP threads
                          --r31 (false) : Write output in Relion-3.1 format
                              --version : Print RELION version and exit

``relion_estimate_gain``
-------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Options ===== 
                                    --i : Input movie STAR file
                                    --o : Output file name
                                --j (1) : Number of threads
                      --max_frames (-1) : Target number of frames to average (rounded to movies; -1 means use all)
                       --random (false) : Randomise the order of input movies before taking subset
                  --dont_invert (false) : Don't take the inverse but simply writes the sum
                   --eer_upsampling (2) : EER upsampling (1 = 4K or 2 = 8K)
                              --version : Print RELION version and exit

``relion_ctf_refine``
----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file containing the particles
                                    --f : Input STAR file with the FSC of the reference (usually from PostProcess)
                                    --o : Output directory, e.g. CtfRefine/job041/
                                --m1 () : Reference map, half 1
                                --m2 () : Reference map, half 2
                      --angpix_ref (-1) : Pixel size of the reference map
                              --mask () : Reference mask
                              --pad (2) : Padding factor
           --only_do_unfinished (false) : Skip those steps for which output files already exist.
                      --ctf_pad (false) : Use larger box to calculate CTF and then downscale to mimic boxing operation in real space
                         --diag (false) : Write out diagnostic data (slower)
    ====== Defocus fit options ===== 
                  --fit_defocus (false) : Perform refinement of per-particle defocus values?
                     --fit_mode (fpmfm) : String of 5 characters describing whether to fit the phase shift (1), 
                                          defocus (2), astigmatism (3), spherical aberration (4) and B-factors (5) 
                                          per particle ('p'), per micrograph ('m') or to keep them fixed ('f')
                                          during the per-micrograph CTF refinement.
              --max_defocus_iters (100) : Maximum number of iterations for CTF refinement.
                          --bf0 (false) : Perform brute-force per-particle defocus search (as in RELION 3.0) prior 
                                          to the per-micrograph CTF refinement.
                          --bf1 (false) : Perform brute-force defocus search after CTF refinement.
                      --bf_only (false) : Skip CTF refinement and only perform a brute-force defocus search.
                     --bf_range (2000.) : Defocus scan range (in A) for brute-force search.
                 --legacy_astig (false) : Estimate independent per-particle astigmatism (from RELION 3.0)
                  --kmin_defocus (30.0) : Inner freq. threshold for defocus estimation [Angst]
    ====== B-factor options ===== 
                    --fit_bfacs (false) : Estimate CTF B-factors
                  --bfac_per_mg (false) : Estimate B-factors per micrograph, instead of per particle
                     --bfac_min_B (-30) : Minimal allowed B-factor
                     --bfac_max_B (300) : Maximal allowed B-factor
                 --bfac_min_scale (0.2) : Minimal allowed scale-factor (essential for outlier rejection)
                     --kmin_bfac (30.0) : Inner freq. threshold for B-factor estimation [Angst]
    ====== Beam-tilt options ===== 
                 --fit_beamtilt (false) : Perform refinement of beamtilt
                     --kmin_tilt (20.0) : Inner freq. threshold for beamtilt estimation [Å]
                  --odd_aberr_max_n (0) : Maximum degree of Zernike polynomials used to fit odd (i.e. antisymmetrical) aberrations
                           --xr0_t (-1) : Exclusion ring start [Å] - use to exclude dominant frequency (e.g. for helices)
                           --xr1_t (-1) : Exclusion ring end [Å]
    ====== Symmetric aberrations options ===== 
                    --fit_aberr (false) : Estimate symmetric aberrations
                    --kmin_aberr (20.0) : Inner freq. threshold for symmetrical aberration estimation [Å]
                 --even_aberr_max_n (4) : Maximum degree of Zernike polynomials used to fit even (i.e. symmetrical) aberrations
                           --xr0_a (-1) : Exclusion ring start [Å]
                           --xr1_a (-1) : Exclusion ring end [Å]
    ====== Anisotropic magnification options ===== 
                    --fit_aniso (false) : Estimate anisotropic magnification
                      --kmin_mag (20.0) : Inner freq. threshold for anisotropic magnification estimation [Angst]
                   --keep_astig (false) : Do not translate astigmatism into new coordinates
                   --part_astig (false) : Allow astigmatism to vary among the particles of a micrograph
    ====== Computational options ===== 
                                --j (1) : Number of (OMP) threads
                           --min_MG (0) : First micrograph index
                          --max_MG (-1) : Last micrograph index (default is to process all)
                        --debug (false) : Write debugging data
                             --verb (1) : Verbosity
                              --version : Print RELION version and exit

``relion_merge_particles``
---------------------------------------------------------------------

.. code-block:: text

    usage: relion_merge_particles <input1> <input2> ... <inputN> <output>

``relion_run_ctffind``
-----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
    ====== CTF estimation ===== 
                                    --i : STAR file with all input micrographs, or a unix wildcard to all micrograph files, e.g. "mics/*.mrc"
                     --use_noDW (false) : Estimate CTFs from rlnMicrographNameNoDW instead of rlnMicrographName (only after MotionCor2)
                     --o (CtfEstimate/) : Directory, where all output files will be stored
               --only_make_star (false) : Don't estimate any CTFs, only join all logfile results in a STAR file
           --only_do_unfinished (false) : Only estimate CTFs for those micrographs for which there is not yet a logfile with Final values.
                      --do_at_most (-1) : Only process up to this number of (unprocessed) micrographs.
                          --ctfWin (-1) : Size (in pixels) of a centered, squared window to use for CTF-estimation
    ====== Microscopy parameters ===== 
                              --CS (-1) : Spherical Aberration (mm) 
                              --HT (-1) : Voltage (kV)
                         --AmpCnst (-1) : Amplitude constrast
                          --angpix (-1) : Pixel size in the input micrographs (A)
    ====== CTFFIND parameters ===== 
                       --ctffind_exe () : Location of ctffind executable (or through RELION_CTFFIND_EXECUTABLE environment variable)
                            --Box (512) : Size of the boxes to calculate FFTs
                         --ResMin (100) : Minimum resolution (in A) to include in calculations
                           --ResMax (7) : Maximum resolution (in A) to include in calculations
                        --dFMin (10000) : Minimum defocus value (in A) to search
                        --dFMax (50000) : Maximum defocus value (in A) to search
                          --FStep (250) : defocus step size (in A) for search
                             --dAst (0) : amount of astigmatism (in A)
    ====== CTFFIND4 parameters ===== 
                  --is_ctffind4 (false) : The provided CTFFIND executable is CTFFIND4 (version 4.1+)
                 --use_given_ps (false) : Use pre-calculated power spectra?
          --do_movie_thon_rings (false) : Calculate Thon rings from movie frames?
                 --avg_movie_frames (1) : Average over how many movie frames (try to get 4 e-/A2)
         --movie_rootname (_movie.mrcs) : Rootname plus extension for movies
                --do_phaseshift (false) : Estimate the phase shift in the images (e.g. from a phase-plate)
                       --phase_min (0.) : Minimum phase shift (in degrees)
                     --phase_max (180.) : Maximum phase shift (in degrees)
                     --phase_step (10.) : Step in phase shift (in degrees)
                                --j (1) : Number of threads (for CTFIND4 only)
                  --fast_search (false) : Disable "Slower, more exhaustive search" in CTFFIND4.1 (faster but less accurate)
    ====== Gctf parameters ===== 
                     --use_gctf (false) : Use Gctf instead of CTFFIND to estimate the CTF parameters
                          --gctf_exe () : Location of Gctf executable (or through RELION_GCTF_EXECUTABLE environment variable)
        --ignore_ctffind_params (false) : Use Gctf default parameters instead of CTFFIND parameters
                          --EPA (false) : Use equi-phase averaging to calculate Thon rinds in Gctf
                --do_validation (false) : Use validation inside Gctf to analyse quality of the fit?
                --extra_gctf_options () : Additional options for Gctf
                               --gpu () : Device ids for each MPI-thread, e.g 0:1:2:3
                              --version : Print RELION version and exit

``relion_preprocess_mpi``
--------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --i () : The STAR file with all (selected) micrographs to extract particles from
                      --coord_suffix () : The suffix for the coordinate files, e.g. "_picked.star" or ".box"
                  --coord_dir (ASINPUT) : The directory where the coordinate files are (default is same as micrographs)
                --part_dir (Particles/) : Output directory for particle stacks
                         --part_star () : Output STAR file with all particles metadata
               --reextract_data_star () : A _data.star file from a refinement to re-extract, e.g. with different binning or re-centered (instead of --coord_suffix)
        --keep_ctfs_micrographs (false) : By default, CTFs from fn_data will be kept. Use this flag to keep CTFs from input micrographs STAR file
                --reset_offsets (false) : reset the origin offsets from the input _data.star file to zero?
                     --recenter (false) : Re-center particle according to rlnOriginX/Y in --reextract_data_star STAR file
                      --recenter_x (0.) : X-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --recenter_y (0.) : Y-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --recenter_z (0.) : Z-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --ref_angpix (-1) : Pixel size of the reference used for recentering. -1 uses the pixel size of particles.
    ====== Particle extraction ===== 
                      --extract (false) : Extract all particles from the micrographs
                    --extract_size (-1) : Size of the box to extract the particles in (in pixels)
              --premultiply_ctf (false) : Premultiply the micrograph/frame with its CTF prior to particle extraction
        --premultiply_extract_size (-1) : Size of the box to extract the particles in (in pixels) before CTF premultiplication
        --ctf_intact_first_peak (false) : When premultiplying with the CTF, leave frequencies intact until the first peak
                   --phase_flip (false) : Flip CTF-phases in the micrograph/frame prior to particle extraction
                   --extract_bias_x (0) : Bias in X-direction of picked particles (this value in pixels will be added to the coords)
                   --extract_bias_y (0) : Bias in Y-direction of picked particles (this value in pixels will be added to the coords)
           --only_do_unfinished (false) : Extract only particles if the STAR file for that micrograph does not yet exist.
    ====== Particle operations ===== 
                    --project3d (false) : Project sub-tomograms along Z to generate 2D particles
                           --scale (-1) : Re-scale the particles to this size (in pixels)
                          --window (-1) : Re-window the particles to this size (in pixels)
                         --norm (false) : Normalise the background to average zero and stddev one
                      --no_ramp (false) : Just subtract the background mean in the normalisation, instead of subtracting a fitted ramping background. 
                       --bg_radius (-1) : Radius of the circular mask that will be used to define the background area (in pixels)
                      --white_dust (-1) : Sigma-values above which white dust will be removed (negative value means no dust removal)
                      --black_dust (-1) : Sigma-values above which black dust will be removed (negative value means no dust removal)
              --invert_contrast (false) : Invert the contrast in the input images
                        --operate_on () : Use this option to operate on an input image stack 
      --operate_out (preprocessed.mrcs) : Output name when operating on an input image stack
    ====== Helix extraction ===== 
                        --helix (false) : Extract helical segments
         --helical_outer_diameter (-1.) : Outer diameter of helical tubes in Angstroms (for masks of helical segments)
                --helical_tubes (false) : Extract helical segments from tube coordinates
                   --helical_nr_asu (1) : Number of helical asymmetrical units
                    --helical_rise (0.) : Helical rise (in Angstroms)
      --helical_bimodal_angular_priors (false) : Add bimodal angular priors for helical segments
      --helical_cut_into_segments (false) : Cut helical tubes into segments
    ====== MPI options ===== 
                    --max_mpi_nodes (8) : Limit the number of effective MPI nodes to protect from too heavy disk I/O (thus ignoring larger values from mpirun)
                              --version : Print RELION version and exit

``relion_run_ctffind_mpi``
---------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
    ====== CTF estimation ===== 
                                    --i : STAR file with all input micrographs, or a unix wildcard to all micrograph files, e.g. "mics/*.mrc"
                     --use_noDW (false) : Estimate CTFs from rlnMicrographNameNoDW instead of rlnMicrographName (only after MotionCor2)
                     --o (CtfEstimate/) : Directory, where all output files will be stored
               --only_make_star (false) : Don't estimate any CTFs, only join all logfile results in a STAR file
           --only_do_unfinished (false) : Only estimate CTFs for those micrographs for which there is not yet a logfile with Final values.
                      --do_at_most (-1) : Only process up to this number of (unprocessed) micrographs.
                          --ctfWin (-1) : Size (in pixels) of a centered, squared window to use for CTF-estimation
    ====== Microscopy parameters ===== 
                              --CS (-1) : Spherical Aberration (mm) 
                              --HT (-1) : Voltage (kV)
                         --AmpCnst (-1) : Amplitude constrast
                          --angpix (-1) : Pixel size in the input micrographs (A)
    ====== CTFFIND parameters ===== 
                       --ctffind_exe () : Location of ctffind executable (or through RELION_CTFFIND_EXECUTABLE environment variable)
                            --Box (512) : Size of the boxes to calculate FFTs
                         --ResMin (100) : Minimum resolution (in A) to include in calculations
                           --ResMax (7) : Maximum resolution (in A) to include in calculations
                        --dFMin (10000) : Minimum defocus value (in A) to search
                        --dFMax (50000) : Maximum defocus value (in A) to search
                          --FStep (250) : defocus step size (in A) for search
                             --dAst (0) : amount of astigmatism (in A)
    ====== CTFFIND4 parameters ===== 
                  --is_ctffind4 (false) : The provided CTFFIND executable is CTFFIND4 (version 4.1+)
                 --use_given_ps (false) : Use pre-calculated power spectra?
          --do_movie_thon_rings (false) : Calculate Thon rings from movie frames?
                 --avg_movie_frames (1) : Average over how many movie frames (try to get 4 e-/A2)
         --movie_rootname (_movie.mrcs) : Rootname plus extension for movies
                --do_phaseshift (false) : Estimate the phase shift in the images (e.g. from a phase-plate)
                       --phase_min (0.) : Minimum phase shift (in degrees)
                     --phase_max (180.) : Maximum phase shift (in degrees)
                     --phase_step (10.) : Step in phase shift (in degrees)
                                --j (1) : Number of threads (for CTFIND4 only)
                  --fast_search (false) : Disable "Slower, more exhaustive search" in CTFFIND4.1 (faster but less accurate)
    ====== Gctf parameters ===== 
                     --use_gctf (false) : Use Gctf instead of CTFFIND to estimate the CTF parameters
                          --gctf_exe () : Location of Gctf executable (or through RELION_GCTF_EXECUTABLE environment variable)
        --ignore_ctffind_params (false) : Use Gctf default parameters instead of CTFFIND parameters
                          --EPA (false) : Use equi-phase averaging to calculate Thon rinds in Gctf
                --do_validation (false) : Use validation inside Gctf to analyse quality of the fit?
                --extra_gctf_options () : Additional options for Gctf
                               --gpu () : Device ids for each MPI-thread, e.g 0:1:2:3
                              --version : Print RELION version and exit

``relion_prepare_subtomo``
---------------------------------------------------------------------

.. code-block:: text


     ### RELION 2.0 sub-tomogram averaging - 23:59, FEB 19, 2014 ###
     # The original python script was written by Tanmay Bharat to support sub-tomogram averaging in RELION.
     # This 'relion_prepare_subtomo' executable was written by Shaoda He in Sjors Scheres' lab.
     # Please ensure that you have provided the directory containing IMOD executables 'extracttilts' and 'newstack'
     # Please provide either CTFFIND or Gctf executable.
     # Please report bugs and comments to tbharat@mrc-lmb.cam.ac.uk or scheres@mrc-lmb.cam.ac.uk
     # Please read the documentation on the RELION wiki, several questions are answered there.
     # This version can set defocus values above a certain tilt to the defocus value of the zero degree tilt.
     # This version will write out all the CTF reconstruction commands in the master file.
     # This version supports RELION 2.0 only. For compatibility with older RELION, please use the original python script.
     # This version depends on IMOD executables (extracttilts, newstack) and CTFFIND or Gctf.

     ### RELION 2.0 sub-tomogram averaging - Usage (also refer to RELION wiki) ###
     # Before running the program: 
     # 1. Create a directory 'Tomogram/tomo???' for each reconstructed 3D tomogram.
     # 2. In each of the individual tomogram directories you need:
     #    a. tomo.mrc	   : the actual reconstructed tomogram.
     #    b. tomo.mrcs   : the aligned tilt series in MRC-stack format (Please rename if they are in .st format!)
     #    c. tomo.star   : a STAR file with at least 3 columns: _rlnCoordinateX, Y and Z. (e.g. STAR file generated by 'relion_helix_toolbox --interpo')
     #        OR  (if STAR file exists then .coords file will be ignored)
     #       tomo.coords : a text file with 3 columns: the X, Y and Z coordinates of each subtomogram (e.g. save this from IMOD).
     #    d. tomo.order  : a text file with 2 columns: the tilt angle of each image in tomo.mrcs and the accumulated dose in e-/A2 for that image.
     #    e. tomo.tlt    : (OPTIONAL) a text file with the final tilt angles from IMOD. If this is not provided then the extended header of the .mrcs will be read.
     # 3. Run the program. (Input files will be checked in the initialisation step. Please pay attention if error messages pop up.)
     # 4. Check the contents of 'do_all_reconstruct_ctfs.sh', (split it into multiple files for parallelisation) and run the .sh script (please provide the reconstruction box size).
     # 5. Process the data with RELION 2.0 GUI.

     ###################################################################
     Checking input data ...
     Calculated pixel size (10000 * DPix / Mag) = 2.18302 Angstrom(s)
    === Backtrace  ===
    relion_prepare_subtomo(_ZN11RelionErrorC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES7_l+0x7d) [0x55d9e2b8bb8d]
    relion_prepare_subtomo(_ZN15prepare_subtomo13initialChecksEv+0x56cb) [0x55d9e2b8443b]
    relion_prepare_subtomo(main+0xa7) [0x55d9e2b64257]
    /lib/x86_64-linux-gnu/libc.so.6(+0x29d90) [0x7f353c0ead90]
    /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0x80) [0x7f353c0eae40]
    relion_prepare_subtomo(_start+0x25) [0x55d9e2b64765]
    ==================
    ERROR: 
    Cannot find IMOD 'extractilts' executable /public/EM/imod/imod-4.5.8/IMOD/bin/extracttilts

``relion_mrc2vtk``
-------------------------------------------------------------

.. code-block:: text

    usage: relion_mrc2vtk X.(mrc/mrcs/tiff/spi)
     -> X.vtk

``relion_flex_analyse_mpi``
----------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                              --data () : The _data.star file with the orientations to be analysed
                             --model () :  The corresponding _model.star file with the refined model
                            --bodies () : The corresponding star file with the definition of the bodies
                          --o (analyse) : Output rootname
    ====== 3D model options ===== 
                     --3dmodels (false) : Generate a 3D model for each experimental particles
                   --size_3dmodels (-1) : Output size of the 3D models (default is same as input particles)
    ====== PCA options ===== 
                   --PCA_orient (false) : Perform a principal components analysis on the multibody orientations
                      --do_maps (false) : Generate maps along the principal components
                               --k (-1) : Number of principal components to generate maps for
                             --v (0.75) : Or use as many principal components to explain this fraction of variance (<0,1])
                  --maps_per_movie (10) : Number of maps to use for the movie of each principal component
                           --bins (100) : Number of bins in histograms of the eigenvalues for each principal component
               --select_eigenvalue (-1) : Output a selection particle.star file based on eigenvalues along this eigenvector
      --select_eigenvalue_min (-99999.) : Minimum for eigenvalue to include particles in selection output star file
       --select_eigenvalue_max (99999.) : Maximum for eigenvalue to include particles in selection output star file
        --write_pca_projections (false) : Write out a text file with all PCA projections for all particles
                             --verb (1) : Verbosity
                              --version : Print RELION version and exit

``relion_postprocess_mpi``
---------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input name of half1, e.g. run_half1_class001_unfil.mrc
                                --i2 () : Input name of half2, (default replaces half1 from --i with half2)
                      --o (postprocess) : Output rootname
                          --angpix (-1) : Pixel size in Angstroms
                    --half_maps (false) : Write post-processed half maps for validation
                     --mtf_angpix (-1.) : Pixel size in the original micrographs/movies (in Angstroms)
                       --molweight (-1) : Molecular weight (in kDa) of ordered protein mass
    ====== Masking options ===== 
                    --auto_mask (false) : Perform automated masking, based on a density threshold
             --inimask_threshold (0.02) : Density at which to threshold the map for the initial seed mask
                  --extend_inimask (3.) : Number of pixels to extend the initial seed mask
                 --width_mask_edge (6.) : Width for the raised cosine soft mask edge (in pixels)
                              --mask () : Filename of a user-provided mask (1=protein, 0=solvent, all values in range [0,1])
                   --force_mask (false) : Use the mask even when the masked resolution is worse than the unmasked resolution
    ====== Sharpening options ===== 
                               --mtf () : User-provided STAR-file with the MTF-curve of the detector
                    --auto_bfac (false) : Perform automated B-factor determination (Rosenthal and Henderson, 2003)
                   --autob_lowres (10.) : Lowest resolution (in A) to include in fitting of the B-factor
                   --autob_highres (0.) : Highest resolution (in A) to include in fitting of the B-factor
                      --adhoc_bfac (0.) : User-provided B-factor (in A^2) for map sharpening, e.g. -400
    ====== Filtering options ===== 
           --skip_fsc_weighting (false) : Do not use FSC-weighting (Rosenthal and Henderson, 2003) in the sharpening process
                         --low_pass (0) : Resolution (in Angstroms) at which to low-pass filter the final map (0: disable, negative: resolution at FSC=0.143)
    ====== Local-resolution options ===== 
                       --locres (false) : Perform local resolution estimation
                --locres_sampling (25.) : Sampling rate (in Angstroms) with which to sample the local-resolution map
                  --locres_maskrad (-1) : Radius (in A) of spherical mask for local-resolution map (default = 0.5*sampling)
                 --locres_edgwidth (-1) : Width of soft edge (in A) on masks for local-resolution map (default = sampling)
            --locres_randomize_at (25.) : Randomize phases from this resolution (in A)
                  --locres_minres (50.) : Lowest local resolution allowed (in A)
    ====== Expert options ===== 
                    --ampl_corr (false) : Perform amplitude correlation and DPR, also re-normalize amplitudes for non-uniform angular distributions
               --randomize_at_fsc (0.8) : Randomize phases from the resolution where FSC drops below this value
                  --randomize_at_A (-1) : Randomize phases from this resolution (in A) onwards (if positive)
                --filter_edge_width (2) : Width of the raised cosine on the low-pass filter edge (in resolution shells)
                             --verb (1) : Verbosity
                      --random_seed (0) : Seed for random number generator (negative value for truly random)
                              --version : Print RELION version and exit

``relion_refine``
------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --i () : Input images (in a star-file)
                                 --o () : Output rootname
                            --iter (50) : Maximum number of iterations to perform
                       --tau2_fudge (1) : Regularisation parameter (values higher than 1 give more weight to the data)
                                --K (1) : Number of references to be refined
               --particle_diameter (-1) : Diameter of the circular mask that will be applied to the experimental images (in Angstroms)
                    --zero_mask (false) : Mask surrounding background in particles to zero (by default the solvent area is filled with random noise)
              --flatten_solvent (false) : Perform masking on the references as well?
                  --solvent_mask (None) : User-provided mask for the references (default is to use spherical mask with particle_diameter)
                 --solvent_mask2 (None) : User-provided secondary mask (with its own average density)
                  --lowpass_mask (None) : User-provided mask for low-pass filtering
                          --lowpass (0) : User-provided cutoff for region specified above
                           --tau (None) : STAR file with input tau2-spectrum (to be kept constant)
                --local_symmetry (None) : Local symmetry description file containing list of masks and their operators
          --split_random_halves (false) : Refine two random halves of the data completely separately
           --low_resol_join_halves (-1) : Resolution (in Angstrom) up to which the two random half-reconstructions will not be independent to prevent diverging orientations
    ====== Initialisation ===== 
                           --ref (None) : Image, stack or star-file with the reference(s). (Compulsory for 3D refinement!)
                 --denovo_3dref (false) : Make an initial 3D model from randomly oriented 2D particles
                          --offset (10) : Initial estimated stddev for the origin offsets (in Angstroms)
                 --firstiter_cc (false) : Perform CC-calculation in the first iteration (use this if references are not on the absolute intensity scale)
                        --ini_high (-1) : Resolution (in Angstroms) to which to limit refinement in the first iteration 
    ====== Orientations ===== 
                     --oversampling (1) : Adaptive oversampling order to speed-up calculations (0=no oversampling, 1=2x, 2=4x, etc)
                    --healpix_order (2) : Healpix order for the angular sampling (before oversampling) on the (3D) sphere: hp2=15deg, hp3=7.5deg, etc
                        --psi_step (-1) : Sampling rate (before oversampling) for the in-plane angle (default=10deg for 2D, hp sampling for 3D)
                     --limit_tilt (-91) : Limited tilt angle: positive for keeping side views, negative for keeping top views
                             --sym (c1) : Symmetry group
                         --relax_sym () : Symmetry to be relaxed
                     --offset_range (6) : Search range for origin offsets (in pixels)
                      --offset_step (2) : Sampling rate (before oversampling) for origin offsets (in pixels)
             --helical_offset_step (-1) : Sampling rate (before oversampling) for offsets along helical axis (in Angstroms)
                        --perturb (0.5) : Perturbation factor for the angular sampling (0=no perturb; 0.5=perturb)
                  --auto_refine (false) : Perform 3D auto-refine procedure?
         --auto_local_healpix_order (4) : Minimum healpix order (before oversampling) from which autosampling procedure will use local searches
                       --sigma_ang (-1) : Stddev on all three Euler angles for local angular searches (of +/- 3 stddev)
                       --sigma_rot (-1) : Stddev on the first Euler angle for local angular searches (of +/- 3 stddev)
                      --sigma_tilt (-1) : Stddev on the second Euler angle for local angular searches (of +/- 3 stddev)
                       --sigma_psi (-1) : Stddev on the in-plane angle for local angular searches (of +/- 3 stddev)
                   --skip_align (false) : Skip orientational assignment (only classify)?
                  --skip_rotate (false) : Skip rotational assignment (only translate and classify)?
                  --bimodal_psi (false) : Do bimodal searches of psi angle?
    ====== Helical reconstruction (in development...) ===== 
                        --helix (false) : Perform 3D classification or refinement for helices?
      --ignore_helical_symmetry (false) : Ignore helical symmetry?
                   --helical_nr_asu (1) : Number of new helical asymmetric units (asu) per box (1 means no helical symmetry is present)
           --helical_twist_initial (0.) : Helical twist (in degrees, positive values for right-handedness)
               --helical_twist_min (0.) : Minimum helical twist (in degrees, positive values for right-handedness)
               --helical_twist_max (0.) : Maximum helical twist (in degrees, positive values for right-handedness)
           --helical_twist_inistep (0.) : Initial step of helical twist search (in degrees)
            --helical_rise_initial (0.) : Helical rise (in Angstroms)
                --helical_rise_min (0.) : Minimum helical rise (in Angstroms)
                --helical_rise_max (0.) : Maximum helical rise (in Angstroms)
            --helical_rise_inistep (0.) : Initial step of helical rise search (in Angstroms)
                   --helical_nstart (1) : N-number for the N-start helix (only useful for rotational priors)
           --helical_z_percentage (0.3) : This box length along the center of Z axis contains good information of the helix. Important in imposing and refining symmetry
         --helical_inner_diameter (-1.) : Inner diameter of helical tubes in Angstroms (for masks of helical references and particles)
         --helical_outer_diameter (-1.) : Outer diameter of helical tubes in Angstroms (for masks of helical references and particles)
      --helical_symmetry_search (false) : Perform local refinement of helical symmetry?
         --helical_sigma_distance (-1.) : Sigma of distance along the helical tracks
      --helical_keep_tilt_prior_fixed (false) : Keep helical tilt priors fixed (at 90 degrees) in global angular searches?
            --helical_exclude_resols () : Resolutions (in A) along helical axis to exclude from refinement (comma-separated pairs, e.g. 50-5)
                  --fourier_mask (None) : Originally-sized, FFTW-centred image with Fourier mask for Projector
    ====== Corrections ===== 
                          --ctf (false) : Perform CTF correction?
                      --pad_ctf (false) : Perform CTF padding to treat CTF aliaising better?
        --ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
            --ctf_corrected_ref (false) : Have the input references been CTF-amplitude corrected?
            --ctf_phase_flipped (false) : Have the data been CTF phase-flipped?
             --only_flip_phases (false) : Only perform CTF phase-flipping? (default is full amplitude-correction)
                         --norm (false) : Perform normalisation-error correction?
                        --scale (false) : Perform intensity-scale corrections on image groups?
                      --no_norm (false) : Switch off normalisation-error correction?
                     --no_scale (false) : Switch off intensity-scale corrections on image groups?
    ====== Stochastic Gradient Descent ===== 
                          --sgd (false) : Perform stochastic gradient descent instead of default expectation-maximization
                --stochastic_em (false) : Perform stochastic EM instead of SGD to avoid patent problems for initial model generation by commercial users
                    --sgd_ini_iter (50) : Number of initial SGD iterations
                    --sgd_fin_iter (50) : Number of final SGD iterations
             --sgd_inbetween_iter (200) : Number of SGD iterations between the initial and final ones
                   --sgd_ini_resol (35) : Resolution cutoff during the initial SGD iterations (A)
                   --sgd_fin_resol (15) : Resolution cutoff during the final SGD iterations (A)
                 --sgd_ini_subset (100) : Mini-batch size during the initial SGD iterations
                 --sgd_fin_subset (500) : Mini-batch size during the final SGD iterations
                             --mu (0.9) : Momentum parameter for SGD updates
                   --sgd_stepsize (0.5) : Step size parameter for SGD updates
          --sgd_sigma2fudge_initial (8) : Initial factor by which the noise variance will be multiplied for SGD (not used if halftime is negative)
        --sgd_sigma2fudge_halflife (-1) : Initialise SGD with 8x higher noise-variance, and reduce with this half-life in # of particles (default is keep normal variance)
              --sgd_skip_anneal (false) : By default, multiple references are annealed during the in_between iterations. Use this option to switch annealing off
                   --sgd_write_iter (1) : Write out model every so many iterations in SGD (default is writing out all iters)
    ====== Computation ===== 
                             --pool (1) : Number of images to pool for each thread task
                                --j (1) : Number of threads to run in parallel (only useful on multi-core machines)
      --dont_combine_weights_via_disc (false) : Send the large arrays of summed weights through the MPI network, instead of writing large files to disc
              --onthefly_shifts (false) : Calculate shifted images on-the-fly, do not store precalculated ones in memory
          --no_parallel_disc_io (false) : Do NOT let parallel (MPI) processes access the disc simultaneously (use this option with NFS)
               --preread_images (false) : Use this to let the leader process read all particles into memory. Be careful you have enough RAM for large data sets!
                       --scratch_dir () : If provided, particle stacks will be copied to this local scratch disk prior to refinement.
               --keep_free_scratch (10) : Space available for copying particle stacks (in Gb)
                --reuse_scratch (false) : Re-use data on scratchdir, instead of wiping it and re-copying all data.
                 --keep_scratch (false) : Don't remove scratch after convergence. Following jobs that use EXACTLY the same particles should use --reuse_scratch.
                 --fast_subsets (false) : Use faster optimisation by using subsets of the data in the first 15 iterations
                          --gpu (false) : Use available gpu resources for some calculations
                  --free_gpu_memory (0) : GPU device memory (in Mb) to leave free after allocation.
    ====== Expert options ===== 
                              --pad (2) : Oversampling factor for the Fourier transforms of the references
                     --ref_angpix (-1.) : Pixel size (in A) for the input reference (default is to read from header)
                           --NN (false) : Perform nearest-neighbour instead of linear Fourier-space interpolation?
                        --r_min_nn (10) : Minimum number of Fourier shells to perform linear Fourier-space interpolation
                             --verb (1) : Verbosity (1=normal, 0=silent)
                     --random_seed (-1) : Number for the random seed generator
                     --coarse_size (-1) : Maximum image size for the first pass of the adaptive sampling approach
            --adaptive_fraction (0.999) : Fraction of the weights to be considered in the first pass of adaptive oversampling 
                         --maskedge (5) : Width of the soft edge of the spherical mask (in pixels)
              --fix_sigma_noise (false) : Fix the experimental noise spectra?
             --fix_sigma_offset (false) : Fix the stddev in the origin offsets?
                       --incr_size (10) : Number of Fourier shells beyond the current resolution to be included in refinement
        --print_metadata_labels (false) : Print a table with definitions of all metadata labels, and exit
           --print_symmetry_ops (false) : Print all symmetry transformation matrices, and exit
              --strict_highres_exp (-1) : High resolution limit (in Angstrom) to restrict probability calculations in the expectation step
               --strict_lowres_exp (-1) : Low resolution limit (in Angstrom) to restrict probability calculations in the expectation step
              --dont_check_norm (false) : Skip the check whether the images are normalised correctly
                    --always_cc (false) : Perform CC-calculation in all iterations (useful for faster denovo model generation?)
          --solvent_correct_fsc (false) : Correct FSC curve for the effects of the solvent mask?
                --skip_maximize (false) : Skip maximization step (only write out data.star file)?
              --failsafe_threshold (40) : Maximum number of particles permitted to be handled by fail-safe mode, due to zero sum of weights, before exiting with an error (GPU only).
         --external_reconstruct (false) : Perform the reconstruction step outside relion_refine, e.g. for learned priors?)
                  --auto_iter_max (999) : In auto-refinement, stop at this iteration.
           --auto_ignore_angles (false) : In auto-refinement, update angular sampling regardless of changes in orientations for convergence. This makes convergence faster.
            --auto_resol_angles (false) : In auto-refinement, update angular sampling based on resolution-based required sampling. This makes convergence faster.
       --allow_coarser_sampling (false) : In 2D/3D classification, allow coarser angular and translational samplings if accuracies are bad (typically in earlier iterations.
               --trust_ref_size (false) : Trust the pixel and box size of the input reference; by default the program will die if these are different from the first optics group of the data
                          --maxsig (-1) : Maximum number of poses & translations to consider
                --skip_gridding (false) : Skip gridding in the M step
                              --version : Print RELION version and exit

``relion_convert_to_tiff_mpi``
-------------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General Options ===== 
                                    --i : Input movie to be compressed (an MRC/MRCS file or a list of movies as .star or .lst)
                               --o (./) : Directory for output TIFF files
           --only_do_unfinished (false) : Only process non-converted movies.
                                --j (1) : Number of threads (useful only for --estimate_gain)
                              --gain () : Estimated gain map and its reliablity map (read)
                          --thresh (50) : Number of success needed to consider a pixel reliable
                --estimate_gain (false) : Estimate gain
    ====== EER rendering options ===== 
                    --eer_grouping (40) : EER grouping
                   --eer_upsampling (1) : EER upsampling (1 = 4K or 2 = 8K)
                        --short (false) : use unsigned short instead of signed byte for EER rendering
    ====== TIFF writing options ===== 
                   --compression (auto) : compression type (none, auto, deflate (= zip), lzw)
                    --deflate_level (6) : deflate level. 1 (fast) to 9 (slowest but best compression)
                 --ignore_error (false) : Don't die on un-expected defect pixels (can be dangerous)
                 --line_by_line (false) : Use one strip per row
                              --version : Print RELION version and exit

``relion_reposition``
----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file containing the particles
                                    --f : Input STAR file with the FSC of the reference (usually from PostProcess)
                       --max_shift (10) : Maximal allowed shift
                           --cc_pad (1) : Cross-correlation padding
                                --m1 () : Reference map, half 1
                                --m2 () : Reference map, half 2
                      --angpix_ref (-1) : Pixel size of the reference map
                              --mask () : Reference mask
                              --pad (2) : Padding factor
                                --j (1) : Number of (OMP) threads
                    --o (repositioned/) : Output path
                              --version : Print RELION version and exit

``relion_reconstruct``
-----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --i () : Input STAR file with the projection images and their orientations
                       --o (relion.mrc) : Name for output reconstruction
                             --sym (c1) : Symmetry group
                          --maxres (-1) : Maximum resolution (in Angstrom) to consider in Fourier space (default Nyquist)
                              --pad (2) : Padding factor
                               --img () : Optional: image path prefix
                          --subset (-1) : Subset of images to consider (1: only reconstruct half1; 2: only half2; other: reconstruct all)
                           --class (-1) : Consider only this class (-1: use all classes)
                          --angpix (-1) : Pixel size in the reconstruction (take from first optics group by default)
    ====== CTF options ===== 
                          --ctf (false) : Apply CTF correction
        --ctf_intact_first_peak (false) : Leave CTFs intact until first peak
            --ctf_phase_flipped (false) : Images have been phase flipped
             --only_flip_phases (false) : Do not correct CTF-amplitudes, only flip phases
    ====== Ewald-sphere correction options ===== 
                        --ewald (false) : Correct for Ewald-sphere curvature (developmental)
                  --mask_diameter (-1.) : Diameter (in A) of mask for Ewald-sphere curvature correction
                  --width_mask_edge (3) : Width (in pixels) of the soft edge on the mask
            --reverse_curvature (false) : Try curvature the other way around
                          --newbox (-1) : Box size of reconstruction after Ewald sphere correction
                          --sectors (2) : Number of sectors for Ewald sphere correction
                    --skip_mask (false) : Do not apply real space mask during Ewald sphere correction
               --skip_weighting (false) : Do not apply weighting during Ewald sphere correction
    ====== Helical options ===== 
                   --nr_helical_asu (1) : Number of helical asymmetrical units
                    --helical_rise (0.) : Helical rise (in Angstroms)
                   --helical_twist (0.) : Helical twist (in degrees, + for right-handedness)
    ====== Expert options ===== 
                          --subtract () : Subtract projections of this map from the images used for reconstruction
                           --NN (false) : Use nearest-neighbour instead of linear interpolation before gridding correction
                         --blob_r (1.9) : Radius of blob for gridding interpolation
                           --blob_m (0) : Order of blob for gridding interpolation
                          --blob_a (15) : Alpha-value of blob for gridding interpolation
                            --iter (10) : Number of gridding-correction iterations
                           --refdim (3) : Dimension of the reconstruction (2D or 3D)
                   --angular_error (0.) : Apply random deviations with this standard deviation (in degrees) to each of the 3 Euler angles
                     --shift_error (0.) : Apply random deviations with this standard deviation (in Angstrom) to each of the 2 translations
                --fom_weighting (false) : Weight particles according to their figure-of-merit (_rlnParticleFigureOfMerit)
                               --fsc () : FSC-curve for regularized reconstruction
                       --3d_rot (false) : Perform 3D rotations instead of backprojections from 2D images
                 --reconstruct_ctf (-1) : Perform a 3D reconstruction from 2D CTF-images, with the given size in pixels
                         --ctf2 (false) : Reconstruct CTF^2 and then take the sqrt of that
                --skip_gridding (false) : Skip gridding part of the reconstruction
                             --debug () : Rootname for debug reconstruction files
                   --debug_ori_size (1) : Rootname for debug reconstruction files
                       --debug_size (1) : Rootname for debug reconstruction files
                 --reconstruct_noise () : Reconstruct noise using sigma2 values in this model STAR file
                 --read_weights (false) : Developmental: read freq. weight files
           --write_debug_output (false) : Write out arrays with data and weight terms prior to reconstruct
         --external_reconstruct (false) : Write out BP denominator and numerator for external_reconstruct program
                             --verb (1) : Verbosity
                              --version : Print RELION version and exit

``relion_find_tiltpairs``
--------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General Options ===== 
                                    --u : STAR file with the untilted xy-coordinates
                                    --t : STAR file with the untilted xy-coordinates
                                 --size : Largest dimension of the micrograph (in pixels), e.g. 4096
                                  --acc : Allowed accuracy (in pixels), e.g. half the particle diameter
                            --dim (200) : Dimension of boxed particles (for EMAN .box files in pixels)
                        --tilt (99999.) : Fix tilt angle (in degrees)
                         --rot (99999.) : Fix direction of the tilt axis (in degrees), 0 = along y, 90 = along x
                     --dont_opt (false) : Skip optimization of the transformation matrix
    ====== Specified tilt axis and translational search ranges ===== 
                           --tilt0 (0.) : Minimum tilt angle (in degrees)
                       --tiltF (99999.) : Maximum tilt angle (in degrees)
                        --tiltStep (1.) : Tilt angle step size (in degrees)
                            --rot0 (0.) : Minimum rot angle (in degrees)
                        --rotF (99999.) : Maximum rot angle (in degrees)
                         --rotStep (1.) : Rot angle step size (in degrees)
                          --x0 (-99999) : Minimum X offset (pixels)
                           --xF (99999) : Maximum X offset (pixels)
                           --xStep (-1) : X offset step size (pixels)
                          --y0 (-99999) : Minimum Y offset (pixels)
                           --yF (99999) : Maximum Y offset (pixels)
                           --yStep (-1) : Y offset step size (pixels)
                              --version : Print RELION version and exit

``relion_convert_star``
------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Options ===== 
                             --i (None) : Input STAR file to be converted
                             --o (None) : Output STAR file to be written
                              --Cs (-1) : Spherical aberration (mm)
                              --Q0 (-1) : Amplitude contrast
                              --version : Print RELION version and exit
    ERROR: 
    Please specify input and output file names
    === Backtrace  ===
    relion_convert_star(_ZN11RelionErrorC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES7_l+0x7d) [0x55ef81a8f54d]
    relion_convert_star(_ZN14star_converter4readEiPPc+0xb62) [0x55ef81a876b2]
    relion_convert_star(main+0x86) [0x55ef81a86136]
    /lib/x86_64-linux-gnu/libc.so.6(+0x29d90) [0x7f7d19878d90]
    /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0x80) [0x7f7d19878e40]
    relion_convert_star(_start+0x25) [0x55ef81a86955]
    ==================
    ERROR: 
    Please specify input and output file names

``relion_run_motioncorr``
--------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : STAR file with all input micrographs, or a Linux wildcard with all micrographs to operate on
                       --o (MotionCorr) : Name for the output directory
                                --j (1) : Number of threads per movie (= process)
                  --max_io_threads (-1) : Limit the number of IO threads.
           --only_do_unfinished (false) : Only run motion correction for those micrographs for which there is not yet an output micrograph.
                      --do_at_most (-1) : Only process at most this number of (unprocessed) micrographs.
                 --grouping_for_ps (-1) : Group this number of frames and write summed power spectrum. -1 == do not write
                        --ps_size (512) : Output size of power spectrum
                  --first_frame_sum (1) : First movie frame used in output sum (start at 1)
                  --last_frame_sum (-1) : Last movie frame used in output sum (0 or negative: use all)
                    --eer_grouping (40) : EER grouping
                   --eer_upsampling (1) : EER upsampling (1 = 4K or 2 = 8K)
    ====== MOTIONCOR2 options ===== 
               --use_motioncor2 (false) : Use Shawn Zheng's MOTIONCOR2.
                    --motioncor2_exe () : Location of MOTIONCOR2 executable (or through RELION_MOTIONCOR2_EXECUTABLE environment variable)
                       --bin_factor (1) : Binning factor (can be non-integer)
                        --bfactor (150) : B-factor (in pix^2) that will be used inside MOTIONCOR2
                           --gainref () : Location of MRC file with the gain reference to be applied
                         --gain_rot (0) : Rotate the gain reference this number times 90 degrees clock-wise (in relion_display). This is same as MotionCor2's RotGain. 0, 1, 2 or 3
                        --gain_flip (0) : Flip the gain reference. This is same as MotionCor2's FlipGain. 0, 1 (flip Y == upside down) or 2 (flip X == left to right)
                          --patch_x (1) : Patching in X-direction for MOTIONCOR2
                          --patch_y (1) : Patching in Y-direction for MOTIONCOR2
                     --group_frames (1) : Average together this many frames before calculating the beam-induced shifts
                       --defect_file () : Location of a MOTIONCOR2-style detector defect file (x y w h) or a defect map (1 means bad)
                           --archive () : Location of the directory for archiving movies in 4-byte MRC format
             --other_motioncor2_args () : Additional arguments to MOTIONCOR2
                               --gpu () : Device ids for each MPI-thread, e.g 0:1:2:3
    ====== Dose-weighting options ===== 
               --dose_weighting (false) : Use dose-weighting scheme
                          --angpix (-1) : Pixel size in Angstroms
                         --voltage (-1) : Voltage (in kV) for dose-weighting
                   --dose_per_frame (1) : Electron dose (in electrons/A2/frame) for dose-weighting
                      --preexposure (0) : Pre-exposure (in electrons/A2) for dose-weighting
    ====== Own motion correction options ===== 
                      --use_own (false) : Use our own implementation of motion correction
                  --skip_defect (false) : Skip hot pixel detection
                    --save_noDW (false) : Save aligned but non dose weighted micrograph
                         --max_iter (5) : Maximum number of iterations for alignment. Only valid with --use_own
           --interpolate_shifts (false) : (EXPERIMENTAL) Interpolate shifts
                   --ccf_downsample (0) : (EXPERT) Downsampling rate of CC map. default = 0 = automatic based on B factor
                --early_binning (false) : Do binning before alignment to reduce memory usage. This might dampen signal near Nyquist. (ON by default)
             --no_early_binning (false) : Disable --early_binning
         --dose_motionstats_cutoff (4.) : Electron dose (in electrons/A2) at which to distinguish early/late global accumulated motion in output statistics
                              --version : Print RELION version and exit

``relion_star_loopheader``
---------------------------------------------------------------------

.. code-block:: text

     === Usage: === 
     /relion_star_loopheader <label1> <label2> ...
 
     === Purpose: === 
     This (bash) script generates the header of STAR-file with the given labels
 
     === Example: ===
     /relion_star_loopheader rlnImageName rlnDefocusU rlnDefocusV rlnDefocusAngle rlnVoltage rlnSphericalAberration rlnAmplitudeContrast
     yields: 
     data_
     loop_
     _rlnImageName
     _rlnDefocusU
     _rlnDefocusV
     _rlnDefocusAngle
     _rlnVoltage
     _rlnSphericalAberration
     _rlnAmplitudeContrast

``relion_star_printtable``
---------------------------------------------------------------------

.. code-block:: text

     === Usage: === 
     /relion_star_printtable <starfile> <tablename> [<label1> <label2> ...]
 
     === Purpose: === 
     This (bash) script prints the contents of a datablock (with name tablename) from a starfile
     If any labels are given, then only those will be printed 
 
     === Example: === 
     /relion_star_printtable run3_it024_model.star data_model_class_1 rlnResolution rlnSsnrMap
     (NOTE: not _rlnResolution)
 
     === Limitations: === 
     This program makes a temporary directory under $TMPDIR. This folder must be writable and have sufficient space.
 
     This program does not perform any error checks.
     When specified table and/or column(s) are absent in the input, the program might give incorrect results.
     In older versions, table names and column names could match only partially. For example, rlnFourierShellCorrelationCorrected matched rlnFourierShellCorrelation. This was dangerous and the match is exact now.
 
     To address these issues, this program will be completely re-written in the next major update (RELION 3.2).
     In the new version, the errors are handled more strictly. Please update your scripts to prepare for transition.


``relion_mask_create``
-----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Mask creation options ===== 
                                 --i () : Input map to use for thresholding to generate initial binary mask
                         --o (mask.mrc) : Output mask
                               --and () : Pixels in the initial mask will be one if the input AND this map are above the --ini_threshold value
                                --or () : Pixels in the initial mask will be one if the input OR this map are above the --ini_threshold value
                           --and_not () : Pixels in the initial mask will be one if the input is above the --ini_threshold AND this map is below it
                            --or_not () : Pixels in the initial mask will be one if the input is above the --ini_threshold OR this map is below it
                 --ini_threshold (0.01) : Initial threshold for binarization
                   --extend_inimask (0) : Extend initial binary mask this number of pixels
                  --width_soft_edge (0) : Width (in pixels) of the additional soft edge on the binary mask
                       --invert (false) : Invert the final mask
                        --helix (false) : Generate a mask for 3D helix
                         --lowpass (-1) : Lowpass filter (in Angstroms) for the input map, prior to binarization (default is none)
                          --angpix (-1) : Pixel size (in Angstroms) for the lowpass filter
                   --z_percentage (0.3) : This box length along the center of Z axis contains good information of the helix
                                --j (1) : Number of threads
    ====== De novo mask creation ===== 
                       --denovo (false) : Create a mask de novo
                        --box_size (-1) : The box size of the mask in pixels
                     --inner_radius (0) : Inner radius of the masked region in pixels
                 --outer_radius (99999) : Outer radius of the mask region in pixels
                         --center_x (0) : X coordinate of the center of the mask in pixels
                         --center_y (0) : Y coordinate of the center of the mask in pixels
                         --center_z (0) : Z coordinate of the center of the mask in pixels
                              --version : Print RELION version and exit

``relion_helix_inimodel2d``
----------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --o () : Output rootname
                                 --i () :  STAR file with the input images and orientation parameters
    ====== Parameters ===== 
                --crossover_distance () : Distance in Angstroms between 2 cross-overs
                            --iter (10) : Maximum number of iterations to perform
                                --K (1) : Number of classes
                          --angpix (-1) : Pixel size in Angstroms (default take from STAR file)
                          --maxres (-1) : Limit calculations to approximately this resolution in Angstroms
                     --search_shift (0) : How many Angstroms to search translations perpendicular to helical axis?
                     --search_angle (0) : How many degrees to search in-plane rotations?
                       --step_angle (1) : The step size (in degrees) of the rotational searches
                            --iniref () : An initial model to starting optimisation path
                              --sym (1) : Order of symmetry in the 2D xy-slice?
                            --smear (0) : Smear out each image along X to ensure continuity
                     --random_seed (-1) : Random seed (default is with clock)
                      --search_size (5) : Search this many pixels up/down of the target downscaled size to fit best crossover distance
                   --mask_diameter (-1) : The diameter (A) of a mask to be aplpied to the 2D reconstruction
                                --j (1) : Number of (openMP) threads
                 --only_make_3d (false) : Take the iniref image, and create a 3D model from that without any alignment of the input images
                              --version : Print RELION version and exit

``relion_localsym_mpi``
------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Show usage ===== 
                --function_help (false) : Show usage for the selected function (JUN 30, 2017)
    ====== Options ===== 
                        --apply (false) : Apply local symmetry to a 3D cryo-EM density map
                    --duplicate (false) : Duplicate subunits/masks according to local symmetry operators
                       --search (false) : Local searches of local symmetry operators
                    --transform (false) : Transform a map according to three Euler angles and XYZ translations
                      --txt2rln (false) : Convert operators from DM to RELION STAR format
                        --debug (false) : (DEBUG ONLY)
    ====== Parameters (alphabetically ordered) ===== 
                          --angpix (1.) : Pixel size (in Angstroms) of input image
                       --ang_range (0.) : Angular search range of operators (in degrees), overwrite rot-tilt-psi ranges if set to positive
                   --ang_rot_range (0.) : Angular (rot) search range of operators (in degrees)
                  --ang_tilt_range (0.) : Angular (tilt) search range of operators (in degrees)
                   --ang_psi_range (0.) : Angular (psi) search range of operators (in degrees)
                        --ang_step (1.) : Angular search step of operators (in degrees)
                            --bin (-1.) : Binning factor (<= 1 means no binning)
                 --ini_threshold (0.01) : Initial threshold for binarization
                             --i_map () : Input 3D unsymmetrised map
           --i_mask_info (maskinfo.txt) : Input file with mask filenames and rotational / translational operators (for local searches)
                --i_op_mask_info (None) : Input file with mask filenames for all operators (for global searches)
                                --n (2) : Create this number of masks according to the input density map
                    --offset_range (0.) : Translational search range of operators (in Angstroms), overwrite x-y-z ranges if set to positive
                  --offset_x_range (0.) : Translational (x) search range of operators (in Angstroms)
                  --offset_y_range (0.) : Translational (y) search range of operators (in Angstroms)
                  --offset_z_range (0.) : Translational (z) search range of operators (in Angstroms)
                     --offset_step (1.) : Translational search step of operators (in Angstroms)
                             --o_map () : Output 3D symmetrised map
      --o_mask_info (maskinfo_refined.txt) : Output file with mask filenames and rotational / translational operators
                             --psi (0.) : Third Euler angle (psi, in degrees)
                             --rot (0.) : First Euler angle (rot, in degrees)
              --sphere_percentage (-1.) : Diameter of spherical mask divided by the box size (< 0.99)
                            --tilt (0.) : Second Euler angle (tilt, in degrees)
                            --xoff (0.) : X-offset (in Angstroms)
                            --yoff (0.) : Y-offset (in Angstroms)
                            --zoff (0.) : Z-offset (in Angstroms)
                         --verb (false) : Verbose output?
    ====== Parameters (expert options - alphabetically ordered) ===== 
                    --i_mask (mask.mrc) : (DEBUG) Input mask
      --i_mask_info_parsed_ext (parsed) : Extension of parsed input file with mask filenames and rotational / translational operators
                  --use_healpix (false) : Use Healpix for angular samplings?
                           --width (5.) : Width of cosine soft edge (in pixels)
                              --version : Print RELION version and exit

``relion_particle_subtract_mpi``
---------------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --i () : Name of optimiser.star file from refinement/classification to use for subtraction
                        --o (Subtract/) : Output directory name
                              --mask () : Name of the 3D mask with all density that should be kept, i.e. not subtracted
                              --data () : Name of particle STAR file, in case not all particles from optimiser are to be used
                 --ignore_class (false) : Ignore the rlnClassNumber column in the particle STAR file.
                            --revert () : Name of particle STAR file to revert. When this is provided, all other options are ignored.
                         --ssnr (false) : Don't subtract, only calculate average spectral SNR in the images
    ====== Centering options ===== 
             --recenter_on_mask (false) : Use this flag to center the subtracted particles on projections of the centre-of-mass of the input mask
                      --center_x (9999) : X-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
                      --center_y (9999) : Y-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
                      --center_z (9999) : Z-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
                         --new_box (-1) : Output size of the subtracted particles
                              --version : Print RELION version and exit

``relion_image_handler``
-------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file, image (.mrc) or movie/stack (.mrcs)
                                 --o () : Output name (for STAR-input: insert this string before each image's extension)
    ====== image-by-constant operations ===== 
                --multiply_constant (1) : Multiply the image(s) pixel values by this constant
                  --divide_constant (1) : Divide the image(s) pixel values by this constant
                    --add_constant (0.) : Add this constant to the image(s) pixel values
               --subtract_constant (0.) : Subtract this constant from the image(s) pixel values
               --threshold_above (999.) : Set all values higher than this value to this value
              --threshold_below (-999.) : Set all values lower than this value to this value
    ====== image-by-image operations ===== 
                          --multiply () : Multiply input image(s) by the pixel values in this image
                            --divide () : Divide input image(s) by the pixel values in this image
                               --add () : Add the pixel values in this image to the input image(s) 
                          --subtract () : Subtract the pixel values in this image to the input image(s) 
                               --fsc () : Calculate FSC curve of the input image with this image
                        --power (false) : Calculate power spectrum (|F|^2) of the input image
                      --adjust_power () : Adjust the power spectrum of the input image to be the same as this image 
                    --fourier_filter () : Multiply the Fourier transform of the input image(s) with this one image 
    ====== additional subtract options ===== 
      --optimise_scale_subtract (false) : Optimise scale between maps before subtraction?
       --optimise_bfactor_subtract (0.) : Search range for relative B-factor for subtraction (in A^2)
            --mask_optimise_subtract () : Use only voxels in this mask to optimise scale for subtraction
    ====== per-image operations ===== 
                        --stats (false) : Calculate per-image statistics?
                          --com (false) : Calculate center of mass?
                         --bfactor (0.) : Apply a B-factor (in A^2)
                        --lowpass (-1.) : Low-pass filter frequency (in A)
                       --highpass (-1.) : High-pass filter frequency (in A)
                       --directional () : Directionality of low-pass filter frequency ('X', 'Y' or 'Z', default non-directional)
                            --LoG (-1.) : Diameter for optimal response of Laplacian of Gaussian filter (in A)
                          --angpix (-1) : Pixel size (in A)
                 --rescale_angpix (-1.) : Scale input image(s) to this new pixel size (in A)
            --force_header_angpix (-1.) : Change the pixel size in the header (in A). Without --rescale_angpix, the image is not scaled.
                         --new_box (-1) : Resize the image(s) to this new box size (in pixel) 
                --filter_edge_width (2) : Width of the raised cosine on the low/high-pass filter edge (in resolution shells)
                        --flipX (false) : Flip (mirror) a 2D image or 3D map in the X-direction?
                        --flipY (false) : Flip (mirror) a 2D image or 3D map in the Y-direction?
                        --flipZ (false) : Flip (mirror) a 3D map in the Z-direction?
                  --invert_hand (false) : Invert hand by flipping X? Similar to flipX, but preserves the symmetry origin. Edge pixels are wrapped around.
                    --shift_com (false) : Shift image(s) to their center-of-mass (only on positive pixel values)
                         --shift_x (0.) : Shift images this many pixels in the X-direction
                         --shift_y (0.) : Shift images this many pixels in the Y-direction
                         --shift_z (0.) : Shift images this many pixels in the Z-direction
                     --avg_ampl (false) : Calculate average amplitude spectrum for all images?
                    --avg_ampl2 (false) : Calculate average amplitude spectrum for all images?
                --avg_ampl2_ali (false) : Calculate average amplitude spectrum for all aligned images?
                      --average (false) : Calculate average of all images (without alignment)
                  --correct_avg_ampl () : Correct all images with this average amplitude spectrum
                   --minr_ampl_corr (0) : Minimum radius (in Fourier pixels) to apply average amplitudes
                   --remove_nan (false) : Replace non-numerical values (NaN, inf, etc) in the image(s)
                      --replace_nan (0) : Replace non-numerical values (NaN, inf, etc) with this value
                 --phase_randomise (-1) : Randomise phases beyond this resolution (in Angstroms)
    ====== 3D operations ===== 
                               --sym () : Symmetrise 3D map with this point group (e.g. D6)
    ====== 2D-micrograph (or movie) operations ===== 
                       --flipXY (false) : Flip the image(s) in the XY direction?
                      --flipmXY (false) : Flip the image(s) in the -XY direction?
                     --add_edge (false) : Add a barcode-like edge to the micrograph/movie frames?
                          --edge_x0 (0) : Pixel column to be used for the left edge
                          --edge_y0 (0) : Pixel row to be used for the top edge
                       --edge_xF (4095) : Pixel column to be used for the right edge
                       --edge_yF (4095) : Pixel row to be used for the bottom edge
    ====== Movie-frame averaging options ===== 
                         --avg_bin (-1) : Width (in frames) for binning average, i.e. of every so-many frames
                       --avg_first (-1) : First frame to include in averaging
                        --avg_last (-1) : Last frame to include in averaging
      --average_all_movie_frames (false) : Average all movie frames of all movies in the input STAR file.
    ====== PNG options ===== 
                            --black (0) : Pixel value for black (default is auto-contrast)
                            --white (0) : Pixel value for white (default is auto-contrast)
                   --sigma_contrast (0) : Set white and black pixel values this many times the image stddev from the mean
                  --colour_fire (false) : Show images in black-grey-white-red colour scheme (highlight high signal)?
                   --colour_ice (false) : Show images in blue-black-grey-white colour scheme (highlight low signal)?
            --colour_fire-n-ice (false) : Show images in blue-grey-red colour scheme (highlight high&low signal)?
               --colour_rainbow (false) : Show images in cyan-blue-black-red-yellow colour scheme?
            --colour_difference (false) : Show images in cyan-blue-black-red-yellow colour scheme (for difference images)?
                              --version : Print RELION version and exit

``relion_motion_refine_mpi``
-----------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file
                                    --o : Output directory, e.g. MotionFit/job041/
                                    --f : Input STAR file with the FSC of the reference (usually from PostProcess)
                                --m1 () : Reference map, half 1
                                --m2 () : Reference map, half 2
                      --angpix_ref (-1) : Pixel size of the reference map
                              --mask () : Reference mask
                              --pad (2) : Padding factor
                      --first_frame (1) : First move frame to process
                      --last_frame (-1) : Last movie frame to process (default is all)
           --only_do_unfinished (false) : Skip those steps for which output files already exist.
                             --verb (1) : Verbosity
    ====== Motion fit options (basic) ===== 
                           --fdose (-1) : Electron dose per frame (in e^-/A^2)
                          --s_vel (0.5) : Velocity sigma [Angst/dose]
                       --s_div (5000.0) : Divergence sigma [Angst]
                          --s_acc (2.0) : Acceleration sigma [Angst/dose]
                       --params_file () : File containing s_vel, s_div and s_acc (overrides command line parameters)
                      --only_group (-1) : Only align micrographs containing particles from this optics group (negative means off)
                         --diag (false) : Write out diagnostic data
    ====== Motion fit options (advanced) ===== 
                         --cc_pad (1.0) : Cross-correlation Fourier-padding
                        --dmg_a ( 3.40) : Damage model, parameter a
                        --dmg_b (-1.06) :                         b
                        --dmg_c (-0.54) :                         c
                    --max_iters (10000) : Maximum number of iterations
                           --eps (1e-5) : Terminate optimization after gradient length falls below this value
                    --no_whiten (false) : Do not whiten the noise spectrum
                   --unreg_glob (false) : Do not regularize global component of motion
                     --glob_off (false) : Compute initial per-particle offsets
                    --glob_off_max (10) : Maximum per-particle offset range [Pixels]
              --absolute_params (false) : Do not scale input motion parameters by dose
                    --debug_opt (false) : Write optimization debugging info
                           --gi (false) : Initialize with global trajectories instead of loading them from metadata file
                   --sq_exp_ker (false) : Use a square-exponential kernel instead of an exponential one
                          --max_ed (-1) : Maximum number of eigendeformations
                      --out_cut (false) : Do not consider frequencies beyond the 0.143-FSC threshold for alignment
    ====== Parameter estimation ===== 
                      --params2 (false) : Estimate 2 parameters instead of motion
                      --params3 (false) : Estimate 3 parameters instead of motion
                     --align_frac (0.5) : Fraction of pixels to be used for alignment
                      --eval_frac (0.5) : Fraction of pixels to be used for evaluation
                         --min_p (1000) : Minimum number of particles on which to estimate the parameters
                       --par_group (-1) : Estimate parameters for this optics group only (negative means all)
                        --s_vel_0 (0.6) : Initial s_vel
                      --s_div_0 (10000) : Initial s_div
                          --s_acc_0 (3) : Initial s_acc
                       --in_step (3000) : Initial step size in s_div
                            --conv (30) : Abort when simplex diameter falls below this
                      --par_iters (100) : Max. number of iterations
                       --mot_range (50) : Limit allowed motion range [Px]
                            --seed (23) : Random seed for micrograph selection
    ====== Combine frames options ===== 
               --combine_frames (false) : Combine movie frames into polished particles.
                           --scale (-1) : Re-scale the particles to this size (by default read from particles star file)
                          --window (-1) : Re-window the particles to this size (in movie-pixels; by default read from particles star file)
                            --crop (-1) : Crop the scaled particles to this size after CTF pre-multiplication
                 --ctf_multiply (false) : Premultiply by CTF.
                    --bfac_minfreq (20) : Min. frequency used in B-factor fit [Angst]
                    --bfac_maxfreq (-1) : Max. frequency used in B-factor fit [Angst]
                          --bfactors () : A .star file with external B/k-factors
                 --diag_bfactor (false) : Write out B/k-factor diagnostic data
                            --suffix () : Add this suffix to shiny MRCS and STAR files
                     --recenter (false) : Re-center particle according to rlnOriginX/Y in --reextract_data_star STAR file
                      --recenter_x (0.) : X-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --recenter_y (0.) : Y-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --recenter_z (0.) : Z-coordinate (in pixel inside the reference) to recenter re-extracted data on
    ====== Computational options ===== 
                                --j (1) : Number of (OMP) threads
                           --min_MG (0) : First micrograph index
                          --max_MG (-1) : Last micrograph index (default is to process all)
                          --sbs (false) : Load movies slice-by-slice to save memory (slower)
    ====== Expert options ===== 
                             --corr_mic : List of uncorrected micrographs (e.g. corrected_micrographs.star)
                --find_shortest (false) : Load only as many frames as are present in all movies.
                        --debug (false) : Write debugging data
                             --mps (-1) : Pixel size of input movies (Angst/pix)
                             --cps (-1) : Pixel size of particle coordinates in star-file (Angst/pix)
                             --hot (-1) : Clip hot pixels to this max. value (-1 = off, TIFF only)
                    --debug_mov (false) : Write debugging data for movie loading
                     --mov_toReplace () : Replace this string in micrograph names...
                     --mov_replaceBy () : ..by this one
                  --eer_upsampling (-1) : EER upsampling (1 = 4K or 2 = 8K)
                    --eer_grouping (-1) : EER grouping
                              --version : Print RELION version and exit

``relion_project``
-------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Options ===== 
                                    --i : Input map to be projected
                             --o (proj) : Rootname for output projections
                          --ctf (false) : Apply CTF to reference projections
               --ctf_phase_flip (false) : Flip phases of the CTF in the output projections
        --ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
                          --angpix (-1) : Pixel size (in Angstroms)
                              --mask () : Mask that will be applied to the input map prior to making projections
                           --ang (None) : Particle STAR file with orientations and CTF for multiple projections (if None, assume single projection)
                      --nr_uniform (-1) :  OR get this many random samples from a uniform angular distribution
                     --sigma_offset (0) : Apply Gaussian errors with this stddev to the XY-offsets
                              --rot (0) : First Euler angle (for a single projection)
                             --tilt (0) : Second Euler angle (for a single projection)
                              --psi (0) : Third Euler angle (for a single projection)
                             --xoff (0) : Origin X-offsets (in pixels) (for a single projection)
                             --yoff (0) : Origin Y-offsets (in pixels) (for a single projection)
                             --zoff (0) : Origin Z-offsets (in pixels) (for a single 3D rotation)
                    --add_noise (false) : Add noise to the output projections (only with --ang)
                      --white_noise (0) : Standard deviation of added white Gaussian noise
                       --model_noise () : Model STAR file with power spectra for coloured Gaussian noise
                 --subtract_exp (false) : Subtract projections from experimental images (in --ang)
         --ignore_particle_name (false) : Ignore the rlnParticleName column (in --ang)
                       --3d_rot (false) : Perform 3D rotations instead of projection into 2D images
                     --simulate (false) : Simulate data with known ground-truth by subtracting signal and adding projection in random orientation.
           --adjust_simulation_SNR (1.) : Relative SNR compared to input images for realistic simulation of data
                      --ang_simulate () : STAR file with orientations for projections of realistic simulations (random from --ang STAR file by default)
                          --maxres (-1) : Maximum resolution (in Angstrom) to consider in Fourier space (default Nyquist)
                              --pad (2) : Padding factor
                         --ctf2 (false) : Apply CTF*CTF to reference projections
                           --NN (false) : Use nearest-neighbour instead of linear interpolation
                              --version : Print RELION version and exit

``relion_star_datablock_stack``
--------------------------------------------------------------------------

.. code-block:: text

     === Usage: === 
     /relion_star_datablock_stack <N> <stackname> <value1> <value2> ...
 
     === Purpose: === 
     This (bash) script generates the datablock for N images in a stack named stackname
     Other (optional) data values are in value1, value2, etc. 
 
     === Example: ===
     /relion_star_datablock_stack 3 my_images.mrcs 10000 10500 0.0 200 2 0.1
     yields: 
     000001@my_images.mrcs 10000 10500 0.0 200 2 0.1
     000002@my_images.mrcs 10000 10500 0.0 200 2 0.1
     000003@my_images.mrcs 10000 10500 0.0 200 2 0.1

``relion_ctf_refine_mpi``
--------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file containing the particles
                                    --f : Input STAR file with the FSC of the reference (usually from PostProcess)
                                    --o : Output directory, e.g. CtfRefine/job041/
                                --m1 () : Reference map, half 1
                                --m2 () : Reference map, half 2
                      --angpix_ref (-1) : Pixel size of the reference map
                              --mask () : Reference mask
                              --pad (2) : Padding factor
           --only_do_unfinished (false) : Skip those steps for which output files already exist.
                      --ctf_pad (false) : Use larger box to calculate CTF and then downscale to mimic boxing operation in real space
                         --diag (false) : Write out diagnostic data (slower)
    ====== Defocus fit options ===== 
                  --fit_defocus (false) : Perform refinement of per-particle defocus values?
                     --fit_mode (fpmfm) : String of 5 characters describing whether to fit the phase shift (1), 
                                          defocus (2), astigmatism (3), spherical aberration (4) and B-factors (5) 
                                          per particle ('p'), per micrograph ('m') or to keep them fixed ('f')
                                          during the per-micrograph CTF refinement.
              --max_defocus_iters (100) : Maximum number of iterations for CTF refinement.
                          --bf0 (false) : Perform brute-force per-particle defocus search (as in RELION 3.0) prior 
                                          to the per-micrograph CTF refinement.
                          --bf1 (false) : Perform brute-force defocus search after CTF refinement.
                      --bf_only (false) : Skip CTF refinement and only perform a brute-force defocus search.
                     --bf_range (2000.) : Defocus scan range (in A) for brute-force search.
                 --legacy_astig (false) : Estimate independent per-particle astigmatism (from RELION 3.0)
                  --kmin_defocus (30.0) : Inner freq. threshold for defocus estimation [Angst]
    ====== B-factor options ===== 
                    --fit_bfacs (false) : Estimate CTF B-factors
                  --bfac_per_mg (false) : Estimate B-factors per micrograph, instead of per particle
                     --bfac_min_B (-30) : Minimal allowed B-factor
                     --bfac_max_B (300) : Maximal allowed B-factor
                 --bfac_min_scale (0.2) : Minimal allowed scale-factor (essential for outlier rejection)
                     --kmin_bfac (30.0) : Inner freq. threshold for B-factor estimation [Angst]
    ====== Beam-tilt options ===== 
                 --fit_beamtilt (false) : Perform refinement of beamtilt
                     --kmin_tilt (20.0) : Inner freq. threshold for beamtilt estimation [Å]
                  --odd_aberr_max_n (0) : Maximum degree of Zernike polynomials used to fit odd (i.e. antisymmetrical) aberrations
                           --xr0_t (-1) : Exclusion ring start [Å] - use to exclude dominant frequency (e.g. for helices)
                           --xr1_t (-1) : Exclusion ring end [Å]
    ====== Symmetric aberrations options ===== 
                    --fit_aberr (false) : Estimate symmetric aberrations
                    --kmin_aberr (20.0) : Inner freq. threshold for symmetrical aberration estimation [Å]
                 --even_aberr_max_n (4) : Maximum degree of Zernike polynomials used to fit even (i.e. symmetrical) aberrations
                           --xr0_a (-1) : Exclusion ring start [Å]
                           --xr1_a (-1) : Exclusion ring end [Å]
    ====== Anisotropic magnification options ===== 
                    --fit_aniso (false) : Estimate anisotropic magnification
                      --kmin_mag (20.0) : Inner freq. threshold for anisotropic magnification estimation [Angst]
                   --keep_astig (false) : Do not translate astigmatism into new coordinates
                   --part_astig (false) : Allow astigmatism to vary among the particles of a micrograph
    ====== Computational options ===== 
                                --j (1) : Number of (OMP) threads
                           --min_MG (0) : First micrograph index
                          --max_MG (-1) : Last micrograph index (default is to process all)
                        --debug (false) : Write debugging data
                             --verb (1) : Verbosity
                              --version : Print RELION version and exit

``relion_plot_delocalisation``
-------------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input particle *.star file
                                  --rad : Particle radius [Å]
                                    --o : Output path
                               --og (1) : Optics group
                        --max_freq (-1) : Max. image frequency [Å] (default is Nyquist)
                         --min_freq (0) : Min. image frequency [Å]
                              --name () : Name of dataset (for the plot)
                     --all_part (false) : Consider all particles, instead of only the first one in each micrograph
                              --s (256) : Square size for estimation
                                --j (1) : Number of threads
                              --version : Print RELION version and exit

``relion_star_plottable``
--------------------------------------------------------------------

.. code-block:: text

     === Usage: === 
     /relion_star_plottable <starfile> <tablename> <yaxis-label> <xaxis-label>
 
     === Purpose: === 
     This (bash) script uses gnuplot to plot content from a datablock (with name <tablename>) in <starfile>
     It will make a plot of the values given for <yaxis-label> against those of <xaxis-label>
     If <xaxis-label> is not given, the values of <yaxis-label> will be plotted linearly
 
     === Example: ===
     /relion_star_plottable run3_it024_model.star run3_it024_model.star data_model_class_1 rlnSsnrMap rlnResolution

``relion_reconstruct_mpi``
---------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --i () : Input STAR file with the projection images and their orientations
                       --o (relion.mrc) : Name for output reconstruction
                             --sym (c1) : Symmetry group
                          --maxres (-1) : Maximum resolution (in Angstrom) to consider in Fourier space (default Nyquist)
                              --pad (2) : Padding factor
                               --img () : Optional: image path prefix
                          --subset (-1) : Subset of images to consider (1: only reconstruct half1; 2: only half2; other: reconstruct all)
                           --class (-1) : Consider only this class (-1: use all classes)
                          --angpix (-1) : Pixel size in the reconstruction (take from first optics group by default)
    ====== CTF options ===== 
                          --ctf (false) : Apply CTF correction
        --ctf_intact_first_peak (false) : Leave CTFs intact until first peak
            --ctf_phase_flipped (false) : Images have been phase flipped
             --only_flip_phases (false) : Do not correct CTF-amplitudes, only flip phases
    ====== Ewald-sphere correction options ===== 
                        --ewald (false) : Correct for Ewald-sphere curvature (developmental)
                  --mask_diameter (-1.) : Diameter (in A) of mask for Ewald-sphere curvature correction
                  --width_mask_edge (3) : Width (in pixels) of the soft edge on the mask
            --reverse_curvature (false) : Try curvature the other way around
                          --newbox (-1) : Box size of reconstruction after Ewald sphere correction
                          --sectors (2) : Number of sectors for Ewald sphere correction
                    --skip_mask (false) : Do not apply real space mask during Ewald sphere correction
               --skip_weighting (false) : Do not apply weighting during Ewald sphere correction
    ====== Helical options ===== 
                   --nr_helical_asu (1) : Number of helical asymmetrical units
                    --helical_rise (0.) : Helical rise (in Angstroms)
                   --helical_twist (0.) : Helical twist (in degrees, + for right-handedness)
    ====== Expert options ===== 
                          --subtract () : Subtract projections of this map from the images used for reconstruction
                           --NN (false) : Use nearest-neighbour instead of linear interpolation before gridding correction
                         --blob_r (1.9) : Radius of blob for gridding interpolation
                           --blob_m (0) : Order of blob for gridding interpolation
                          --blob_a (15) : Alpha-value of blob for gridding interpolation
                            --iter (10) : Number of gridding-correction iterations
                           --refdim (3) : Dimension of the reconstruction (2D or 3D)
                   --angular_error (0.) : Apply random deviations with this standard deviation (in degrees) to each of the 3 Euler angles
                     --shift_error (0.) : Apply random deviations with this standard deviation (in Angstrom) to each of the 2 translations
                --fom_weighting (false) : Weight particles according to their figure-of-merit (_rlnParticleFigureOfMerit)
                               --fsc () : FSC-curve for regularized reconstruction
                       --3d_rot (false) : Perform 3D rotations instead of backprojections from 2D images
                 --reconstruct_ctf (-1) : Perform a 3D reconstruction from 2D CTF-images, with the given size in pixels
                         --ctf2 (false) : Reconstruct CTF^2 and then take the sqrt of that
                --skip_gridding (false) : Skip gridding part of the reconstruction
                             --debug () : Rootname for debug reconstruction files
                   --debug_ori_size (1) : Rootname for debug reconstruction files
                       --debug_size (1) : Rootname for debug reconstruction files
                 --reconstruct_noise () : Reconstruct noise using sigma2 values in this model STAR file
                 --read_weights (false) : Developmental: read freq. weight files
           --write_debug_output (false) : Write out arrays with data and weight terms prior to reconstruct
         --external_reconstruct (false) : Write out BP denominator and numerator for external_reconstruct program
                             --verb (1) : Verbosity
                              --version : Print RELION version and exit

``relion_ctf_toolbox``
-----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Pre-multiply options ===== 
                                 --i () : Input STAR file with CTF information
                                 --o () : Output rootname (for multiple images: insert this string before each image's extension)
    ====== OR: simulate options ===== 
                          --simulate () : Output name for simulated CTF image
                          --angpix (1.) : Pixel size (A)
                            --box (256) : Box size (pix)
                             --kV (300) : Voltage (kV)
                             --Q0 (0.1) : Amplitude contrast
                             --Cs (2.7) : Spherical aberration (mm)
                         --defU (20000) : Defocus in U-direction (A)
                           --defV (-1.) : Defocus in V-direction (A, default = defU)
                          --defAng (0.) : Defocus angle (deg)
                     --phase_shift (0.) : Phase shift (deg)
    ====== Shared options ===== 
        --ctf_intact_first_peak (false) : Leave CTFs intact until first peak
      --ctf_intact_after_first_peak (false) : Leave CTFs intact after first peak
                      --ctf_pad (false) : Pre-multiply with a 2x finer-sampled CTF that is then downscaled
                              --version : Print RELION version and exit

``relion_stack_create``
------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file with the images (as rlnImageName) to be saved in a stack
                           --o (output) : Output rootname
                --spider_format (false) : Write out in SPIDER stack format (by default MRC stack format)
         --split_per_micrograph (false) : Write out separate stacks for each micrograph (needs rlnMicrographName in STAR file)
         --apply_transformation (false) : Apply the inplane-transformations (needs _rlnOriginX/Y and _rlnAnglePsi in STAR file) by real space interpolation
      --apply_rounded_offsets_only (false) : Apply the rounded translations only (so-recentering without interpolation; needs _rlnOriginX/Y in STAR file)
                --ignore_optics (false) : Ignore optics groups. This allows you to read and write RELION 3.0 STAR files but does NOT allow you to convert 3.1 STAR files back to the 3.0 format.
                   --one_by_one (false) : Write particles one by one. This saves memory but can be slower.
                              --version : Print RELION version and exit

``relion_external_reconstruct``
--------------------------------------------------------------------------

.. code-block:: text

    ERROR: 
      Usage: relion_external_reconstruct input.star
    === Backtrace  ===
    relion_external_reconstruct(_ZN11RelionErrorC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES7_l+0x7d) [0x561b0d91604d]
    relion_external_reconstruct(_ZN21ext_recons_parameters4readEiPPc+0x120b) [0x561b0d8eb8bb]
    relion_external_reconstruct(main+0x45) [0x561b0d8e1645]
    /lib/x86_64-linux-gnu/libc.so.6(+0x29d90) [0x7f332f717d90]
    /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0x80) [0x7f332f717e40]
    relion_external_reconstruct(_start+0x25) [0x561b0d8e1ca5]
    ==================
    ERROR: 
      Usage: relion_external_reconstruct input.star

``relion_tomo_test``
---------------------------------------------------------------

.. code-block:: text

    reading: frames/bin4_0.mrc

``relion_flex_analyse``
------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                              --data () : The _data.star file with the orientations to be analysed
                             --model () :  The corresponding _model.star file with the refined model
                            --bodies () : The corresponding star file with the definition of the bodies
                          --o (analyse) : Output rootname
    ====== 3D model options ===== 
                     --3dmodels (false) : Generate a 3D model for each experimental particles
                   --size_3dmodels (-1) : Output size of the 3D models (default is same as input particles)
    ====== PCA options ===== 
                   --PCA_orient (false) : Perform a principal components analysis on the multibody orientations
                      --do_maps (false) : Generate maps along the principal components
                               --k (-1) : Number of principal components to generate maps for
                             --v (0.75) : Or use as many principal components to explain this fraction of variance (<0,1])
                  --maps_per_movie (10) : Number of maps to use for the movie of each principal component
                           --bins (100) : Number of bins in histograms of the eigenvalues for each principal component
               --select_eigenvalue (-1) : Output a selection particle.star file based on eigenvalues along this eigenvector
      --select_eigenvalue_min (-99999.) : Minimum for eigenvalue to include particles in selection output star file
       --select_eigenvalue_max (99999.) : Maximum for eigenvalue to include particles in selection output star file
        --write_pca_projections (false) : Write out a text file with all PCA projections for all particles
                             --verb (1) : Verbosity
                              --version : Print RELION version and exit

``relion_refine_mpi``
----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --i () : Input images (in a star-file)
                                 --o () : Output rootname
                            --iter (50) : Maximum number of iterations to perform
                       --tau2_fudge (1) : Regularisation parameter (values higher than 1 give more weight to the data)
                                --K (1) : Number of references to be refined
               --particle_diameter (-1) : Diameter of the circular mask that will be applied to the experimental images (in Angstroms)
                    --zero_mask (false) : Mask surrounding background in particles to zero (by default the solvent area is filled with random noise)
              --flatten_solvent (false) : Perform masking on the references as well?
                  --solvent_mask (None) : User-provided mask for the references (default is to use spherical mask with particle_diameter)
                 --solvent_mask2 (None) : User-provided secondary mask (with its own average density)
                  --lowpass_mask (None) : User-provided mask for low-pass filtering
                          --lowpass (0) : User-provided cutoff for region specified above
                           --tau (None) : STAR file with input tau2-spectrum (to be kept constant)
                --local_symmetry (None) : Local symmetry description file containing list of masks and their operators
          --split_random_halves (false) : Refine two random halves of the data completely separately
           --low_resol_join_halves (-1) : Resolution (in Angstrom) up to which the two random half-reconstructions will not be independent to prevent diverging orientations
    ====== Initialisation ===== 
                           --ref (None) : Image, stack or star-file with the reference(s). (Compulsory for 3D refinement!)
                 --denovo_3dref (false) : Make an initial 3D model from randomly oriented 2D particles
                          --offset (10) : Initial estimated stddev for the origin offsets (in Angstroms)
                 --firstiter_cc (false) : Perform CC-calculation in the first iteration (use this if references are not on the absolute intensity scale)
                        --ini_high (-1) : Resolution (in Angstroms) to which to limit refinement in the first iteration 
    ====== Orientations ===== 
                     --oversampling (1) : Adaptive oversampling order to speed-up calculations (0=no oversampling, 1=2x, 2=4x, etc)
                    --healpix_order (2) : Healpix order for the angular sampling (before oversampling) on the (3D) sphere: hp2=15deg, hp3=7.5deg, etc
                        --psi_step (-1) : Sampling rate (before oversampling) for the in-plane angle (default=10deg for 2D, hp sampling for 3D)
                     --limit_tilt (-91) : Limited tilt angle: positive for keeping side views, negative for keeping top views
                             --sym (c1) : Symmetry group
                         --relax_sym () : Symmetry to be relaxed
                     --offset_range (6) : Search range for origin offsets (in pixels)
                      --offset_step (2) : Sampling rate (before oversampling) for origin offsets (in pixels)
             --helical_offset_step (-1) : Sampling rate (before oversampling) for offsets along helical axis (in Angstroms)
                        --perturb (0.5) : Perturbation factor for the angular sampling (0=no perturb; 0.5=perturb)
                  --auto_refine (false) : Perform 3D auto-refine procedure?
         --auto_local_healpix_order (4) : Minimum healpix order (before oversampling) from which autosampling procedure will use local searches
                       --sigma_ang (-1) : Stddev on all three Euler angles for local angular searches (of +/- 3 stddev)
                       --sigma_rot (-1) : Stddev on the first Euler angle for local angular searches (of +/- 3 stddev)
                      --sigma_tilt (-1) : Stddev on the second Euler angle for local angular searches (of +/- 3 stddev)
                       --sigma_psi (-1) : Stddev on the in-plane angle for local angular searches (of +/- 3 stddev)
                   --skip_align (false) : Skip orientational assignment (only classify)?
                  --skip_rotate (false) : Skip rotational assignment (only translate and classify)?
                  --bimodal_psi (false) : Do bimodal searches of psi angle?
    ====== Helical reconstruction (in development...) ===== 
                        --helix (false) : Perform 3D classification or refinement for helices?
      --ignore_helical_symmetry (false) : Ignore helical symmetry?
                   --helical_nr_asu (1) : Number of new helical asymmetric units (asu) per box (1 means no helical symmetry is present)
           --helical_twist_initial (0.) : Helical twist (in degrees, positive values for right-handedness)
               --helical_twist_min (0.) : Minimum helical twist (in degrees, positive values for right-handedness)
               --helical_twist_max (0.) : Maximum helical twist (in degrees, positive values for right-handedness)
           --helical_twist_inistep (0.) : Initial step of helical twist search (in degrees)
            --helical_rise_initial (0.) : Helical rise (in Angstroms)
                --helical_rise_min (0.) : Minimum helical rise (in Angstroms)
                --helical_rise_max (0.) : Maximum helical rise (in Angstroms)
            --helical_rise_inistep (0.) : Initial step of helical rise search (in Angstroms)
                   --helical_nstart (1) : N-number for the N-start helix (only useful for rotational priors)
           --helical_z_percentage (0.3) : This box length along the center of Z axis contains good information of the helix. Important in imposing and refining symmetry
         --helical_inner_diameter (-1.) : Inner diameter of helical tubes in Angstroms (for masks of helical references and particles)
         --helical_outer_diameter (-1.) : Outer diameter of helical tubes in Angstroms (for masks of helical references and particles)
      --helical_symmetry_search (false) : Perform local refinement of helical symmetry?
         --helical_sigma_distance (-1.) : Sigma of distance along the helical tracks
      --helical_keep_tilt_prior_fixed (false) : Keep helical tilt priors fixed (at 90 degrees) in global angular searches?
            --helical_exclude_resols () : Resolutions (in A) along helical axis to exclude from refinement (comma-separated pairs, e.g. 50-5)
                  --fourier_mask (None) : Originally-sized, FFTW-centred image with Fourier mask for Projector
    ====== Corrections ===== 
                          --ctf (false) : Perform CTF correction?
                      --pad_ctf (false) : Perform CTF padding to treat CTF aliaising better?
        --ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
            --ctf_corrected_ref (false) : Have the input references been CTF-amplitude corrected?
            --ctf_phase_flipped (false) : Have the data been CTF phase-flipped?
             --only_flip_phases (false) : Only perform CTF phase-flipping? (default is full amplitude-correction)
                         --norm (false) : Perform normalisation-error correction?
                        --scale (false) : Perform intensity-scale corrections on image groups?
                      --no_norm (false) : Switch off normalisation-error correction?
                     --no_scale (false) : Switch off intensity-scale corrections on image groups?
    ====== Stochastic Gradient Descent ===== 
                          --sgd (false) : Perform stochastic gradient descent instead of default expectation-maximization
                --stochastic_em (false) : Perform stochastic EM instead of SGD to avoid patent problems for initial model generation by commercial users
                    --sgd_ini_iter (50) : Number of initial SGD iterations
                    --sgd_fin_iter (50) : Number of final SGD iterations
             --sgd_inbetween_iter (200) : Number of SGD iterations between the initial and final ones
                   --sgd_ini_resol (35) : Resolution cutoff during the initial SGD iterations (A)
                   --sgd_fin_resol (15) : Resolution cutoff during the final SGD iterations (A)
                 --sgd_ini_subset (100) : Mini-batch size during the initial SGD iterations
                 --sgd_fin_subset (500) : Mini-batch size during the final SGD iterations
                             --mu (0.9) : Momentum parameter for SGD updates
                   --sgd_stepsize (0.5) : Step size parameter for SGD updates
          --sgd_sigma2fudge_initial (8) : Initial factor by which the noise variance will be multiplied for SGD (not used if halftime is negative)
        --sgd_sigma2fudge_halflife (-1) : Initialise SGD with 8x higher noise-variance, and reduce with this half-life in # of particles (default is keep normal variance)
              --sgd_skip_anneal (false) : By default, multiple references are annealed during the in_between iterations. Use this option to switch annealing off
                   --sgd_write_iter (1) : Write out model every so many iterations in SGD (default is writing out all iters)
    ====== Computation ===== 
                             --pool (1) : Number of images to pool for each thread task
                                --j (1) : Number of threads to run in parallel (only useful on multi-core machines)
      --dont_combine_weights_via_disc (false) : Send the large arrays of summed weights through the MPI network, instead of writing large files to disc
              --onthefly_shifts (false) : Calculate shifted images on-the-fly, do not store precalculated ones in memory
          --no_parallel_disc_io (false) : Do NOT let parallel (MPI) processes access the disc simultaneously (use this option with NFS)
               --preread_images (false) : Use this to let the leader process read all particles into memory. Be careful you have enough RAM for large data sets!
                       --scratch_dir () : If provided, particle stacks will be copied to this local scratch disk prior to refinement.
               --keep_free_scratch (10) : Space available for copying particle stacks (in Gb)
                --reuse_scratch (false) : Re-use data on scratchdir, instead of wiping it and re-copying all data.
                 --keep_scratch (false) : Don't remove scratch after convergence. Following jobs that use EXACTLY the same particles should use --reuse_scratch.
                 --fast_subsets (false) : Use faster optimisation by using subsets of the data in the first 15 iterations
                          --gpu (false) : Use available gpu resources for some calculations
                  --free_gpu_memory (0) : GPU device memory (in Mb) to leave free after allocation.
    ====== Expert options ===== 
                              --pad (2) : Oversampling factor for the Fourier transforms of the references
                     --ref_angpix (-1.) : Pixel size (in A) for the input reference (default is to read from header)
                           --NN (false) : Perform nearest-neighbour instead of linear Fourier-space interpolation?
                        --r_min_nn (10) : Minimum number of Fourier shells to perform linear Fourier-space interpolation
                             --verb (1) : Verbosity (1=normal, 0=silent)
                     --random_seed (-1) : Number for the random seed generator
                     --coarse_size (-1) : Maximum image size for the first pass of the adaptive sampling approach
            --adaptive_fraction (0.999) : Fraction of the weights to be considered in the first pass of adaptive oversampling 
                         --maskedge (5) : Width of the soft edge of the spherical mask (in pixels)
              --fix_sigma_noise (false) : Fix the experimental noise spectra?
             --fix_sigma_offset (false) : Fix the stddev in the origin offsets?
                       --incr_size (10) : Number of Fourier shells beyond the current resolution to be included in refinement
        --print_metadata_labels (false) : Print a table with definitions of all metadata labels, and exit
           --print_symmetry_ops (false) : Print all symmetry transformation matrices, and exit
              --strict_highres_exp (-1) : High resolution limit (in Angstrom) to restrict probability calculations in the expectation step
               --strict_lowres_exp (-1) : Low resolution limit (in Angstrom) to restrict probability calculations in the expectation step
              --dont_check_norm (false) : Skip the check whether the images are normalised correctly
                    --always_cc (false) : Perform CC-calculation in all iterations (useful for faster denovo model generation?)
          --solvent_correct_fsc (false) : Correct FSC curve for the effects of the solvent mask?
                --skip_maximize (false) : Skip maximization step (only write out data.star file)?
              --failsafe_threshold (40) : Maximum number of particles permitted to be handled by fail-safe mode, due to zero sum of weights, before exiting with an error (GPU only).
         --external_reconstruct (false) : Perform the reconstruction step outside relion_refine, e.g. for learned priors?)
                  --auto_iter_max (999) : In auto-refinement, stop at this iteration.
           --auto_ignore_angles (false) : In auto-refinement, update angular sampling regardless of changes in orientations for convergence. This makes convergence faster.
            --auto_resol_angles (false) : In auto-refinement, update angular sampling based on resolution-based required sampling. This makes convergence faster.
       --allow_coarser_sampling (false) : In 2D/3D classification, allow coarser angular and translational samplings if accuracies are bad (typically in earlier iterations.
               --trust_ref_size (false) : Trust the pixel and box size of the input reference; by default the program will die if these are different from the first optics group of the data
                          --maxsig (-1) : Maximum number of poses & translations to consider
                --skip_gridding (false) : Skip gridding in the M step
    ====== MPI options ===== 
       --halt_all_followers_except (-1) : For debugging: keep all followers except this one waiting
      --keep_debug_reconstruct_files (false) : For debugging: keep temporary data and weight files for debug-reconstructions.
                              --version : Print RELION version and exit

``relion_star_handler``
------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file
                         --o (out.star) : Output STAR file
                --ignore_optics (false) : Provide this option for relion-3.0 functionality, without optics groups
                          --angpix (1.) : Pixel size in Angstrom, for when ignoring the optics groups in the input star file
                       --i_tablename () : If ignoring optics, then read table with this name
    ====== Compare options ===== 
                           --compare () : STAR file name to compare the input STAR file with
                            --label1 () : 1st metadata label for the comparison (may be string, int or RFLOAT)
                            --label2 () : 2nd metadata label for the comparison (RFLOAT only) for 2D/3D-distance)
                            --label3 () : 3rd metadata label for the comparison (RFLOAT only) for 3D-distance)
                        --max_dist (0.) : Maximum distance to consider a match (for int and RFLOAT only)
    ====== Select options ===== 
                            --select () : Metadata label (number) to base output selection on (e.g. rlnCtfFigureOfMerit)
                  --minval (-99999999.) : Minimum acceptable value for this label (inclusive)
                   --maxval (99999999.) : Maximum acceptable value for this label (inclusive)
                     --select_by_str () : Metadata label (string) to base output selection on (e.g. rlnMicrographname)
                    --select_include () : select rows that contains this string in --select_by_str 
                    --select_exclude () : exclude rows that contains this string in --select_by_str 
    ====== Discard based on image statistics options ===== 
             --discard_on_stats (false) : Discard images if their average/stddev deviates too many sigma from the ensemble average
         --discard_label (rlnImageName) : MetaDataLabel that points to the images to be used for discarding based on statistics
                   --discard_sigma (4.) : Discard images with average or stddev values that lie this many sigma away from the ensemble average
    ====== Combine options ===== 
                      --combine (false) : Combine input STAR files (multiple individual filenames, all within double-quotes after --i)
                  --check_duplicates () : MetaDataLabel (for a string only!) to check for duplicates, e.g. rlnImageName
    ====== Split options ===== 
                        --split (false) : Split the input STAR file into one or more smaller output STAR files
                 --random_order (false) : Perform splits on randomised order of the input STAR file
                     --random_seed (-1) : Random seed for randomisation.
                        --nr_split (-1) : Split into this many equal-sized STAR files
                      --size_split (-1) : AND/OR split into subsets of this many lines
    ====== Operate options ===== 
                           --operate () : Operate on this metadata label
                          --operate2 () : Operate also on this metadata label
                          --operate3 () : Operate also on this metadata label
                            --set_to () : Set all the values for the --operate label(s) to this value
                     --multiply_by (1.) : Multiply all the values for the --operate label(s) by this value
                          --add_to (0.) : Add this value to all the values for the --operate label(s)
    ====== Center options ===== 
                       --center (false) : Perform centering of particles according to a position in the reference.
                        --center_X (0.) : X-coordinate in the reference to center particles on (in pix)
                        --center_Y (0.) : Y-coordinate in the reference to center particles on (in pix)
                        --center_Z (0.) : Z-coordinate in the reference to center particles on (in pix)
    ====== Column options ===== 
                     --remove_column () : Remove the column with this metadata label from the input STAR file.
                        --add_column () : Add a column with this metadata label from the input STAR file.
                  --add_column_value () : Set this value in all rows for the added column
                  --copy_column_from () : Copy values in this column to the added column
                       --hist_column () : Calculate histogram of values in the column with this metadata label
                   --in_percent (false) : Show a histogram in percent (need --hist_column)
              --show_cumulative (false) : Show a histogram of cumulative distribution (need --hist_column)
                       --hist_bins (-1) : Number of bins for the histogram. By default, determined automatically by Freedman–Diaconis rule.
                      --hist_min (-inf) : Minimum value for the histogram (needs --hist_bins)
                       --hist_max (inf) : Maximum value for the histogram (needs --hist_bins)
    ====== Duplicate removal ===== 
               --remove_duplicates (-1) : Remove duplicated particles within this distance [Angstrom]. Negative values disable this.
                    --image_angpix (-1) : For down-sampled particles, specify the pixel size [A/pix] of the original images used in the Extract job
                              --version : Print RELION version and exit

``relion_star_datablock_singlefiles``
--------------------------------------------------------------------------------

.. code-block:: text

     === Usage: === 
     /relion_star_datablock_singlefiles "*.spi" <value1> <value2> ...
 
     === Purpose: === 
     This (bash) script generates the datablock for all images represented by the wildcard in the first argument
     Other (optional) data values are in value1, value2, etc. 
 
     === Example: ===
     /relion_star_datablock_singlefiles "tmp/*" 10000 10500 0.0 200 2 0.1
     yields: 
     tmp/t1.spi 10000 10500 0.0 200 2 0.1
     tmp/t2.spi 10000 10500 0.0 200 2 0.1
     tmp/t3.spi 10000 10500 0.0 200 2 0.1

``relion_qsub``
--------------------------------------------------------------

.. code-block:: text

    /bin/sh: 1: relion_qsub.csh: not found

``relion_align_symmetry``
--------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Options ===== 
                                    --i : Input map to be projected
                                  --sym : Target point group symmetry
                      --o (aligned.mrc) : Rootname for output projections
                        --box_size (64) : Working box size in pixels. Very small box (such that Nyquist is aroud 20 A) is usually sufficient.
                  --keep_centre (false) : Do not re-centre the input
                          --angpix (-1) : Pixel size (in Angstroms)
                     --only_rot (false) : Keep TILT and PSI fixed and search only ROT (rotation along the Z axis)
                     --nr_uniform (400) : Randomly search this many orientations
                          --maxres (-1) : Maximum resolution (in Angstrom) to consider in Fourier space (default Nyquist)
               --local_search_range (2) : Local search range (1 + 2 * this number)
                --local_search_step (2) : Local search step (in degrees)
                              --pad (2) : Padding factor
                           --NN (false) : Use nearest-neighbour instead of linear interpolation
                              --version : Print RELION version and exit

``relion_autopick``
--------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Micrograph STAR file OR filenames from which to autopick particles, e.g. "Micrographs/*.mrc"
                  --pickname (autopick) : Rootname for coordinate STAR files
                     --odir (AutoPick/) : Output directory for coordinate files (default is to store next to micrographs)
                           --angpix (1) : Pixel size of the micrographs in Angstroms
               --particle_diameter (-1) : Diameter of the circular mask that will be applied to the experimental images (in Angstroms, default=automatic)
             --shrink_particle_mask (2) : Shrink the particle mask by this many pixels (to detect Einstein-from-noise classes)
          --outlier_removal_zscore (8.) : Remove pixels that are this many sigma away from the mean
               --write_fom_maps (false) : Write calculated probability-ratio maps to disc (for re-reading in subsequent runs)
                 --no_fom_limit (false) : Ignore default maximum limit of 30 fom maps being written
                --read_fom_maps (false) : Skip probability calculations, re-read precalculated maps from disc
          --skip_optimise_scale (false) : Skip the optimisation of the micrograph scale for better prime factors in the FFTs. This runs slower, but at exactly the requested resolution.
           --only_do_unfinished (false) : Only autopick those micrographs for which the coordinate file does not yet exist
                          --gpu (false) : Use GPU acceleration when availiable
    ====== References options ===== 
                               --ref () : STAR file with the reference names, or an MRC stack with all references, or "gauss" for blob-picking
                      --angpix_ref (-1) : Pixel size of the references in Angstroms (default is same as micrographs)
                       --invert (false) : Density in micrograph is inverted w.r.t. density in template
                             --ang (10) : Angular sampling (in degrees); use 360 for no rotations
                         --lowpass (-1) : Lowpass filter in Angstroms for the references (prevent Einstein-from-noise!)
                        --highpass (-1) : Highpass filter in Angstroms for the micrographs
                          --ctf (false) : Perform CTF correction on the references?
        --ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
                      --gauss_max (0.1) : Value of the peak in the Gaussian blob reference
                    --healpix_order (1) : Healpix order for projecting a 3D reference (hp0=60deg; hp1=30deg; hp2=15deg)
                             --sym (C1) : Symmetry point group for a 3D reference
    ====== Laplacian-of-Gaussian options ===== 
                          --LoG (false) : Use Laplacian-of-Gaussian filter-based picking, instead of template matching
                    --LoG_diam_min (-1) : Smallest particle diameter (in Angstroms) for blob-detection by Laplacian-of-Gaussian filter
                    --LoG_diam_max (-1) : Largest particle diameter (in Angstroms) for blob-detection by Laplacian-of-Gaussian filter
                  --LoG_neighbour (100) : Avoid neighbouring particles within (the detected diameter + the minimum diameter) times this percent
                   --Log_invert (false) : Use this option if the particles are white instead of black
            --LoG_adjust_threshold (0.) : Use this option to adjust the picking threshold: positive for less particles, negative for more
          --LoG_upper_threshold (99999) : Use this option to set the upper limit of the picking threshold
                  --LoG_use_ctf (false) : Use CTF until the first peak in Laplacian-of-Gaussian picker
    ====== Helix options ===== 
                        --helix (false) : Are the references 2D helical segments? If so, in-plane rotation angles (psi) are estimated for the references.
        --helical_tube_kappa_max (0.25) : Factor of maximum curvature relative to that of a circle
      --helical_tube_outer_diameter (-1) : Tube diameter in Angstroms
         --helical_tube_length_min (-1) : Minimum tube length in Angstroms
                      --amyloid (false) : Activate specific algorithm for amyloid picking?
            ----max_diam_local_avg (-1) : Maximum diameter to calculate local average density in Angstroms
    ====== Peak-search options ===== 
                     --threshold (0.25) : Fraction of expected probability ratio in order to consider peaks?
                    --min_distance (-1) : Minimum distance (in A) between any two particles (default is half the box size)
                --max_stddev_noise (-1) : Maximum standard deviation in the noise area to use for picking peaks (default is no maximum)
                --min_avg_noise (-999.) : Minimum average in the noise area to use for picking peaks (default is no minimum)
                        --skip_side (0) : Keep this many extra pixels (apart from particle_size/2) away from the edge of the micrograph 
    ====== Expert options ===== 
                             --verb (1) : Verbosity
                              --pad (2) : Padding factor for Fourier transforms
                      --random_seed (1) : Number for the random seed generator
                         --shrink (1.0) : Reduce micrograph to this fraction size, during correlation calc (saves memory and time)
                  --Log_max_search (5.) : Maximum diameter in LoG-picking multi-scale approach is this many times the min/max diameter
                        --extra_pad (0) : Number of pixels for additional padding of the original micrograph
                              --version : Print RELION version and exit

``relion_particle_subtract``
-----------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --i () : Name of optimiser.star file from refinement/classification to use for subtraction
                        --o (Subtract/) : Output directory name
                              --mask () : Name of the 3D mask with all density that should be kept, i.e. not subtracted
                              --data () : Name of particle STAR file, in case not all particles from optimiser are to be used
                 --ignore_class (false) : Ignore the rlnClassNumber column in the particle STAR file.
                            --revert () : Name of particle STAR file to revert. When this is provided, all other options are ignored.
                         --ssnr (false) : Don't subtract, only calculate average spectral SNR in the images
    ====== Centering options ===== 
             --recenter_on_mask (false) : Use this flag to center the subtracted particles on projections of the centre-of-mass of the input mask
                      --center_x (9999) : X-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
                      --center_y (9999) : Y-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
                      --center_z (9999) : Z-coordinate of 3D coordinate, which will be projected to center the subtracted particles.
                         --new_box (-1) : Output size of the subtracted particles
                              --version : Print RELION version and exit

``relion_particle_symmetry_expand``
------------------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Options ===== 
                                    --i : Input particle STAR file
                    --o (expanded.star) : Output expanded particle STAR file
                             --sym (C1) : Symmetry point group
    ====== Helix ===== 
                        --helix (false) : Do helical symmetry expansion
                           --twist (0.) : Helical twist (deg)
                            --rise (0.) : Helical rise (A)
                          --angpix (1.) : Pixel size (A)
                              --asu (1) : Number of asymmetrical units to expand
                    --frac_sampling (1) : Number of samplings in between a single asymmetrical unit
                     --frac_range (0.5) : Range of the rise [-0.5, 0.5> to be sampled
                --ignore_optics (false) : Provide this option for relion-3.0 functionality, without optics groups
                              --version : Print RELION version and exit

``relion_localsym``
--------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Show usage ===== 
                --function_help (false) : Show usage for the selected function (JUN 30, 2017)
    ====== Options ===== 
                        --apply (false) : Apply local symmetry to a 3D cryo-EM density map
                    --duplicate (false) : Duplicate subunits/masks according to local symmetry operators
                       --search (false) : Local searches of local symmetry operators
                    --transform (false) : Transform a map according to three Euler angles and XYZ translations
                      --txt2rln (false) : Convert operators from DM to RELION STAR format
                        --debug (false) : (DEBUG ONLY)
    ====== Parameters (alphabetically ordered) ===== 
                          --angpix (1.) : Pixel size (in Angstroms) of input image
                       --ang_range (0.) : Angular search range of operators (in degrees), overwrite rot-tilt-psi ranges if set to positive
                   --ang_rot_range (0.) : Angular (rot) search range of operators (in degrees)
                  --ang_tilt_range (0.) : Angular (tilt) search range of operators (in degrees)
                   --ang_psi_range (0.) : Angular (psi) search range of operators (in degrees)
                        --ang_step (1.) : Angular search step of operators (in degrees)
                            --bin (-1.) : Binning factor (<= 1 means no binning)
                 --ini_threshold (0.01) : Initial threshold for binarization
                             --i_map () : Input 3D unsymmetrised map
           --i_mask_info (maskinfo.txt) : Input file with mask filenames and rotational / translational operators (for local searches)
                --i_op_mask_info (None) : Input file with mask filenames for all operators (for global searches)
                                --n (2) : Create this number of masks according to the input density map
                    --offset_range (0.) : Translational search range of operators (in Angstroms), overwrite x-y-z ranges if set to positive
                  --offset_x_range (0.) : Translational (x) search range of operators (in Angstroms)
                  --offset_y_range (0.) : Translational (y) search range of operators (in Angstroms)
                  --offset_z_range (0.) : Translational (z) search range of operators (in Angstroms)
                     --offset_step (1.) : Translational search step of operators (in Angstroms)
                             --o_map () : Output 3D symmetrised map
      --o_mask_info (maskinfo_refined.txt) : Output file with mask filenames and rotational / translational operators
                             --psi (0.) : Third Euler angle (psi, in degrees)
                             --rot (0.) : First Euler angle (rot, in degrees)
              --sphere_percentage (-1.) : Diameter of spherical mask divided by the box size (< 0.99)
                            --tilt (0.) : Second Euler angle (tilt, in degrees)
                            --xoff (0.) : X-offset (in Angstroms)
                            --yoff (0.) : Y-offset (in Angstroms)
                            --zoff (0.) : Z-offset (in Angstroms)
                         --verb (false) : Verbose output?
    ====== Parameters (expert options - alphabetically ordered) ===== 
                    --i_mask (mask.mrc) : (DEBUG) Input mask
      --i_mask_info_parsed_ext (parsed) : Extension of parsed input file with mask filenames and rotational / translational operators
                  --use_healpix (false) : Use Healpix for angular samplings?
                           --width (5.) : Width of cosine soft edge (in pixels)
                              --version : Print RELION version and exit

``relion_preprocess``
----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                 --i () : The STAR file with all (selected) micrographs to extract particles from
                      --coord_suffix () : The suffix for the coordinate files, e.g. "_picked.star" or ".box"
                  --coord_dir (ASINPUT) : The directory where the coordinate files are (default is same as micrographs)
                --part_dir (Particles/) : Output directory for particle stacks
                         --part_star () : Output STAR file with all particles metadata
               --reextract_data_star () : A _data.star file from a refinement to re-extract, e.g. with different binning or re-centered (instead of --coord_suffix)
        --keep_ctfs_micrographs (false) : By default, CTFs from fn_data will be kept. Use this flag to keep CTFs from input micrographs STAR file
                --reset_offsets (false) : reset the origin offsets from the input _data.star file to zero?
                     --recenter (false) : Re-center particle according to rlnOriginX/Y in --reextract_data_star STAR file
                      --recenter_x (0.) : X-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --recenter_y (0.) : Y-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --recenter_z (0.) : Z-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --ref_angpix (-1) : Pixel size of the reference used for recentering. -1 uses the pixel size of particles.
    ====== Particle extraction ===== 
                      --extract (false) : Extract all particles from the micrographs
                    --extract_size (-1) : Size of the box to extract the particles in (in pixels)
              --premultiply_ctf (false) : Premultiply the micrograph/frame with its CTF prior to particle extraction
        --premultiply_extract_size (-1) : Size of the box to extract the particles in (in pixels) before CTF premultiplication
        --ctf_intact_first_peak (false) : When premultiplying with the CTF, leave frequencies intact until the first peak
                   --phase_flip (false) : Flip CTF-phases in the micrograph/frame prior to particle extraction
                   --extract_bias_x (0) : Bias in X-direction of picked particles (this value in pixels will be added to the coords)
                   --extract_bias_y (0) : Bias in Y-direction of picked particles (this value in pixels will be added to the coords)
           --only_do_unfinished (false) : Extract only particles if the STAR file for that micrograph does not yet exist.
    ====== Particle operations ===== 
                    --project3d (false) : Project sub-tomograms along Z to generate 2D particles
                           --scale (-1) : Re-scale the particles to this size (in pixels)
                          --window (-1) : Re-window the particles to this size (in pixels)
                         --norm (false) : Normalise the background to average zero and stddev one
                      --no_ramp (false) : Just subtract the background mean in the normalisation, instead of subtracting a fitted ramping background. 
                       --bg_radius (-1) : Radius of the circular mask that will be used to define the background area (in pixels)
                      --white_dust (-1) : Sigma-values above which white dust will be removed (negative value means no dust removal)
                      --black_dust (-1) : Sigma-values above which black dust will be removed (negative value means no dust removal)
              --invert_contrast (false) : Invert the contrast in the input images
                        --operate_on () : Use this option to operate on an input image stack 
      --operate_out (preprocessed.mrcs) : Output name when operating on an input image stack
    ====== Helix extraction ===== 
                        --helix (false) : Extract helical segments
         --helical_outer_diameter (-1.) : Outer diameter of helical tubes in Angstroms (for masks of helical segments)
                --helical_tubes (false) : Extract helical segments from tube coordinates
                   --helical_nr_asu (1) : Number of helical asymmetrical units
                    --helical_rise (0.) : Helical rise (in Angstroms)
      --helical_bimodal_angular_priors (false) : Add bimodal angular priors for helical segments
      --helical_cut_into_segments (false) : Cut helical tubes into segments
                              --version : Print RELION version and exit

``relion_run_motioncorr_mpi``
------------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : STAR file with all input micrographs, or a Linux wildcard with all micrographs to operate on
                       --o (MotionCorr) : Name for the output directory
                                --j (1) : Number of threads per movie (= process)
                  --max_io_threads (-1) : Limit the number of IO threads.
           --only_do_unfinished (false) : Only run motion correction for those micrographs for which there is not yet an output micrograph.
                      --do_at_most (-1) : Only process at most this number of (unprocessed) micrographs.
                 --grouping_for_ps (-1) : Group this number of frames and write summed power spectrum. -1 == do not write
                        --ps_size (512) : Output size of power spectrum
                  --first_frame_sum (1) : First movie frame used in output sum (start at 1)
                  --last_frame_sum (-1) : Last movie frame used in output sum (0 or negative: use all)
                    --eer_grouping (40) : EER grouping
                   --eer_upsampling (1) : EER upsampling (1 = 4K or 2 = 8K)
    ====== MOTIONCOR2 options ===== 
               --use_motioncor2 (false) : Use Shawn Zheng's MOTIONCOR2.
                    --motioncor2_exe () : Location of MOTIONCOR2 executable (or through RELION_MOTIONCOR2_EXECUTABLE environment variable)
                       --bin_factor (1) : Binning factor (can be non-integer)
                        --bfactor (150) : B-factor (in pix^2) that will be used inside MOTIONCOR2
                           --gainref () : Location of MRC file with the gain reference to be applied
                         --gain_rot (0) : Rotate the gain reference this number times 90 degrees clock-wise (in relion_display). This is same as MotionCor2's RotGain. 0, 1, 2 or 3
                        --gain_flip (0) : Flip the gain reference. This is same as MotionCor2's FlipGain. 0, 1 (flip Y == upside down) or 2 (flip X == left to right)
                          --patch_x (1) : Patching in X-direction for MOTIONCOR2
                          --patch_y (1) : Patching in Y-direction for MOTIONCOR2
                     --group_frames (1) : Average together this many frames before calculating the beam-induced shifts
                       --defect_file () : Location of a MOTIONCOR2-style detector defect file (x y w h) or a defect map (1 means bad)
                           --archive () : Location of the directory for archiving movies in 4-byte MRC format
             --other_motioncor2_args () : Additional arguments to MOTIONCOR2
                               --gpu () : Device ids for each MPI-thread, e.g 0:1:2:3
    ====== Dose-weighting options ===== 
               --dose_weighting (false) : Use dose-weighting scheme
                          --angpix (-1) : Pixel size in Angstroms
                         --voltage (-1) : Voltage (in kV) for dose-weighting
                   --dose_per_frame (1) : Electron dose (in electrons/A2/frame) for dose-weighting
                      --preexposure (0) : Pre-exposure (in electrons/A2) for dose-weighting
    ====== Own motion correction options ===== 
                      --use_own (false) : Use our own implementation of motion correction
                  --skip_defect (false) : Skip hot pixel detection
                    --save_noDW (false) : Save aligned but non dose weighted micrograph
                         --max_iter (5) : Maximum number of iterations for alignment. Only valid with --use_own
           --interpolate_shifts (false) : (EXPERIMENTAL) Interpolate shifts
                   --ccf_downsample (0) : (EXPERT) Downsampling rate of CC map. default = 0 = automatic based on B factor
                --early_binning (false) : Do binning before alignment to reduce memory usage. This might dampen signal near Nyquist. (ON by default)
             --no_early_binning (false) : Disable --early_binning
         --dose_motionstats_cutoff (4.) : Electron dose (in electrons/A2) at which to distinguish early/late global accumulated motion in output statistics
                              --version : Print RELION version and exit

``relion_helix_toolbox``
-------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Show usage ===== 
                --function_help (false) : Show usage for the selected function (FEB 19, 2017)
    ====== List of functions (alphabetically ordered) ===== 
                        --check (false) : Check parameters for 3D helical reconstruction in RELION
                      --cut_out (false) : Cut out a small part of the helix
                     --cylinder (false) : Create a cylinder as 3D initial reference
                       --impose (false) : Impose helical symmetry (in real space)
                      --interpo (false) : Interpolate 3D curve for 3D helical sub-tomogram extraction
                         --norm (false) : Normalise 2D/3D helical segments in a STAR file
                    --pdb_helix (false) : Simulate a helix from a single PDB file of protein molecule
               --remove_bad_ctf (false) : Remove micrographs with poor-quality CTF
              --remove_bad_tilt (false) : Remove helical segments with large tilt angle deviation (away from 90 degrees)
               --remove_bad_psi (false) : Remove helical segments with large psi angle deviation (away from psi prior)
                       --search (false) : Local search of helical symmetry
                --select_3dtomo (false) : Select 3D subtomograms given 2D projections
               --simulate_helix (false) : Create a helical 3D reference of spheres
            --simulate_segments (false) : Simulate helical segments using a STAR file
                 --sort_tube_id (false) : Sort segments in _data.star file according to helical tube IDs
               --spherical_mask (false) : Apply soft spherical mask to 3D helical reference
                --average_au_2d (false) : Average multiple asymmetrical units in 2D along the helical axis?
    ====== List of functions which can be called in Relion GUI ===== 
                 --combine_gctf (false) : Combine Autopicker priors (tilt and psi) with Gctf local search results
                 --central_mask (false) : Crop the central part of a helix
               --coords_emn2rln (false) : Convert EMAN2 coordinates of helical segments into RELION STAR format
               --coords_xim2rln (false) : Convert XIMDISP coordinates of helical segments into RELION STAR format
                       --divide (false) : Divide one huge STAR file into many small ones
                  --extract_emn (false) : Extract EMAN2 coordinates of helical segments from specified straight tubes
                  --extract_rln (false) : Extract RELION coordinates of helical segments from specified straight tubes
                  --extract_xim (false) : Extract XIMDISP coordinates of helical segments from specified straight tubes
               --impose_fourier (false) : Impose helical symmetry (simulate what is done in 3D reconstruction in Fourier space)
                    --init_tilt (false) : Set tilt angles to 90 degrees for all helical segments
                        --merge (false) : Merge small STAR files into a huge one
             --set_xmipp_origin (false) : Set Xmipp origin
                        --debug (false) : (Debug only)
    ====== Parameters (alphabetically ordered) ===== 
                      --3d_tomo (false) : Simulate 3D subtomograms using a STAR file?
                            --ang (91.) : Cut out a small part of the helix within this angle (in degrees)
                          --angpix (1.) : Pixel size (in Angstroms)
                      --bimodal (false) : Do bimodal searches of tilt and psi angles in 3D helical reconstruction?
                              --bin (1) : Binning factor used in manual segment picking
                          --boxdim (-1) : Box size (in pixels)
                   --center_pdb (false) : Translate all atoms in the original PDB to the center of mass of this molecule?
                   --ctf_fom_min (-999) : Minimum figure-of-merit - threshold used in removing micrographs with bad CTF
              --cyl_inner_diameter (-1) : Inner diameter of the cylindrical mask (in Angstroms)
              --cyl_outer_diameter (-1) : Outer diameter of the cylindrical mask (in Angstroms)
                    --df_min (-999999.) : Minimum defocus (in Angstroms)
                     --df_max (999999.) : Maximum defocus (in Angstroms)
                 --EPA_lowest_res (999) : Lowest EPA resolution (in Angstroms) - threshold used in removing micrographs with bad CTF
                          --i (file.in) : Input file
                       --i1 (file01.in) : Input file #1
                       --i2 (file02.in) : Input file #2
            --i_root (_rootnameIn.star) : Rootname of input files
         --i1_root (_rootnameIn01.star) : Rootname #1 of input files
         --i2_root (_rootnameIn02.star) : Rootname #2 of input files
      --ignore_helical_symmetry (false) : Ignore helical symmetry in 3D reconstruction?
                           --nr_asu (1) : Number of helical asymmetrical units
                     --nr_outfiles (10) : Number of output files
                     --nr_subunits (-1) : Number of helical subunits
                        --nr_tubes (-1) : Number of helical tubes
                         --o (file.out) : Output file
           --o_root (_rootnameOut.star) : Rootname of output files
                        --polar (false) : Construct a 3D reference for helical reconstruction with polarity along Z axis?
                    --psi_max_dev (15.) : Maximum deviation of psi angles allowed (away from psi prior)
                     --random_seed (-1) : Random seed (set to system time if negative)
                            --rise (-1) : Helical rise (in Angstroms)
                    --rise_inistep (-1) : Initial step of helical rise search (in Angstroms)
                        --rise_min (-1) : Minimum helical rise (in Angstroms)
                        --rise_max (-1) : Maximum helical rise (in Angstroms)
               --seam_nr_filaments (-1) : Number of filaments in a helix with seam (>= 2)
                   --search_sym (false) : Perform local searches of helical symmetry in 3D reconstruction?
                     --segments (false) : Cut helical tubes into segments?
                    --sigma_offset (5.) : Sigma of translational offsets (in pixels)
                       --sigma_psi (5.) : Sigma of psi angles (in degrees)
                      --sigma_tilt (5.) : Sigma of tilt angles (in degrees)
              --sphere_percentage (0.9) : Diameter of spherical mask divided by the box size (0.10~0.90 or 0.01~0.99)
                --subunit_diameter (-1) : Diameter of helical subunits (in Angstroms)
                           --sym_Cn (1) : Rotational symmetry Cn
                   --tilt_max_dev (15.) : Maximum deviation of tilt angles allowed (away from +90 degrees)
                --topbottom_ratio (0.5) : Top-bottom width ratio for construction of polarised helical reference
                           --twist (-1) : Helical twist (in degrees, + for right-handedness)
                   --twist_inistep (-1) : Initial step of helical twist search (in degrees)
                       --twist_min (-1) : Minimum helical twist (in degrees, + for right-handedness)
                       --twist_max (-1) : Maximum helical twist (in degrees, + for right-handedness)
                         --verb (false) : Detailed screen output?
                     --white_noise (1.) : Standard deviation of added white Gaussian noise
                           --width (5.) : Width of cosine soft edge (in pixels)
                          --xdim (4096) : Dimension X (in pixels) of the micrographs
                          --ydim (4096) : Dimension Y (in pixels) of the micrographs
                   --z_percentage (0.3) : Percentage of cropped length (along Z axis, 0.1~0.9)
                              --version : Print RELION version and exit

``relion_motion_refine``
-------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input STAR file
                                    --o : Output directory, e.g. MotionFit/job041/
                                    --f : Input STAR file with the FSC of the reference (usually from PostProcess)
                                --m1 () : Reference map, half 1
                                --m2 () : Reference map, half 2
                      --angpix_ref (-1) : Pixel size of the reference map
                              --mask () : Reference mask
                              --pad (2) : Padding factor
                      --first_frame (1) : First move frame to process
                      --last_frame (-1) : Last movie frame to process (default is all)
           --only_do_unfinished (false) : Skip those steps for which output files already exist.
                             --verb (1) : Verbosity
    ====== Motion fit options (basic) ===== 
                           --fdose (-1) : Electron dose per frame (in e^-/A^2)
                          --s_vel (0.5) : Velocity sigma [Angst/dose]
                       --s_div (5000.0) : Divergence sigma [Angst]
                          --s_acc (2.0) : Acceleration sigma [Angst/dose]
                       --params_file () : File containing s_vel, s_div and s_acc (overrides command line parameters)
                      --only_group (-1) : Only align micrographs containing particles from this optics group (negative means off)
                         --diag (false) : Write out diagnostic data
    ====== Motion fit options (advanced) ===== 
                         --cc_pad (1.0) : Cross-correlation Fourier-padding
                        --dmg_a ( 3.40) : Damage model, parameter a
                        --dmg_b (-1.06) :                         b
                        --dmg_c (-0.54) :                         c
                    --max_iters (10000) : Maximum number of iterations
                           --eps (1e-5) : Terminate optimization after gradient length falls below this value
                    --no_whiten (false) : Do not whiten the noise spectrum
                   --unreg_glob (false) : Do not regularize global component of motion
                     --glob_off (false) : Compute initial per-particle offsets
                    --glob_off_max (10) : Maximum per-particle offset range [Pixels]
              --absolute_params (false) : Do not scale input motion parameters by dose
                    --debug_opt (false) : Write optimization debugging info
                           --gi (false) : Initialize with global trajectories instead of loading them from metadata file
                   --sq_exp_ker (false) : Use a square-exponential kernel instead of an exponential one
                          --max_ed (-1) : Maximum number of eigendeformations
                      --out_cut (false) : Do not consider frequencies beyond the 0.143-FSC threshold for alignment
    ====== Parameter estimation ===== 
                      --params2 (false) : Estimate 2 parameters instead of motion
                      --params3 (false) : Estimate 3 parameters instead of motion
                     --align_frac (0.5) : Fraction of pixels to be used for alignment
                      --eval_frac (0.5) : Fraction of pixels to be used for evaluation
                         --min_p (1000) : Minimum number of particles on which to estimate the parameters
                       --par_group (-1) : Estimate parameters for this optics group only (negative means all)
                        --s_vel_0 (0.6) : Initial s_vel
                      --s_div_0 (10000) : Initial s_div
                          --s_acc_0 (3) : Initial s_acc
                       --in_step (3000) : Initial step size in s_div
                            --conv (30) : Abort when simplex diameter falls below this
                      --par_iters (100) : Max. number of iterations
                       --mot_range (50) : Limit allowed motion range [Px]
                            --seed (23) : Random seed for micrograph selection
    ====== Combine frames options ===== 
               --combine_frames (false) : Combine movie frames into polished particles.
                           --scale (-1) : Re-scale the particles to this size (by default read from particles star file)
                          --window (-1) : Re-window the particles to this size (in movie-pixels; by default read from particles star file)
                            --crop (-1) : Crop the scaled particles to this size after CTF pre-multiplication
                 --ctf_multiply (false) : Premultiply by CTF.
                    --bfac_minfreq (20) : Min. frequency used in B-factor fit [Angst]
                    --bfac_maxfreq (-1) : Max. frequency used in B-factor fit [Angst]
                          --bfactors () : A .star file with external B/k-factors
                 --diag_bfactor (false) : Write out B/k-factor diagnostic data
                            --suffix () : Add this suffix to shiny MRCS and STAR files
                     --recenter (false) : Re-center particle according to rlnOriginX/Y in --reextract_data_star STAR file
                      --recenter_x (0.) : X-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --recenter_y (0.) : Y-coordinate (in pixel inside the reference) to recenter re-extracted data on
                      --recenter_z (0.) : Z-coordinate (in pixel inside the reference) to recenter re-extracted data on
    ====== Computational options ===== 
                                --j (1) : Number of (OMP) threads
                           --min_MG (0) : First micrograph index
                          --max_MG (-1) : Last micrograph index (default is to process all)
                          --sbs (false) : Load movies slice-by-slice to save memory (slower)
    ====== Expert options ===== 
                             --corr_mic : List of uncorrected micrographs (e.g. corrected_micrographs.star)
                --find_shortest (false) : Load only as many frames as are present in all movies.
                        --debug (false) : Write debugging data
                             --mps (-1) : Pixel size of input movies (Angst/pix)
                             --cps (-1) : Pixel size of particle coordinates in star-file (Angst/pix)
                             --hot (-1) : Clip hot pixels to this max. value (-1 = off, TIFF only)
                    --debug_mov (false) : Write debugging data for movie loading
                     --mov_toReplace () : Replace this string in micrograph names...
                     --mov_replaceBy () : ..by this one
                  --eer_upsampling (-1) : EER upsampling (1 = 4K or 2 = 8K)
                    --eer_grouping (-1) : EER grouping
                              --version : Print RELION version and exit

``relion_pipeliner``
---------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Check job completion options ===== 
         --check_job_completion (false) : Use this flag to only check whether running jobs have completed
    ====== Add scheduled jobs options ===== 
                    --addJobFromStar () : Add a job with the type and options as in this job.star to the pipeline
                            --addJob () : Add a job of this type to the pipeline
                     --addJobOptions () : Options for this job (either through --addJobFromStar or --addJob)
                       --setJobAlias () : Set an alias to this job
    ====== Run scheduled jobs options ===== 
                           --RunJobs () : Run these jobs
                          --schedule () : Name of the scheduler for running the scheduled jobs
               --overwrite_jobs (false) : Use this flag to overwrite existing jobs, instead of continuing them
                           --repeat (1) : Run the scheduled jobs this many times
                         --min_wait (0) : Wait at least this many minutes between each repeat
                  --min_wait_before (0) : Wait this many minutes before starting the running the first job
                  --sec_wait_after (10) : Wait this many seconds after a process finishes (workaround for slow IO)
    ====== Expert options ===== 
                   --pipeline (default) : Name of the pipeline
                    --gentle_clean (-1) : Gentle clean this job
                     --harsh_clean (-1) : Harsh clean this job
                              --version : Print RELION version and exit

``relion_star_datablock_ctfdat``
---------------------------------------------------------------------------

.. code-block:: text

     === Usage: === 
     /relion_star_datablock_ctfdat <xmippctfdatfile> 
 
     === Purpose: === 
     This (bash) script generates the STAR datablock for all images in an xmipp-format CTFDAT file
     Note that the sign for XMIPP's defocusU, defocusV and Q0 values is reversed 
 
     === Example: ===
     /relion_star_datablock_ctfdat all_images.ctfdat 

``relion_import``
------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input (wildcard) filename
                                 --odir : Output directory (e.g. "Import/job001/"
                                --ofile : Output file name (e.g. "movies.star"
                    --do_movies (false) : Import movies
               --do_micrographs (false) : Import micrographs
               --do_coordinates (false) : Import coordinates
                  --do_halfmaps (false) : Import unfiltered half maps
                 --do_particles (false) : Import particle STAR files
       --particles_optics_group_name () : Rename optics group for all imported particles (e.g. "opticsGroupLMBjan2019"
                     --do_other (false) : Import anything else
    ====== Specific options for movies or micrographs ===== 
      --optics_group_name (opticsGroup1) : Name for this optics group
                  --optics_group_mtf () : Name for this optics group's MTF
                         --angpix (1.0) : Pixel size (Angstrom)
                             --kV (300) : Voltage (kV)
                             --Cs (2.7) : Spherical aberration (mm)
                             --Q0 (0.1) : Amplitude contrast
                     --beamtilt_x (0.0) : Beam tilt (X; mrad)
                     --beamtilt_y (0.0) : Beam tilt (Y; mrad)
                     --continue (false) : Continue and old run, add more files to the same import directory
                              --version : Print RELION version and exit

``relion_scheduler``
---------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                             --schedule : Directory name of the schedule
                              --copy () : Make a copy of the schedule into this directory
    ====== Add elements to the schedule ===== 
                               --add () : Specify category of element to add to the schedule (variable, operator, job, edge or fork)
                              --type () : Specify type of that element to add to the schedule
                                 --i () : Specify input to the element 
                                --i2 () : Specify 2nd input to the element 
                              --bool () : Name of boolean variable (for forks)
                                 --o () : Specify output of the element 
                                --o2 () : Specify 2nd output of the element 
                              --name () : Name of the variable or job to be added
                             --value () : Value of the variable to be added
                    --original_value () : Original value of the variable to be added
                              --mode () : Mode (for jobs): new, overwrite or continue
    ====== Set values of variables in the schedule ===== 
                        --reset (false) : Reset all variables to their original values
                        --abort (false) : Abort a schedule that is running
                           --set_var () : Name of a variable to set (using also the --value argument)
                      --set_job_mode () : Name of a job whose mode to set (using also the --value argument)
                  --set_current_node () : Name of a node to which to set current_node
    ====== Run the scheduler within a pipeline ===== 
                          --run (false) : Run the scheduler
                             --verb (1) : Running verbosity: 0, 1, 2 or 3)
               --run_pipeline (default) : Name of the pipeline in which to run this schedule
                              --version : Print RELION version and exit

     Different ways of using this program: 

     ++ Add a variable (of type float, bool or file): 
        --schedule test --add variable --name iter --value 0
        --schedule test --add variable --name is_finished --value False
        --schedule test --add variable --name initial_model --value map.mrc

     ++ Add an operator node (of type float, bool or file): 
        --schedule test --add operator --type float=plus --i iter --i2 iter_step --o iter
        --schedule test --add operator --type float=plus --i iter --i2 1 --o iter
        --schedule test --add operator --type touch_file --i initial_model
        --schedule test --add operator --type bool=gt --i iter --i2 10 --o is_finished
        --schedule test --add operator --type bool=file_exists --i initial_model --o is_finished

     ++ Add a job node: 
        --schedule test --add job --i my_import --mode continue/new/overwrite
        --schedule test --add job --i exit

     ++ Add an edge: 
        --schedule test --add edge --i inputnodename --o outputnodename

     ++ Add a fork: 
        --schedule test --add fork --i inputnodename --bool boolvar --o outputnodename --o2 outputnodename_if_false
    TODO: add information about setting variables etc too!


``relion_autopick_mpi``
------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Micrograph STAR file OR filenames from which to autopick particles, e.g. "Micrographs/*.mrc"
                  --pickname (autopick) : Rootname for coordinate STAR files
                     --odir (AutoPick/) : Output directory for coordinate files (default is to store next to micrographs)
                           --angpix (1) : Pixel size of the micrographs in Angstroms
               --particle_diameter (-1) : Diameter of the circular mask that will be applied to the experimental images (in Angstroms, default=automatic)
             --shrink_particle_mask (2) : Shrink the particle mask by this many pixels (to detect Einstein-from-noise classes)
          --outlier_removal_zscore (8.) : Remove pixels that are this many sigma away from the mean
               --write_fom_maps (false) : Write calculated probability-ratio maps to disc (for re-reading in subsequent runs)
                 --no_fom_limit (false) : Ignore default maximum limit of 30 fom maps being written
                --read_fom_maps (false) : Skip probability calculations, re-read precalculated maps from disc
          --skip_optimise_scale (false) : Skip the optimisation of the micrograph scale for better prime factors in the FFTs. This runs slower, but at exactly the requested resolution.
           --only_do_unfinished (false) : Only autopick those micrographs for which the coordinate file does not yet exist
                          --gpu (false) : Use GPU acceleration when availiable
    ====== References options ===== 
                               --ref () : STAR file with the reference names, or an MRC stack with all references, or "gauss" for blob-picking
                      --angpix_ref (-1) : Pixel size of the references in Angstroms (default is same as micrographs)
                       --invert (false) : Density in micrograph is inverted w.r.t. density in template
                             --ang (10) : Angular sampling (in degrees); use 360 for no rotations
                         --lowpass (-1) : Lowpass filter in Angstroms for the references (prevent Einstein-from-noise!)
                        --highpass (-1) : Highpass filter in Angstroms for the micrographs
                          --ctf (false) : Perform CTF correction on the references?
        --ctf_intact_first_peak (false) : Ignore CTFs until their first peak?
                      --gauss_max (0.1) : Value of the peak in the Gaussian blob reference
                    --healpix_order (1) : Healpix order for projecting a 3D reference (hp0=60deg; hp1=30deg; hp2=15deg)
                             --sym (C1) : Symmetry point group for a 3D reference
    ====== Laplacian-of-Gaussian options ===== 
                          --LoG (false) : Use Laplacian-of-Gaussian filter-based picking, instead of template matching
                    --LoG_diam_min (-1) : Smallest particle diameter (in Angstroms) for blob-detection by Laplacian-of-Gaussian filter
                    --LoG_diam_max (-1) : Largest particle diameter (in Angstroms) for blob-detection by Laplacian-of-Gaussian filter
                  --LoG_neighbour (100) : Avoid neighbouring particles within (the detected diameter + the minimum diameter) times this percent
                   --Log_invert (false) : Use this option if the particles are white instead of black
            --LoG_adjust_threshold (0.) : Use this option to adjust the picking threshold: positive for less particles, negative for more
          --LoG_upper_threshold (99999) : Use this option to set the upper limit of the picking threshold
                  --LoG_use_ctf (false) : Use CTF until the first peak in Laplacian-of-Gaussian picker
    ====== Helix options ===== 
                        --helix (false) : Are the references 2D helical segments? If so, in-plane rotation angles (psi) are estimated for the references.
        --helical_tube_kappa_max (0.25) : Factor of maximum curvature relative to that of a circle
      --helical_tube_outer_diameter (-1) : Tube diameter in Angstroms
         --helical_tube_length_min (-1) : Minimum tube length in Angstroms
                      --amyloid (false) : Activate specific algorithm for amyloid picking?
            ----max_diam_local_avg (-1) : Maximum diameter to calculate local average density in Angstroms
    ====== Peak-search options ===== 
                     --threshold (0.25) : Fraction of expected probability ratio in order to consider peaks?
                    --min_distance (-1) : Minimum distance (in A) between any two particles (default is half the box size)
                --max_stddev_noise (-1) : Maximum standard deviation in the noise area to use for picking peaks (default is no maximum)
                --min_avg_noise (-999.) : Minimum average in the noise area to use for picking peaks (default is no minimum)
                        --skip_side (0) : Keep this many extra pixels (apart from particle_size/2) away from the edge of the micrograph 
    ====== Expert options ===== 
                             --verb (1) : Verbosity
                              --pad (2) : Padding factor for Fourier transforms
                      --random_seed (1) : Number for the random seed generator
                         --shrink (1.0) : Reduce micrograph to this fraction size, during correlation calc (saves memory and time)
                  --Log_max_search (5.) : Maximum diameter in LoG-picking multi-scale approach is this many times the min/max diameter
                        --extra_pad (0) : Number of pixels for additional padding of the original micrograph
                              --version : Print RELION version and exit

``relion_convert_to_tiff``
---------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General Options ===== 
                                    --i : Input movie to be compressed (an MRC/MRCS file or a list of movies as .star or .lst)
                               --o (./) : Directory for output TIFF files
           --only_do_unfinished (false) : Only process non-converted movies.
                                --j (1) : Number of threads (useful only for --estimate_gain)
                              --gain () : Estimated gain map and its reliablity map (read)
                          --thresh (50) : Number of success needed to consider a pixel reliable
                --estimate_gain (false) : Estimate gain
    ====== EER rendering options ===== 
                    --eer_grouping (40) : EER grouping
                   --eer_upsampling (1) : EER upsampling (1 = 4K or 2 = 8K)
                        --short (false) : use unsigned short instead of signed byte for EER rendering
    ====== TIFF writing options ===== 
                   --compression (auto) : compression type (none, auto, deflate (= zip), lzw)
                    --deflate_level (6) : deflate level. 1 (fast) to 9 (slowest but best compression)
                 --ignore_error (false) : Don't die on un-expected defect pixels (can be dangerous)
                 --line_by_line (false) : Use one strip per row
                              --version : Print RELION version and exit

``relion_postprocess``
-----------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input name of half1, e.g. run_half1_class001_unfil.mrc
                                --i2 () : Input name of half2, (default replaces half1 from --i with half2)
                      --o (postprocess) : Output rootname
                          --angpix (-1) : Pixel size in Angstroms
                    --half_maps (false) : Write post-processed half maps for validation
                     --mtf_angpix (-1.) : Pixel size in the original micrographs/movies (in Angstroms)
                       --molweight (-1) : Molecular weight (in kDa) of ordered protein mass
    ====== Masking options ===== 
                    --auto_mask (false) : Perform automated masking, based on a density threshold
             --inimask_threshold (0.02) : Density at which to threshold the map for the initial seed mask
                  --extend_inimask (3.) : Number of pixels to extend the initial seed mask
                 --width_mask_edge (6.) : Width for the raised cosine soft mask edge (in pixels)
                              --mask () : Filename of a user-provided mask (1=protein, 0=solvent, all values in range [0,1])
                   --force_mask (false) : Use the mask even when the masked resolution is worse than the unmasked resolution
    ====== Sharpening options ===== 
                               --mtf () : User-provided STAR-file with the MTF-curve of the detector
                    --auto_bfac (false) : Perform automated B-factor determination (Rosenthal and Henderson, 2003)
                   --autob_lowres (10.) : Lowest resolution (in A) to include in fitting of the B-factor
                   --autob_highres (0.) : Highest resolution (in A) to include in fitting of the B-factor
                      --adhoc_bfac (0.) : User-provided B-factor (in A^2) for map sharpening, e.g. -400
    ====== Filtering options ===== 
           --skip_fsc_weighting (false) : Do not use FSC-weighting (Rosenthal and Henderson, 2003) in the sharpening process
                         --low_pass (0) : Resolution (in Angstroms) at which to low-pass filter the final map (0: disable, negative: resolution at FSC=0.143)
    ====== Local-resolution options ===== 
                       --locres (false) : Perform local resolution estimation
                --locres_sampling (25.) : Sampling rate (in Angstroms) with which to sample the local-resolution map
                  --locres_maskrad (-1) : Radius (in A) of spherical mask for local-resolution map (default = 0.5*sampling)
                 --locres_edgwidth (-1) : Width of soft edge (in A) on masks for local-resolution map (default = sampling)
            --locres_randomize_at (25.) : Randomize phases from this resolution (in A)
                  --locres_minres (50.) : Lowest local resolution allowed (in A)
    ====== Expert options ===== 
                    --ampl_corr (false) : Perform amplitude correlation and DPR, also re-normalize amplitudes for non-uniform angular distributions
               --randomize_at_fsc (0.8) : Randomize phases from the resolution where FSC drops below this value
                  --randomize_at_A (-1) : Randomize phases from this resolution (in A) onwards (if positive)
                --filter_edge_width (2) : Width of the raised cosine on the low-pass filter edge (in resolution shells)
                             --verb (1) : Verbosity
                      --random_seed (0) : Seed for random number generator (negative value for truly random)
                              --version : Print RELION version and exit

``relion_tiltpair_plot``
-------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --u : Input STAR file with untilted particles
                                    --t : Input STAR file with tilted particles
                     --o (tiltpair.eps) : Output EPS file 
                             --sym (C1) : Symmetry point group
                        --exp_tilt (0.) : Choose symmetry operator that gives tilt angle closest to this value
                        --exp_beta (0.) : Choose symmetry operator that gives beta angle closest to this value
                 --dist_from_alpha (0.) : Direction (alpha angle) of tilt axis from which to calculate distance
                  --dist_from_tilt (0.) : Tilt angle from which to calculate distance
                       --max_tilt (90.) : Maximum tilt angle to plot in the EPS file
                      --spot_radius (3) : Radius in pixels of the spots in the tiltpair plot
                              --version : Print RELION version and exit

``relion_particle_reposition``
-------------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== Options ===== 
                                    --i : Input STAR file with rlnMicrographName's 
                                  --opt : Optimiser STAR file with the 2D classes or 3D maps to be repositioned
                                 --o () : Output rootname, to be added to input micrograph names
                              --odir () : Output directory (default is same as input micrographs directory
                              --data () : Data STAR file with selected particles (default is to use all particles)
                     --background (0.1) : The fraction of micrograph background noise in the output micrograph
                       --invert (false) : Invert the contrast in the references?
                          --ctf (false) : Apply CTF for each particle to the references?
                     --norm_radius (-1) : Radius of the circle used for background normalisation (in pixels)
                     --subtract (false) : Subtract repositioned micrographs from the input ones?
                              --version : Print RELION version and exit

``relion_particle_FCC``
------------------------------------------------------------------

.. code-block:: text

    +++ RELION: command line arguments (with defaults for optional ones between parantheses) +++
    ====== General options ===== 
                                    --i : Input particle *.star file
                                    --f : Input STAR file with the FSC of the reference (usually from PostProcess)
                                    --o : Output path
                                --m1 () : Reference map, half 1
                                --m2 () : Reference map, half 2
                      --angpix_ref (-1) : Pixel size of the reference map
                              --mask () : Reference mask
                              --pad (2) : Padding factor
                         --min_freq (0) : Min. image frequency [px]
                --opposite_half (false) : Correlate with opposite half-set
                  --predict_CTF (false) : Modulate prediction by CTF
                           --min_MG (0) : First micrograph index
                          --max_MG (-1) : Last micrograph index (default is to process all)
                                --j (1) : Number of threads
                              --version : Print RELION version and exit

