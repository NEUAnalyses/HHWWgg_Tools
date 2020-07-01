for filename in crab_projects/*; do
  echo $filename
  crab status -d $filename
done
