for filename in crab_projects/*; do
  echo $filename
  crab kill -d $filename
done
