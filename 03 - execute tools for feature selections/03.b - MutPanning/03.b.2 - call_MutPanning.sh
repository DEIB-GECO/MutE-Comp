# gui command:
# java -Xmx8G -classpath $ff/commons-math3-3.6.1.jar:$ff/jdistlib-0.4.5-bin.jar:$ff MutPanningDesktop

source <(grep = ../../data.ini)  

MutPanning="/mnt/Data/_ThesisEX/programs/MutPanningV2/"
hg19="/mnt/Data/_ThesisEX/Hg19/"

mutations=../../${mutpanning___all_noHypoHyper___in_dir}mutations.maf
samples=../../${mutpanning___all_noHypoHyper___in_dir}samples.txt
output=../../${mutpanning___all_noHypoHyper___out_dir}

mutations_RAS=../../${mutpanning___all_noHypoHyper_RAS___in_dir}mutations.maf
samples_RAS=../../${mutpanning___all_noHypoHyper_RAS___in_dir}samples.txt
output_RAS=../../${mutpanning___all_noHypoHyper_RAS___out_dir}

mutations_nonRAS=../../${mutpanning___all_noHypoHyper_nonRAS___in_dir}mutations.maf
samples_nonRAS=../../${mutpanning___all_noHypoHyper_nonRAS___in_dir}samples.txt
output_nonRAS=../../${mutpanning___all_noHypoHyper_nonRAS___out_dir}

java -Xmx8G -classpath $MutPanning/commons-math3-3.6.1.jar:$MutPanning/jdistlib-0.4.5-bin.jar:$MutPanning MutPanning $output $mutations $samples $hg19
java -Xmx8G -classpath $MutPanning/commons-math3-3.6.1.jar:$MutPanning/jdistlib-0.4.5-bin.jar:$MutPanning MutPanning $output_RAS $mutations_RAS $samples_RAS $hg19
java -Xmx8G -classpath $MutPanning/commons-math3-3.6.1.jar:$MutPanning/jdistlib-0.4.5-bin.jar:$MutPanning MutPanning $output_nonRAS $mutations_nonRAS $samples_nonRAS $hg19
