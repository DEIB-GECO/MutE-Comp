MaxMIF=/mnt/Data/_ThesisEX/programs/MaxMIF
project="/mnt/Data/_ThesisEX/RAS-CRC_analysis"

source <(grep = ../../data.ini)

input=$project/${maxmif___all_noHypoHyper___in}
output=$project/${maxmif___all_noHypoHyper___out_dir}

input_RAS=$project/${maxmif___all_noHypoHyper_RAS___in}
output_RAS=$project/${maxmif___all_noHypoHyper_RAS___out_dir}

input_nonRAS=$project/${maxmif___all_noHypoHyper_nonRAS___in}
output_nonRAS=$project/${maxmif___all_noHypoHyper_nonRAS___out_dir}

cd $MaxMIF

echo $input
$MaxMIF/MaxMIF $input all_noHypoHyper
mv ./Output/* $output
echo RAS
$MaxMIF/MaxMIF $input_RAS all_noHypoHyper_RAS
mv ./Output/* $output_RAS
echo nonRAS
$MaxMIF/MaxMIF $input_nonRAS all_noHypoHyper_nonRAS
mv ./Output/* $output_nonRAS
