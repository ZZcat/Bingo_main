from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.bubble import Bubble
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
####

Builder.load_string('''
#template for menu items
[ListButton@ToggleButton]
    background_down: 'atlas://data/images/defaulttheme/bubble_btn'
    background_normal: 'atlas://data/images/defaulttheme/bubble_btn_pressed'
    group: 'context_menue_root'
    on_release: ctx.on_release(self) if hasattr(ctx, 'on_release') else None
    size_hint: ctx.size_hint if hasattr(ctx, 'size_hint') else (1, 1)
    width: ctx.width if hasattr(ctx, 'width') else 1
    text: ctx.text if hasattr(ctx, 'text') else ''
    Image:
        source: ctx.btn_img if ctx.text == 'hows' \
            else 'atlas://data/images/defaulttheme/bubble_btn'
        size: (20, 20)
        y: self.parent.y + (self.parent.height/2) - (self.height/2)
        x: self.parent.x + (self.parent.width - self.width)

<Test>
    Button:
        text: 'Gamemode'
        size_hint: .2, .2
        on_release:  root.add_menu(args[0])

<Cmenu>
    size_hint: None, None
    size: 240, 500
    pos: (5, 50)
    padding: 5
    background_color: .2, .9, 1, .7
    #wanna have some fun? set this to 'data/images/image-loading.gif'
    background_image: 'atlas://data/images/defaulttheme/button_pressed'
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: None, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Regular Bingo'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Double Bingo'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Small Picture Frame'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Double Postage Stamp'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Trails T'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Letter X'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Hardway Bingo'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Cover-all'
                        on_release: root.menu_selected
                        
                # end root menu
                #sub-menu
                BoxLayout:
                    ListButton:
                        # go back(root menu) button
                        text: '<'
                        size_hint: (.25, 1)
                        on_release: root.menu_selected
                #end sub-menu
''')


class Cmenu(Bubble):

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'
            global gamemode
            gamemode = l[0].text
            if gamemode == "Regular Bingo":
                gamemode = 1
            elif gamemode == "Double Bingo":
                gamemode = 2
            elif gamemode == "Small Picture Frame":
                gamemode = 4
            elif gamemode == "Double Postage Stamp":
                gamemode = 5
            elif gamemode == "Trails T":
                gamemode = 6
            elif gamemode == "Letter X":
                gamemode = 8
            elif gamemode == "Hardway Bingo":
                gamemode = 9
            elif gamemode == "Cover-all":
                gamemode = 10
            
            App.get_running_app().stop()

class Test(FloatLayout):

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

    def on_touch_down(self, *l):
        #allow kids to get touch
        if super(Test, self).on_touch_down(*l):
            return True
        # remove menu when touched and menu exists
        if hasattr(self, 'context_menu'):
            self.remove_widget(self.context_menu)

    def add_menu(self, obj, *l):
        if not hasattr(self, 'context_menu'):
            self.context_menu = Cmenu()
        self.remove_widget(self.context_menu)
        self.add_widget(self.context_menu)
        self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]

class MyApp(App):
    def build(self):
        return Test()
MyApp().run()
####
Builder.load_string('''
#template for menu items
[ListButton@ToggleButton]
    background_down: 'atlas://data/images/defaulttheme/bubble_btn'
    background_normal: 'atlas://data/images/defaulttheme/bubble_btn_pressed'
    group: 'context_menue_root'
    on_release: ctx.on_release(self) if hasattr(ctx, 'on_release') else None
    size_hint: ctx.size_hint if hasattr(ctx, 'size_hint') else (1, 1)
    width: ctx.width if hasattr(ctx, 'width') else 1
    text: ctx.text if hasattr(ctx, 'text') else ''
    Image:
        source: ctx.btn_img if ctx.text == 'hows' \
            else 'atlas://data/images/defaulttheme/bubble_btn'
        size: (20, 20)
        y: self.parent.y + (self.parent.height/2) - (self.height/2)
        x: self.parent.x + (self.parent.width - self.width)

<Test>
    Button:
        text: 'Gamemode'
        size_hint: .2, .2
        on_release:  root.add_menu(args[0])

<Cmenu>
    size_hint: None, None
    size: 240, 500
    pos: (5, 50)
    padding: 5
    background_color: .2, .9, 1, .7
    #wanna have some fun? set this to 'data/images/image-loading.gif'
    background_image: 'atlas://data/images/defaulttheme/button_pressed'
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: None, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: '1'
                        on_release: root.menu_selected
                    ListButton:
                        text: '2'
                        on_release: root.menu_selected
                    ListButton:
                        text: '3'
                        on_release: root.menu_selected
                    ListButton:
                        text: '4'
                        on_release: root.menu_selected
                    ListButton:
                        text: '5'
                        on_release: root.menu_selected
                    ListButton:
                        text: '6'
                        on_release: root.menu_selected
                    ListButton:
                        text: '7'
                        on_release: root.menu_selected
                    ListButton:
                        text: '8'
                        on_release: root.menu_selected
                        
                # end root menu
                #sub-menu
                BoxLayout:
                    ListButton:
                        # go back(root menu) button
                        text: '<'
                        size_hint: (.25, 1)
                        on_release: root.menu_selected
                #end sub-menu
''')


class Cmenu(Bubble):

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'
            global NumberOfCard
            NumberOfCard = l[0].text
            App.get_running_app().stop()


class Test(FloatLayout):

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

    def on_touch_down(self, *l):
        #allow kids to get touch
        if super(Test, self).on_touch_down(*l):
            return True
        # remove menu when touched and menu exists
        if hasattr(self, 'context_menu'):
            self.remove_widget(self.context_menu)

    def add_menu(self, obj, *l):
        if not hasattr(self, 'context_menu'):
            self.context_menu = Cmenu()
        self.remove_widget(self.context_menu)
        self.add_widget(self.context_menu)
        self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]

class MyApp(App):
    def build(self):
        return Test()
MyApp().run()
print "A "*100
##def show_entry_fields():
##    global gamemode
##    global NumberOfCard
##    NumberOfCard = (e2.get())
##    gamemode = (e1.get())
##    master.destroy()
##    return 
##master = Tk()
##master.wm_title("Bingo game")
##Label(master, text="1 - Regular Bingo\n2 - Double Bingo\n3 - Regular Bingo\n4 - Small Picture Frame\n5 - Double Postage Stamp\n6 - Trails T\n7 - Regular Bingo\n8 - Letter X\n9 - Hardway Bingo\n10 - Cover All\n\n").grid(row=0)
##Label(master, text="Number of cards    -->").grid(row=1)
##e1 = Entry(master)
##e2 = Entry(master)
##e1.insert(10,"Game #")
##e2.insert(10,"Cards")
##e1.grid(row=0, column=1)
##e2.grid(row=1, column=1)
##Button(master, text='Chose', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
##mainloop( )
###
global allcards
allcards = [[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]]##while not int(NumberOfCard) == 0:
##    root = Tk()
##    root.wm_title("Bingo card(free space is zero)    #"+str(NumberOfCard))
##    rows = []
##    for i in range(5):
##        cols = []
##        for j in range(5):
##            e = Entry(relief=RIDGE)
##            e.grid(row=i, column=j, sticky=NSEW)
##            e.insert(END, "3")
##            cols.append(e)
##        rows.append(cols)
##
##    card = []
##    card_line = []
##    def onPress():
##        for row in rows:
##            card_line = []
##            for col in row:
##                card_line.append(col.get())
##            card.append(card_line)
##        root.destroy()
##
##    Button(text='Set card', command=onPress).grid()
##    mainloop()
##    (NumberOfCard) = int(NumberOfCard) - 1
##    allcards.append(card)
###
numbers = [0]
bcard = []
print "\n\nb\n\n"
def win():
    global card
    global allcards
    itemN = 0
    print "WIN!!!  "*100
    new_allcards = []
    for remove_card_allcards in allcards:
        if not list(remove_card_allcards) == list(card):
            new_allcards.append(remove_card_allcards)
            print "YES"
        else:
            print "NO"
    allcards = new_allcards

    ###
def test_win():
    global allcards
    global numbers
    global card_showentry_number
    card_showentry_number = 0
    for card in allcards:
        global card
        card_showentry_number = card_showentry_number + 1
        global bcard
        bcard = []
        print "\n\n"
        print card
        for card_rows in card:
            bcard_lines = []
            print card_rows
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

class MyApp(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)
        layout.add_widget(self.txt1)
        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "Last number: " + self.txt1.text
        numbers.append(self.txt1.text)
        test_win()

MyApp().run()

##def win():
##    global allcards
##    master = Tk()
##    master.wm_title("You won!!!")
##    listbox = Listbox(master)
##    listbox.pack()
##    TrashABC = "Card:" ,card_showentry_number
##    listbox.insert(END, TrashABC)
##    itemN = 0
##    for item in bcard:
##        itemN = itemN + 1
##        listbox.insert(itemN,item)
##    new_allcards = []
##    for remove_card_allcards in allcards:
##        if not list(remove_card_allcards) == list(card):
##            new_allcards.append(remove_card_allcards)
##            print "YES"
##        else:
##            print "NO"
##    allcards = new_allcards
##
##    ###
##def show_entry_fields():
##    global allcards
##    numbers.append(e1.get())
##    e1.delete(0,END)
##    global card_showentry_number
##    card_showentry_number = 0
##    for card in allcards:
##        card_showentry_number = card_showentry_number + 1
##        global bcard
##        bcard = []
##        for card_rows in card:
##            bcard_lines = []
##            for card_lines in card_rows:
##                e = False
##                for number in numbers:
##                    try:
##                        if int(number) == int(card_lines):
##                            e = True
##                    except:
##                        pass
##                if e:
##                    bcard_lines.append(1)
##                else:
##                    bcard_lines.append(0)
##            bcard.append(bcard_lines)
##        if int(gamemode) == 1 or int(gamemode) == 3 or int(gamemode) == 7:
##            if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1):
##                win()
##            elif int(bcard[1][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1):
##                win()
##            elif int(bcard[2][0]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[2][4]) == int(1):
##                win()
##            elif int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1):
##                win()
##            elif int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1):
##                win()
##            elif int(bcard[0][0]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[4][0]) == int(1):
##                win()
##            elif int(bcard[0][1]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][1]) == int(1):
##                win()
##            elif int(bcard[0][2]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[4][2]) == int(1):
##                win()
##            elif int(bcard[0][3]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][3]) == int(1):
##                win()
##            elif int(bcard[0][4]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][4]) == int(1):
##                win()                                                                                                                                              
##            elif int(bcard[0][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][4]) == int(1):
##                win()
##            elif int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1):
##                win()
##            elif int(bcard[0][0]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[4][4]) == int(1) and int(bcard[4][0]) == int(1):
##                win()
##            
##            
##        elif int(gamemode) == 2:
##            d_bingo = 0
##            if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[1][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[2][0]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[2][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][0]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[4][0]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][1]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][1]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][2]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[4][2]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][3]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][3]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][4]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][4]) == int(1):
##                d_bingo = d_bingo + 1                                                                                                                                             
##            if int(bcard[0][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][0]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[4][4]) == int(1) and int(bcard[4][0]) == int(1):
##                d_bingo = d_bingo + 1 
##            
##            if int(d_bingo) > 2:
##                win()
##            
##        elif int(gamemode) == 4:
##            if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]):
##                win()
##        elif int(gamemode) == 5:
##            def cor_b():
##                int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1)
##            def cor_c():
##                int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1)
##            def cor_a():
##                int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[z][1]) == int(1)
##            def cor_d():
##                int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1)
##            if cor_a() and cor_b():
##                win()
##            elif cor_a() and cor_c():
##                win()
##            elif cor_a() and cor_d():
##                win()
##            elif cor_b() and cor_c():
##                win()
##            elif cor_b() and cor_d():
##                win()
##            elif cor_c() and cor_d():
##                win()
##        elif int(gamemode) == 6:
##            def cor_b():
##                int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1)
##            def cor_c():
##                int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1)
##            def cor_a():
##                int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[z][1]) == int(1)
##            def cor_d():
##                int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1)
##            if cor_c() and cor_d() and int(bcard[1][0]) and int(bcard[1][1]) and int(bcard[1][3]) and int(bcard[1][4]) and int(bcard[2][0]) and int(bcard[2][1]) and int(bcard[2][3]) and int(bcard[2][4]):
##                win()
##        elif int(gamemode) == 8: 
##            pass
##        elif int(gamemode) == 9:
##            pass
##        elif int(gamemode) == 10:
##            d_bingo = 0
##            if int(bcard[0][0]) == int(1) and int(bcard[0][1]) == int(1) and int(bcard[0][2]) == int(1) and int(bcard[0][3]) == int(1) and int(bcard[0][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[1][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[1][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[2][0]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[2][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[3][0]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[3][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[4][0]) == int(1) and int(bcard[4][1]) == int(1) and int(bcard[4][2]) == int(1) and int(bcard[4][3]) == int(1) and int(bcard[4][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][0]) == int(1) and int(bcard[1][0]) == int(1) and int(bcard[2][0]) == int(1) and int(bcard[3][0]) == int(1) and int(bcard[4][0]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][1]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][1]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][1]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][2]) == int(1) and int(bcard[1][2]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][2]) == int(1) and int(bcard[4][2]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][3]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][3]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][3]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][4]) == int(1) and int(bcard[1][4]) == int(1) and int(bcard[2][4]) == int(1) and int(bcard[3][4]) == int(1) and int(bcard[4][4]) == int(1):
##                d_bingo = d_bingo + 1                                                                                                                                             
##            if int(bcard[0][0]) == int(1) and int(bcard[1][1]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][3]) == int(1) and int(bcard[4][4]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][4]) == int(1) and int(bcard[1][3]) == int(1) and int(bcard[2][2]) == int(1) and int(bcard[3][1]) == int(1) and int(bcard[4][0]) == int(1):
##                d_bingo = d_bingo + 1
##            if int(bcard[0][0]) == int(1) and int(bcard[4][0]) == int(1) and int(bcard[0][4]) == int(1) and int(bcard[4][4]) == int(1) and int(bcard[4][0]) == int(1):
##                d_bingo = d_bingo + 1 
##            if int(d_bingo) == 13:
##                win()
##    return 
##master = Tk()
##Label(master, text="Number").grid(row=0)
##e1 = Entry(master)
##e1.insert(10,"0")
##e1.grid(row=0, column=1)
##Button(master, text='Check', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
##mainloop( )
