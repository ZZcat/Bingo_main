from Tkinter import *



def show_entry_fields():
    global gamemode
    global NumberOfCard
    NumberOfCard = (e2.get())
    gamemode = (e1.get())
    master.destroy()
    return 
master = Tk()
master.wm_title("Bingo game")
Label(master, text="1 - Regular Bingo\n2 - Double Bingo\n3 - Regular Bingo\n4 - Small Picture Frame\n5 - Double Postage Stamp\n6 - Trails T\n7 - Regular Bingo\n8 - Letter X\n9 - Hardway Bingo\n10 - Cover All\n\n").grid(row=0)
Label(master, text="Number of cards    -->").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.insert(10,"Game #")
e2.insert(10,"Cards")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='Chose', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )
###
global allcards
allcards = []
while not int(NumberOfCard) == 0:
    root = Tk()
    root.wm_title("Bingo card(free space is zero)    #"+str(NumberOfCard))
    rows = []
    for i in range(5):
        cols = []
        for j in range(5):
            e = Entry(relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, "3")
            cols.append(e)
        rows.append(cols)

    card = []
    card_line = []
    def onPress():
        for row in rows:
            card_line = []
            for col in row:
                card_line.append(col.get())
            card.append(card_line)
        root.destroy()

    Button(text='Set card', command=onPress).grid()
    mainloop()
    (NumberOfCard) = int(NumberOfCard) - 1
    allcards.append(card)
###

numbers = [0]
bcard = []

def win():
    global allcards
    master = Tk()
    master.wm_title("You won!!!")
    listbox = Listbox(master)
    listbox.pack()
    TrashABC = "Card:" ,card_showentry_number
    listbox.insert(END, TrashABC)
    itemN = 0
    for item in bcard:
        itemN = itemN + 1
        listbox.insert(itemN,item)
    new_allcards = []
    for remove_card_allcards in allcards:
        if not list(remove_card_allcards) == list(card):
            new_allcards.append(remove_card_allcards)
            print "YES"
        else:
            print "NO"
    allcards = new_allcards

    ###
def show_entry_fields():
    global allcards
    numbers.append(e1.get())
    e1.delete(0,END)
    global card_showentry_number
    card_showentry_number = 0
    for card in allcards:
        card_showentry_number = card_showentry_number + 1
        global bcard
        bcard = []
        for card_rows in card:
            bcard_lines = []
            for card_lines in card_rows:
                e = False
                for number in numbers:
                    try:
                        if int(number) == int(card_lines):
                            e = True
                    except:
                        pass
                if e:
                    bcard_lines.append(1)
                else:
                    bcard_lines.append(0)
            bcard.append(bcard_lines)
        if int(gamemode) == 1 or int(gamemode) == 3 or int(gamemode) == 7:
            if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1):
                win()
            elif int(bcard[1][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1):
                win()
            elif int(bcard[2][0]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[2][4]) == int(1):
                win()
            elif int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1):
                win()
            elif int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1):
                win()
            elif int(bcard[0][0]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[4][0]) == int(1):
                win()
            elif int(bcard[0][1]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][1]) == int(1):
                win()
            elif int(bcard[0][2]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[4][2]) == int(1):
                win()
            elif int(bcard[0][3]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][3]) == int(1):
                win()
            elif int(bcard[0][4]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][4]) == int(1):
                win()                                                                                                                                              
            elif int(bcard[0][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][4]) == int(1):
                win()
            elif int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1):
                win()
            elif int(bcard[0][0]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[4][4]) == int(1) and int(bcard[4][0]) == int(1):
                win()
            
            
        elif int(gamemode) == 2:
            d_bingo = 0
            if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[1][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[2][0]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[2][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][0]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[4][0]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][1]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][1]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][2]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[4][2]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][3]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][3]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][4]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][4]) == int(1):
                d_bingo = d_bingo + 1                                                                                                                                             
            if int(bcard[0][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][0]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[4][4]) == int(1) and int(bcard[4][0]) == int(1):
                d_bingo = d_bingo + 1 
            
            if int(d_bingo) > 2:
                win()
            
        elif int(gamemode) == 4:
            if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]):
                win()
        elif int(gamemode) == 5:
            def cor_b():
                int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1)
            def cor_c():
                int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1)
            def cor_a():
                int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[z][1]) == int(1)
            def cor_d():
                int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1)
            if cor_a() and cor_b():
                win()
            elif cor_a() and cor_c():
                win()
            elif cor_a() and cor_d():
                win()
            elif cor_b() and cor_c():
                win()
            elif cor_b() and cor_d():
                win()
            elif cor_c() and cor_d():
                win()
        elif int(gamemode) == 6:
            def cor_b():
                int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1)
            def cor_c():
                int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1)
            def cor_a():
                int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[z][1]) == int(1)
            def cor_d():
                int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1)
            if cor_c() and cor_d() and int(bcard[1][0]) and int(bcard[1][1]) and int(bcard[1][3]) and int(bcard[1][4]) and int(bcard[2][0]) and int(bcard[2][1]) and int(bcard[2][3]) and int(bcard[2][4]):
                win()
        elif int(gamemode) == 8: 
            pass
        elif int(gamemode) == 9:
            pass
        elif int(gamemode) == 10:
            d_bingo = 0
            if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[1][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[2][0]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[2][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][0]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[4][0]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][1]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][1]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][2]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[4][2]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][3]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][3]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][4]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][4]) == int(1):
                d_bingo = d_bingo + 1                                                                                                                                             
            if int(bcard[0][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][4]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1):
                d_bingo = d_bingo + 1
            if int(bcard[0][0]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[4][4]) == int(1) and int(bcard[4][0]) == int(1):
                d_bingo = d_bingo + 1 
            if int(d_bingo) == 13:
                win()
    return 
master = Tk()
Label(master, text="Number").grid(row=0)
e1 = Entry(master)
e1.insert(10,"0")
e1.grid(row=0, column=1)
Button(master, text='Check', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )
