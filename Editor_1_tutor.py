# по книге по книге Микки Нардо - Учебное пособие по Tkinter для новичков

# импортирование модулей python
from tkinter import *

# класс родительского окна
class main:
  def __init__(self, master):
    self.master = master
    self.master.title('editor')
    self.master.iconname('editor')
    self.master.geometry('600x400+100+100')
    self.myBar = Frame(self.master, height=4, relief = RAISED, bd=2)
    self.fileMenu()
    self.editMenu()
    self.myBar.pack(side = TOP, expand = YES, fill = BOTH)
    self.myScroll = Scrollbar(self.master)
    self.myScroll.pack(side=RIGHT, fill=Y)
    self.myText = Text(self.master,
                       background = 'white',
                       height = 30,
                       width = 90,
                       yscrollcommand=(self.myScroll, 'set'))
    self.myText.pack(side=LEFT, fill=BOTH, expand=YES)
    self.myScroll.configure(command = self.myText.yview)
    self.master.protocol('WM_DELETE_WINDOW', self.exitMethod)
    self.master.mainloop()

# добавление меню file в панель меню
  def fileMenu(self):
    mButton = Menubutton(self.myBar,
                         text = 'file  ',
                         font= 14,
                         underline = 0)
    mButton.pack(side = LEFT)
    menu = Menu(mButton, tearoff = 0)
    menu.add_command(label = 'new',
                     underline = 0,
                     command = self.getMessage)
    menu.add_command(label = 'open...',
                     underline = 0,
                     command = self.getMessage)
    menu.add_separator({})
    menu.add_command(label = 'save',
                     underline = 0,
                     command = self.getMessage)
    menu.add_command(label = 'save as...',
                     underline = 5,
                     command = self.getMessage)
    mButton.configure(menu = menu)
    return mButton

# добавление меню edit в панель меню
  def editMenu(self):
    mButton = Menubutton(self.myBar, text = 'edit  ', font=14, underline = 0)
    mButton.pack(side = LEFT)
    menu = Menu(mButton, tearoff = 0)
    menu.add_command(label = 'cut',
                     underline = 2,
                     command = self.getMessage)
    menu.add_command(label = 'copy',
                     underline = 0,
                     command = self.getMessage)
    menu.add_command(label = 'paste',
                     underline = 0,
                     command = self.getMessage)
    menu.add_separator({})
    menu.add_command(label = 'find...',
                     underline = 0,
                     command = self.getMessage)
    menu.add_command(label = 'find next',
                     underline = 5,
                     command = self.getMessage)
    menu.add_command(label = 'replace...',
                     underline = 0,
                     command = self.getMessage)
    mButton.configure(menu = menu)
    return mButton

# выход из редактора
  def exitMethod(self):
    self.dialog = yesno(self.master)
    self.myMssg = 'Do you want to exit?'
    self.returnValue = self.dialog.go(message = self.myMssg)
    if self.returnValue:
      self.master.destroy()

# вызов родового [generic] сообщения
  def getMessage(self):
    message(self.master)

# класс окна сообщений
class message:
  def __init__(self, master = None, title = 'message',
                                    message = 'Under construction!',
                                    geometry = '150x70+325+265'):
    self.top = Toplevel(master)
    self.top.title(title)
    self.top.geometry(geometry)
    self.ok_button = Button(self.top,
                            text = 'ok',
                            command = self.ok)
    self.ok_button.pack(side = BOTTOM)
    self.label = Label(self.top,
                       text = message)
    self.label.pack(side = TOP, fill = BOTH, expand = YES)
    self.top.grab_set()
    self.top.focus_set()
    self.top.wait_window()

  def ok(self):
    self.top.destroy()

# класс диалогового окна выхода
class yesno:
  def __init__(self, master):
    self.slave = Toplevel(master)
    self.frame = Frame(self.slave)
    self.frame.pack(side = BOTTOM)
    self.yes_button = Button(self.frame,
                             text = 'yes',
                             command = self.yes)
    self.yes_button.pack(side = LEFT)
    self.no_button = Button(self.frame,
                            text = 'no',
                            command = self.no)
    self.no_button.pack(side = RIGHT)
    self.label = Label(self.slave)
    self.label.pack(side = TOP,
                    fill = BOTH,
                    expand = YES)
    self.slave.protocol('WM_DELETE_WINDOW', self.no)

  def go(self, title = 'question',
               message = '[question goes here]',
               geometry = '200x70+300+265'):
    self.slave.title(title)
    self.slave.geometry(geometry)
    self.label.configure(text = message)
    self.booleanValue = TRUE
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()
    return self.booleanValue

  def yes(self):
    self.booleanValue = TRUE
    self.slave.destroy()

  def no(self):
    self.booleanValue = FALSE
    self.slave.destroy()

# создание окна
root = Tk()

# запуск окна
main(root)

