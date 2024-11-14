#!/bin/bash

# Set the desired density (DPI) and PNG compression level
DENSITY=600
QUALITY=100
COMPRESSION_LEVEL=4  # Adjust this between 1 (low) to 5 (medium) for balanced file size and quality

# Loop over all PDF files in the current directory
for pdf_file in *.pdf; do
    # Check if there are any PDF files
    if [[ -f "$pdf_file" ]]; then
        # Remove the .pdf extension to get the base file name
        base_name="${pdf_file%.pdf}"

        # Use magick to convert the PDF to a PNG with specified density, quality, and moderate compression
        magick -density "$DENSITY" "$pdf_file" -quality "$QUALITY" -define png:compression-level="$COMPRESSION_LEVEL" -background white -alpha remove "${base_name}.png"

        echo "Converted $pdf_file to ${base_name}.png with compression level $COMPRESSION_LEVEL"
    else
        echo "No PDF files found in the directory."
    fi
done