# Execute on server

DriverML="$HOME/DriverML"
refGenome="$HOME/data/hg19.fa"

input="$HOME/data/all_noHypoHyper_mutations.csv"
input_RAS="$HOME/data/all_noHypoHyper_RAS_mutations.csv"
input_nonRAS="$HOME/data/all_noHypoHyper_nonRAS_mutations.csv"

cd $DriverML

# DO NOT RUN THE THREE RUNS IN PARALLEL FOR THEY WILL USE ALL THE MEMORY AVAILABLE
echo "all"
$DriverML/run.driverml.sh -w $DriverML -i $input -f $refGenome -r $refGenome -o all_noHypoHyper

echo "RAS"
$DriverML/run.driverml.sh -w $DriverML -i $input_RAS -f $refGenome -r $refGenome -o all_noHypoHyper_RAS

echo "nonRAS"
$DriverML/run.driverml.sh -w $DriverML -i $input_nonRAS -f $refGenome -r $refGenome -o all_noHypoHyper_nonRAS

