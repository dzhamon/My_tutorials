# Учебны материал по книге Микки Нардо - Учебное пособие по Tkinter для новичков

"""
# LESSON 1 Создание родительских и дочерних окон
from tkinter import *

# создаем класс родительских окон

class main:
	def __init__(self, master):  # конструктор для создания экземпляра объекта
		self.master = root  # создается переменная master, и ей присваивается глобальное знач root
		self.master.title('parent')
		self.master.geometry('200x150+200+150')
		# child() # вызов другого класса, сгенериованного в модуле
		self.master.mainloop()
		
	# классы дочерних окон
		class child:
			def __init__(self):
				self.slave = Toplevel(root)
				self.slave.title('child')
				self.slave.geometry('200x150+400+300')

# создание окна
root = Tk()
# Запуск окна
main(root)
"""

"""# LESSON 2 -------- МЕТОДЫ --------

from tkinter import *

class main:
	def __init__(self, master):
		self.master = root
		self.master.title('parent')
		self.master.geometry('200x150+200+150')
		self.button = Button(self.master,
		                     text='MyButton',
		                     command=self.openDialog) # в классе main мы создали новый объект-виджет
		self.button.pack(side = BOTTOM)
		self.master.mainloop()
	def openDialog(self): # это введенный метод класса main. Он создает экземпляр объекта child (экземпляр класса main
		child(self.master)
	
class child:
	def __init__(self, master):
		self.slave = Toplevel(master)
		self.slave.title('child')
		self.slave.geometry('200x150+400+300')

root = Tk()
main(root)
"""

# LESSON 3 ---- Отсылка сообщений из родительского окна дочернему
"""
from tkinter import *


class main:
	def __init__(self, master):
		self.master = root
		self.master.title('parent')
		self.master.geometry('200x150+200+150')
		self.button = Button(self.master,
		                     text='MyButton',
		                     command=self.openDialog)
		self.button.pack(side=BOTTOM)
		self.text = Text(self.master,
		                 background='white') # создается Text, содержимое которого будет передано в дочерн окно
		self.text.pack(side=TOP,
		               fill=BOTH,
		               expand=YES)
		self.master.mainloop()
	
	def openDialog(self):
		child(self.master, self.text.get('0.0', END)) # содержимое текста родительского окна
															  # принимается (get) и передается дочке

class child:
	def __init__(self, master, myText=''):
		self.slave = Toplevel(master)
		self.slave.title('child')
		self.slave.geometry('200x150+400+300')
		self.text = Text(self.slave,
		                 background='white') # в дочке создается Text, который отобразит полученное от родителя
		self.text.pack(side=TOP,
		               fill=BOTH,
		               expand=YES)
		self.text.insert('0.0', myText) # вставку текста делает insert
		self.slave.grab_set()
		self.slave.focus_set()
		self.slave.wait_window()

root = Tk()
main(root)
"""
"""
# LESSON 4 ----- Отсылка сообщений в обоих направлениях-----

from tkinter import *

class main:
	def __init__(self, master):
		self.master = master
		self.master.title('parent')
		self.master.geometry('200x150+200+150')
		self.button = Button(self.master,
		                     text='dialog',
		                     command=self.openDialog)
		self.button.pack(side=BOTTOM)
		self.text = Text(self.master,
		                 background='white')  # создается Text, содержимое которого будет передано в дочерн окно
		self.text.pack(side=TOP,
		               fill=BOTH,
		               expand=YES)
		self.master.mainloop()
	
	def openDialog(self):
		self.dialog = child(self.master)
		print(123)
		self.sendValue = self.text.get(0.0, END)
		self.returnValue = self.dialog.go(self.sendValue)
		print(self.returnValue)
		if self.returnValue:
			self.text.delete(0.0,END)
			self.text.insert(0.0, self.returnValue)


class child:
	def __init__(self, master):
		self.slave = Toplevel(master)
		self.slave.title('child')
		self.slave.geometry('200x150+400+300')
		
		self.button = Button(self.slave,
		                     text='accept',
		                     command=self.accept)
		self.button.pack(side=BOTTOM)
		
		self.text = Text(self.slave,
		                 background='white')  # в дочке создается Text, который отобразит полученное от родителя
		self.text.pack(side=TOP,
		               fill=BOTH,
		               expand=YES)
		
	def go(self, myText = ''):
		self.text.insert('0.0', myText)  # вставку текста делает insert
		self.newValue = None
		self.slave.grab_set()
		self.slave.focus_set()
		self.slave.wait_window()
		return self.newValue
		
	def accept(self):
		self.newValue = self.text.get(0.0, END)
		self.slave.destroy()
		
root = Tk()
main(root)
"""

"""
# LESSON 5 -------- Усложнение диалогов-------
from tkinter import *

class main:
	def __init__(self, master):
		self.master = master
		self.master.title('parent')
		self.master.geometry('400x300+200+150')
		self.button = Button(self.master,
		                     text='dialog',
		                     command=self.openDialog)
		self.button.pack(side=BOTTOM)
		self.text = Text(self.master,
		                 background='white')
		self.text.pack(side=TOP,
		               fill=BOTH,
		               expand=YES)
		self.master.protocol('WM_DELETE_WINDOW',
		                     self.exitMethod)
		self.master.mainloop()
	
	def openDialog(self):
		self.dialog = child(self.master)
		self.sendValue = self.text.get('0.0', END)
		self.returnValue = self.dialog.go(self.sendValue)
		if self.returnValue:
			self.text.delete('0.0', END)
			self.text.insert('0.0', self.returnValue)
	
	def exitMethod(self):
		self.dialog = yesno(self.master)
		self.returnValue = self.dialog.go('question',
		                                  'Do you want to exit?')
		if self.returnValue:
			self.master.destroy()
			
# класс дочернего окна
class child:
	def __init__(self, master):
		self.slave = Toplevel(master)
		self.slave.title('child')
		self.slave.geometry('200x150+500+375')
		self.frame = Frame(self.slave)
		self.frame.pack(side = BOTTOM)
		self.accept_button = Button(self.frame,
	                                text = 'accept',
	                                command = self.accept)
		self.accept_button.pack(side = LEFT)
		self.cancel_button = Button(self.frame,
	                                text = 'cancel',
	                                command = self.cancel)
		self.cancel_button.pack(side = RIGHT)
		self.text = Text(self.slave, background = 'white')
		self.text.pack(side = TOP, fill = BOTH, expand = YES)
		self.slave.protocol('WM_DELETE_WINDOW', self.cancel)
	
	def go(self, myText=''):
		self.text.insert('0.0', myText)
		self.newValue = None
		self.slave.grab_set()
		self.slave.focus_set()
		self.slave.wait_window()
		return self.newValue
	
	def accept(self):
		self.newValue = self.text.get('0.0', END)
		self.slave.destroy()
	
	def cancel(self):
		self.slave.destroy()

# класс диалогового окна выхода
class yesno:
	def __init__(self, master):
		self.slave = Toplevel(master)
		self.slave.title('exit dialog')
		self.slave.geometry('200x100+300+250')
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
		self.label.pack(side = TOP, fill = BOTH, expand = YES)
		self.slave.protocol('WM_DELETE_WINDOW', self.no)

	def go(self, title = '', message = ''):
		self.slave.title(title)
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
"""

# LESSON 6 -------- Пример разбиения программы на несколько модулей------
# Принцип организации - в книге.

# LESSON 7 ------------ Управление файлами ---------------------
