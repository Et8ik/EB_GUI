import sys
import PyQt5.QtWidgets as qtw
from PyQt5.Qt import QIcon


class App(qtw.QWidget):                         #base-class = QWidget                      
    
    #set Window Parameter
    def __init__(self):
        super().__init__()                      #avoid base-class-init
        self.title = 'Advanced Search'          #set title
        self.left = 700                         #set x-pos
        self.top = 100                          #set y-pos
        self.width = 500                        #set x-length
        self.height = 700                       #set y-length
        self.icon = QIcon('py_log.png')         #set an new Icon and form the .png to an Qicon object
        self.initGUI()                          #call GUI-init   
          

    #place Window Parametr and Widgets
    def initGUI(self):
        self.setWindowTitle(self.title)         
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(self.icon)
        
        


        #create a Button (name,gui)
        button_1 =qtw.QPushButton('Suchen',self)     
        #set destination position parameters (x,y)
        button_1.move(220,650)
        #call function after click 
        button_1.clicked.connect(self.button_1_function)
 
        
        self.show()                                #show app

    #function for 
    def button_1_function(self):
        print('Keine Suche hinterlegt !')






if __name__ == "__main__":              #execute only as a script
    app = qtw.QApplication(sys.argv)    #create App
    ex = App()                          #start App
    sys.exit(app.exec_())               #close Programm after closing window