for filename in crab_projects/*; do
  echo $filename
  crab resubmit -d $filename
done
