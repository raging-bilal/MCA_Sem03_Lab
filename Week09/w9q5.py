# 5. Write a program in python to find alphabet/s having maximum number of instances in a given file. 

def count_alphabet(file_name):
    
    alphabet_set = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    with open(file_name) as f:
        for line in f:
            for char in line.lower():
                if char in alphabet_set:
                    alphabet_set[char] += 1

    max_alphabet = max(alphabet_set, key=alphabet_set.get)
    max_count = alphabet_set[max_alphabet]

    print('The alphabet with maximum occurrence:')
    for alphabet, count in alphabet_set.items():
        if count == max_count:
            print(f'The maximum count of alphabet {alphabet} is {count}')


file_name = 'file1.txt'
count_alphabet(file_name)
