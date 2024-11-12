#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_mp3_folder>"
    exit 1
fi

mp3_folder="$1"
output_filename="${2:-output}"

filelist="filelist.txt"
> "$filelist"

for file in "$mp3_folder"/*.mp3; do
    echo "file '$file'" >> "$filelist"
done

ffmpeg -f concat -safe 0 -i "$filelist" -c copy "$1"/"$output_filename".mp3

rm "$filelist"
