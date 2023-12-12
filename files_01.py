# по книге по книге Микки Нардо - Учебное пособие по Tkinter для новичков
# импортирование модулей python
from tkinter import *
import os, string

# класс диалога для работы с файлами
class files:
  def __init__(self, master = None):
    self.toplevel = Toplevel(master)
    self.toplevel.geometry('400x300+200+150')
    self.bottomFrame = Frame(self.toplevel)
    self.bottomFrame.pack(side=BOTTOM, pady=5 )
    self.accept_button = Button(self.bottomFrame,
                                width=7,
                                text="accept",
                                command=self.accept)
    self.accept_button.pack(side=LEFT, expand=YES, padx=8)
    self.cancel_button = Button(self.bottomFrame,
                                width=7,
                                text="cancel",
                                command = self.cancel)
    self.cancel_button.pack(side=RIGHT, expand=YES, padx=8)
    self.selectionFrame = Frame(self.toplevel)
    self.selectionFrame.pack(side=BOTTOM, padx=36, pady=5, fill=X)
    self.selection = Entry(self.selectionFrame, background = 'white')
    self.selection.pack(side=LEFT, expand=YES, fill=X)
    self.directoryFrame = Frame(self.toplevel)
    self.directoryFrame.pack(side=TOP, pady=8)
    self.directory = self.createMenu(self.directoryFrame)
    self.directory.pack(side=LEFT, expand=YES, fill=X)
    self.labelFrame = Frame(self.toplevel)
    self.labelFrame.pack(side=TOP, padx=5, fill=X)
    self.folderLabel = Label(self.labelFrame, text = 'folders:')
    self.folderLabel.pack(side=LEFT, expand=YES, fill=X)
    self.fileLabel = Label(self.labelFrame, text = ' files: ')
    self.fileLabel.pack(side=RIGHT, expand=YES, fill=X)
    self.middleFrame = Frame(self.toplevel)
    self.middleFrame.pack(expand=YES, padx=5, fill=BOTH)
    self.filesBar = Scrollbar(self.middleFrame)
    self.filesBar.pack(side=RIGHT, fill=Y)
    self.files = Listbox(self.middleFrame,
                         background = 'white',
                         exportselection=0,
                         yscrollcommand=(self.filesBar, 'set'))
    self.files.pack(side=RIGHT, expand=YES, fill=BOTH)
    btags = self.files.bindtags()

    self.files.bindtags(btags[1:] + btags[:1])
    self.files.bind('<ButtonRelease-1>', self.files_select_event)
    self.files.bind('<Double-ButtonRelease-1>', self.files_double_event)
    self.filesBar.configure(command = self.files.yview)
    self.subBar = Scrollbar(self.middleFrame)
    self.subBar.pack(side=LEFT, fill=Y)
    self.subDirectory = Listbox(self.middleFrame,
                                background = 'white',
                                exportselection=0,
                                yscrollcommand=(self.subBar, 'set'))
    self.subDirectory.pack(side=LEFT, expand=YES, fill=BOTH)
    self.subBar.configure(command = self.subDirectory.yview)
    btags = self.subDirectory.bindtags()
    self.subDirectory.bindtags(btags[1:] + btags[:1])
    self.subDirectory.bind('<ButtonRelease-1>', self.subDirectory_select_event)

# добавление элемента управления меню каталогов в диалог для работы с файлами
  def createMenu(self, master = None):
    self.button = Menubutton(master, indicatoron=1, relief = RAISED)
    self.button.pack()
    self.menu = Menu(self.button, tearoff = 0)
    self.button.configure(menu = self.menu)
    return self.button

# обновление изображения при выделении пользователем новых элементов
  def refreshDisplay(self, pathString):
    self.myDirectory = pathString
    myList = self.parseDirectory(self.myDirectory)
    self.button.configure(text = myList[0])
    self.menu.delete(0, END)
    for i in myList[1:]:
      self.menu.add_command(label = i, command = self.evaluateDirectory)
    try:
      names = os.listdir(self.myDirectory)
    except os.error:
      self.toplevel.bell()
      return
    names.sort()
    if (self.myDirectory == os.sep) or (not os.sep in self.myDirectory):
      subdirs = []
    else:
      subdirs = [os.pardir]
    matchingfiles = []
    for name in names:
      fullname = os.path.join(self.myDirectory, name)
      if os.path.isdir(fullname) and name[0] != '.':
        subdirs.append(name)
      elif name[0] != '.':
        matchingfiles.append(name)
    self.subDirectory.delete(0, END)
    for name in subdirs:
      self.subDirectory.insert(END, name)
    self.files.delete(0, END)
    for name in matchingfiles:
      self.files.insert(END, name)
    self.set_selection('')

# анализ имени директории для меню каталогов
  def parseDirectory(self, directoryString):
    if directoryString == os.sep:
      return [directoryString]
    if not os.sep in directoryString:
      return [directoryString]
    myList = []
    myString = ''
    myElements = string.split(directoryString, os.sep)
    for element in myElements:
      myString = myString + element
      if element == '':
        myString = os.path.normpath(myString + os.sep)
        myPost = ''
      else:
        myPost = os.sep
      myList.append(myString)
      myString = myString + myPost
    myList.reverse()
    return myList

# обработка строки с именем текущего каталога
  def evaluateDirectory(self):
    self.refreshDisplay(self.menu.entrycget(ACTIVE, 'label'))

# переменной selection присваивается значение, равное имени файла
  def set_selection(self, file):
    self.selection.delete('0', END)
    self.selection.insert('0', file)

# возвращает имя выделенного файла из переменной selection
  def get_selection(self):
    return self.selection.get()

# при щелчке мышкой по списку подкаталогов
  def subDirectory_select_event(self, event):
    subdir = self.subDirectory.get('active')
    self.refreshDisplay(os.path.normpath(os.path.join(self.myDirectory, subdir)))

# при щелчке мышкой по списку файлов
  def files_select_event(self, event):
    self.set_selection(self.files.get('active'))

# при двойном щелчке мышкой по списку файлов
  def files_double_event(self, event):
    self.accept()

# запуск диалога
  def go(self, title = 'file dialog', startPath = os.getcwd()):
    self.newValue = None
    self.toplevel.title(title)
    if os.path.isfile(startPath):
      startPath, myFile = os.path.split(startPath)
      self.refreshDisplay(startPath)
      self.set_selection(myFile)
    else:
      self.refreshDisplay(startPath)
    self.toplevel.grab_set()
    self.toplevel.focus_set()
    self.toplevel.wait_window()
    return self.newValue

# при нажатии мышкой на кнопку accept
  def accept(self):
    self.newValue = self.get_selection()
    self.toplevel.destroy()

# при нажатии мышкой на кнопку cancel
  def cancel(self):
    self.toplevel.destroy()

# диалог открытия файлов
class openDialog(files):
  def accept(self):
    self.myFile = os.path.join(self.myDirectory, self.get_selection())
    self.newValue = None
    if os.path.isfile(self.myFile):
      self.newValue = self.myFile
      self.toplevel.destroy()
    else:
      message(title = 'error',
              message =  self.myFile + ' is not a file',
              geometry = '250x70+387+349')

# диалог сохранения файлов
class saveDialog(files):
  def accept(self):
    self.myFile = os.path.join(self.myDirectory, self.get_selection())
    self.newValue = None
    if os.path.isdir(self.myFile):
      message(title = self.myFile,
              message = 'Please enter a file name.',
              geometry = '250x70+387+349')
    elif os.path.isfile(self.myFile):
        self.dialog = question()
        self.answer = self.dialog.go(
                      title = self.myFile,
                      message = 'This file exists!\nOverwrite it?')
        if self.answer:
          self.newValue = self.myFile
          self.toplevel.destroy()
    else:
        self.newValue = self.myFile
        self.toplevel.destroy()

# класс окна вопросов
class question:
  def __init__(self, master = None):
    self.top = Toplevel(master)
    self.frame = Frame(self.top)
    self.frame.pack(side = BOTTOM)
    self.yes_button = Button(self.frame,
                                text = 'yes',
                                command = self.yes)
    self.yes_button.pack(side = LEFT)
    self.no_button = Button(self.frame,
                                text = 'no',
                                command = self.no)
    self.no_button.pack(side = RIGHT)
    self.label = Label(self.top)
    self.label.pack(side = TOP,
                   fill = BOTH,
                   expand = YES)
    self.top.protocol('WM_DELETE_WINDOW', self.no)

  def go(self, title = 'question',
               message = 'question goes here!',
               geometry =  '200x100+412+334'):
    self.top.title(title)
    self.top.geometry(geometry)
    self.label.configure(text = message)
    self.booleanValue = None
    self.top.grab_set()
    self.top.focus_set()
    self.top.wait_window()
    return self.booleanValue

  def yes(self):
    self.booleanValue = TRUE
    self.top.destroy()

  def no(self):
    self.booleanValue = FALSE
    self.top.destroy()

# класс окна сообщений
class message:
  def __init__(self, master = None, title = 'message',
                             message = 'Under construction!',
                             geometry = '150x70+437+349'):
    self.top = Toplevel(master)
    self.top.title(title)
    self.top.geometry(geometry)
    self.ok_button = Button(self.top, text = 'ok', command = self.ok)
    self.ok_button.pack(side = BOTTOM)
    self.label = Label(self.top, text = message)
    self.label.pack(side = TOP, fill = BOTH, expand = YES)
    self.top.grab_set()
    self.top.focus_set()
    self.top.wait_window()

  def ok(self):
    self.top.destroy()

# тестовая команда
if __name__ == '__main__':
  root = Tk()
  root.withdraw()
  myTest1 = openDialog(root)
  print(myTest1.go(title = 'open file dialog'))
  myTest2 = saveDialog(root)
  print(myTest2.go(title = 'save file dialog'))