#!/usr/bin/env Rscript

source("read_ini.r")
source("06.a - mutclustsw/MutClustSW_1.0.R")


mutations <- paste0(
  get_ini_value(
    "data.ini",
    "mutclustsw___all_noHypoHyper___in_dir"
  ),
  "mutationPositions.txt"
)

lengths <- paste0(
  get_ini_value(
    "data.ini",
    "mutclustsw___all_noHypoHyper___in_dir"
  ),
  "genesLengths.txt"
)

out_file <- get_ini_value(
  "data.ini",
  "mutclustsw___all_noHypoHyper___out"
)


mutations_ras <- paste0(
  get_ini_value(
    "data.ini",
    "mutclustsw___all_noHypoHyper_RAS___in_dir"
  ),
  "mutationPositions.txt"
)

lengths_ras <- paste0(
  get_ini_value(
    "data.ini",
    "mutclustsw___all_noHypoHyper_RAS___in_dir"
  ),
  "genesLengths.txt"
)

out_file_ras <- get_ini_value(
  "data.ini",
  "mutclustsw___all_noHypoHyper_RAS___out"
)


mutations_non_ras <- paste0(
  get_ini_value(
    "data.ini",
    "mutclustsw___all_noHypoHyper_nonRAS___in_dir"
  ),
  "mutationPositions.txt"
)

lengths_non_ras <- paste0(
  get_ini_value(
    "data.ini",
    "mutclustsw___all_noHypoHyper_nonRAS___in_dir"
  ),
  "genesLengths.txt"
)

out_file_non_ras <- get_ini_value(
  "data.ini",
  "mutclustsw___all_noHypoHyper_nonRAS___out"
)

print("all")
mutclust(mutations, lengths, out_file)

print("RAS")
mutclust(mutations_ras, lengths_ras, out_file_ras)

print("nonRAS")
mutclust(mutations_non_ras, lengths_non_ras, out_file_non_ras)
