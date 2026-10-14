server="bellomo@131.175.120.88"

source <(grep = ../../data.ini)

input=../../${driverml___all_noHypoHyper___in}

input_RAS=../../${driverml___all_noHypoHyper_RAS___in}

input_nonRAS=../../${driverml___all_noHypoHyper_nonRAS___in}

echo "copy all data"
scp $input $server:~/data/$(basename "$input")

echo "copy RAS data"
scp $input_RAS $server:~/data/$(basename "$input_RAS")

echo "copy nonRAS data"
scp $input_nonRAS $server:~/data/$(basename "$input_nonRAS")

echo "copy runDriverML script"
scp "04.c.0.b - call_DriverML.sh" $server:~/
