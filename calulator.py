
from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator 


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

	first_num = None
	userIsTypingSecondNumber = False

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
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

		
		self.pushButton_add.setCheckable(True)
		self.pushButton_sub.setCheckable(True)
		self.pushButton_mult.setCheckable(True)
		self.pushButton_divd.setCheckable(True)
	def digit_pressed(self):
		button = self.sender()

		if (self.pushButton_add.isChecked() or self.pushButton_sub.isChecked() or self.pushButton_mult.isChecked() or self.pushButton_divd.isChecked()   and not self.userIsTypingSecondNumber):
			newLabel = format(float(button.text()),".15g")
			self.userIsTypingSecondNumber = True

		else :
			if  "." in self.label.text() and button.text() == "0":
				newLabel = format(self.label.text() + button.text(), "15")
			else :
				newLabel = format(float(self.label.text()+ button.text()),".15g")
		self.label.setText(newLabel)
 
	def decimal_pressed(self):
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
			

#		self.userIsTypingSecondNumber = False

	def clear_pressed(self):
		self.pushButton_add.setChecked(False)
		self.pushButton_sub.setChecked(False)
		self.pushButton_mult.setChecked(False)
		self.pushButton_divd.setChecked(False)


		self.userIsTypingSecondNumber = False

		self.label.setText("0")
