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
        number.append(self.txt1.text)

# run app
if __name__ == "__main__":
    MyApp().run()
