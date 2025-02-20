#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf_paths, output_path):
    """Merge the PDF files provided in pdf_paths and save the output to output_path."""
    writer = PdfWriter()
    for pdf_path in pdf_paths:
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                writer.add_page(page)
            print(f"Added '{pdf_path}'")
        except Exception as e:
            print(f"Error processing '{pdf_path}': {e}")
    
    # Write out the merged PDF
    try:
        with open(output_path, 'wb') as out_file:
            writer.write(out_file)
        print(f"Merged PDF saved as '{output_path}'")
    except Exception as e:
        print(f"Error writing output file '{output_path}': {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Merge multiple PDF files into a single PDF file."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-f', '--files',
        nargs='+',
        help='List of PDF files to merge (space-separated).'
    )
    group.add_argument(
        '-d', '--directory',
        help='Directory containing PDF files to merge (all PDFs in the directory will be considered).'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output file name (and path) for the merged PDF.'
    )

    args = parser.parse_args()

    pdf_paths = []
    if args.files:
        # Validate each provided file path ends with .pdf (case-insensitive)
        pdf_paths = [Path(f) for f in args.files if f.lower().endswith('.pdf')]
        if not pdf_paths:
            print("No valid PDF files provided in the file list.")
            return
    elif args.directory:
        directory = Path(args.directory)
        if not directory.is_dir():
            print(f"The directory '{args.directory}' does not exist or is not a directory.")
            return
        # Get all PDF files in the directory (non-recursive)
        pdf_paths = sorted(directory.glob('*.pdf'))
        if not pdf_paths:
            print(f"No PDF files found in directory '{args.directory}'.")
            return

    # Ensure the output directory exists
    output_path = Path(args.output)
    if output_path.parent and not output_path.parent.exists():
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Could not create output directory '{output_path.parent}': {e}")
            return

    merge_pdfs(pdf_paths, output_path)

if __name__ == '__main__':
    main()
