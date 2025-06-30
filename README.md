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

1. **Run the script:**

```bash
python sequence_analysis_tool.py

2. **A window will appear prompting you to select a FASTA file.**

3. **Once selected, the program will parse and analyze its contents, displaying the results in a scrollable text window.**

## How it works

1. When you select a FASTA file, the tool determines whether it is DNA or protein based on its sequence characters:

**DNA Sequences:**

    Calculates GC content (percentage of G and C nucleotides)

    Estimates melting temperature using the 2/4 rule: 2*(A+T) + 4*(G+C)
  
    Reports nucleotide frequencies

**Protein Sequences:**

    Calculates molecular weight

    Reports amino acid frequencies

    If the sequence cannot be clearly classified or contains ambiguous characters, the program will display a message indicating this.

## Limitations

1. The melting temperature calculation uses a basic approximation and should only be used for rough estimates.

2. Only standard unambiguous DNA or protein sequences are supported.

3. Sequences containing ambiguous or non-standard letters may not be classified correctly.

## Installation

Install Biopython using pip:

```bash
pip install biopython
