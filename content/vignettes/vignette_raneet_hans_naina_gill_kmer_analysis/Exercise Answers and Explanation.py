#!/usr/bin/env python
# coding: utf-8

# # Introduction to Sequence Analysis using k-mers : Answers and Explanations

# ## Exercise 1: Calculating the Number of k-mers in a Sequence
# In order to determine how many k-mers can be extracted from a sequence, we will use the formula `n - k + 1`, where `n` is the length of the sequence given. This shows the number of valid starting positions for a substring of length `k`. If `k` is greater than `n`, no k-mers can be formed and the function will return `0`. 

# In[93]:


def num_kmers(n, k):
    """
    Returns the number of k-mers that can be generated from a sequence of length n.

    Parameters:
    n (int): Length of the sequence.
    k (int): Length of each k-mer.

    Returns:
    int: Number of k-mers, or 0 if k > n.
    """
    
    if k > n:
        return 0        # if k is longer than the sequence, no k-mers can be formed
    return n - k + 1    # Number of valid starting positions for a k-mer

# Example 1: Valid case 
sequence = "ATGCGTAC"
k = 4
print("k =", k, end="\n\n")
print("Sequence 1:", sequence)
print("Output:", num_kmers(len(sequence), k), end="\n\n")

# Example 2: k longer than sequence 
sequence = "ATG" 
k = 4
print("Sequence 2:", sequence)
print("Output:", num_kmers(len(sequence), k))


# #### Example 1: 
# The sequence given above `"ATGCGTAC"` is 8 base pairs long, making our `n` value to be `8`. Since we picked our `k` value to be `4`, we are extracting k-mers of length `4`. To extract `4-mers`, we slide a window of size `4` across the sequence. This way we can see that the number of valid starting positions is `8 - 4 + 1 = 5` using the formula given above. This means that we can extract five unique `4-mers` without going past the boundary of the sequence.
# 
# #### Example 2: 
# Here, we can see that if we wanted to extract the number of `4-mers` from the new sequence given above `"ATG"`, we get an output of `0`. This is because we can see that `k` > `n`, and thus there are no possible `4-mers` that can be extracted from that sequence. 

# ## Exercise 2: Checking for Unique k-mers in a Sequence
# To determine whether all the k-mers in a sequence are unique, we need to extract all the possible k-mers and then compare the total number to the number of unique entries. If every k-mer appears only once, then the sequence has no internal repetition at that unique k-mer length. This is useful when we need to identify repetitve regions or validate assumptions during motif discovery. 

# In[95]:


def get_kmers(sequence, k):
    """
    Extracts all k-mers from a sequence.

    Parameters:
    sequence (str): Genomic sequence. 
    k (int): Length of each k-mer.

    Returns:
    list: List of all k-mers
    """

    # Uses a sliding window to extract each k-mer
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

    
def all_kmers_unique(sequence, k):
    """
    Checks whether all k-mers in a sequence are unique or not

    Parameters: 
    sequence(str): Genomic sequence. 
    k (int): Length of each k-mer.

    Returns: 
    bool: True if all k-mers are unique, False if not
    """
    
    kmers = get_kmers(sequence, k)
    
    # Compare number of k-mers to number of unique k-mers
    return len(kmers) == len(set(kmers)) 

# Example 1: All unique k-mers
sequence = "ATGCGTAC"
k = 3
print("Sequence 1:", sequence)
print("Output:", all_kmers_unique(sequence, k), end="\n\n")

# Example 2: Repeated k-mers
sequence  = "ATGATGATG"
k = 3
print("Sequence 1:", sequence)
print("Output:", all_kmers_unique(sequence, k))


# #### Example 1: 
# The sequence `"ATGCGTAC"` is 8  base pairs long. If we extract the 3-mers of that sequence, we get the following: `'ATG'`, `'TGC'`,`'GCG'`, `'CGT'`,`'GTA'`, and `'TAC'`. Each of these appear only once, thus showing that each of these k-mers are unique. Since the number of total k-mers equals the number of unique k-mers, the function returns `True`, which also confirms that there are no repeated 3-mers in the sequence. 
# 
# #### Example 2: 
# In this example, the sequence `"ATGATGATG"` has that following 3-mers: `'ATG'`, `'TGA'`, and `'GAT'`. Each of these appear multiple times, thus showing that each of these k-mers are not unique. The function then returns `False`, which confirsm that there are repeated 3-mers in teh sequence 

# ## Exercise 3: Identifying the Most Frequent k-mers
# To be able to find the most frequent k-mer in a sequence, we count how many times each k-mer appears and return the one with the highest frequency. This is useful for identifying dominant motifs, repetitive elements, or potential sequencing artifacts. If multiple k-mers share the highest count, all of them are returned. If only one k-mer is most frequent, it will be returned alone. 
# 

# In[31]:


from collections import Counter

def count_kmers(sequence, k):
    """
    Counts the frequency of each k-mer in a sequence.

    Parameters:
    sequence (str): Genomic Sequence.
    k (int): Length of each k-mer.

    Returns: 
    Counter: Dictionary-like object with k-mer frequencies. 
    """

    # Uses a sliding window to extract each k-mer and count occurences
    return Counter(sequence[i:i+k] for i in range(len(sequence) - k + 1))
    
def most_frequent_kmer(sequence, k):
    """
    Returns all k-mers with the highest frequency in a sequence.

    Parameters: 
    sequence (str): Genomic Sequence.
    k (int): Length of each k-mer. 

    Returns: 
    list: List of most frequent k-mers.
    """
    
    counts = count_kmers(sequence, k)  # Get frequency of each k-mer
    max_freq = max(counts.values())    # Find the highest frequency

    # Return all k-mers that match the highest frequency
    return [kmer for kmer, freq in counts.items() if freq == max_freq] 

# Example 1: Tie between multiple k-mers
sequence = "ATGCGATGCGAT"
k = 3
print("Sequence 1:", sequence)
print("Output:", most_frequent_kmer(sequence, k), end="\n\n")

# Example 2: One dominant k-mer
sequence = "ATGATGATGCGT"
k = 3
print("Sequence 2:", sequence)
print("Output:", most_frequent_kmer(sequence, k))


# #### Example 1:
# The sequence `"ATGCGATGCGAT"` has 10 overalapping 3-mers. Each of the five unique 3-mers appear twice, so they all have the highest frequency. The function wil return all of them showing that no single motif is dominant. 
# 
# #### Example 2:
# However, in the sequence `"ATGATGATGCGT"`, `'ATG'` appears `3` times while the others only appear once. Thus the function returns the k-mer `'ATG'` as the only most frequent k-mer, showing that that motif is dominant. 

# ## Exercise 4: Visualizing k-mer Frequencies
# In order to visualize how often each k-mer appears in a sequence, we count their frequencies and display them as a bar chart. This is useful for spotting overrepresented motifs, assessing sequence complexity, and guiding downstream motif selection. The chart can be useful to connect numeric outputs to biological patterns. 

# In[96]:


import matplotlib.pyplot as plt
from collections import Counter

def count_kmers(sequence, k):
    """
    Counts the frequency of each k-mer in a sequence.

    Parameters:
    sequence (str): Genomic sequence.
    k (int): Length of each k-mer.

    Returns:
    Counter: Dictionary-like object with k-mer frequencies.
    """

    # Uses a sliding window to extract each k-mer and count occurences
    return Counter(sequence[i:i+k] for i in range(len(sequence) - k + 1))

def get_all_unique_kmers(sequences, k):
    """
    Collects all unique k-mers across multiple sequences.

    Parameters:
    sequences (list): List of DNA sequences.
    k (int): Length of each k-mer.

    Returns:
    list: Sorted list of unique k-mers.
    """
    unique_kmers = set()
    for seq in sequences: 
        unique_kmers.update(seq[i:i+k] for i in range(len(seq) - k + 1))  # Add each k-mer from the current sequence to the set
    return sorted(unique_kmers)

def map_kmers_to_colors(kmers, color_list):
    """
    Maps each unique k-mer to a color from the provided list.

    Parameters:
    kmers (list): List of unique k-mers.
    color_list (list): List of color hex codes or names.

    Returns:
    dict: Dictionary mapping each k-mer to a color.
    """

    # Assign each k-mer a color, cycling through the list if needed
    return {kmer: color_list[i % len(color_list)] for i, kmer in enumerate(kmers)}

def plot_kmer_frequencies(sequence, k, ax, color_map):
    """
    Plots the frequency of k-mers in a sequence using a bar chart with mapped colors.

    Parameters:
    sequence (str): Genomic sequence.
    k (int): Length of each k-mer.
    ax (matplotlib.axes.Axes): Axis object to plot on.
    color_map (dict): Dictionary mapping each k-mer to a color.

    Returns:
    None
    """
    counts = count_kmers(sequence, k)  # Count k-mers in the sequence
    kmers = list(counts.keys())  # Extract k-mer labels
    frequencies = list(counts.values())  # Extract corresponding frequencies
    bar_colors = [color_map[kmer] for kmer in kmers]  # Assign colors to each bar

    # Plot the Bar Chart
    ax.bar(kmers, frequencies, width=0.5, color=bar_colors)
    ax.set_xlabel("k-mers", fontsize=10)
    ax.set_ylabel("Frequency", fontsize=10)
    ax.set_title(f"Sequence: {sequence}", fontsize=10)
    ax.tick_params(axis='x', labelrotation=45)
    ax.grid(False)

# Example 1: No dominant k-mer
sequence1 = "ATGCGATGCGAT"

# Example 2: One dominant k-mer
sequence2 = "ATGATGATGCGT"
k = 3

# Color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#ffea2f', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Get all unique k-mers across both sequences
all_kmers = get_all_unique_kmers([sequence1, sequence2], k)

# Map each k-mer to a unique color
color_map = map_kmers_to_colors(all_kmers, colors)

# Create side-by-side plots
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_kmer_frequencies(sequence1, k, axes[0], color_map)
plot_kmer_frequencies(sequence2, k, axes[1], color_map)
plt.tight_layout()
plt.show()


# #### Example 1 (Left): 
# In the sequence `"ATGCGATGCGAT"`, we can see that all k-mers appear twice, so our bar chart shows all evenly sized bars, thus showing no dominant k-mer motif. 
# 
# #### Example 2 (Right):
# However, in the sequence `"ATGATGATGCGT"`, we can see that the k-mer `'ATG'` appears 3 times, making its bar taller than the others, showing that this sequence had one dominant k-mer motif.
# 
# Each k-mer is assigned a unique color from the palette, and the same k-mer gets the same color in both plots which makes the comparisions more intuitive and visually consistent.

# ## Exercise 5: Including the Reverse Complements
# To ensure strand-independent motif detection, we include both k-mers and their reverse complements when analyzing a sequence. This is important because DNA is double-stranded, and biologically relevant motifs may appear on either strand. Including reverse complements ensures that no strand-specific bias can affect the analysis. 

# In[97]:


def reverse_complement(seq):
    """
    Returns the reverse complement of a DNA sequence. 

    Parameters:
    seq (str): DNA sequence.

    Returns: 
    str: Reverse complement. 
    """
    
    complement = {'A':'T','T':'A','G':'C','C':'G'}  # Base Pairing Rules

    # Reverse the sequence and replace each base with its complement
    return ''.join(complement[base] for base in reversed(seq))  

def get_kmers_with_rc(sequence, k):
    """
    Returns a set of k-mers including reverse complements.

    Parameters: 
    sequence(str): Genomic sequence. 
    k (int): Length of each k-mer.

    Returns:
    set: Set of k-mers and their reverse complements. 
    """
    
    kmers = [sequence[i:i+k] for i in  range(len(sequence) - k + 1)]  # Extract original k-mers
    rc_kmers = [reverse_complement(kmer) for kmer in kmers]  # Compute reverse complements

    # Combine both sets and remove any duplicates
    return set(kmers + rc_kmers)

# Example 
sequence = "ATGCGT"
k = 3
print("Original k-mers:", [sequence[i:i+k] for i in range(len(sequence) - k + 1)])
print("With reverse complements:", get_kmers_with_rc(sequence, k))


# In the sequence `"ATGCGT"`, the 3-mers are `'ATG'`,`'TGC'`,`'GCG'`, and `'CGT'`. Their reverse complements are `'CAT'`,`'GCA'`,`'CGC'`, and `ACG'`. By including both the original k-mers and their reverse complements, we ensure that motifs like `'CAT'` are not missed just because they are appearing on the reverse (complementary) strand. This is very important in motif discovery, genome comparison, and elementary analysis on regulatory elements like promoters, enhancers, etc. 

# ## Exercise 6: Shared k-mers across varying k values 
# In order to compare two sequences across different levels of resolution, we need to calculate how many k-mers they share at varying k-mer lengths. This is useful for understanding how similarity can change with k, choosing an appropriate k-mer size for comparison, and visualizing the trade-offs between sensitivity and specificty of the k chosen. Short k-mers tend to match more easily, while longer k-mers are more specific and provide a much higher level analysis, but require more sequence data. 

# In[98]:


import matplotlib.pyplot as plt

def shared_kmers(seq1, seq2, k):
    """
    Identifies the set of shared k-mers between two sequences.

    Parameters: 
    seq1 (str): First DNA sequence.
    seq2 (str): Second DNA sequence.
    k (int): Length of each k-mer.

    Returns:
    set: Set of k-mers that appear in both sequences.
    """

    # Extract all k-mers from each sequence and convert it to sets
    kmers1 = set(seq1[i:i+k] for i in range(len(seq1) - k + 1))
    kmers2 = set(seq2[i:i+k] for i in range(len(seq2) - k + 1))

    # Return the intersection of both sets (shared k-mers)
    return kmers1.intersection(kmers2)

def shared_kmer_trend(seq1, seq2, k_min=2, k_max=10):
    """
    Plots the number of shared k-mers between two sequences across a range of k values.

    Parameters: 
    seq1 (str): First DNA sequence.
    seq2 (str): Second DNA sequence.
    k_min (int): Minimum k-mer length to test.
    k_max (int): Maximum k-mer length to test.

    Returns:
    None
    """
    
    ks = []  # List to store k values
    shared_counts = []  # List to store number of shared k-mers for each k

    for k in range(k_min, k_max + 1):
        shared = shared_kmers(seq1, seq2, k)  # Get shared k-mers for current k
        
        ks.append(k)
        shared_counts.append(len(shared))  # Store the count of shared k-mers

    # Plot the trend of shared k-mers vs. k
    plt.plot(ks, shared_counts, marker='o')
    plt.xlabel("k-mer length (k)")
    plt.ylabel("Number of shared k-mers")
    plt.title("Shared k-mers vs. k")
    plt.grid(False)
    plt.tight_layout()
    plt.show()

# Example
seq1 = "ATGCGATGCGAT"
seq2 = "ATGATGATGCGT"

shared_kmer_trend(seq1, seq2)  # Plot shared k-mer trend across k = 2 to k = 10


# This plot shows how the number of shared k-mers between two sequences changes as `k` increases. 
# - At a small `k`, many short k-mers are shared due to common substrings.
# - As `k` increases, the number of shared k-mers drops which reflects an increase in specificity.
# 
# This is useful as it helps us understand how resolution affects sequence comparison and is helpful in guiding which `k` value to use in clustering and alignments. 

# ## Exercise 7: Comparing Actual Bacterial Genomes (Pseudocode)
# 
# #### Introduction 
# In order to compare the k-mer profiles of two bacterial genomes, we first need to extract their DNA sequences from FASTA files. Then, we compute the frequency of each k-mer and compare the profiles to identify conserved motifs, species-specific patterns, or compositional biases. This is very useful in comparitive genomes, microbial classification, and motif discovery. 
# 
# #### Pseudocode w/ Code Snippets
# **Step 1:** Download Genomes
# - Go to NCBI or a similar site and download complete genome FASTA files for:
#   - *Escherichia coli* (e.g., `ecoli.fasta`)
#   - *Staphylococcus aureus* (e.g., `staph.fasta`)
# <br>
# 
# *Make sure that these are plain-text `.fasta` files containing the full genomic sequence.*
# 
# <br>
# 
# **Step 2:** Parse FASTA files
# - Use `Biopython` to read and concatenate the genome sequences.
# <br>
# 
# *If the genome is split across multiple contigs or chromosomes, this will combine them into one long string*
# 

# In[99]:


from Bio import SeqIO

def read_genome_fasta(filepath):
    """
    Reads a FASTA file and returns the concatenated genome sequence

    Parameters:
    filepath (str): Path to the FASTA file.

    Returns:
    str: Concatenated DNA sequence from all records:
    """

    # Reads each record and joins them into one continuous sequence
    return ''.join(str(record.seq) for record in SeqIO.parse(filepath, "fasta"))


# *If you get an error saying that `Bio` is not installed, you might need to install `Biopython` to your own environment. You can do so using the following command:* <br>
# `!pip install biopython`

# **Step 3:** Choose k-mer Length
# - Select a value for `k`(e.g., `k = 4` for codons, or `k = 6` for short motifs)
# <br>
# 
# *You can play around with the value of k and even implement the plot for varying k values as shown in `Exercise 6` to find out which k value suits your needs*
# 

# **Step 4:** Count k-mers
# - For each genome:
#   - Slide a window of length `k` across the sequence.
#   - Count how many times each k-mer appears. 

# In[100]:


from collections import Counter 

def count_kmers(sequence, k):
    """
    Counts the frequency of each k-mer in a DNA sequence.

    Parameters: 
    sequence (str): Genomic DNA sequence.
    k (int): Length of each k-mer.

    Returns: 
    Counter: Dictionary-like object that maps kmers  to their frequency.
    """

    # Uses a sliding window to extract each k-mer and count occurences
    return Counter(sequence[i:i+k] for i in range(len(sequence) - k + 1))
    


# **Step 5:** Align k-mer Sets
# - Create a unified list of all unique k-mers found in either genome.
# - This helps ensure a consistent comparison 

# In[1]:


def get_all_unique_kmers(sequences, k):
    """
    Collects all unique k-mers across multiple sequences.

    Parameters:
    sequences (list of str): List of DNA sequences.
    k (int): Length of each k-mer.

    Returns: 
    list: Sorted list of unique k-mers found in any sequence.
    """
    
    unique_kmers = set()

    # Add all the k-mers from each sequence to the set
    for seq in sequences:
        
        unique_kmers.update(seq[i:i+k] for i in range(len(seq) - k + 1)) 
    return sorted(unique_kmers)


# **Step 6:** Compare Frequencies
# - For each k-mer:
#   - Record its frequency in *E.coli* and in *Staphylococcus*.
#   - Print a table showing both counts.

# In[103]:


def compare_kmer_profiles(genome1, genome2, label1, label2, k):
    """
    Compares k-mer frequencies between two genomes and prints a summary table

    Parameters:
    genome1 (str): DNA sequence of the first genome. 
    genome2 (str): DNA sequence of the second genome.
    label1 (str): Label for the first genome (e.g., 'E.coli')
    label2 (str): Label for the second genome (e.g., 'Staphylococcus')
    k (int): Length of each k-mer.

    Returns:
    None
    """
    
    counts1 = count_kmers(genome1, k)  # Count k-mers in genome 1
    counts2 = count_kmers(genome2, k)  # Count k-mers in genome 2
    all_kmers = get_all_unique_kmers([genome1, genome2], k)  # Get all unique k-mers

    # Print Header
    print(f"{'k-mer':<8} | {label1:<10} | {label2:<15}")
    print("-" * 35)

    # Print frequency of each k-mer in both genomes
    for kmer in all_kmers:
        print(f"{kmer:<8} | {counts1.get(kmer,0):<10} | {counts2.get(kmer,0):<15}")
        


# **Step 7:** Interpret Results
# - Look for:
#     - k-mers with similar counts --> *conserved motifs*
#     - k-mers that are dominant in one genome --> *species- specific*
#     - overal `GC` vs `AT` bias --> *compositional differences*
# 

# #### Example Output
# <pre> 
#     k-mer     | E.coli    | Staphylococcus
#     ---------------------------------------
#     ATGC      | 120       | 45
#     GAAA      | 98        | 12
#     TTTT      | 30        | 110
#     AATT      | 25        | 95
#     CGTA      | 60        | 60
#  </pre>

# - `'CGTA'` is conserved.
# - `'ATGC'`and `'GAAA'` are enriched in *E.coli.*
# - `'TTTT'` and `'AATT'` are eriched in *Staphylococcus.*

# In[ ]:




