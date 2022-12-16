# When a program runs it has a current working director.
# All the relative path are taken from the CWD as a starting point
# FileName consists of two part: directory or pathname and base name.

# Chaning the CWD(current working directory)
# import os
# f1 = open("test1.txt", "r")
# text = f1.read().split(" ")
# f1.close()
# chars = []
# counts = []
# for c in text:
#     if(c in chars):
#         i = chars.index(c)
#         counts[i] = counts[i] + 1
#     else:
#         chars.append(c)
#         counts.append(1)
# i = 0
# while i < len(chars):
#     print(chars[i], counts[i])
#     i = i+1
# chars = {}
# for c in text:
#     if(c in chars):
#         chars[c] = chars[c]+1
#     else:
#         chars[c] = 1

# for c in chars:
#     print(c, chars[c])
# Types of Files
# A wide range of file type exists which depends on the operating system bu also on the format that application need in order to function properly. example text file and binary file.
# text file contain the printable characterand spaces organizec into lines seperaged by newline character.

# def copyFile(oldFile,newFile):
#     f1 = open(oldFile,"r")
#     f2 = open(newFile,"w")
#     texts = f1.read();
#     for text in texts:
#         if(text != ""):
#             f2.write(text)
#     f2.close()
#     f1.close()

# copyFile("./notes.txt","./test1.txt")

# with open("test1.txt") as file:
#     data = file.read(10)
#     print(data);

def countCharacter(filename):
    character=[]
    count = []
    file = open(filename,"r");
    data = file.read().upper()
    file.close()
    for char in data:
        if char in character:
            i = character.index(char)
            count[i] += 1;
        else:
            character.append(char)
            count.append(1)
    i = 0;
    for i in range(len(character)-1):
        print(character[i],count[i])

countCharacter("test1.txt");
print("(((((((((((((((((((((((((((((((((((((________")
def countCharacterDict(filename):
    file = open(filename,"r");
    data = file.read().upper()
    file.close()
    characters = {}
    for char in data:
        if char in characters.keys:
            characters['char']+=1
        else:
            characters[char] = 1
    for character,value in characters.items():
        print(character,value)

countCharacter("test1.txt")