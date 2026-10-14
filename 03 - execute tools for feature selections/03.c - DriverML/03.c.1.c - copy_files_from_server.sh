server="bellomo@131.175.120.88"

source <(grep = ../../data.ini)

output=../../${driverml___all_noHypoHyper___out}

output_RAS=../../${driverml___all_noHypoHyper_RAS___out}

output_nonRAS=../../${driverml___all_noHypoHyper_nonRAS___out}

echo "copy all data"
scp $server:~/DriverML/all_noHypoHyper $output

echo "copy RAS data"
scp $server:~/DriverML/all_noHypoHyper_RAS $output_RAS

echo "copy nonRAS data"
scp $server:~/DriverML/all_noHypoHyper_nonRAS $output_nonRAS
