'''

import pyautogui as pg
import csv
import os
from datetime import datetime as dt


timex = str(dt.now()).split()[0]
namex = pg.prompt("Enter Name :")
addx = pg.prompt("Enter Address")
gstx = pg.prompt("Enter GSTIN :")

items = []
total =0
while True :
    itemx = pg.prompt("Enter Items Name ")
    sizx = pg.prompt("Enter " + itemx+" Size")
    ratex = pg.prompt("Enter " + itemx+" Rate")
    quantity = pg.prompt("Enter " + itemx+" Quantity")
    


print(timex)



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(200,200,1280,720)
win.setWindowTitle("My Anime")



label = QtWidgets.QLabel(win)
label.setText("My Anime")
label.move(400,400)















win.show()

sys.exit(app.exec_())
'''


from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator 


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

	first_num = None         
	userIsTypingSecondNumber = False   #remains false unless any binary operator is pressed

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

		#connecting the buttons to the window
		self.pushButton_0.clicked.connect(self.digit_pressed)
		self.pushButton_1.clicked.connect(self.digit_pressed)
		self.pushButton_2.clicked.connect(self.digit_pressed)
		self.pushButton_3.clicked.connect(self.digit_pressed)
		self.pushButton_4.clicked.connect(self.digit_pressed)
		self.pushButton_5.clicked.connect(self.digit_pressed)
		self.pushButton_6.clicked.connect(self.digit_pressed)
		self.pushButton_7.clicked.connect(self.digit_pressed)
		self.pushButton_8.clicked.connect(self.digit_pressed)
		self.pushButton_9.clicked.connect(self.digit_pressed)

		self.pushButton_deci.clicked.connect(self.decimal_pressed)

		self.pushButton_mrc.clicked.connect(self.unary_operation_press)
		
		self.pushButton_persent.clicked.connect(self.unary_operation_press)


		self.pushButton_add.clicked.connect(self.binary_operation_press)
		self.pushButton_sub.clicked.connect(self.binary_operation_press)
		self.pushButton_divd.clicked.connect(self.binary_operation_press)
		self.pushButton_mult.clicked.connect(self.binary_operation_press)


		self.pushButton_equals.clicked.connect(self.equal_pressed)

		self.pushButton_clear.clicked.connect(self.clear_pressed)

		#checking is any operator is pressed or not
		self.pushButton_add.setCheckable(True)
		self.pushButton_sub.setCheckable(True)
		self.pushButton_mult.setCheckable(True)
		self.pushButton_divd.setCheckable(True)



	def digit_pressed(self):

		button = self.sender()

		#if any binary operator is pressed user should be typing the second number 
		#therefore set userIsTypingSecondNumber to True
		if (self.pushButton_add.isChecked() or self.pushButton_sub.isChecked() or self.pushButton_mult.isChecked() or self.pushButton_divd.isChecked()   and not self.userIsTypingSecondNumber):
			newLabel = format(float(button.text()),".15g")  # ".15g" is for 15 digit precision of floting point 
			self.userIsTypingSecondNumber = True			


		#to show zero on the right side of decimal point
		#though they are equal
		else :
			if  "." in self.label.text() and button.text() == "0":
				newLabel = format(self.label.text() + button.text(), "15")
			else :
				newLabel = format(float(self.label.text()+ button.text()),".15g")
		self.label.setText(newLabel)
 	

 	#for decimal point pressing 
	def decimal_pressed(self):

		#checking if there is already a point 
		#the point wouldn't be added when clicked 2nd time
		if "." not in self.label.text():
			self.label.setText(self.label.text() + ".")
		else :
			pass


	def unary_operation_press(self):
		button = self.sender()

		labelnumber = float(self.label.text())
		if button.text() == "+/-":
			labelnumber = labelnumber * (-1)
		else :
			labelnumber = labelnumber * .01


		newlabel = format(labelnumber, '.15g')
		self.label.setText(newlabel)


	def binary_operation_press(self):

		button= self.sender()

		self.first_num = float(self.label.text())

		button.setChecked(True)


	def equal_pressed(self):

		second_num = float(self.label.text())

		if self.pushButton_add.isChecked():
			labelnumber= self.first_num + second_num
			newLabel = format(labelnumber, ".15g")
			self.label.setText(newLabel)
			self.pushButton_add.setChecked(False)

		elif self.pushButton_sub.isChecked():
			labelnumber= self.first_num - second_num
			newLabel = format(labelnumber, ".15g")
			self.label.setText(newLabel)
			self.pushButton_sub.setChecked(False)
			
		elif self.pushButton_mult.isChecked():
			labelnumber= self.first_num * second_num
			newLabel = format(labelnumber, ".15g")
			self.label.setText(newLabel)
			self.pushButton_mult.setChecked(False)
			
		elif self.pushButton_divd.isChecked():
			labelnumber= self.first_num / second_num
			newLabel = format(labelnumber, ".15g")
			self.label.setText(newLabel)
			self.pushButton_divd.setChecked(False)
			
		#after equal is pressed  second number is not
		#be typed 
		self.userIsTypingSecondNumber = False

	#when clear is pressed 
	#remove everything and display 0
	def clear_pressed(self):
		self.pushButton_add.setChecked(False)
		self.pushButton_sub.setChecked(False)
		self.pushButton_mult.setChecked(False)
		self.pushButton_divd.setChecked(False)


		self.userIsTypingSecondNumber = False

		self.label.setText("0")
