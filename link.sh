#!/bin/zsh

parentDirectory="$(cd "$( dirname "${(%):-%N}" )" && pwd -P)"

addOnDirectory=~/Library/Application\ Support/Anki2/addons21

for brokenLink in "$addOnDirectory"/*(N-@D); do
	rm "$brokenLink"
done

# Add link to this directory
if [[ ! -e "$addOnDirectory"/"$(basename "$parentDirectory")" ]]; then
	ln -s "$parentDirectory" "$addOnDirectory"
fi
