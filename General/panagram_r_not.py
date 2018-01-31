import string
# a sentence or verse that contains all the letters of the alphabet.
def panagram():
    sent = 'a sentence or verse that contains all the letters of the alphabet'
    s = sent.split()
    print(s)
    newsent = []
    for i in range(0,len(s)):
        r = s[i]
        for j in range(0,len(r)):
            if r[j] not in newsent:
                newsent.append(r[j])
    print(newsent)

    print(string.ascii_lowercase)
    az = string.ascii_lowercase
    missing_letters = []
    for i in range(0,len(az)):
        if az[i] not in newsent:
            missing_letters.append(az[i])
    print(missing_letters)
    #for i in range(0, len(newsent)):







panagram()


