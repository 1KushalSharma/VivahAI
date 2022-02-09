import tk as tk

from UI import UI
from start import nltkProcessing

class UI1:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1920x1080')
        self.window.resizable(0, 0)
        self.window.wm_attributes('-fullscreen', 'True')        
