import os

from PIL import Image as img, ImageTk
from textwrap import wrap
from tkinter import ttk
import tkinter as tk
from tkinter import *

from matplotlib import image
# from Clearing import Clear
import atexit
from tkinter import filedialog

from imageExtract import siteOpener

# from PIL import ImageTk
# from PIL import Image


atexit.register(print, "Program exited successfully!")
# For email
os.environ.setdefault('SENDER_EMAIL', "1rn18ec022.archindeepak@gmail.com")
os.environ.setdefault('SENDER_EMAIL_PASSWORD', "@rch1n2203")
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
SMALL_FONT_STYLE = ('Arial', 11, 'italic')
LARGE_FONT_STYLE = ('Arial', 40, 'bold')
DIGIT_FONT_STYLE = ('Arial', 24, 'bold')
SMALLEST_FONT_STYLE = ('Arial', 9, 'italic')


class UI:
    def __init__(self, article):
        self.articles = article
        self.window = tk.Tk()
        self.window.geometry('1920x1080')
        self.window.resizable(0, 0)
        self.window.wm_attributes('-fullscreen', 'True')

        # self.image = img.open('./src/wiki.jpg')
        # self.photo = ImageTk.PhotoImage(self.image)

        #  self.articles = 'Stephen Curry'
        # self.articles = 'Who is Usain Bolt'
        # self.articles='M S Dhoni'
        # self.articles = 'Barack Obama'
        # self.articles = 'Shah Rukh Khan'
        # self.articles = ''
        # self.articles = ''

        # self.articleSet=setArticle()
        self.main_frame = self.create_display_frame()
        self.frame1 = self.frame1_create_display()
        self.frame2 = self.frame2_create_display()
        self.frame3 = self.frame3_main_create_display()
        # self.frame3_1 = self.frame3_1_create_display()
        # self.frame3_2 = self.frame3_2_create_display()
        self.url = ''
        self.listURL = []
        self.write2 = self.frame2_text()
        self.image1 = self.frame1_images()
        self.write3_1 = self.frame3_1_text()

    #  def setArticle(self, article):
    #     self.articles = article

    def frame1_create_display(self):
        frame = tk.Frame(self.main_frame, width=960, height=1080, bg=BLACK)
        frame.pack(expand=True)
        # n(bottom), ne(bottom left), e(left), se(top left), s(top), sw(top right), w(right), nw(bottom right), or center
        frame.place(anchor='e', relx=0.5, rely=0.5)
        return frame

    def frame1_images(self):
        from start import nltkProcessing
        self.url, self.listURL = nltkProcessing(self.articles)
        siteOpener(self.url)
        nltkProcessing(self.articles)
        # image = img.open('3.png')
        # photo = ImageTk.PhotoImage(image)
        self.image = img.open('./src/wiki.jpg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(image=self.photo, width=650, height=1080, bg=BLACK)
        self.label.pack()
        self.label.place(x=-30, y=-85)
        return self.label

    def frame2_create_display(self):
        frame = tk.Frame(self.main_frame, width=960, height=600, bg=BLACK)
        frame.pack(expand=False)
        # n(bottom), ne(bottom left), e(left), se(top left), s(top), sw(top right), w(right), nw(bottom right), or center
        frame.place(anchor='sw', relx=0.5, rely=0.5)
        return frame

    def frame2_text(self):
        from aboutExtract import about
        canvas = Canvas(self.frame2, width=960, height=540)
        canvas.create_text(330, 375, text=about(self.articles), fill=BLACK, justify=LEFT, width=600,
                           font=SMALL_FONT_STYLE)
        canvas.pack()

    def frame3_main_create_display(self):
        frame = tk.Frame(self.main_frame, width=960, height=480, bg=LIGHT_BLUE)
        frame.pack(expand=True)
        # n(bottom), ne(bottom left), e(left), se(top left), s(top), sw(top right), w(right), nw(bottom right), or center
        frame.place(anchor='nw', relx=0.5, rely=0.5)
        return frame

    # def frame3_1_create_display(self):
    #     frame = tk.Frame(self.frame3, width=960, height=540, bg=GREEN)
    #     frame.pack(expand=True)
    #     # n(bottom), ne(bottom left), e(left), se(top left), s(top), sw(top right), w(right), nw(bottom right), or center
    #     frame.place(anchor='e', relx=0.5, rely=0.5)
    #     return frame

    def frame3_1_text(self):
        canvas = Canvas(self.frame3, width=960, height=400)
        canvas.create_text(620, 150, anchor='e', text=self.listURL, fill=BLACK, justify=LEFT, width=600,
                           font=SMALL_FONT_STYLE)
        canvas.pack()

    # def frame3_2_create_display(self):
    #     frame = tk.Frame(self.frame3, width=480, height=540)
    #     frame.pack(expand=True)
    #     # n(bottom), ne(bottom left), e(left), se(top left), s(top), sw(top right), w(right), nw(bottom right), or center
    #     frame.place(anchor='w', relx=0.5, rely=0.5)
    #     return frame

    def create_display_frame(self):
        frame = tk.Frame(self.window, width=1920, height=1080, bg=BLACK)
        frame.pack(expand=True, fill='both')
        return frame

    def siteOpener(self):
        import webbrowser
        webbrowser.open(self.url)

    def run(self):
        self.window.mainloop()

# Clear()
