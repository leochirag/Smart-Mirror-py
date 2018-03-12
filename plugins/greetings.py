from plugins import *


class Greetings(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        # Initialize main greetings
        self.main_greeting = ''
        self.mainLbl = Label(self, font=('Helvetica', large_text_size), fg="white", bg="black")
        self.mainLbl.pack(fill="none", expand=True)
        # self.timeLbl.place(relx=.5, rely=.5, anchor="center")
        # Initialize Dobby's replies
        self.dobby_greeting = ''
        self.dobbyLbl = Label(self, text=self.dobby_greeting, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.dobbyLbl.pack(fill="none", expand=True)


        self.greet()

    def greet(self):
        self.main_greeting = 'Hello Buddy!!'
        self.dobby_greeting = 'Hello, Dobby here ..'
        self.mainLbl.config(text=self.main_greeting)
        self.dobbyLbl.config(text=self.dobby_greeting)
