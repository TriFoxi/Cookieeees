
cks = open("cookies.txt", "r")
cookies = int(cks.readline())
cks.close()

inc = open("inc.txt", "r")
increase = int(inc.readline())
inc.close()

pz = open("pizza.txt", "r")
pza = int(pz.readline())
pz.close()

clks = 0
p = 0

x2 = False
x4 = False
x8 = False

#Per Refresh [on enter]
def Refresh():

    #functions
    
    #pizza
    def pizza(piza):
        if piza == 0:
            print(" // ""--.._")
            print("||  (_)  _ -._")
            print("||    _ (_)    '-.")
            print("||   (_)   __..-'")
            print(" \\__..--""")
        elif piza == 1:
            print(" // ""--.._")
            print("||  (_)  _ -._")
            print("||    _ (_)    |")
            print("||   (_)   __..|")
            print(" \\__..--""")
        elif piza == 2:
            print(" // ""--.._")
            print("||  (_)  _ -|")
            print("||    _ (_)|")
            print("||   (_)   _|")
            print(" \\__..--""")
        elif piza == 3:
            print(" // ""--..")
            print("||  (_)  |")
            print("||    _ |")
            print("||   (_) |")
            print(" \\__..--")
        elif piza == 4:
            print(" // ")
            print("||  (|")
            print("||    |")
            print("||   |")
            print(" \\__|")
        elif piza == 5:
            print(" |")
            print("|| |")
            print("||")
            print("||")
            print(" |")
        elif piza == 6:
            print("")
            print("")
            print("")
            print("")
            print("")

    global clks
    global increase
    global cookies
    global p
    global pza
    global shop

    ck = False
    
    #Enter?
    c = input("")
    if c == "":
        ck = True
        clks = clks + 1
    elif c == "shop":
        shop = True

    #increase
    if ck == True:
        increase = 1
        if x2 == True:
            increase = increase * 2
        if x4 == True:
            increase = increase * 4
        if x8 == True:
            increase = increase * 8
        if increase > 32:
            increase = 32

    #Cookie Clicked
    if ck == True:
        cookies = cookies + increase

    #draw
    if ck == True:
        p = p + 1
        if p > 6:
            p = 0
        if p == 6:
            pza = pza + 1
        cookies = str(cookies)
        pza = str(pza)
        print("")
        print("")
        print("")
        print("")
        pizza(p)
        print("")
        print("")
        print("CKs" + cookies + "  PZa" + pza)
        cookies = int(cookies)
        pza = int(pza)

#shop
def Shop():
    
    global cookies
    global pza
    global shop
    global x2
    global x4
    global x8
    
    #items
    item1 = "x2"
    it1p = 50
    item2 = "x4"
    it2p = 100
    item3 = "x8"
    it3p = 200
    item4 = "Itm4"
    it4p = 200

    #draw shop#
    cookies = str(cookies)
    pza = str(pza)

    #cls lmao
    for i in "ffffffffffffffffffffffffffffffffffffffffffffffffff":
        print("")
    
    print("CKs" + cookies + "  PZa" + pza)
    cookies = int(cookies)
    pza = int(pza)
    
    print("")
    print("")
    print("")
    print("")

    it1p = str(it1p)
    it2p = str(it2p)
    it3p = str(it3p)
    it4p = str(it4p)
    
    print(item1 + ": " + it1p)
    print(item2 + ": " + it2p)
    print(item3 + ": " + it3p)
    print(item4 + ": " + it4p)
    print("Convert PZa into CKs: [C]")
    print("Close ------------- : [close]")

    it1p = int(it1p)
    it2p = int(it2p)
    it3p = int(it3p)
    it4p = int(it4p)
    #//#

    while shop == True:
        i = input("Select item to purchase, [1] to [4]: ")
        if i == "1":
            if cookies > it1p:
                print(item1 + " bought")
                cookies = cookies - it1p
                x2 = True
            else:
                cookies = str(cookies)
                print("not enough CKs. You have CKs" + cookies)
                cookies = int(cookies)
        elif i == "2":
            if cookies > it1p:
                print(item2 + " bought")
                cookies = cookies - it1p
                x4 = True
            else:
                cookies = str(cookies)
                print("not enough CKs. You have CKs" + cookies)
                cookies = int(cookies)
        elif i == "3":
            if cookies > it1p:
                print(item3 + " bought")
                cookies = cookies - it1p
                x8 = True
            else:
                cookies = str(cookies)
                print("not enough CKs. You have CKs" + cookies)
                cookies = int(cookies)
        elif i.lower() == "c":
            s = input("8CKs/PZa. Confirm? [Y/N]")
            if s.lower() == "y":
                add = pza * 8
                cookies = cookies + add
                cookies = str(cookies)
                add = str(add)
                print(add + "CKs added. You now have " + cookies)
                cookies = int(cookies)
                add = int(add)
            else:
                print("Okie then never mind... :C")
        elif i == "close":
            shop = False

    
            
#comp
shop = False
r = True
while r == True:
    if shop == False:
        Refresh()
    elif shop == True:
        Shop()
    
    
