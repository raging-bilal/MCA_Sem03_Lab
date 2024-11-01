# 7. Write a Python program to create a list of user’s supplied distinct integers having even number of elements. The program further creates two lists of equal lengths based on the original list, where first list is having all elements less than elements of second list. Display both the lists. 

def sort_split(main_list):
    
    main_list.sort()

    
    mid = len(main_list) // 2
    l1 = main_list[:mid]  
    l2 = main_list[mid:]  

    return l1, l2


main_string = input("Enter distinct integers separated by spaces (must be an even number of elements): ")
main_list = list(map(int, main_string.split()))


if len(main_list) % 2 != 0:
    print("Please enter an even number of distinct integers.")
else:

    l1, l2 = sort_split(main_list)
    
    print("Original sorted list:", main_list)
    print("List 1 (smaller elements):", l1)
    print("List 2 (larger elements):", l2)
