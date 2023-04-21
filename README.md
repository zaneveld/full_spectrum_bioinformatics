![Full Spectrum Bioinformatics](./cover_image/full_spectrum_bioinformatics_cover.png "A cover image for Full Spectrum Bioinformatics, showing the text title in rainbow colors with a phylogenetic tree, nucleotide substitution diagram, tRNA secondary structure, sequence alignment and principle coordinates analysis plot shown below it.")

<a href="https://zenodo.org/badge/latestdoi/198281370"><img src="https://zenodo.org/badge/198281370.svg" alt="DOI"></a>
[![NSF-1942647](https://img.shields.io/badge/NSF-1942647-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1942647). 

[![licensebuttons by-nc-sa](https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0)
<br>
**Authors**: Jesse Zaneveld<sup>1</sup>, Nia Prabhu<sup>\*</sup><sup>1</sup>, Aziz Bajouri<sup>\*</sup><sup>1,2</sup>, Ayomikun Akinrinade<sup>\*</sup><sup>1,3</sup>, Dr. Mushtaq Bilal<sup>\*</sup><sup>4</sup>
 <br>
 <br>
 <font size=+1>
 <sup>\*</sup> Chapter and Vignette authors contributed equally and are listed in chronological order of first contribution.<br>
 <sup>1</sup> Division of Biological Sciences, School of STEM, University of Washington, Bothell, Washington, USA<br>
 <sup>2</sup> Division of Computer and Software Systems, School of STEM, University of Washington, Bothell, Washington, USA<br>
 <sup>3</sup> Division of Health Studies, School of Nursing and Health Studies, University of Washington, Bothell, Washington, USA<br>
  <sup>4</sup> 
 </font>
 
## About the Project

**Full Spectrum Bioinformatics** is a free online text designed to introduce key topics in Bioinformatics using the Python programming language. The text is written in interactive Jupyter Notebooks, which allow you to try out and modify example code and analyses. 

In addition to explanations of concepts, Full Spectrum Bioinformatics also includes **Bioinformatics Vignettes** written by readers of the text. Each vignette is focused around a particular core concept, and show how readers have applied that concepts to their research projects. 

## How to Read the Text

 If you happen to already be familiar with GitHub and Jupyter Notebooks, you can download the entire project and run it interactively, or click the 'Open in Colab' links (they looks like this: ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)) to open interactive versions of each section in Google Colab (you will need to 'Save as' your own copy in order to change code).
 
 If you would just like to read a chapter, you can also view a static version of each section using the `nbviewer` links (they look like this:  ![Open in nbviewer](assets/nbviewer_badge.svg)). `nbviewer` stands for 'notebook viewer', so this is just a way to view chapters with code in them without actually running the code. This will generally be the best way to view the chapters non-interactively.  

Finally, you can also use the direct GitHub links (the link that's the name of each chapter) to view any chapeter. This shows the chapter on GitHub. It usually works well, but you may sometimes get a GitHub error message. Usually hitting reload page or using the ![Open in nbviewer](assets/nbviewer_badge.svg) link avoids this issue.

# Table of Contents

The text is currently in prototype status. Chapters with content you can preview are linked below:

-  **Chapter 1. [Foreword](./content/01_foreword/foreword.ipynb)** [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/01_foreword/foreword.ipynb)
 
- **Chapter 2. Introduction**
     - **The Many Paths to Bioinformatics**
     - **Speaking Each Other's Language**
         - **An Absurdly Brief Introduction to Biology**
         - **An Absurdly Brief Introduction to Computer Science**
         - **An Absurdly Brief Introduction to Statistics**    
     
- **Chapter 3. The Command Line**     
     - [Using the Command Line](./content/03_the_command_line/the_commandline.ipynb) [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/03_the_command_line/the_commandline.ipynb)
     - [**Exercise**: Little Brother is Missing](content/03_the_command_line/exercise_little_brother_is_missing.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/03_the_command_line/exercise_little_brother_is_missing.ipynb) 
   - [**Exercise**: Duck vs. Yeast](content/08_phylogenetic_trees/duck_vs_yeast.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/08_phylogenetic_trees/duck_vs_yeast.ipynb)   
- **Chapter 4. Exploring Python**
     - **Warm-up Exercise**: Spot the Difference
     - [Exploring Python](./content/04_exploring_python/exploring_python.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/exploring_python.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/exploring_python.ipynb) 
     - [A Tour of Python Data Types](./content/04_exploring_python/exploring_python_data_types.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/exploring_python_data_types.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/exploring_python_data_types.ipynb) 
     -  [A Tour of Python Syntax (functions, conditions, iteration, classes)](./content/04_exploring_python/A_Tour_of_Python_Syntax.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/A_Tour_of_Python_Syntax.ipynb) 
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/A_Tour_of_Python_Syntax.ipynb) 
     -  [A Quick Win: using Python to run Statistical Tests and Make Simple Graphs](./content/04_exploring_python/a_quick_win.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/a_quick_win.ipynb)
        [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/a_quick_win.ipynb) 

- **Chapter 5. Project Design**
     - [Using Literature Surveys to Ask Good Questions and Propose Testable Hypotheses](./content/05_project_design/project_design.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/05_project_design/project_design.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/05_project_design/project_design.ipynb)
     - [Write a Literature Synthesis...and get your Introduction for free!](./content/05_project_design/literature_synthesis.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/05_project_design/literature_synthesis.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/05_project_design/literature_synthesis.ipynb)
     - [How Not to Repeatedly Reformat 96 Citations by Hand: Zotero for Beginners (Dr. Mushtaq Bilal)](./content/05_project_design/zotero.ipynb) [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/05_project_design/zotero.ipynb)

- **Chapter 6. Biological Sequences**
     - [An introduction to Biological Sequences](./content/06_biological_sequences/biological_sequences.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/biological_sequences.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/biological_sequences.ipynb) 
     - [Representing and Manipulating Biological Sequences as Python Strings](./content/06_biological_sequences/representing_and_manipulating_biological_sequences_with_python_strings.ipynb) 
      [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/representing_and_manipulating_biological_sequences_with_python_strings.ipynb)
      [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/representing_and_manipulating_biological_sequences_with_python_strings.ipynb)
     - [Analyzing Biological Sequences with For Loops and If Statements](./content/06_biological_sequences/using_for_loops_to_analyze_biological_sequences.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/using_for_loops_to_analyze_biological_sequences.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/using_for_loops_to_analyze_biological_sequences.ipynb)
     -  [Reading and writing FASTA files using Python](./content/06_biological_sequences/reading_and_writing_fasta_files.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/reading_and_writing_fasta_files.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/reading_and_writing_fasta_files.ipynb)
     - **Bioinformatics Vignette (Aziz Bajouri):** [Using set objects to find circular RNAs involved in multiple diseases](https://github.com/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_aziz_bajouri_using_set_objects_to_find_circular_RNAs_present_in_multiple_diseases/vignette_aziz_bajouri_using_set_objects_to_find_circular_RNAs_associated_with_multiple_diseases.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_aziz_bajouri_using_set_objects_to_find_circular_RNAs_present_in_multiple_diseases/vignette_aziz_bajouri_using_set_objects_to_find_circular_RNAs_associated_with_multiple_diseases.ipynb) [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_aziz_bajouri_using_set_objects_to_find_circular_RNAs_present_in_multiple_diseases/vignette_aziz_bajouri_using_set_objects_to_find_circular_RNAs_associated_with_multiple_diseases.ipynb)
     - **Exercise**: [Error Bingo](./content/04_exploring_python/exercise_error_bingo.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/exercise_error_bingo.ipynb)
     - [Error Messages in Python](./content/04_exploring_python/error_messages_in_python.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/error_messages_in_python.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/04_exploring_python/error_messages_in_python.ipynb) 
     - **Bioinformatics Vignette (Nia Prabhu):** [Using For Loops and Dictionaries to Compare Nucleotide Composition in Pandemic and Non-Pandemic Causing Influenza Strains](https://github.com/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_nia_prabhu_using_for_loops_to_compare_influenza_glycoprotein_gene_sequences/vignette_nia_prabhu_using_for_loops_to_compare_influenza_glycoprotein_gene_sequences.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_nia_prabhu_using_for_loops_to_compare_influenza_glycoprotein_gene_sequences/vignette_nia_prabhu_using_for_loops_to_compare_influenza_glycoprotein_gene_sequences.ipynb)
 [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_nia_prabhu_using_for_loops_to_compare_influenza_glycoprotein_gene_sequences/vignette_nia_prabhu_using_for_loops_to_compare_influenza_glycoprotein_gene_sequences.ipynb)
     - [**Capstone**: testing for depletion of CG dinucleotides in the human genome](./content/06_biological_sequences/capstone_cg_dinucleotides.ipynb)  
        [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/capstone_cg_dinucleotides.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/06_biological_sequences/capstone_cg_dinucleotides.ipynb)
 
- **Chapter 7. 'Omics**
     -  [An Introduction to 'Omics](./content/07_tabular_omics_data/tabular_omics_data.ipynb) 
        [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/tabular_omics_data.ipynb)
        [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/tabular_omics_data.ipynb)
     -  [Working with Tabular 'Omic data in Python using Pandas](./content/07_tabular_omics_data/analyzing_tabular_omics_data_in_pandas.ipynb)
        [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/analyzing_tabular_omics_data_in_pandas.ipynb)
        [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/analyzing_tabular_omics_data_in_pandas.ipynb)
     -  [Joining and Filtering Pandas DataFrames](./content/07_tabular_omics_data/merging_tables.ipynb)
        [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/merging_tables.ipynb)
        [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/merging_tables.ipynb)
     -   Analyzing Microbiome Alpha Diversity in Python
     -   Analyzing Microbiome Beta Diversity in Python
     -   [Simulating the Effect of Sequencing Depth on Diversity Estimates](https://github.com/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/simulating_microbiome_sampling_depth.ipynb)[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/simulating_microbiome_sampling_depth.ipynb)[![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/07_tabular_omics_data/simulating_microbiome_sampling_depth.ipynb)

- **Level Up: Taking Stock of your Project and Revising your Process**
     - Reflecting on your Project so Far
     - Project Organization Strategies for Collaborative and Reproducible Research
     - Test Code: a powerful strategy for ensuring your results aren't lies.      
 
- **Chapter 8. Visualization**
  - Graphs as a Visual Language
  - [**Exercise**: Anger Tufte](./content/09_visualization/anger_tufte.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/09_visualization/anger_tufte.ipynb)[![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/09_visualization/anger_tufte.ipynb)       
   - [Representing Correlation](./content/09_visualization/visualizing_correlation.ipynb)
        [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/09_visualization/visualizing_correlation.ipynb) [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/09_visualization/visualizing_correlation.ipynb) 
    - Representing Distribution

- **Chapter 9. Alignment and Phylogenetics**
     - **9a. Alignment**
     - Homology and Alignment
     - [Global Alignment with the Needleman-Wunsch algorithm](/content/08_phylogenetic_trees/needleman_wunsch_alignment.ipynb)
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/08_phylogenetic_trees/needleman_wunsch_alignment.ipynb)
    [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/08_phylogenetic_trees/needleman_wunsch_alignment.ipynb)
     - Local Alignment with the Smith-Waterman algorithm
     - BLAST and the k-mer trick
     - **Exercise:** Duck vs. Yeast 
     - **9b. Phylogenetics**
     - Tree thinking
     - [Representing Phylogenetic Trees with Python Classes](./content/08_phylogenetic_trees/phylogenetic_trees.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/08_phylogenetic_trees/phylogenetic_trees.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/08_phylogenetic_trees/phylogenetic_trees.ipynb)
     - [Generating Trees Using Birth-Death Models](./content/08_phylogenetic_trees/birth_death_models.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/08_phylogenetic_trees/birth_death_models.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/08_phylogenetic_trees/birth_death_models.ipynb)
     - Working with Traits on Trees
     - Maximum Parsimony Ancestral State Reconstruction
     - Phylogenetic Comparative Methods   
     - Trait prediction

- **Chapter 10. Simulation**
     - Simulating Biological Networks
     - [Simulating the Population Genetics of Natural Selection and Genetic Drift](./content/10_simulation/simulating_evolution.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/10_simulation/simulating_evolution.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/10_simulation/simulating_evolution.ipynb)
     - Simulating the Evolution of Social Behavior

- **Chapter 11. Statistics**
     - [Linear Models - a Statistical Swiss Army Knife](./content/11_statistics/linear_models.ipynb)
       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/rank_based_methods.ipynb)
       [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/linear_models.ipynb)       
     - [Monte Carlo simulation and the Fundamental Unity of Statistical Hypothesis Tests](./content/11_statistics/monte_carlo_methods_and_the_fundamental_unity_of_statistical_tests.ipynb) 
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/monte_carlo_methods_and_the_fundamental_unity_of_statistical_tests.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/monte_carlo_methods_and_the_fundamental_unity_of_statistical_tests.ipynb)
     - Statistical Distributions and Parametric Tests
     - [Rank Transformations](./content/11_statistics/rank_based_methods.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/rank_based_methods.ipynb)
      [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/rank_based_methods.ipynb)
     - [Monte Carlo simulation of Effect Size, Sample Size, and Significance](./content/11_statistics/effect_size_sample_size_and_significance.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/effect_size_sample_size_and_significance.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/effect_size_sample_size_and_significance.ipynb)
     - [Dealing with Multiple Comparisons](https://github.com/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/dealing_with_multiple_comparisons.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/dealing_with_multiple_comparisons.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/dealing_with_multiple_comparisons.ipynb)
     - [**Exercise**: Revising your writing about statistical results](./content/11_statistics/exercise_revising_your_writing_about_statistical_results.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/exercise_revising_your_writing_about_statistical_results.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/11_statistics/exercise_revising_your_writing_about_statistical_results.ipynb)
     - An Introduction to Maximum Likelihood optimization
     - The Best Model of A Cat is a Cat - model complexity, overfitting, and the AIC
     - An Introduction to Bayesian Approaches

- **Chapter 12. Multivariate Statistics and Machine Learning**
     - Unsupervised Classification: of ordination, clustering and fishtanks
     - Supervised Classification: from lines to trees to forests.
     - **Bioinformatics Vignette (Ayomikun Akinrinade)**: [Using K-Nearest Neighbors and Binary Decision Tree Algorithms to Predict Enzyme Function from Protein Sequences](https://github.com/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_ayomikun_akinrinade_protein_function_prediction/vignette_ayomikun_akinrinade.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_ayomikun_akinrinade_protein_function_prediction/vignette_ayomikun_akinrinade.ipynb)[![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/vignettes/vignette_ayomikun_akinrinade_protein_function_prediction/vignette_ayomikun_akinrinade.ipynb)
 

- **Chapter 13. Presenting Research**
     - Presentations as Verbal Chess

- **Chapter 14. Polishing and Publishing**
     - [Presenting Research](./content/13_presenting_research/12_Presenting_Research.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/13_presenting_research/12_Presenting_Research.ipynb)
      [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/13_presenting_research/12_Presenting_Research.ipynb)
     - From Data to Conclusion: building a research manuscript brick by brick
     - Resistance is Futile: becoming a language Borg
     - **Exercise**: generating a targeted title using templating
     - The Inverted Pyramid: optimizing your text from a reader's perspective     

- **Chapter 15. Careers that draw on Bioinformatics**    
     - [Fighting for an Inclusive Workplace](./content/15_careers/fighting_for_an_inclusive_workplace.ipynb)[![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/15_careers/fighting_for_an_inclusive_workplace.ipynb)
          - Examining Privilege and Identity
          - Making Your Science and Teaching Accessible and Inclusive
          - Campus and Local Activism
          - Improving University Policy                       
     - Happiness Matters
     - Radical Collaboration 
     - Cognitive Bias and Networking     
     - Open-source Science as Shield and Sword
     - [Applying for Grants](./content/13_presenting_research/applying_for_grants.ipynb)
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/13_presenting_research/applying_for_grants.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/zaneveld/full_spectrum_bioinformatics/blob/master/content/13_presenting_research/applying_for_grants.ipynb)

- **Appendices:**      
     - Appendix A - [Data Sources for Bioinformatics Projects](https://github.com/zaneveld/full_spectrum_bioinformatics/blob/master/content/14_appendix_data_sources/14_Appendix_Data_Sources.ipynb)
     [![Open in nbviewer](assets/nbviewer_badge.svg)](https://github.com/zaneveld/full_spectrum_bioinformatics/blob/master/content/14_appendix_data_sources/14_Appendix_Data_Sources.ipynb)
     - Appendix B - Timesaving Starter Code
       - Template Script with Interface and Test Code
       - IUPAC codes in python
       - Standard Translation Tables in Python
     - Appendix C - Contributing a Community Example
     - Appendix D - Paper Formatting Kit 
     - Appendix E - Project Specifications 

## Acknowledgements

This project is being developed with support from NSF Integrative and Organismal Systems award [![NSF-1942647](https://img.shields.io/badge/NSF-1942647-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1942647). 
 
 ## Feedback
You can submit feedback about completed chapters at the following [link](https://docs.google.com/forms/d/e/1FAIpQLSeUQPI_JbyKcX1juAFLt5z1CLzC2vTqaCYySUAYCNElNwZqqQ/viewform?usp=sf_link)
