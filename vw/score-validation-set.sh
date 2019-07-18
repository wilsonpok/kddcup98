#!/bin/bash
set -eux

# Inputs
binary_model=$HOME/kddcup98/models/model.vw
val_binary_vw_file=$HOME/kddcup98/data/val_binary.vw

# Outputs
val_binary_preds=$HOME/kddcup98/data/val_binary_preds.csv



vw \
	--data $val_binary_vw_file \
	--initial_regressor $binary_model \
	--predictions $val_binary_preds \

