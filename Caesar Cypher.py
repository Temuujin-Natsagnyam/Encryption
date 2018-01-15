import datetime

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']

def user():
    word = str(input("\nEnter message to encrypt\n\n"))
    key = str(input("\nEnter key\n"))
    product = encrypt(word,key)

    print("\n")
    print(product+"\n")

def seperate(word):
    result = []
    for l in word:
        result.append(l)
    return result

def caesar(letter,key): #simple caesar function to be used in Vermund function
    i = 0
    for l in alphabet:
        if l == letter:break
        i = i+1

    akey = i + int(key)
    if akey > 26:   # the key here will be random so it may be very high
        while akey > 26:
            akey = akey - 27
    cypher = alphabet[akey]
    cypher = str(cypher)
    return cypher

def encrypt(word,key):
    emsg = []
    letters = seperate(word)

    ctr = 0
    while ctr < len(letters):
        leter = caesar(letters[ctr],key)
        emsg.append(leter)
        ctr += 1

    final = ''.join(emsg)
    return final

while 1:
    user()

