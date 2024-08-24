# 5. Write a program to count the number of occurrences of item 50 from below tuple tp1:
# tp1= (50, 10, 60, 70, 50)

def count_occurrences(tp, item):
    return tp.count(item)


tp1 = (50, 10, 60, 70, 50)
count_50 = count_occurrences(tp1, 50)
print(f'Number of occurrences of 50: {count_50}') 
