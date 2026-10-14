Netsig="/mnt/Data/_ThesisEX/programs/netsig"

source <(grep = ../../data.ini)

input=../../${netsig___all_noHypoHyper___in}
output=../../${netsig___all_noHypoHyper___out_dir}

input_RAS=../../${netsig___all_noHypoHyper_RAS___in}
output_RAS=../../${netsig___all_noHypoHyper_RAS___out_dir}

input_nonRAS=../../${netsig___all_noHypoHyper_nonRAS___in}
output_nonRAS=../../${netsig___all_noHypoHyper_nonRAS___out_dir}

echo all
$Netsig/runNetwork -p $input -j 1 -J 1 -n $Netsig/input/network.sym -N all_noHypoHyper -i 1000 -P 3 -g -o $output
echo RAS
$Netsig/runNetwork -p $input_RAS -j 1 -J 1 -n $Netsig/input/network.sym -N all_noHypoHyper_RAS -i 1000 -P 3 -g -o $output_RAS
echo nonRAS
$Netsig/runNetwork -p $input_nonRAS -j 1 -J 1 -n $Netsig/input/network.sym -N all_noHypoHyper_nonRAS -i 1000 -P 3 -g -o $output_nonRAS
