def find_sentence(s, str):

    a = []

    for i in range(0, len(str)+1):
        for j in range(i, len(str)+1):
            if str[i:j] in s:
                a.append(str[i:j])
                i = j-1
    
    return a

        



s = {"quick", "brown", "the", "fox"}
str = "thequickbrownfox"
print(find_sentence(s, str))

s2 = {"bed", "bath", "bedbath", "and", "beyond"}
str2 = "bedbathandbeyond"
print(find_sentence(s2, str2))