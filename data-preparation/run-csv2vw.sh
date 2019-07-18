#!/bin/bash
set -eux

# Inputs
lrn_binary_file=$HOME/kddcup98/data/lrn_binary.csv
val_binary_file=$HOME/kddcup98/data/val_binary.csv

# Outputs
lrn_binary_vw_file=$HOME/kddcup98/data/lrn_binary.vw
val_binary_vw_file=$HOME/kddcup98/data/val_binary.vw


cd $HOME/kddcup98/data-preparation


python csv2vw.py \
	--skip_headers \
	--convert_zeros \
	$lrn_binary_file \
	$lrn_binary_vw_file


python csv2vw.py \
	--skip_headers \
	--convert_zeros \
	$val_binary_file \
	$val_binary_vw_file
