from tkinter import *

import calculator

class tkNumButton(Button):
    def __init__(self, master=None, **kw):
        self.master = master
        super().__init__(master, **kw)
        self['background'] = '#404040'
        self['foreground'] = '#FFFFFF'
        self['font'] = ('device',15)
        self['borderwidth'] = 0
        self['activebackground'] = '#272727'
        self['activeforeground'] = '#e8e8e8'

        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Configure>', self.fontsize)

    def on_enter(self, event):
        self['background'] = '#333333'

    def on_leave(self, event):
        self['background'] = '#404040'

    def fontsize(self, event):
        self['font'] = ('device', int(self.master.winfo_height()/28))

class tkOperationButton(Button):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self['background'] = '#333333'
        self['foreground'] = '#FFFFFF'
        self['font'] = ('device',15)
        self['borderwidth'] = 0
        self['activebackground'] = self['background']
        self['activeforeground'] = '#e8e8e8'

        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Configure>', self.fontsize)

    def on_enter(self, event):
        self['background'] = '#404040'

    def on_leave(self, event):
        self['background'] = '#333333'

    def fontsize(self, event):
        self['font'] = ('device', int(self.master.winfo_height()/28))

class tkEqualButton(Button):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self['background'] = '#b9b5f5'
        self['foreground'] = '#333333'
        self['font'] = ('device',15)
        self['borderwidth'] = 0
        self['activebackground'] = '#9b97d7'
        self['foreground'] = '#242424'

        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Configure>', self.fontsize)

    def on_enter(self, event):
        self['background'] = '#aaa6e6'

    def on_leave(self, event):
        self['background'] = '#b9b5f5'

    def fontsize(self, event):
        self['font'] = ('device', int(self.master.winfo_height()/28))

class tkNumDisplay(Label):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self['background'] = '#222222'
        self['foreground'] = '#FFFFFF'
        self['font'] = ('device',20)
        self['anchor'] = 'e'

        self.bind('<Configure>', self.fontsize)
        
    def fontsize(self, event):
        self['font'] = ('device', int(self.master.winfo_height()/15))

class App:
    def __init__(self, root):
        
        self.root = root
        self.nums = []
        self.operation = ''
        self.isFullNum = False
        self.NumButtons = []
        self.OperationButtons = []

        self.root.title("Calculator")
        self.root.geometry('800x450')

        self.root['background'] = '#222222'
        self.root.columnconfigure(0, weight = 1)
        self.root.columnconfigure(1, weight = 1)
        self.root.columnconfigure(2, weight = 1)
        self.root.columnconfigure(3, weight = 1)
        
        self.root.rowconfigure(0, weight = 1)
        self.root.rowconfigure(1, weight = 1)
        self.root.rowconfigure(2, weight = 1)
        self.root.rowconfigure(3, weight = 1)
        self.root.rowconfigure(4, weight = 1)
        self.root.rowconfigure(5, weight = 1)
        self.root.rowconfigure(6, weight = 1)

        self.display = StringVar()
        self.display.set(0)
        self.display_label = tkNumDisplay(self.root, textvariable=self.display)
        self.display_label['background'] = self.root['background']
        self.display_label.grid(column = 0, row = 0, columnspan = 4, sticky = (N,W,E,S))

        root.bind('0',self.num0)
        root.bind('1',self.num1)
        root.bind('2',self.num2)
        root.bind('3',self.num3)
        root.bind('4',self.num4)
        root.bind('5',self.num5)
        root.bind('6',self.num6)
        root.bind('7',self.num7)
        root.bind('8',self.num8)
        root.bind('9',self.num9)

        root.bind('=',self.equals)
        root.bind('<Return>',self.equals)

        root.bind("+", self.add)
        root.bind("-", self.subt)
        root.bind("*", self.mult)
        root.bind("/", self.div)

        root.bind('%',self.percent)

        root.bind('<BackSpace>',self.backspace)
        root.bind('C',self.cancel)

        #Number buttons
        for i in range(0, 10):
            self.NumButtons.append(tkNumButton(self.root, text=str(i)))
            self.NumButtons[i].grid(padx = 1, pady = 1, sticky = (N,W,E,S))
            if i != 0:
                self.NumButtons[i].grid_configure(column = ((i%3)-1) if i%3 > 0 else 2)
                if i==1 or i==2 or i==3:
                    self.NumButtons[i].grid_configure(row = 5)
                elif i==4 or i==5 or i==6:
                    self.NumButtons[i].grid_configure(row = 4)
                else:
                    self.NumButtons[i].grid_configure(row = 3)
            else:
                self.NumButtons[i].grid_configure(column = 1, row = 6)
        for i in ['+/-','.']:
            self.NumButtons.append(tkNumButton(self.root, text=i))
        self.NumButtons[10].grid(padx = 1, pady = 1, column = 0, row = 6, sticky=(N,W,E,S))
        self.NumButtons[11].grid(padx = 1, pady = 1, column = 2, row = 6, sticky=(N,W,E,S))
        
        self.NumButtons[9].configure(command = self.num9)
        self.NumButtons[8].config(command = self.num8)
        self.NumButtons[7]['command'] = self.num7
        self.NumButtons[6]['command'] = self.num6
        self.NumButtons[5]['command'] = self.num5
        self.NumButtons[4]['command'] = self.num4
        self.NumButtons[3]['command'] = self.num3
        self.NumButtons[2]['command'] = self.num2
        self.NumButtons[1]['command'] = self.num1
        self.NumButtons[0]['command'] = self.num0

        #Buttons for operations and backspace, cancel etc.
        for i in ['⌫','÷','×','-','+','%','CE','C','1/x','x²','√x']:
            self.OperationButtons.append(tkOperationButton(self.root, text=i))
        for i in range(0,5):
            self.OperationButtons[i].grid(padx = 1, pady = 1, column = 3, row = i+1, sticky=(N,W,E,S))
        for i in range(5,8):
            self.OperationButtons[i].grid(padx = 1, pady = 1, column = i-5, row = 1, sticky=(N,W,E,S))
        for i in range(8,11):
            self.OperationButtons[i].grid(padx = 1, pady = 1, column = i-8, row = 2, sticky=(N,W,E,S))

        self.OperationButtons[4]['command'] = self.add
        self.OperationButtons[3]['command'] = self.subt
        self.OperationButtons[2]['command'] = self.mult
        self.OperationButtons[1]['command'] = self.div

        self.OperationButtons[5]['command'] = self.percent
        self.OperationButtons[8]['command'] = self.reciprocal
        self.OperationButtons[9]['command'] = self.square
        self.OperationButtons[10]['command'] = self.sqroot

        self.OperationButtons[0]['command'] = self.backspace
        self.OperationButtons[7]['command'] = self.cancel
        
        #Equal Button
        self.EqualButton = tkEqualButton(self.root, text='=', command=self.equals)
        self.EqualButton.grid(row = 6, column = 3, sticky = (N,W,E,S))
        
    def num9(self, *event):
        if self.isFullNum == False:
            self.nums.append(9)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '9'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num8(self, *event):
        if self.isFullNum == False:
            self.nums.append(8)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '8'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num7(self, *event):
        if self.isFullNum == False:
            self.nums.append(7)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '7'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num6(self, *event):
        if self.isFullNum == False:
            self.nums.append(6)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '6'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num5(self, *event):
        if self.isFullNum == False:
            self.nums.append(5)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '5'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num4(self, *event):
        if self.isFullNum == False:
            self.nums.append(4)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '4'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num3(self, *event):
        if self.isFullNum == False:
            self.nums.append(3)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '3'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num2(self, *event):
        if self.isFullNum == False:
            self.nums.append(2)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '2'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num1(self, *event):
        if self.isFullNum == False:
            self.nums.append(1)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '1'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])
    def num0(self, *event):
        if self.isFullNum == False:
            self.nums.append(0)
            self.isFullNum = True
        else:
            self.nums[-1] = str(self.nums[-1]) + '0'
            self.nums[-1] = int(self.nums[-1])
        self.display.set(self.nums[-1])

    def add(self, *event):
        self.operation = 'add'
        self.isFullNum = False
        self.display.set('+')
    def subt(self, *event):
        if self.operation != '' and self.isFullNum == False:
          self.nums.append('-')
          self.display.set(self.nums[-1])
          self.isFullNum = True
        else:
          self.operation = 'subtract'
          self.isFullNum = False
          self.display.set('-')
    def mult(self, *event):
        self.operation = 'multiply'
        self.isFullNum = False
        self.display.set('×')
    def div(self, *event):
        self.operation = 'divide'
        self.isFullNum = False
        self.display.set('÷')

    def percent(self, *event):
        self.nums[-1] /= 100
        isFullNum = False
        self.display.set(self.nums[-1])
    def reciprocal(self, *event):
        self.nums[-1] = 1/self.nums[-1]
        isFullNum = False
        self.display.set(self.nums[-1])
    def square(self, *event):
        self.nums[-1] **= 2
        isFullNum = False
        self.display.set(self.nums[-1])
    def sqroot(self, *event):
        self.nums[-1] **= 0.5
        isFullNum = False
        self.display.set(self.nums[-1])

    def equals(self, *event): 
        result = calculator.calc(self.operation, self.nums)
        self.display.set(result)

        self.isFullNum = False
        self.nums = []
        self.operation = ''

    def backspace(self, *event):
        if self.display.get() == '+' or self.display.get() == '-' or self.display.get() == '×' or self.display.get() == '÷':
            self.display.set(self.nums[-1])
            self.operation = ''
            self.isFullNum = True
        elif self.nums == []:
            self.display.set(0)
            self.isFullNum = False
        elif self.display.get() == str(self.nums[-1]):
            if len(str(self.nums[-1])) > 1:
                num = list(str(self.nums[-1]))
                num.pop()
                self.nums[-1] = ''
                for i in range(len(num)):
                    self.nums[-1] += num[i]
                self.nums[-1] = int(self.nums[-1])
                self.display.set(self.nums[-1])
                self.isFullNum = True
            else:
                self.nums.pop()
                if self.operation != '':
                    if self.operation == 'add':
                        self.display.set('+')
                    elif self.operation == 'subtract':
                        self.display.set('-')
                    elif self.operation == 'multiply':
                        self.display.set('*')
                    elif self.operation == 'divide':
                        self.display.set('/')
                        
                    self.isFullNum = False
                else:
                    self.display.set(0)
                    self.isFullNum = False
                                
    def cancel(self, *event):
        self.isFullNum = False
        self.nums = []
        self.operation = ''
        self.display.set(0)
