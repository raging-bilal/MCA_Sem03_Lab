# 6. Write a program in python to find vowels having maximum number of instances in a given file. 
# (Note: File contains variety of data such as English alphabets, numbers etc.).

def count_vowel(file_name):

    vowel_set={'a':0,'e':0,'i':0,'o':0,'u':0,}

    with open(file_name) as f:
        for line in f:
            for char in line.lower():
                if char in vowel_set:
                    vowel_set[char]+=1

    max_vowel=max(vowel_set,key=vowel_set.get)
    max_count=vowel_set[max_vowel]


    print('The vowel with maximum occurence!')
    for vowel,count in vowel_set.items():
        if count== max_count:
            print(f'The max count of vowel is of {vowel} is {count}')



file_name='file1.txt'
count_vowel(file_name)
