# 5# Write a program in python to find word/s having maximum number of instances in a given file and replace all its occurrences with “Aligarh”. 


from collections import Counter
import re

def replace_word(file_path):
    with open(file_path, 'r+') as f:
        text = f.read()

        words = re.findall(r'\b\w+\b', text.lower())
        
        w_counts = Counter(words)
        
        max_occ_word, freq = w_counts.most_common(1)[0]

        pattern = re.compile(r'\b' + re.escape(max_occ_word) + r'\b', re.IGNORECASE)
        n_text = pattern.sub("Aligarh", text)

        if text != n_text:
            f.seek(0)
            f.write(n_text)
            f.truncate()

            print("Replacement successful!")
            print(f"Highest occurrence word: '{max_occ_word}' with {freq} occurrences.")
            print(f"'{max_occ_word}' has been replaced with 'Aligarh'.")
        else:
            print("No changes! The most frequent word is 'Aligarh' or no replacement needed.")

replace_word('file1.txt')
