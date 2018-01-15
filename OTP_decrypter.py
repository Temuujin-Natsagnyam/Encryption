alphabet = ['i', 'l', 'o', 'v', 'e', 'k', 'a', 'n', 'b', 'r', 'u', 'g', 'm', 'h', 'c', 'p', 'q', 'j', 's', 't', 'f',
            'd', 'z', 'y', 'x', 'w', ' ']

def neg_caesar(letter,key):
    key = int(key)
    i = 0
    for l in alphabet:
        if l == letter:break
        i = i+1
    index = i - key
    if index < 0:
        while index < 0:
            index = index + 27
    cypher = alphabet[index]
    return cypher

def neg_vermund(emsg,keylist):
    umsg = []
    ctr = 0
    while ctr < len(emsg):
        umsg.append(neg_caesar(emsg[ctr],keylist[ctr]))
        ctr += 1
    return umsg

def user_input():
    emsg = str(input("\nEnter Encrypted message\n"))
    key = input("\nEnter key\n").split()
    list_msg = neg_vermund(emsg,key)
    final_msg = ''.join(list_msg)
    print(final_msg)
    return(final_msg)

while 25 == 25:
    print("\n")
    userinput = int(input("Enter 1 to begin\n"))
    if userinput == 1:
        user_input()