#!/bin/bash
set -eux

# Inputs
lrn_binary_vw_file=$HOME/kddcup98/data/lrn_binary.vw
val_binary_vw_file=$HOME/kddcup98/data/val_binary.vw

# Outputs
lrn_binary_preds=$HOME/kddcup98/data/lrn_binary_preds.csv
binary_model=$HOME/kddcup98/models/model.vw
readable_model=$HOME/kddcup98/models/model-readable.txt


vw \
	--data $lrn_binary_vw_file \
	--cbify 2 \
	--predictions $lrn_binary_preds \
	--final_regressor $binary_model \
	--readable_model $readable_model
