from plugins import *


class Commands(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        # Initialize commands text
        self.commands_text = " Say 'What can I say' for list of commands..."
        self.commandLbl = Label(self, text= '', font=('Helvetica', small_text_size), fg="white",
                              bg="black")
        self.commandLbl.pack(fill="none", expand=True, anchor="center")

        self.user_command = ''
        self.responsLbl = Label(self, text='', font=('Helvetica', small_text_size), fg="white",
                                bg="black")
        self.responsLbl.pack(fill="none", expand=True, anchor="center")

    def command_actions(self, command):

        if command == 'weather':
            self.user_command = 'showing weather'
        elif command == 'news':
            self.user_command = 'showing news'

        else:
            self.user_command = 'not understood'

        self.responsLbl.config(text=self.user_command)