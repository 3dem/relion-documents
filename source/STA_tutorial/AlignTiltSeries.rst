.. _sec_sta_aligntiltseries:

Tilt Series Alignment
=====================

Before tomogram reconstruction, each tilt series must be aligned by tilt series alignment. 
To do this, we can either use IMOD or AreTomo. For the tutorial dataset, we will use IMOD’s fiducial based alignment 
as the raw data contains gold beads as fiducial markers. 
As a general rule, for your own data, it is probably worth trying all of the different methods available in RELION 5 
and later comparing the quality of the tomograms that each produces.
 
Start by selecting the :guitab:`I/O` tab on the :jobtype:`Align tilt-series` job.

:Input tilt series: ExcludeTiltImages/job[Number]/slected_tilt_series.star

On the :guitab:`IMOD` tab:

:Use IMOD's fiducial based alignment?: Yes

:Fiducal diameter (nm): 10

:Use IMOD's patch-tracking for alignment?: No
(For your own data, if you want to use IMOD’s patch tracking select Yes and select No for fiducial based alignment.
You may adjust patch size and overlap to optimise the alignment.)

If you want to run AreTomo instead, select No for both IMOD options. Then on the :guitab:`AreTomo` tab 

:Use AreTomo: Yes

:Expected sample thickness (nm): xx
The ‘Expected sample thickness’ field controls the -AlignZ field in AreTomo which the AreTomo manual defines as: 
*"This function specifies the z height of the temporary volume reconstructed for projection matching as part of the alignment process. 
This value plays an important role in alignment accuracy. This z height should be always smaller than [the desired Z height of the final tomogram]"*.
In other words, if your tomograms are going to be 300nm thick, but the sample within the tomograms is only going to cover the central 150nm, 
then set this value to ~150nm. Note that in some tomograms the sample will not be perfectly in the middle so the value should be increased to account for this. 
We also recommend setting **Correct tilt angle offset? Yes** which corrects any slanting of the sample in tomograms which arise due to sample mounting or milling angle. 
This doesn’t make a big difference in the tutorial dataset, but we have found that it is very useful for in situ data. 
As AreTomo uses GPU(s), you can specify the GPU(s) to use in the final field. If you wish to use multiple GPUs, separate their IDs using a ‘:’. 
For example, if you wish to use GPUS 0, 1, and 2, enter: ‘0:1:2’. 

Run by clicking the :runbutton:`Run!` button. 
You can view the metadata from IMOD or AreTomo in the AlignTiltSeries/job[Number]/external/ directory.


