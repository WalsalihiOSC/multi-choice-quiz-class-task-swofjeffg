from tkinter import *

QUESTION = "What is the capital of Mongolia?"
OPTIONS = ["Vladivostok", "Astana", "Ulan Bator", "Lhasa"]  # I'm from vladivostok haha
ANSWER_INDEX = OPTIONS.index("Ulan Bator")

class App:
    def __init__(self, parent):
        self.parent = parent
        
        self.answer = IntVar()   # answer given by user
        self.create_widgets()
        
    def create_widgets(self):
        super_frame = Frame(self.parent)
        super_frame.place(relx=.5, rely=.5, anchor=CENTER)
        
        Label(super_frame, text=f"Question:\n{QUESTION}").pack()
        self.output = Label(super_frame, text="Waiting for answer....")
        self.output.pack()
        for value, text in enumerate(OPTIONS):
            Radiobutton(super_frame, text=text, variable=self.answer, value=value, command=self.output_update).pack()
            
    def output_update(self):
        if self.answer.get() == ANSWER_INDEX:
            self.output['text']="Correct!"
        else:
            self.output['text']="Incorrect :("

if __name__ == '__main__':
    root = Tk()
    root.title("Mutli Choice Quiz!")
    root.geometry("250x250")
    App(root)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()