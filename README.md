# TV show script generation


This repository has a collection of Python scripts designed to scrape, clean, and analyze specific character dialogue from a corpus of text files.

While we used it for a specific character cript, the logic can be easily adapted for any character-based text analysis.

# Workflow:

The project is broken down into a multi-stage pipeline to take raw, messy text files and turn them into statistics.

### Extraction & Preparation

- oneLine.py: A pre-processing script that strips newlines from raw text files. This ensures that dialogue blocks aren't accidentally cut off during the regex phase.

- joiner.py: This script scans the input directory, identifies dialogue blocks using regex, and compiles everything into a single output.txt.

### Cleaning & Normalization
- contractions.py: Uses nltk to expand English contractions (e.g., turning "don't" into "do not"). This is crucial for accurate word counting and vocabulary analysis.

- strip.py: This script removes brackets, unwanted punctuation, and handles sentence segmentation by replacing period symbols with newlines.

### Analysis
questions.py: This script goes over the cleaned data to answer:

What is the total word count?

How many hapaxes (unique words appearing only once) exist?

What are the longest sentences in the corpus?

What is the average sentence length and the most common vocabulary?

# Tech Stack
Python 3.x

Regex (regular expression): For pattern matching within the dialogue.

NLTK: For tokenization and expansion.


# Sample Output
When running questions.py, you'll get a snapshot of the character's linguistic profile:

Totaal aantal woorden = 4521

Er zijn 842 hapaxen

De top 3 langste zinnen zijn:

Zin 142 met 32 woorden...

Het gemiddelde aantal woorden per zin is 12.4

# How to Use
Drop your raw .txt files into the Teksten folder.

Run strip.py and contractions.py to clean the data (you need nltk for this).

Run oneLine.py and joiner.py to create generated TV scripts.

Run questions.py for analytics!
