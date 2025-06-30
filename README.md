# DNA & Protein Sequence Analysis Tool

This Python application provides a graphical user interface (GUI) to analyze DNA and protein sequences from FASTA files. It calculates key properties such as GC content, melting temperature, molecular weight, and nucleotide/amino acid frequencies, making it a handy bioinformatics utility.

## Features

- Analyze both DNA and protein FASTA sequences
- Calculates:
  - DNA GC content
  - DNA melting temperature (approximate)
  - DNA nucleotide frequency
  - Protein molecular weight
  - Protein amino acid frequency
- Automatic detection of sequence type (DNA vs. protein)
- User-friendly Tkinter-based GUI
- Supports `.fasta` and `.fa` file formats

## Requirements

- Python 3.x
- [Biopython](https://biopython.org/)

## Usage

1. Run the script:

   ```bash
   python sequence_analysis_tool.py
2. A window will appear prompting you to select a FASTA file.
3. Once selected, the program will parse and analyze its contents, displaying the results in a scrollable text window.

## How It Works

When you select a FASTA file, the tool automatically determines whether it is a DNA or protein sequence based on the characters it contains:

- **DNA Sequences:**
  - Calculates GC content (percentage of G and C nucleotides)
  - Estimates melting temperature using the simple formula `2*(A+T) + 4*(G+C)` (2/4 rule)
  - Reports the frequency of each nucleotide

- **Protein Sequences:**
  - Calculates molecular weight
  - Reports the frequency of each amino acid

If the sequence cannot be clearly classified or contains ambiguous characters, the program will display a warning message.

## Limitations

- The melting temperature calculation uses a simple approximation and should only be used for rough estimates, not for experimental design.
- Only standard unambiguous DNA and protein sequences are supported.
- Sequences with ambiguous or non-standard characters may not be analyzed correctly.
