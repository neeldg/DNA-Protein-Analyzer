from Bio import SeqIO
from Bio.SeqUtils import molecular_weight
from tkinter import Tk, filedialog, Label, Button, Text, END

# DNA Analysis 
def calculate_gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    gc_content = ((g + c) / len(sequence)) * 100
    return round(gc_content, 2)

def calculate_melting_temp(sequence):
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    tm = 2 * (a + t) + 4 * (g + c)
    return tm

def nucleotide_frequency(sequence):
    return {base: sequence.count(base) for base in "ATGC"}

# Protein Analysis 
def amino_acid_frequency(sequence):
    return {aa: sequence.count(aa) for aa in set(sequence)}

def process_fasta_file(filepath, output):
    output.delete(1.0, END)
    for record in SeqIO.parse(filepath, "fasta"):
        seq = str(record.seq).upper()
        output.insert(END, f"Sequence ID: {record.id}\n")
        output.insert(END, f"Length: {len(seq)}\n")

        # Determine if it's likely DNA or protein
        dna_bases = set("ATGC")
        protein_letters = set("ACDEFGHIKLMNPQRSTVWY")

        if all(base in dna_bases for base in seq):
            gc = calculate_gc_content(seq)
            tm = calculate_melting_temp(seq)
            freq = nucleotide_frequency(seq)

            output.insert(END, f"Type: DNA\n")
            output.insert(END, f"GC Content: {gc}%\n")
            output.insert(END, f"Melting Temperature: {tm}°C\n")
            output.insert(END, f"Nucleotide Frequency: {freq}\n\n")

        elif all(base in protein_letters for base in seq):
            freq = amino_acid_frequency(seq)
            mw = molecular_weight(seq, seq_type="protein")

            output.insert(END, f"Type: Protein\n")
            output.insert(END, f"Molecular Weight: {round(mw, 2)} Da\n")
            output.insert(END, f"Amino Acid Frequency: {freq}\n\n")
        else:
            output.insert(END, f"Unknown sequence type or contains ambiguous characters.\n\n")


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta *.fa")])
    if filepath:
        process_fasta_file(filepath, output_text)


root = Tk()
root.title("DNA & Protein Sequence Analysis Tool")
root.geometry("700x500")

label = Label(root, text="Select a FASTA file to analyze (DNA or Protein):")
label.pack(pady=10)

select_button = Button(root, text="Open FASTA File", command=open_file)
select_button.pack(pady=5)

output_text = Text(root, wrap='word', height=25, width=80)
output_text.pack(pady=10)

root.mainloop()
