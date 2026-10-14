#!/usr/bin/env Rscript

library(org.Hs.eg.db)
hs <- org.Hs.eg.db

source("read_ini.r")

mutations <- read.csv(
                      get_ini_value("data.ini",
                                    "all_noHypoHyper___mutations"),
                      header = TRUE,
                      sep = "\t",
                      comment.char = "#")

hugo_symbols <- unique(mutations$Hugo_Symbol)

entrez_ids <- mapIds(
                     hs,
                     keys = hugo_symbols,
                     column = "ENTREZID",
                     keytype = "SYMBOL",
                     multiVals = function(x) paste(x, collapse = " | "))

write.table(
            data.frame(
                       hugo_symbol = hugo_symbols,
                       entrez_id = entrez_ids),
            file = paste0(
                          get_ini_value("data.ini",
                                        "muffinn"),
                          "/hugo_symbol_to_entrez_id.csv"),
            sep = "\t",
            quote = FALSE,
            row.names = FALSE,
            col.names = TRUE)
