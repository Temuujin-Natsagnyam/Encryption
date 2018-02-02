import datetime
alphabet = ['i', 'l', 'o', 'v', 'e', 'k', 'a', 'n', 'b', 'r', 'u', 'g', 'm', 'h', 'c', 'p', 'q', 'j', 's', 't', 'f',
            'd', 'z', 'y', 'x', 'w', ' ']
def caesar(letter,key):
    i = 0
    for l in alphabet:
        if l == letter:break
        i = i+1
    global akey
    akey = i + key
    if akey > 26:
        while akey > 26:
            akey = akey - 27
    cypher = alphabet[akey]
    return cypher

def randkey(length):             # custom random sequence generator (not perfect)
    now = datetime.datetime.now()
    list1 = []
    keyy = []

    x = 0
    ctr = 0
    mask = 0xff

    while (ctr <= mask):
        nnn = now.microsecond
        coeff = now.second
        if x == 1: # I added this because 1^n is still 1
            k = coeff + coeff * nnn
            k = k & mask
        else:
            k = coeff * x ^ 3 + nnn * x ^ 2 + x + nnn
            k = k & mask
        if k not in list1:
            list1.append(k)
        ctr += 1
        x += 1
    ctr1 = 0
    counter = 0
    while (ctr1 < mask) and counter < length:
        if list1[ctr1] != 0 :
            keyy.append(list1[ctr1])
        ctr1 += 1
        counter += 1
    return keyy

def vermund(word):
    emsg = []
    counter = 0
    ctr = 0
    wordletters = []
    for l in word:
        wordletters.append(l)
    global keylist                               #gets OTP
    keylist = randkey(len(word))

    while counter < len(word):
        emsg.append(caesar(wordletters[ctr],keylist[ctr]))
        ctr += 1
        counter += 1
    return emsg

#====================User Interface=========================================
def user():
    wordy = str(input("\nEnter message to encrypt\n\n"))
    product = vermund(wordy)
    wordd = ''.join(product)
    print("\n",wordd,"\n")
    print("Key: ")
    return keylist

while 25 == 25:
    print(user())
