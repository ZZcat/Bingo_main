from Tkinter import *

root = Tk()
root.wm_title("Bingo card")
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

numbers = []
bcard = []

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
                    print "Yes"
            if e:
                bcard_lines.append(1)
            else:
                bcard_lines.append(0)
        bcard.append(bcard_lines)
    if bcard[1][0]==1 and bcard[1][1]==1 and bcard[1][2]==1 and bcard[1][3]==1 and bcard[1][4]==1 and 
    print bcard
    return bcard
master = Tk()
Label(master, text="Number").grid(row=0)
e1 = Entry(master)
e1.insert(10,"0")
e1.grid(row=0, column=1)
Button(master, text='Check', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )
print bcard
