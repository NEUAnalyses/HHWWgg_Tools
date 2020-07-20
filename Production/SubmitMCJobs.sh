#!/bin/bash

# For each MC configuration, submit a crab job 
# This is currently only configured for fragments created in CMSSW_9_3_9_patch1 

#unset jsonkeys 
jsonkeys=(step events jobs_jobsize fragment_directory pileup localGridpack Campaign Year dryRun)
 
i=$((0)) # jsonkey 
for jsonkey in "${jsonkeys[@]}" 
do
    :
    #echo "i = $i"
    thisconfigname=config_
    thisconfigname+=$i
    unset thisconfigname
    thisconfigname=()
    for keyitem in `jq ".[] | .$jsonkey" MC_Configs.json `
    do
        :
        # echo "key item = $keyitem" 
        keyitem=$keyitem
        eval thisconfigname+=($keyitem)
        #echo "this config elements = ${thisconfigname[@]}"
    done

    name=''
    name+=saved_array
    name+=_$i
    unset $name 
    declare -a $name 
    #eval `unset $name`
    #eval `declare -a $name`

    j=$((0)) #keyitem 
    for el in "${thisconfigname[@]}"
    do 
        :
        #echo "el = $el"
        #echo "j = $j"
        eval $name[$j]=$el

        j=$((j+1))
    done

    i=$((i+1))
done

#echo "saved_array = ${saved_array[@]}"
echo "MC Configuration parameters:"
echo "  Steps: ${saved_array_0[@]}" # step
echo "  Events: ${saved_array_1[@]}" # events
echo "  Jobs_jobsize= ${saved_array_2[@]}" # jobs_jobsize 
echo "  Fragment_Directory = ${saved_array_3[@]}" # fragment_directory
echo "  Pileup = ${saved_array_4[@]}" # pileup 
echo "  LocalGridpack  = ${saved_array_5[@]}" # 0) Don't need to add gridpack to sandbox. 1) Need to add to sandbox and change path to /srv/<gridpack> in pythia fragment
echo "  Campaign = ${saved_array_6[@]}" # Campaign name 
echo "  Year = ${saved_array_7[@]}" # Year 
echo "  dryRun  = ${saved_array_8[@]}" # dryRun 
# Number of crab configurations
num_configs=${#saved_array_0[@]}
max_el=$((num_configs - 1)) # because arrays are zero indexed 

# Submit crab job for each MC configuration 
for i in $(seq 0 $max_el) 
do 
    :
    echo "Submitting crab job $i"
    cd /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production
    source /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production/MC_Producer_Setup.sh ${saved_array_0[$i]} ${saved_array_1[$i]} ${saved_array_2[$i]} ${saved_array_3[$i]} ${saved_array_4[$i]} ${saved_array_5[$i]} ${saved_array_6[$i]} ${saved_array_7[@]} ${saved_array_8[@]}

done 

end_script
