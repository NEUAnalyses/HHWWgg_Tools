# Abe Tishelman-Charny
# 5 December 2019 
# The purpose of the script is to save crab status outputs to a file for easy viewing 

#" " >> test_output.txt 

for path in "."/crab_*
do
	crab status -d $path 
	#crab resubmit -d $path 
	# crab status -d $path >> tmp_output.txt 
	# tmp_output.txt >> test_output.txt 
	# rm tmp_output.txt 
done 

# from: Status on the scheduler:        SUBMITTED
# to:  Output dataset:                 /ggF_X450_WWgg_qqlnugg/atishelm-HHWWgg_v1-94X_mc2017-RunIIFall18-v0-atishelm-100000events_wPU_MINIAOD-5f646ecd4e1c7a39ab0ed099ff55ceb9-4d2010f8ba2360fb4de1038d4a1ef29e/USER
