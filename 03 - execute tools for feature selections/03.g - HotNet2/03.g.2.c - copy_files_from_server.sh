server="bellomo@131.175.120.88"
data_server="~/data/hotnet2"

source <(grep = ../../data.ini)

out=../../${hotnet2___all_noHypoHyper___out_dir}
out_RAS=../../${hotnet2___all_noHypoHyper_RAS___out_dir}
out_nonRAS=../../${hotnet2___all_noHypoHyper_nonRAS___out_dir}

out_net=../../${hotnet2___networks}

echo "copy all output data"
rsync -r "$server:$data_server/all_noHypoHyper/output/*" ${out}

echo "copy RAS output data"
rsync -r "$server:$data_server/all_noHypoHyper_RAS/output/*" ${out_RAS}

echo "copy nonRAS output data"
rsync -r "$server:$data_server/all_noHypoHyper_nonRAS/output/*" ${out_nonRAS}

# DO NOT DOWNLOAD NETWORK DATA (it is too big)
# echo "copy network data"
# rsync -r $server:$data_server/networks/* ${out_net}
