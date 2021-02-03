def spin_words(sentence):
    # Your code goes here
    words = sentence.split()
    stack = []
    flWord = ""
    finalWord = ""
    

    for words in words:
        if(len(words) >= 5):
            for letter in words:
                stack.append(letter)
            for letter in range(len(stack)):
                flWord = flWord + stack.pop()
            if (finalWord == ""):
                finalWord = finalWord + flWord
                flWord = ""
            else:
                finalWord = finalWord + " " + flWord
                flWord = ""
        else:
            if (finalWord == ""):
                finalWord = finalWord + words
            else:
                finalWord = finalWord + " " + words
        
    return finalWord

    
""" def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")]) 
    MiraliN, medve, mega-mac-slice, lunardragon, MisterTexas, Noshii, MartiONE, RostaTasha, shobhitpathak, abhrajit (plus 204 more warriors), some other cooler code
    """


print(spin_words("Welcolm"))