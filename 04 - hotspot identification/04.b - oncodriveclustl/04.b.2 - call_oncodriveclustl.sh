source <(grep = ../../data.ini)

mutations=../../${oncodriveclustl___all_noHypoHyper___in_dir}mutations.csv
annotations=../../${oncodriveclustl___all_noHypoHyper___in_dir}annotations.csv

output_default=../../${oncodriveclustl___all_noHypoHyper}output_defaultParams/
output_coadread=../../${oncodriveclustl___all_noHypoHyper}output_coadreadParams/


# DEFAULT PARAMS
echo "all - defaultParams"
oncodriveclustl -i $mutations -r $annotations -o $output_default -g "hg19" --seed ${seed} --cores 12

# COADREAD PARAMS
echo "all - coadreadParams"
oncodriveclustl -i $mutations -r $annotations -o $output_coadread -g "hg19" -kmer 3 -simw 51 -sw 15 -cw 11 --seed ${seed} --cores 12
