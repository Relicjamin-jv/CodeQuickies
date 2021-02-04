def duplicate_count(text):
    # Your code goes here
    letters = []
    duplicates = []
    count = 0
    lc = text.lower()
    first = 0
    second = 1
    
    for letter in lc:
        letters.append(letter) #populate the list with the lowercase version of the sentance

    while first < len(letters):
        while second < len(letters):
            print(letters[second])
            if(letters[first] == letters[second] and letters[first] not in duplicates):
                count = count + 1
                break
            second = second + 1
        duplicates.append(letters[first])
        first = first + 1
        second = first + 1
    
    print(duplicates)

    return count

""" def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1]) tpatja, nkrause323, alpen0, lixiang, user4431345, timm liu, Olas, JL20119, yalisovetskyAS, Arycoo (plus 10 more warriors) A simpler solution
 """


print(duplicate_count("Lol"))
    
