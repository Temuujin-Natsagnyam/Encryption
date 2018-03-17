#Temuujin.N Encryption Algorithm competition submission 02/03/2018
#
#
# Alphabet used to encrypt and decrypt, there are two because dictionaries cannot be accessed vice versa
numdict = {'a': 0, 'b': 1, 'c': 2, "d": 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
            'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
            'z': 25}
alphadict = {0:'a', 1:'b',2:'c', 3:'d', 4:'e',5:'f',6:'g', 7:'h',8:'i',9:'j', 10:'k',11:'l',12:'m', 13:'n',14:'o',15:'p',
             16:'q',17:'r',18:'s', 19:'t',20:'u',21:'v', 22:'w',23:'x',24:'y', 25:'z'}
#---------------------------------------------------------------------------------------------------------

def seperate(word):     # a function that turns its input into a list of everything in the input
    result = []       # this function does not have anything to do with the encryption logic
    for l in word:    # it's just used to turn a word into a list of every letter in it , etc.
        result.append(l)  # used in lines (COME BACK TO THIS)
    return result

def calc_mono(text):   # calculates the product of the number of letters in each word in a sentence e.g "hi boss" = 2*4
    words = text.split()
    z = 1
    for x in (words):
        y = len(x)
        z = z * y
    return z

def encrypt():
    text = str(input("\nPlease enter message(only consisting of letters in alphabet) to be encrypted.\n>>\t")).lower()
    text_list = seperate(text)   # text list is a list of all the characters inside the input (spaces included)

    #------------distinct derivable features of input---------------------------------------------------------------
    char_num = len(text)               #how long it is in terms of characters
    monoliew = calc_mono(text)         #Multiplication Of Number Of Letters In Each Word e.g "hi boss" = 2*4

    key = monoliew % char_num          # determines position of key
    lkey = text_list[key]              # finds letter in that position
    try:
        vkey = numdict[lkey]               # finds the numeric value of that letter in the alphabet dictionary
    except KeyError:
        print ("\nSorry, can't do that one. Can you try again with a different word, or get rid of redundant spaces at the end")
        return(None)

    for x in range(len(text_list)):    # this is a loop with x being the position of each character in the input in the respective iteration
        if x == key or text_list[x] == " ": # this condition is to keep the key and blank spaces unchanged
            pass
        else:
            try:
                temp = numdict[text_list[x]]   # the letter's numeric value according to the dictionary is stored under temp
                temp = (temp + (vkey * x)) % len(alphadict) # the value of the key times the position of the letter is added to-
                # -the value of the letter, then modulo'ed by the length of the alphabet
                eletter = alphadict[temp] #the new encrypted letter is stored
                text_list[x] = eletter    #the original input letter is replaced by the new encrypted letter
            except KeyError:     #this makes the program ignore characters that are not in the alphabet dictionary
                pass

    print("".join(text_list))       #this just squeezes back the list of encrypted letters into a single string

def decrypt():
    text = str(input("\nPlease enter message(only consisting of letters in alphabet) to be decrypted.\n>>\t"))
    text_list = seperate(text)
    char_num = len(text)  # number of things
    monoliew = calc_mono(text)  # Multiplication Of Number Of Letter In Each Word

    key = monoliew % char_num
    lkey = text_list[key]
    vkey = numdict[lkey]
    for x in range(len(text_list)):
        if x == key or text_list[x] == " ":
            pass
        else:
            try:
                temp = numdict[text_list[x]]
                temp = (temp - (vkey * x)) % len(alphadict)   #instead of adding it is subtracted here.
                eletter = alphadict[temp]
                text_list[x] = eletter
            except KeyError:
                pass
    print("".join(text_list))

while True:
    encrypt()
    decrypt()
