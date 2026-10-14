MUFFINN=/mnt/Data/_ThesisEX/programs/MUFFINN/MUFFINN
project="/mnt/Data/_ThesisEX/RAS-CRC_analysis"

source <(grep = ../../data.ini)

input=$project/${muffinn___all_noHypoHyper___in}
output=$project/${muffinn___all_noHypoHyper___out_dir}

input_RAS=$project/${muffinn___all_noHypoHyper_RAS___in}
output_RAS=$project/${muffinn___all_noHypoHyper_RAS___out_dir}

input_nonRAS=$project/${muffinn___all_noHypoHyper_nonRAS___in}
output_nonRAS=$project/${muffinn___all_noHypoHyper_nonRAS___out_dir}

cd $MUFFINN

echo all
perl $MUFFINN/muffinn.pl $input all_noHypoHyper
mv ./output/* $output

echo RAS
perl $MUFFINN/muffinn.pl $input_RAS all_noHypoHyper_RAS
mv ./output/* $output_RAS

echo nonRAS
perl $MUFFINN/muffinn.pl $input_nonRAS all_noHypoHyper_nonRAS
mv ./output/* $output_nonRAS
