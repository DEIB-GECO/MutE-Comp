# Execute on server

hotnet2="$HOME/hotnet2"
data="$HOME/data/hotnet2"

num_cores=16
num_network_permutations=100
num_heat_permutations=1000

# # in/out heat data

freq=$data/all_noHypoHyper/input/mutation_frequencies.csv
mutsigP=$data/all_noHypoHyper/input/mutsig_pvalues.csv
mutsigQ=$data/all_noHypoHyper/input/mutsig_qvalues.csv

out_freq=$data/all_noHypoHyper/output/heat/mutation_frequencies.json
out_mutsigP=$data/all_noHypoHyper/output/heat/mutsig_pvalues.json
out_mutsigQ=$data/all_noHypoHyper/output/heat/mutsig_qvalues.json

freq_RAS=$data/all_noHypoHyper_RAS/input/mutation_frequencies.csv
mutsigP_RAS=$data/all_noHypoHyper_RAS/input/mutsig_pvalues.csv
mutsigQ_RAS=$data/all_noHypoHyper_RAS/input/mutsig_qvalues.csv

out_freq_RAS=$data/all_noHypoHyper_RAS/output/heat/mutation_frequencies.json
out_mutsigP_RAS=$data/all_noHypoHyper_RAS/output/heat/mutsig_pvalues.json
out_mutsigQ_RAS=$data/all_noHypoHyper_RAS/output/heat/mutsig_qvalues.json

freq_nonRAS=$data/all_noHypoHyper_nonRAS/input/mutation_frequencies.csv
mutsigP_nonRAS=$data/all_noHypoHyper_nonRAS/input/mutsig_pvalues.csv
mutsigQ_nonRAS=$data/all_noHypoHyper_nonRAS/input/mutsig_qvalues.csv

out_freq_nonRAS=$data/all_noHypoHyper_nonRAS/output/heat/mutation_frequencies.json
out_mutsigP_nonRAS=$data/all_noHypoHyper_nonRAS/output/heat/mutsig_pvalues.json
out_mutsigQ_nonRAS=$data/all_noHypoHyper_nonRAS/output/heat/mutsig_qvalues.json

# out network data

out_hinthi2012=$data/networks/hint+hi2012
out_irefindex9=$data/networks/irefindex9
out_multinet=$data/networks/multinet

# out hotnet2

out=$data/all_noHypoHyper/output/results
out_RAS=$data/all_noHypoHyper_RAS/output/results
out_nonRAS=$data/all_noHypoHyper_nonRAS/output/results


# # Create heat files
# echo "CREATE HEAT FILES"

# echo "all freq"
# python2 $hotnet2/makeHeatFile.py scores -hf $freq -o  $out_freq -n  all_noHypoHyper_freq
# echo "all mutsigP"
# python2 $hotnet2/makeHeatFile.py scores -hf $mutsigP -o  $out_mutsigP -n  all_noHypoHyper_mutsigP
# echo "all mutsigQ"
# python2 $hotnet2/makeHeatFile.py scores -hf $mutsigQ -o  $out_mutsigQ -n  all_noHypoHyper_mutsigQ

# echo "RAS freq"
# python2 $hotnet2/makeHeatFile.py scores -hf $freq_RAS -o  $out_freq_RAS -n  all_noHypoHyper_RAS_freq
# echo "RAS mutsigP"
# python2 $hotnet2/makeHeatFile.py scores -hf $mutsigP_RAS -o  $out_mutsigP_RAS -n  all_noHypoHyper_RAS_mutsigP
# echo "RAS mutsigQ"
# python2 $hotnet2/makeHeatFile.py scores -hf $mutsigQ_RAS -o  $out_mutsigQ_RAS -n  all_noHypoHyper_RAS_mutsigQ

# echo "nonRAS freq"
# python2 $hotnet2/makeHeatFile.py scores -hf $freq_nonRAS -o  $out_freq_nonRAS -n  all_noHypoHyper_nonRAS_freq
# echo "nonRAS mutsigP"
# python2 $hotnet2/makeHeatFile.py scores -hf $mutsigP_nonRAS -o  $out_mutsigP_nonRAS -n  all_noHypoHyper_nonRAS_mutsigP
# echo "nonRAS mutsigQ"
# python2 $hotnet2/makeHeatFile.py scores -hf $mutsigQ_nonRAS -o  $out_mutsigQ_nonRAS -n  all_noHypoHyper_nonRAS_mutsigQ

# # Create network data
# echo "CREATE NETWORK DATA"

# echo "hint+hi2012"
# python2 $hotnet2/makeNetworkFiles.py \
#     -e  $hotnet2/paper/data/networks/hint+hi2012/hint+hi2012_edge_list \
#     -i  $hotnet2/paper/data/networks/hint+hi2012/hint+hi2012_index_gene \
#     -nn hint+hi2012 \
#     -p  hint+hi2012 \
#     -b  0.4 \
#     -o  $out_hinthi2012 \
#     -np $num_network_permutations \
#     -c  $num_cores

# echo "iRefIndex9"
# python2 $hotnet2/makeNetworkFiles.py \
#     -e  $hotnet2/paper/data/networks/irefindex9/irefindex9_edge_list \
#     -i  $hotnet2/paper/data/networks/irefindex9/irefindex9_index_gene \
#     -nn irefindex9 \
#     -p  irefindex9 \
#     -b  0.45 \
#     -o  $out_irefindex9 \
#     -np $num_network_permutations \
#     -c  $num_cores

# echo "multinet"
# python2 $hotnet2/makeNetworkFiles.py \
#     -e  $hotnet2/paper/data/networks/multinet/multinet_edge_list \
#     -i  $hotnet2/paper/data/networks/multinet/multinet_index_gene \
#     -nn multinet \
#     -p  multinet \
#     -b  0.5 \
#     -o  $out_multinet \
#     -np $num_network_permutations \
#     -c  $num_cores

# Run HotNet2
echo "RUN HOTNET2"

echo "all"
python2 $hotnet2/HotNet2.py \
    -nf     $out_hinthi2012/hint+hi2012_ppr_0.4.h5 \
            $out_irefindex9/irefindex9_ppr_0.45.h5 \
            $out_multinet/multinet_ppr_0.5.h5 \
    -pnp    $out_hinthi2012/permuted/hint+hi2012_ppr_0.4_10.h5 \
            $out_irefindex9/permuted/irefindex9_ppr_0.45_5.h5 \
            $out_multinet/permuted/multinet_ppr_0.5_5.h5 \
    -hf     $out_freq \
            $out_mutsigQ \
    -np     $num_network_permutations \
    -hp     $num_heat_permutations \
    -o      $out \
    -c      $num_cores

echo "RAS"
python2 $hotnet2/HotNet2.py \
    -nf     $out_hinthi2012/hint+hi2012_ppr_0.4.h5 \
            $out_irefindex9/irefindex9_ppr_0.45.h5 \
            $out_multinet/multinet_ppr_0.5.h5 \
    -pnp    $out_hinthi2012/permuted/hint+hi2012_ppr_0.4_10.h5 \
            $out_irefindex9/permuted/irefindex9_ppr_0.45_5.h5 \
            $out_multinet/permuted/multinet_ppr_0.5_5.h5 \
    -hf     $out_freq_RAS \
            $out_mutsigQ_RAS \
    -np     $num_network_permutations \
    -hp     $num_heat_permutations \
    -o      $out_RAS \
    -c      $num_cores

echo "nonRAS"
python2 $hotnet2/HotNet2.py \
    -nf     $out_hinthi2012/hint+hi2012_ppr_0.4.h5 \
            $out_irefindex9/irefindex9_ppr_0.45.h5 \
            $out_multinet/multinet_ppr_0.5.h5 \
    -pnp    $out_hinthi2012/permuted/hint+hi2012_ppr_0.4_10.h5 \
            $out_irefindex9/permuted/irefindex9_ppr_0.45_5.h5 \
            $out_multinet/permuted/multinet_ppr_0.5_5.h5 \
    -hf     $out_freq_nonRAS \
            $out_mutsigQ_nonRAS \
    -np     $num_network_permutations \
    -hp     $num_heat_permutations \
    -o      $out_nonRAS \
    -c      $num_cores
