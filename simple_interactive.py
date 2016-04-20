import sys
from PySide.QtGui import *
from PySide.QtCore import *

class Form(QDialog):
	def __init__(self,parent=None):
		super(Form,self).__init__(parent)
		self.setWindowTitle("Myform")


if __name__ == '__main__':
	# Create the Qt Application
	app = QApplication(sys.argv)
	# Create and show the form
	form = Form()
	form.show()
	form.resize(250,150)
	# Run the main Qt loop
	sys.exit(app.exec_())
