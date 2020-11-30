from PyQt5.QtWidgets import QApplication
import sys
from calulator import CalculatorWindow


app = QApplication(sys.argv)
 
calculator = CalculatorWindow()

app.exit(app.exec_())
