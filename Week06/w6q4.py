# 4. Write a program that inputs a main string and then creates an encrypted string by embedding a short symbol-based string after each character. The program should also be able to produce the decrypted string from encrypted string.




def enc(m_s,s_s):
    e=""
    for i in m_s:
        e+=i+s_s
    return e

def dec(e,s_s):
    d=""
    s_l=len(s_s)
    for i in range(0,len(e),s_l +1):
        d+=e[i]
        
    return d

m_s=input("Enter the main string: ")
s_s=input("Enter the sort symbol: ")


print("The ENCRYPTED STRING: ",enc(m_s,s_s))
print("The DECRYPTED STRING: ",dec(enc(m_s,s_s),s_s))



