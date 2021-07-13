# importing libraries

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# creating a clock class

class Clock(QMainWindow):

	# constructor
	def __init__(self):
		super().__init__()

		
		timer = QTimer(self) # creating a timer object
		timer.timeout.connect(self.update)# adding action to the timer update the whole code
		timer.start(1000) # setting start time of timer i.e 1 second

		
		self.setWindowTitle('Clock') # setting window title		
		self.setGeometry(200, 200, 300, 300) # setting window geometry		
		self.setStyleSheet("background : darkcyan;") # setting background color to the window

		
		self.hPointer = QtGui.QPolygon([QPoint(6, 7), QPoint(-6, 7), QPoint(0, -50)]) # creating hour hand		
		self.mPointer = QPolygon([QPoint(6, 7), QPoint(-6, 7), QPoint(0, -70)]) # creating minute hand		
		self.sPointer = QPolygon([QPoint(1, 1), QPoint(-1, 1), QPoint(0, -90)]) # creating second hand

	
		self.bColor = Qt.black # colors color for minute and hour hand		
		self.sColor = Qt.red # color for second hand

	#-------------------------------------------------------------------------------------------------------------------------------------
	def paintEvent(self, event): # method for paint event

		
		rec = min(self.width(), self.height()) # getting minimum of width and height  so that clock remain square		
		tik = QTime.currentTime() # getting current time
		painter = QPainter(self) # creating a painter object


	#----------------------------------------------------------------------------------------------------------------------------------------	
		
		def drawPointer(color, rotation, pointer): # method to draw the hands, argument : color rotation and which hand should be pointed

			
			painter.setBrush(QBrush(color)) # setting brush			
			painter.save() # saving painter			
			painter.rotate(rotation) # rotating painter
			painter.drawConvexPolygon(pointer) # draw the polygon i.e hand
			painter.restore() # restore the painter

        #-----------------------------------------------------------------------------------------------------------------------------------------
		
		painter.setRenderHint(QPainter.Antialiasing) # tune up painter
		painter.translate(self.width() / 2, self.height() / 2) # translating the painter
		painter.scale(rec / 200, rec / 200) # scale the painter
		painter.setPen(QtCore.Qt.NoPen) # set current pen as no pen


		# draw each hand
		drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
		drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
		drawPointer(self.sColor, (6 * tik.second()), self.sPointer)


		painter.setPen(QPen(self.bColor)) # drawing background

		
		for i in range(0, 60):
			
			if (i % 5) == 0: # drawing background lines
				painter.drawLine(87, 0, 97, 0)
			
			painter.rotate(6) # rotating the painter
		
		painter.end() # ending the painter


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':  # Driver code
	app = QApplication(sys.argv)
	
win = Clock() # creating a clock object
win.show() # show
	
exit(app.exec_())
