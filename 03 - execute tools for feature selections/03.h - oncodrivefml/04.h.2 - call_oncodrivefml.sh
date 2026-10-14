source <(grep = ../../data.ini)

input=../../${oncodrivefml___all_noHypoHyper___in_dir}input.csv
regions=../../${oncodrivefml___all_noHypoHyper___in_dir}regions.csv
output=../../${oncodrivefml___all_noHypoHyper___out_dir}


echo "all"
oncodrivefml -i $input -e $regions -o $output -c "./oncodrivefml_config.conf" --signature-correction wx --seed ${seed} --force --cores 4
