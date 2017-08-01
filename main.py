from Tkinter import *



def show_entry_fields():
    global gamemode
    gamemode = (e1.get())
    return gamemode
master = Tk()
master.wm_title("Bingo game")
Label(master, text="1(Regular bingo)\n 2(Double bingo)\n 3(Small picture frame)\n 4(Double postage stamp)\n 5(Trails T)\n 6(Letter x)\n 7(Hardway bingo)\n 8(Cover-all)").grid(row=0)
e1 = Entry(master)
e1.insert(10,"0")
e1.grid(row=0, column=1)
Button(master, text='Chose', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )
###
print gamemode

root = Tk()
root.wm_title("Bingo card(free space is zero)")
rows = []
for i in range(5):
    cols = []
    for j in range(5):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d%d' % (i, j))
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
    print card

Button(text='Set card', command=onPress).grid()
mainloop()

###

numbers = [0]
bcard = []

def win():
    print "WIN!!!",bcard

def show_entry_fields():
    bcard = []
    numbers.append(e1.get())
    e1.delete(0,END)
    for card_rows in card:
        bcard_lines = []
        for card_lines in card_rows:
            e = False
            for number in numbers:
                if int(number) == int(card_lines):
                    e = True
            if e:
                bcard_lines.append(1)
            else:
                bcard_lines.append(0)
        bcard.append(bcard_lines)
    if int(gamemode) == 1:
        if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1):
            win()
        if int(bcard[1][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1):
            win()
        if int(bcard[2][0]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[2][4]) == int(1):
            win()
        if int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1):
            win()
        if int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1):
            win()
        if int(bcard[0][0]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[4][0]) == int(1):
            win()
        if int(bcard[0][1]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][1]) == int(1):
            win()
        if int(bcard[0][2]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[4][2]) == int(1):
            win()
        if int(bcard[0][3]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][3]) == int(1):
            win()
        if int(bcard[0][4]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][4]) == int(1):
            win()                                                                                                                                              
        if int(bcard[0][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][4]) == int(1):
            win()
        if int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1):
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
        
        if int(d_bingo) > 2:
            win()
        
    elif int(gamemode) == 3:
        if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]):
            win()
    elif int(gamemode) == 4:
        pass
    elif int(gamemode) == 5:
        pass
    elif int(gamemode) == 6:
        pass
    elif int(gamemode) == 7:
        pass
    elif int(gamemode) == 8:
        pass
    
    
    return bcard
master = Tk()
Label(master, text="Number").grid(row=0)
e1 = Entry(master)
e1.insert(10,"0")
e1.grid(row=0, column=1)
Button(master, text='Check', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )
