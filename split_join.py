text=""

def spi(text, deli=" "):
    splitted_word=""
    new_text=[]
    for words in text:
        if words == deli:
            new_text.append(splitted_word)
        else:
            splitted_word+=words    
    return new_text

def joining(text, conca="-"):
    new_text=""
    for words in text:
        new_text+=words
        if text.index(words)<len(text):
            new_text+=conca
    return new_text

if __name__ =='__main__':
    splited = spi(text)
    joi = joining(splited)
    print(joi)