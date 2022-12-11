import tkinter


class Calculator:
    def __init__(self):
        self.state = False
        self.result = 0
        self.text = ""
        self.row = 0
        self.col = 0
        self.createCalc()

    def createCalc(self):
        btns_list = ["CLR", 0, "ON", 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", "/", "(", "*", ")", "**", "=", "DEL"]
        for btn in btns_list:
            self.createBtns(btn)
            self.col = self.col + 1
            self.col = self.col % 3
            if self.col == 0:
                self.row = self.row + 1

    def btnClicked(self, txt):
        if txt == "ON":
            self.state = True
        if self.state:
            input_box = tkinter.Entry(bg="gray", fg="white", width=30, font=('New Times Roman', 18, "bold"))
            input_box.grid(row=self.row, columnspan=3, pady=(20, 20))
            input_box.focus()
            if txt == "CLR" or txt == "ON":
                self.text = ""
                input_box.insert(0, self.text)
            else:
                if txt == "=":
                    if self.text == "":
                        input_box.insert(0, 0)
                    else:
                        '''Reference to eval():
                        https://realpython.com/python-eval-function/
                        '''
                        self.result = eval(self.text)
                        # print(self.text, self.result)
                        input_box.delete(0, "end")
                        input_box.insert(0, self.result)
                        self.text = ""
                elif txt == "DEL":
                    if self.text != "":
                        self.text = self.text[:-1]
                        input_box.insert(0, self.text)
                else:
                    self.text = self.text + str(txt)
                    input_box.insert(0, self.text)

    def createBtns(self, btn):
        btn = tkinter.Button(text=btn, command=lambda: self.btnClicked(btn.cget('text')))
        btn.grid(column=self.col, row=self.row, padx=3, pady=3)
        btn.config(width=8, height=2, font=('New Times Roman', 18, "bold"))


if __name__ == '__main__':
    calc_window = tkinter.Tk()
    calc_window.title("Python Calculator".upper())
    # calc_window.minsize(width=800, height=600)
    calc_window.config(bg='#f7f5dd')

    calc = Calculator()

    calc_window.mainloop()
