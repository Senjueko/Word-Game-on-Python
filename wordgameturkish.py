import sys
import time



def letters(n):
    valids = []
    for character in n:
        if character.isalpha():
            valids.append(character)
    return ''.join(valids)
def kucukHarf(sStr):
    str      = sStr
    aranan   = ''
    HARFDIZI = [
                ('İ','i'), ('Ğ','ğ'),('Ü','ü'), ('Ş','ş'), ('Ö','ö'),('Ç','ç'),
                ('I','ı')
               ]
    for aranan, harf in HARFDIZI:
        str  = str.replace(aranan, harf)
    str      = str.lower()
    return str

def buyukHarf(sStr):
    str      = sStr
    aranan   = ''
    HARFDIZI = [
                ('i','İ'), ('ğ','Ğ'),('ü','Ü'), ('ş','Ş'), ('ö','Ö'),('ç','Ç'),
                ('ı','I')
               ]
    for aranan, harf in HARFDIZI:
        str  = str.replace(aranan, harf)
    str      = str.upper()
    return str
d1 = {}
d2 = {}

if len(sys.argv) != 3:
    print("You must write two arguments for this program")
    quit()

with open(sys.argv[1],'r',encoding='utf-8-sig',errors='ignore') as f:
    for line in f:
        x = line.split(":")
        y = str(x[:])
        z = y.split(",")
        a = z[0]
        b = str(z[1:])
        d1[b] = a

with open(sys.argv[2],'r',encoding='utf-8-sig',errors='ignore') as d:
    for satir in d:
        (key,val) = satir.split(":")
        d2[key] = int(val)
def game():
    for i in d1.values():
        score = 0
        list = []
        print("Shuffled letters are: ",letters(i) ,"Please guess words for these letters with minimum three letters")
        clock = 30
        while True:
            start_time = time.time()
            word = input("Guessed word:")
            if word not in kucukHarf(str(d1.keys())):
                print("Your guessed word is not a valid word")

            end_time = time.time()
            difference = int(end_time - start_time)
            clock = clock - difference
            if clock <= 0:
                print("You have ", 0 , "time")
                print("Score for ",letters(i) , "is" , score, "and guessed words are: ",' '.join(list[:-1]))
                break
            else:
                if word.lower() in list:
                    print("This word is guessed before")
                elif word in kucukHarf(str(d1.keys())):
                    for q in str(buyukHarf(word)):
                        score = score + (int(d2[q]) * len(word))
                    list.append(word)
                    list.append("-")
                print("You have ", clock, "time")




game()