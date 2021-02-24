#!/bin/bash
# Script to fetch the data and code. 
# It uses config as the configuration file
echo "Reading configuration from ./config....." >&2
source ./conf.ig
if [[ $ready_to_download -eq 0 ]]; then
  echo "Please read the documentation and edit the config file accordingly." >&2
  exit 1
fi
if [ ! -d "$destination" ]; then
    mkdir "$destination"
fi

source_path="http://mo2cap2.mpi-inf.mpg.de/datasets/"
echo "Download to $destination " >&2

if [ $download_code -ne 0 ]; then
  wget "$source_path/code.zip" -P "$destination/"
fi

if [ $download_test -ne 0 ]; then
  wget "$source_path/test_data.zip" -P "$destination/"
fi

if [ $download_training -ne 0 ]; then
  mkdir "$destination/training_data"
  for chunk in {0001..0530}; do
    wget "$source_path/training_data/mo2cap2_chunk_$chunk.hdf5" -P "$destination/training_data"
  done
fi