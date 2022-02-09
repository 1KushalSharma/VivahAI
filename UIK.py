import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


kivy.require('2.0.0')

# colours used
LIGHT_BLUE = '#CCEDFF'
LIGHT_GRAY = '#F5F5F5'
OFF_WHITE = '#F8FAFF'
WHITE = '#FFFFFF'
GREEN = '#008000'
BLACK = '#000000'
RED = '#FF0000'

# fonts used
DEFAULT_FONT_STYLE = ('Arial', 20)
SMALL_FONT_STYLE =('Arial',16,'italic')
LARGE_FONT_STYLE = ('Arial', 40, 'bold')
DIGIT_FONT_STYLE = ('Arial', 24, 'bold')

class GridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text='Name:', font_size=25))
        self.Name = TextInput(multiline=False, font_size=25)
        self.add_widget(self.Name)
        
        self.add_widget(Label(text='Password:', font_size=25))
        self.password = TextInput(multiline=False, password=True, font_size=25)
        self.add_widget(self.password)
        
        # create a button
        self.submit = Button(text='Submit', font_size=25)
        self.add_widget(self.submit)
        
        # self.inside = GridLayout()
        # self.inside.cols = 2

class ADTV(App):
	# Function that returns the root widget
	def build(self):	
		return GridLayout()


ADTV().run()			
