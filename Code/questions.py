from collections import Counter

with open('output2.txt', 'r') as myFile:      
    text = myFile.read()

# Hoe lang is je tekst? 
    totalwords = 0
    for line in text.split('\n'):   
        totalwords += len(line.split())

    print(f'Totaal aantal woorden = {totalwords}')

# Hoeveel zinnen zijn er? 

    num_sentences = text.count('\n')

    # print(f'Total sentences = {num_sentences}')

# Hoeveel hapaxen heeft uw corpus? (woorden die maar 1 keer voorkomen) 
    words = {}

    for line in text.split('\n'):   
        for word in line.split():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    
    hapaxes = []

    for word, count in words.items():
        if count == 1:
            hapaxes.append(word)

    print(f'Er zijn {len(hapaxes)} hapaxen')

# Hoe lang zijn de zinnen? 

    line_lens = {}
    line_index = 0

    # Dict met hoeveelheid woorden van elke zin

    for line in text.split('\n'):
        line_index += 1
        word_count = 0
        for word in line.split():
            word_count += 1
            line_lens[line_index] = word_count
    
    # print(line_lens)

    top_n = 3
    top_sentences = Counter(line_lens).most_common(top_n)

    print(f'De top {top_n} langste zinnen zijn:')
    for sentence, length in top_sentences:
        print(f'Zin {sentence} met {length} woorden')

    print(f'Het gemiddelde aantal woorden per zin is {float(totalwords/num_sentences)}')

# Hoe groot is de woordenschat? 

    vocab = len(words)

    print(f'Er zijn {vocab} verschillende woorden in onze corpus')

# Wat zijn de meest voorkomende woorden? 

    top_words = Counter(words).most_common(top_n)

    print(f'De top {top_n} meest voorkomende woorden zijn:')
    for word, count in top_words:
        print(f"Het woord '{word}', die {count} keer voorkomt")