## upgram is a word in which consecutvive letters are ... alphabetically

def smaller(word1, word2):
    if len(word1) > len(word2):
        return -1
    elif len(word2) > len(word1):
        return 1
    else:
        if word1 < word2:
            return -1
        else:
            return 1

def upgrams(filename, reverse=False):
    u = []
    with open(filename) as f:
        for line in f:
            word = line.strip()
            if  word.islower():
                if reverse==True:
                    if list(word) == sorted(word, reverse=True):
                        u.append(word)
                else:
                    if list(word) == sorted(word):
                        u.append(word)

    u.sort(smaller)
    return u

if __name__ == '__main__':
    print upgrams('/usr/share/dict/polish')
    print upgrams('/usr/share/dict/polish', reverse=True)
    print upgrams('/usr/share/dict/words')
    print upgrams('/usr/share/dict/words', reverse=True)
