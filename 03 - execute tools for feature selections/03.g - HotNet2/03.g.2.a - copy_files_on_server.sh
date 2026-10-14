server="bellomo@131.175.120.88"

source <(grep = ../../data.ini)

freq=../../${hotnet2___all_noHypoHyper___in_dir}mutation_frequencies.csv
mutsigP=../../${hotnet2___all_noHypoHyper___in_dir}mutsig_pvalues.csv
mutsigQ=../../${hotnet2___all_noHypoHyper___in_dir}mutsig_qvalues.csv

freq_RAS=../../${hotnet2___all_noHypoHyper_RAS___in_dir}mutation_frequencies.csv
mutsigP_RAS=../../${hotnet2___all_noHypoHyper_RAS___in_dir}mutsig_pvalues.csv
mutsigQ_RAS=../../${hotnet2___all_noHypoHyper_RAS___in_dir}mutsig_qvalues.csv

freq_nonRAS=../../${hotnet2___all_noHypoHyper_nonRAS___in_dir}mutation_frequencies.csv
mutsigP_nonRAS=../../${hotnet2___all_noHypoHyper_nonRAS___in_dir}mutsig_pvalues.csv
mutsigQ_nonRAS=../../${hotnet2___all_noHypoHyper_nonRAS___in_dir}mutsig_qvalues.csv

echo "copy all data"
scp $freq $server:~/data/hotnet2/all_noHypoHyper/input/$(basename "$freq")
scp $mutsigP $server:~/data/hotnet2/all_noHypoHyper/input/$(basename "$mutsigP")
scp $mutsigQ $server:~/data/hotnet2/all_noHypoHyper/input/$(basename "$mutsigQ")

echo "copy RAS data"
scp $freq_RAS $server:~/data/hotnet2/all_noHypoHyper_RAS/input/$(basename "$freq_RAS")
scp $mutsigP_RAS $server:~/data/hotnet2/all_noHypoHyper_RAS/input/$(basename "$mutsigP_RAS")
scp $mutsigQ_RAS $server:~/data/hotnet2/all_noHypoHyper_RAS/input/$(basename "$mutsigQ_RAS")

echo "copy nonRAS data"
scp $freq_nonRAS $server:~/data/hotnet2/all_noHypoHyper_nonRAS/input/$(basename "$freq_nonRAS")
scp $mutsigP_nonRAS $server:~/data/hotnet2/all_noHypoHyper_nonRAS/input/$(basename "$mutsigP_nonRAS")
scp $mutsigQ_nonRAS $server:~/data/hotnet2/all_noHypoHyper_nonRAS/input/$(basename "$mutsigQ_nonRAS")

echo "copy runHotNet2 script"
scp "04.g.1.b - server_call_hotnet2.sh" $server:~/
