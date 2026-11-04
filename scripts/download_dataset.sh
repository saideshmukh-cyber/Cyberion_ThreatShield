#!/usr/bin/env bash
set -euo pipefail

DEST="data/raw/EVTX-ATTACK-SAMPLES"
URL="https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES.git"

mkdir -p data/raw

if [ -d "$DEST/.git" ]; then
  echo "Dataset repository already exists at: $DEST"
  echo "Updating shallow clone..."
  git -C "$DEST" pull --ff-only
else
  if [ -e "$DEST" ]; then
    echo "ERROR: $DEST exists but is not a Git repository."
    echo "Rename or move it before running this script."
    exit 1
  fi
  echo "Cloning EVTX-ATTACK-SAMPLES (shallow clone)..."
  git clone --depth 1 "$URL" "$DEST"
fi

echo
echo "Dataset repository is available at: $DEST"
echo "EVTX files:"
find "$DEST" -type f -iname '*.evtx' | wc -l
echo
echo "NOTE: Raw third-party dataset files should remain out of your Git commits."
