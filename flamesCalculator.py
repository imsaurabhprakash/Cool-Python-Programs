def calculateFlames(name1, name2):
    lower1 = name1.replace(' ','').lower()
    lower2 = name2.replace(' ','').lower()
    flames = "flames"
    flamesDict = {
        'f':'FRIENDS',
        'l':'LOVE',
        'a':'ADORE',
        'm':'MARRIAGE',
        'e':'ENEMIES',
        's':'SISTER'
    }
    #Remove common characters from both names
    for i in lower1:
        if i in lower1 and i in lower2:
            lower1 = lower1.replace(i,'',1)
            lower2 = lower2.replace(i,'',1)

    print(flamesDict[flames[len(lower1+lower2)%len(flames)]])

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

calculateFlames(name1, name2)