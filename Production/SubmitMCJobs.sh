#!/bin/bash

# For each MC configuration, submit a crab job 
# This is currently only configured for fragments created in CMSSW_9_3_9_patch1 

#unset jsonkeys 
jsonkeys=(step events jobs_jobsize fragment_directory pileup)
 
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
        #echo "key item = $keyitem" 
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

# i=$((0)) # config number  
# for config in "${saved_array_0[@]}"
# do
#     :
#     unset $config # Make sure array name is free in memory 
#     declare -A $config # associative array
#     #echo "config = $config"
#     eval $config["filename"]=${saved_array_1[$i]}
#     eval $config["step"]=${saved_array_2[$i]}
#     eval $config["events"]=${saved_array_3[$i]}
#     eval $config["jobs"]=${saved_array_4[$i]}
#     #eval `$config+=(["filename"]=saved_array_1[$i] ["step"]=saved_array_2[$i] ["events"]=saved_array_3[$i] ["jobs"]=saved_array_4[$i] )`
#     i=$((i+1))
# done

# Number of crab configurations
num_configs=${#saved_array_0[@]}
max_el=$((num_configs - 1)) # because arrays are zero indexed 

# Submit crab job for each MC configuration 
for i in $(seq 0 $max_el) 
do 
    :
    echo "Submitting crab job $i"
    cd /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production
    source /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production/MC_Producer_Setup.sh ${saved_array_0[$i]} ${saved_array_1[$i]} ${saved_array_2[$i]} ${saved_array_3[$i]} ${saved_array_4[$i]}

done 

end_script
