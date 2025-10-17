#!/usr/bin/env python
# coding: utf-8

# # Introduction to Sequence Analysis using k-mers
# 

# ## About Us
# **Naina:** I've always been interested in coding and computational biology, and even though I'm pursuing medicine, I still enjoy the logical rhythms and efficiency of writing programs. This vignette focuses on exploring k-mers, which I think are a very fascinating and underexplored region of genome analysis. I hope that through the introduction and exercises I've written, you'll find k-mers as exciting as I do. I encourage you to explore and design your own branches of this project, and to keep being curious. =) <br>
# **Raneet:** I'm fairly new to the world of computer science, and my strengths have always lied closer to the conceptual side of biology. Even so, I was intrigued by this course, and I've really enjoyed all the new things I've learned. Coding can seem quite daunting for a beginner, so I wanted to create this vignette to help invite people like me to practice and grow their programming skills. Plus, k-mers are super cool! I hope you enjoy this project, and that it inspires you to keep building your bioinformatics toolkit. =D
# 
# ## About our Research
# We were initially interested in analyzing existing methods of genome analysis. A lot of the tools currently out there have their pros and cons, so our first goal was to test the limits of how well programs like ANI fare when sorting between different ecological niches of bacterial genomes. We then designed a new method, using k-mers, to fill the gaps that ANI left behind, and to be more functional when working with less-than-ideal datasets. We saw that ANI lacks the ability to do things like metagenomic screening, contamination detection, taxonomic profiling, and computing large scale genome clustering with raw data or minimal reasources, where in these areas k-mers/Mash dominate. As our research continues, we're evaluating the effectiveness of our new program and refining it to become a tool that can one day be used to improve the efficiency of genomic analysis.

# ## What is a k-mer?
# A k-mer is a substring of length 'k' that is extracted from DNA or RNA sequences. These short fragments are very essential to genomic analysis, including genome assembly, motif discovery, and sequence comparison. 
# 
# **Example:** 
# <br>
# For the sequence *ATGCA* if we assume that k = 3, we get the following 3-mers: 
# - ATG
# - TGC
# - GCA
# <br>
# 
# By breaking the sequence into k-mers of a certain length (in this case 3), we can capture short, local patterns that may reflect things like evolutionary or ecological signals or other functional elements. This approach is useful, particularly when comparing genomes without relying on complete genome alignments and it is very easy to scale efficiently to larger datasets. 

# In[ ]:





# ## Extracting k-mers from a Sequence
# In order to extract k-mers, we use a sliding window approach: moving a window of size *k* across the sequence one nucleotide base at a time and recording each substring consecutively.
# The function below includes `raise ValueError(...)`, which stops the execution of the function and displays an error message if the input is not valid. This ensures that the function behaves as we predict and prevents any failures that are silent/hidden. 
# 

# In[15]:


def get_kmers(sequence, k):
    """
    Returns a list of all the k-mers (substrings of length k) from the input sequence in order

    Parameters:
    sequence (str): A string representing a genomic sequence.
    k (int): Length of each k-mer to extract.

    Returns:
    List[str]: A list of k-mers extracted from the sequence.
    """
    if k > len(sequence):
        raise ValueError("k cannot be larger than the input sequence length")
 #       for i in range(len(sequence) - k + 1):
 #          yield sequence[i:i+k]
        # add this * for practical application later
        
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)] # generate all k-mers (substrings of length k) from the sequence by sliding a window one base at a time

sequence = "ATGCA"
k = 3
kmers = get_kmers(sequence, k)
print("Output:", kmers)


# Extracting k-mers allows us to analyze the sequences in managable units, which helps facilitate the detection of recurring patterns and allows for genomic comparisons to become easier across species. This is memory-effecient and avoids the computational overhead of traditional alignment algorithms like ANI. 
# 

# ## Counting k-mer Frequencies
# Once we have the k-mers, we often want to quantify or count how frequently each one appears in a sequence. This can help reveal motifs that may be overrepresented, repetitive regions, or sequencing artifacts. In the function below, we use `Counter` from Python's `collections` module to tally or count (thats crazy, the counter function counts?) of each k-mer. It results in the creation of a dictionary where each k-mer is a key and its count is the value.

# In[16]:


from collections import Counter 

def count_kmers(sequence, k): 
    """
    Counts the frequency of each k-mer in the input sequence.

    Parameters:
    sequence (str): A string representing a genomic sequence.
    k (int): Length of each k-mer to count.

    Returns:
    dict: A dictionary mapping each k-mer to its frequency in the sequence.
    """
    kmers = get_kmers(sequence, k) # this will extract k-mers from the sequence 

    return dict(Counter(kmers)) # this will return a dictionary that has the count for how many times each k-mer appears in the sequence

sequence = "ATGCATGC"
k = 2
kmer_counts = count_kmers(sequence, k)
print("Output:", kmer_counts)


# K-mers that appear more frequently may correspond to elements that have been conserved over time that may act as regulatory factors, or simply present as repetitive genomic regions. Counting them provides a concise, alignment-free output that summarizes the content of the sequence and prepares the data for tasks that may appear later in projects such as clustering or classification. 
# 

# ## Comparing k-mers Between Sequences 
# In order to compare two sequences, we need to examine the set of k-mers that they share. This can help us identify which regions of the genome are conserved between species or estimate sequence similarity. We use Python's `set()` function to remove any duplicates and `&` to help compute the intersection between the k-mers that appear in both sequences. 
# 

# In[17]:


def shared_kmers(sequence_1, sequence_2, k):
    """
    Identifies k-mers that are shared between two input sequences.

    Parameters:
    sequence_1 (str): First genomic sequence.
    sequence_2 (str): Second genomic sequence.
    k (int): Length of each k-mer to compare.

    Returns:
    set: A set of k-mers that appear in both sequences.
    """
    
    kmers_1 = set(get_kmers(sequence_1, k)) # this will help to convert the first sequence into k-mers 
    kmers_2 = set(get_kmers(sequence_2, k)) # this will help to convert the second sequence into k-mers

    return kmers_1 & kmers_2 # this returns the shared k-mers

sequence_1 = "ATGCAT"
sequence_2 = "GCATGC" 
k = 3
shared = shared_kmers(sequence_1, sequence_2, k)
print("Output:", shared)


# Shared k-mers can often reflect homologus regions or conserved functional elements in species genomes. Set-based comparisons are computationally efficient and also avoid the complexity of sequence alignment which makes it especially useful for larger or fragmented datasets. 
# 

# ## Scaling k-mer Analysis Across Multiple Sequences
# To analyze multiple genomes or sequences, we need to construct a function that returns k-mer profiles for each one. This allows for parallel comparison and supports broader investigations across sample sets. <br>
# We use a dictionary to store the results, where each genome name is a key and its k-mer profile is the value. 
# 

# In[18]:


def all_kmer_profiles(sequences, k):
    """
    Computes k-mer frequency profiles for multiple sequences.

    Parameters:
    sequences (dict): A dictionary mapping sequence names to genomic sequences.
    k (int): Length of each k-mer to analyze.

    Returns:
    dict: A dictionary mapping each sequence name to its k-mer frequency profile.
    """
    
    profiles = {} # initialize an empty dictionary to store results 

    for name, seq in sequences.items():
        profiles[name] = count_kmers(seq, k) # computes and stores k-mer profiles

    return profiles

sequences = {
    "Genome_1": "ATGCATGC",
    "Genome_2": "GCATGCAT",
    "Genome_3": "TGCATGCA"
}

k = 3
profiles = all_kmer_profiles(sequences, k)

print("Output:")
for name, profile in profiles.items():
    print(name, profile)


# This structure allows for the comparisons of k-mer distributions across genomes, revealing ecological adaptations, taxonomic relationships, or horizontal gene transfer(HGTs). It also supports features like batch processing and integrates well within machine learning workflows.

# ## Comparing Sequences Using k-mer Similarity
# In order to compare two genomic sequences without using alignment-based methods like ANI, we can use a k-mer-based similarity score. This allows us to evaluate how many k-mers are shared between the two sequences relative to the total number of unique k-mers found in both. <br>
# It is especially useful for fragmented or noisy data, and is commonly used in metagenomics, genome clustering, and contamination detection.<br>
# The function below uses set operations to compute the `intersection` and `union` of k-mers from each sequence. The similarity score is then defined as the ratio of shared k-mers to the total number of unique k-mers. If both sequences are empty or contain no valid k-mers, the function returns `0.0` to avoid division by zero.
# 

# In[19]:


def kmer_similarity(seq1, seq2, k):
    """
    Computes a similarity score between two sequences based on shared k-mers.

    Parameters:
    seq1 (str): First genomic sequence.
    seq2 (str): Second genomic sequence.
    k (int): Length of k-mers to compare.

    Returns:
    float: Similarity score between 0 and 1.
    """
    
    kmers1 = set(get_kmers(seq1, k))  # extract unique k-mers from first sequence
    kmers2 = set(get_kmers(seq2, k))  # extract unique k-mers from second sequence

    shared = kmers1 & kmers2          # compute intersection (shared k-mers)
    union = kmers1 | kmers2           # compute union (all unique k-mers)

    if not union:
        return 0.0                    # return 0 if no valid k-mers are found

    return len(shared) / len(union)   # compute similarity score


seq1 = "ATGCAT"
seq2 = "GCATGC"
k = 3
score = kmer_similarity(seq1, seq2, k)
print("Output:", score)


# The output of `1.0` indicates that the two sequences share all of their k-mers. In this case, both `"ATGCAT"` and `"GCATGC"` produce the same set of four 3-mers: `'ATG'`, `'TGC'`, `'GCA'`, and `'CAT'`. Since the intersection and union of these sets are identical, the similarity score—defined as the number of shared k-mers divided by the total number of unique k-mers—is `4 / 4 = 1.0`. This reflects complete overlap in k-mer content between the two sequences.
# 

# ## Exercises
# 
# 1. Write a function that returns how many k-mers will be generated from a sequence of length `n` and a given `k`. <br> **Hint:** The number of k-mers is `n - k + 1` if `k <= n`. If `k > n`, return 0 or raise an error.
# 
# 2. Given a sequence and a value of `k`, determine whether all k-mers in the sequence are unique. <br> **Hint:** Extract the k-mers and compare the length of the list to the length of the set. If they match, all k-mers are unique.
# 
# 3. Write a function that returns the most frequent k-mer in a sequence. <br> **Hint:** use your `count_kmers()` function and apply `max()` with `key = counts.get` to find the k-mer with the highest count. 
# 
# 4. Use `matplotlib` or `seaborn` to plot the frequency of k-mers for a given sequence. <br> **Hint:** Convert the dictionary of k-mer counts into two lists: one for the k-mers and one for their frequencies. Use a *bar plot* to visualize results.
# 
# 5. Modify your k-mer extraction to include reverse complements. Compare how this affects shared k-mer analysis. <br> **Hint:** Write a helper function that returns the reverse complement of a DNA string. Include both the original and its reverse complement in your k-mer set.* <-- put in main text instead
# 
# 6. Analyze how the number of shared k-mers change as you vary `k` from 2 to 10. <br> **Hint:** Loop over a range of `k` values and record the number of shared k-mers at each step. Plot the results to observe trends.
# 
# 7. **EXTRA CHALLENGE >:)** --> Download two bacterial genomes (e.g., *E.coli* and *Staphylococcus* and compare their k-mer profiles. <br> **Hint:** Use a FASTA parser (e.g., from `Biopython`) to read the sequences. Apply your existing functions to compute and compare k-mer profiles. Focus on conserved or highly frequent k-mers. 
