from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import Qt
import time
import sys

class startTicTocToeGame(QMainWindow):
     def __init__(self):
          super().__init__()
          self.setGeometry(400,100,450,450) 
          self.setWindowTitle('start game')
          
          self.label = QLabel(self)
          self.label.setGeometry(0,0,450,450)
          self.image = QPixmap('./gameImage_1.jpg')
          changeImageSize = self.image.scaled(450,450)
          self.label.setPixmap(changeImageSize)

          self.startButton = QPushButton('play',self)
          self.startButton.setGeometry(150,370,150,50)
          self.startButton.setFont(QFont('Arial',14))
          self.startButton.clicked.connect(self.startGame)
          self.startButton.setStyleSheet("""
          color:#408000;
          background-color:#adad85;
          border:2px solid #264d00;
          border-radius:10px;
          """)
          
     def startGame(self):
          self.secondWin = TicTocToeGame()
          self.secondWin.show()
          self.close()
     
     def startNewGame(self,text):
          self.startButton.setEnabled(False)
          self.winnerPlayer = QLabel(text,self)
          self.winnerPlayer.setGeometry(150,250,160,55)
          self.winnerPlayer.setFont(QFont('Arial',18))
          self.winnerPlayer.setAlignment(Qt.AlignCenter)
          self.winnerPlayer.setStyleSheet("""
          color:#408000;
          background-color:#adad85;
          border:2px solid #264d00;
          border-radius:10px;
          """)
          self.restartGame = QPushButton('play again',self)
          self.restartGame.setGeometry(150,370,160,55)
          self.restartGame.setFont(QFont('Arial',18))
          self.restartGame.setStyleSheet("""
          color:#408000;
          background-color:#adad85;
          border:2px solid #264d00;
          border-radius:10px;
          """)
          self.restartGame.clicked.connect(self.resGame)
     def resGame(self):
          self.new = TicTocToeGame()
          self.new.show()
          self.close()

class TicTocToeGame(QWidget):
    
     def __init__(self):
          super().__init__()
          self.mainWindow()
     def mainWindow(self):
          self.listButton = []
          self.text =""
          self.counter = 0
          self.time = 0
          self.setGeometry(500,100,400,450)
          self.setWindowTitle('game')
          self.setStyleSheet('background-color:#001a33;')

          self.image = QLabel(self)
          self.image.setGeometry(0,0,400,450)
          self.pixmap = QPixmap('./gameImage_2.webp')
          changePixmapSize = self.pixmap.scaled(400,450)
          self.image.setPixmap(changePixmapSize)

          for i in range(3):
               temp = []
               for j in range(3):
                    temp.append(QPushButton(self.text,self))
               self.listButton.append(temp)
          x = 120
          y = 140
          for i in range(3):
               for j in range(3):
                    self.listButton[i][j].move(50,50)
                    self.listButton[i][j].setGeometry(i*x+30,j*y+30,100,100)
                    self.listButton[i][j].setFont(QFont('Arial',14))
                    self.listButton[i][j].setStyleSheet("background-color:#b3d9ff;")
                    self.listButton[i][j].pressed.connect(self.calledAction)
          
     def calledAction(self):
          self.btn = self.sender()
          self.time+=1
          if self.counter==0:
               self.btn.setText('X')
               self.btn.setFont(QFont('Arial',18))
               self.btn.setStyleSheet("color: #ff1a1a;")
               self.btn.setEnabled(False)
               self.counter=1
          else:
               self.btn.setText('O')
               self.btn.setFont(QFont('Arial',18))
               self.btn.setStyleSheet("color: #ffff33;")
               self.btn.setEnabled(False)
               self.counter=0
 
          winner = self.whoIsWin(self.listButton)
          
          if winner:
               if self.counter==1:
                    self.res = startTicTocToeGame()
                    self.res.startNewGame('won X🏆🥳')
                    self.res.show()
                    time.sleep(0.5)
                    self.close()
               else:
                    self.res = startTicTocToeGame()
                    self.res.startNewGame('won O🏆🥳')
                    self.res.show()
                    time.sleep(0.5)
                    self.close()       
          elif self.time==9:
               self.res = startTicTocToeGame()
               self.res.startNewGame('draw 💆🏻‍♂️🙂')
               self.res.show()
               time.sleep(0.5)
               self.close()

     def whoIsWin(self,lst):
          listXorO = lst
          diagonalyx1,diagonalyx2 = 0 , 0
          diagonalyo1,diagonalyo2 = 0 , 0
          gorizonXList = [0,0,0]
          gorizonOList = [0,0,0]
          for item in range(len(listXorO)):
               vertikx = 0
               vertiko = 0
               for i in range(len(listXorO[item])):
                    if listXorO[item][i].text()=='X':
                         gorizonXList[i]+=1
                         if gorizonXList[i]==3:
                              return True
                         if item==i:
                              diagonalyx1+=1
                         if i==3-item-1:
                              diagonalyx2+=1
                         vertikx+=1
                         if vertikx==3 or diagonalyx1==3 or diagonalyx2==3:
                              return True
                    elif listXorO[item][i].text()=='O':
                         gorizonOList[i]+=1
                         if gorizonOList[i]==3:
                              return True
                         if item==i:
                              diagonalyo1+=1
                         if i==3-item-1:
                              diagonalyo2+=1
                         vertiko+=1
                         if vertiko==3 or diagonalyo1==3 or diagonalyo2==3:
                              return True
app = QApplication(sys.argv)
win = startTicTocToeGame() 
win.show()
app.exec_()    