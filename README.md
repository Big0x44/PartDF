# PartDF
A simple CLI application to merge PDF files.

## Usage

The tool supports merging PDFs by providing either a list of files or a directory containing PDF files.

### Merge Specific PDF Files

Use the -f or --files option to specify one or more PDF files to merge.

```bash
python partdf.py -f file1.pdf file2.pdf file3.pdf -o merged_output.pdf
```

### Merge All PDF Files in a Directory

Use the -d or --directory option to merge all PDFs in a specified directory.

```bash
python partdf.py -d /path/to/pdf_directory -o merged_output.pdf
```