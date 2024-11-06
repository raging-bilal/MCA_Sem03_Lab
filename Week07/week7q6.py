def swaap(file1,file2):

    with open(file1,'r') as f1:
        content1=f1.readlines()

    with open(file2,'r') as f2:
        content2=f2.readlines()

    if len(content1)%2==0:
        raise ValueError("Please make sure that File 1 has the odd numbers of lines!")
    
    m_index=len(content1)//2
    mid_line1=content1[m_index]

    last_line2=content2[-1]

    content1[m_index]=last_line2
    content2[-1]=mid_line1

    with open(file1,'w') as f1:
        f1.writelines(content1)

    with open(file2,'w') as f2:
        f2.writelines(content2)

    print("Swapping is completed successfully.")

file1='a.txt'
file2='b.txt'

swaap(file1,file2)