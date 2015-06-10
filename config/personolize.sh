#!/bin/bash
home=$(echo $HOME | sed -e 's/\//\\\//g')
outfile=config.cfg.json.tmp
if [ "$1" = "-r" ] ; then
  outfile=config.cfg.json
fi
sed -e "s/%%%USER%%%/$USER/g" < config.cfg.json.tmpl | sed -e "s/%%%HOME%%%/$home/g" > $outfile

