#!/bin/bash

ARG=$1

if [ "$ARG" == "install" ]; then
  scp -r custom_components/marshall ha:config/custom_components/
  exit 0
fi

if [ "$ARG" == "reinstall" ]; then
  ssh ha 'rm -r config/custom_components/marshall'
  scp -r custom_components/marshall ha:config/custom_components/
  exit 0
fi

if [ "$ARG" == "uninstall" ]; then
  ssh ha 'rm -r config/custom_components/marshall'
  exit 0
fi

echo "usage: $0 <install|reinstall|uninstall>"
exit 1



# scp -r custom_components/marshall ha:config/custom_components/
# ssh ha 'rm -r config/custom_components/marshall'