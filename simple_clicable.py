import sys
from PySide.QtCore import *
from PySide.QtGui import *
def sayHello():
	print ("Hello")

app=QApplication(sys.argv)
button=QPushButton("Say cheese")
button.clicked.connect(sayHello)
button.show()
app.exec_()
