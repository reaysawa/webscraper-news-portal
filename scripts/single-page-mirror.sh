#!/bin/bash

BAD_ARGS=-1

function print_usage() {
  echo "### USAGE: single-page-mirror http(s)://[front_page] [directory_name]"
  echo "  - DO NOT include spaces in the arguments. Preferably escape both arguments with single quotes."
  echo "  - The files will be automatically added to the fixtures folder."
  exit $1
}

i=0
for arg in "$@"; do
  if [ "$arg" == "--help" ]; then
    print_usage 0
  fi
  if [ $i -gt 2 ]; then
    echo "ERR: Directory name or website URL hasn't been properly escaped."
    print_usage $BAD_ARGS
  fi

  i=$(( i + 1 ))
done

if [ $i -eq 1 ]; then
  print_usage $BAD_ARGS
fi

if ! [ -e "fixtures" ]; then
  echo "ERR: Run this from the project root (i.e. a place that contains the fixture folder)"
  exit -2
fi

readarray -t target_url <<< $(echo "$1" | \
  awk '{
      m=match($0, /^(https?:\/\/)(.*)/, arr)
      if (m) {
        printf("%s\n%s", arr[1], arr[2])
      }
  }')

if ! [[ "${target_url[@]}" ]]; then
  echo "ERR: Invalid URL. Provide the full-schema, HTTP protocol prefix included."
  print_usage $BAD_ARGS
fi

full_url="${target_url[0]}${target_url[1]}"

cd ./fixtures

if [ -e "$2" ]; then
  echo "Folder '$2' is already there."
  exit
fi
mkdir "$2" && cd "$2"

# https://superuser.com/a/136335
# wget --adjust-extension --span-hosts --convert-links --backup-converted --page-requisites
w=$(wget -E -H -k -K -p "$full_url" 2>/dev/null)

readarray -t target_folder <<< $(find -maxdepth 1 | grep "${target_url[1]}")
if [[ "${target_folder[@]}" ]]; then
  for f in "${target_folder[@]}"; do
    ln -s "$f"/* .
  done
else
  echo "Could not identify where the main page has been saved."
  exit 1
fi

