# -*- coding: utf-8 -*-
import os, sys ,cv2 , platform,ctypes , time
import  win32con, win32ui

#from ffpyplayer import *

from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import*
from PyQt5.uic import *
#from PIL import *


'''
Created on Thu Oct 22 13:20:09 2020
Title: HOMEWORK#1 PIRPLE CERTIFimpICATIOn
@author: ALEX ONUKWUGHA
HOMEWORK DETAILS:
    ~Create Python file name main.py
    ~Create list of all attributes for a song
    ~Create variables for each attribute-> Ex: Genre = "Jazz"
    ~Create as many variables as possible
        >>Artist = "Dave Brubeck"
        >>Genre = "Jazz"
        >>DurationInSeconds = "328"
        .
        .
        .
        >> etc = "..."
    ~Extra Credit Comment in file
    -Compress to Zip file & Place in Pirple in Dropbox
    
 ###############################################################   
       vidcapture = cv2.VideoCapture(vidURL)
        sound = MediaPlayer(vidURL)
        
        #in case video frames don't work displays error
        if vidcapture.isOpened()==False:
            print('Error opening video stream')
        
        #cycles through opening, then reading, and destroying image/audio every millosecond
        while vidcapture.isOpened():
            ret, frame = vidcapture.read()
            audio, vol = sound.get_frame()
        
        
            if ret == True:
                cv2.imshow('Song_VIDEO',frame)
        #stops loop if q key is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            if vol != 'eof' and audio is not None:
                img,t = audio
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
        vidcapture.release()
        cv2.destroyAllWindows()
    
    #############################################################
    
'''


#simulates video frames with audio synced
#VideoPlayer class was coppied directly from Stack overflow
#All variations I tried to create with independent Qt Objects failed
#SOURCE: https://stackoverflow.com/questions/57842104/how-to-play-videos-in-pyqt
class VideoPlayer(QWidget):

    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        # Creates Dependent Qt Objects
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.videoItem = QGraphicsVideoItem()
        self.videoItem.setSize(QSizeF(640, 480))

        scene = QGraphicsScene(self)
        graphicsView = QGraphicsView(scene)

        scene.addItem(self.videoItem)

        rotateSlider = QSlider(Qt.Horizontal)
        rotateSlider.setRange(-180,  180)# Rotate bound by semi-circle
        rotateSlider.setValue(0)
        rotateSlider.valueChanged.connect(self.rotateVideo)

        openButton = QPushButton("Open...")
        openButton.clicked.connect(self.openFile)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)# Disable button
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(graphicsView)
        layout.addWidget(rotateSlider)
        layout.addLayout(controlLayout)

        self.setLayout(layout)
        # Set media output && share media player properties
        self.mediaPlayer.setVideoOutput(self.videoItem)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

    def sizeHint(self):
        return QSize(int(w*(2/3)), int(h*(2/3)))

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                str(os.path.abspath('MEDIAPLAYER')))

        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def rotateVideo(self, angle):
        x = self.videoItem.boundingRect().width() / 2.0
        y = self.videoItem.boundingRect().height() / 2.0

        self.videoItem.setTransform(
                QTransform().translate(x, y).rotate(angle).translate(-x, -y))




#THIS IS USED  for one thing in a classs attribute
#BELOW, but honestly doesn't effect much
def numofSPACES (line,k)->int:
    for i in line:
        #print(i)
        if i == ' ':
            k+=1
    return k
#Prints in consle and gets first button function
class pySngAttributes:
    print('www.pirple.com ==>>> Homework#1 \nProgram is Executing...')

    global Lyrics,f_INPUT,kk, N_space
    Lyrics = []
    f_INPUT = open('LYRICS_HW1.txt', 'r')
    
    
    kk = 0
    for j in f_INPUT:
        Lyrics.append(j.strip('\n'))
        N_space = numofSPACES(j,kk)
        kk = N_space
        kk+=1
        
#All buttons are strait forward
def sdiscripBTTN():
    global SongTitle, Genre, Album
    
    SongTitle = 'Monster You Made' ;Genre, Album ={'Protest Anthem':'(Rap)Hip-Hop'}, 'Twice As Tall'
    gI = list(Genre.keys());gI2 = list(Genre.values());sdlist = []; sdlist.append(SongTitle)
    sdlist.append(gI[0] + '/' + gI2[0]);sdlist.append(Album)
    pitems = ['SongTitle.jpg','ProtestAnthem.jpg','AlbumCover.jpg']
    fll = []
    tmpWG = QWidget();tmpLYT = QVBoxLayout();
    for i in range(3):
        ttl = QLabel(sdlist[i]);ttl.setFont(font3);ttl.setAlignment(Qt.AlignCenter)
        ttla = QLabel(); ttlam = QPixmap(pitems[i])
        ttla.setMinimumWidth(int(w/2));ttla.setMinimumHeight(int(h/2))
        ttl.setStyleSheet("background-color: lightBlue")
        ttla.setPixmap(ttlam.scaled(int(w/2),int(h/2)))
        ttla.setAlignment(Qt.AlignCenter);
        fll.append(ttl);fll.append(ttla)
    j = 0;
    for i in fll:
        tmpLYT.addWidget(i)
        if j%2 == 1:
            tmpLYT.addSpacing(int(h/4))
        j+=1
    tmpWG.setLayout(tmpLYT)
    fm.setWidget(tmpWG)

    print('\npyGUI Song Details Displayed...')
        #print( Artist[0],'#1, ', Artist[1],'#2')


def stm_dtlsBTTN():
    global Year, Month, Day, monthname, monthnumb, dayname, daynumb
    Year = 2020
    Month, Day = {'August':'8'}, {'Monday':'27th'}
    monthname, monthnumb, dayname, daynumb = str(list(Month.keys())[0]), str(list(Month.values())[0]), str(list(Day.keys())[0]), str(list(Day.values())[0])
    Duration = '237[seconds]'; lblist = [str(Year),monthname,monthnumb,dayname,daynumb,Duration]
    fll = []
    tmpWG = QWidget();tmpLYT = QVBoxLayout()
    for i in lblist:
        tmp = QLabel(i);tmp.setFont(font3);tmp.setStyleSheet("background-color: lightBlue")
        tmp.setAlignment(Qt.AlignCenter);fll.append(tmp)
    for i in fll:
        tmpLYT.addWidget(i);
    tmpWG.setLayout(tmpLYT);
    fm.setWidget(tmpWG);fm.setAlignment(Qt.AlignCenter)
    
    print('\npyGUI Song Release/Time Displayed...')    
def a_ftBTTN():
    global Artist, Featured_Artist, ftartst1_alias, ftartst1_name
    global ftartst2_alias, ftartst2_name, burnaboy_PIC, ChrisMartin_PIC, MusLink
    Artist, Featured_Artist  =   ('Burna Boy','Damini Ebunoluwa'),{'featuring Chris Martin':'Christopher Martin', 'featuring Ama Ata Aidoo':'Christina Ama Aidoo'}
    ftartst1_alias, ftartst1_name, ftartst2_alias, ftartst2_name = str(list(Featured_Artist.keys())[0]), str(list(Featured_Artist.values())[0]), str(list(Featured_Artist.keys())[1]), str(list(Featured_Artist.values())[1]),
    burnaboy_PIC, ChrisMartin_PIC, Christina_Aidoo = ('BURNABOYPIC.jpg'),('ChrisMartin.jpg'),('ChristinaAidoo.jpg')
    lblist = [Artist[0],Artist[1],ftartst1_alias, ftartst1_name, ftartst2_alias, ftartst2_name]
    pclist  =[burnaboy_PIC, ChrisMartin_PIC, Christina_Aidoo]
    tmpWG = QWidget();tmpLYT = QVBoxLayout();flltll = [];fllpic = []
    for i in lblist:
        ttl = QLabel(i);ttl.setFont(font3);ttl.setStyleSheet("background-color: lightBlue")
        flltll.append(ttl)
    for i in pclist:
        pttl = QLabel();ptl = QPixmap(i);
        pttl.setMinimumWidth(int(w/2));pttl.setMinimumHeight(int(h/2))
        pttl.setStyleSheet("background-color: lightBlue")
        pttl.setPixmap(ptl.scaled(int(w/2),int(h/2)))
        pttl.setAlignment(Qt.AlignCenter)
        fllpic.append(pttl)
        
    for i in range(0,6,2):
        tmpLYT.addWidget(flltll[i])      
        tmpLYT.addWidget(fllpic[int(i/2)])
        
        if i < 6:
            tmpLYT.addWidget(flltll[i+1])
            tmpLYT.addSpacing(int(h/4))

    tmpWG.setLayout(tmpLYT)
    fm.setWidget(tmpWG)
    print('\npyGUI Artist/Featured Artist Displayed...')
    
def flyrcBTTN()->[]:
    tmp = QTextEdit();tmp.setFont(font2);tmp.setAlignment(Qt.AlignCenter)
    string = str()
    j = 0
    for i in Lyrics:
    
        string =  string +'line#'+ str(j) +': '+ i + '\n\n'
        j+=1
    tmp.setPlainText( '\n\n'+ string)
    tmp.setMinimumWidth(int(w));tmp.setMinimumHeight(int(h))
    fm.setWidget(tmp)
    print('\npyGUI Lyrics Displayed...')
    return Lyrics

def lyrcdtlsBTTN():
    global numbofLines, numbofletters, numbofwords 
   
    numbofLines, numbofletters, numbofwords = len(Lyrics), os.stat('LYRICS_HW1.txt').st_size, N_space
    nmblst = [numbofLines, numbofletters, numbofwords];tnlst = ['number of lines ','number of letters','number of spaces']
    
    tmpWG = QWidget();tmpLYT = QVBoxLayout()
    
    fll = []
    for i in range(3):
        tmp = QLabel(str(str(nmblst[i]) +' '+ tnlst[i]))
        tmp.setMinimumWidth(int(w/2));tmp.setMinimumHeight(int(h/8))
        tmp.setFont(font3);tmp.setStyleSheet("background-color: lightBlue")
        tmp.setAlignment(Qt.AlignCenter)
        fll.append(tmp)
        tmpLYT.addWidget(fll[i])
    tmpWG.setLayout(tmpLYT)
    fm.setWidget(tmpWG)
        
    print('\npyGUI Lyric Details Diplayed...')
    #print(numbofLines, numbofletters, numbofwords)




def slogiBTTN():
    global Location, cmbckt, csize, data, tmp, _tmp
    Location = 'Nigeria'
    tmpWG = QWidget();tmpLYT = QVBoxLayout()

    tbff = QLabel();tbff.setText(str('The location of Song \nTook place in ' + Location + '"\nType comments below:'))
    tbff.setFont(font3);tbff.setStyleSheet("background-color: lightBlue")
    tmp = QTextEdit()
    _tmp = QTextEdit()
    btmp = QPushButton('Post New Comments');btmp.setFont(font2)
    btmp.setStyleSheet("background-color: lightBlue")
    btmp2 = QPushButton('Clear && Delete All Comments');btmp2.setFont(font2)
    btmp2.setStyleSheet("background-color: Orange")

    btmp.clicked.connect(posSUBBTTN)
    btmp2.clicked.connect(delSUBBTTN)

    tmp.setStyleSheet("background-color: white");tmp.setFont(font2)
    tmp.setMaximumHeight(int(h/10));tmp.scrollBarWidgets(Qt.AlignRight)

    _tmp.setStyleSheet("background-color: Orange");_tmp.setFont(font2)
    _tmp.setMinimumHeight(int(h/2));_tmp.scrollBarWidgets(Qt.AlignRight)
    _tmp.setReadOnly(True)
    tmp.setReadOnly(False)

    spc = '\t'
    for i in range(int(w/50)):
        spc = spc + '\t'
    tmp.setPlaceholderText(spc + '...Please Enter Text here...')
    _tmp.setPlaceholderText(spc + ' ... Previouse Posts (Read-Only) '
                                  '...\n'+ spc + spc + 'Currently No Post')
    cmbckt = open('Commentbucket.txt')
    fll= list(map(lambda x:x.strip(), list(tuple(cmbckt))))
    strng = ''
    csize = sum(1 for line in fll)
    for i in fll:
        strng = str(i)
        _tmp.append(strng)

    tmpLYT.addWidget(tbff);tmpLYT.addWidget(_tmp);tmpLYT.addWidget(tmp)
    tmpLYT.addWidget(btmp);tmpLYT.addWidget(btmp2)
    tmpWG.setLayout(tmpLYT);fm.setWidget(tmpWG)

    print('\npyGUI Song Logistics/Comment Area Displayed...')


def delSUBBTTN():
    cmwrt = open('Commentbucket.txt','w')
    if csize > 0:
        cmwrt.close()
    slogiBTTN()

def posSUBBTTN():
    cmwrt = open('Commentbucket.txt','w')
    data = tmp.toPlainText()
    rtnw = datetime.now()
    tmstmp = rtnw.strftime("%b %d, %Y (%H:%M:%S)")
    poststmp = 'POSTED ON: ' + tmstmp + '[MILITARY TIME]'
    sprt = ''
    for i in range(int(w/50)):
       sprt = sprt + ' _'
    print('...')
    _tmp.append(data + '\n'+ poststmp+ '\n' +sprt +'\n')

    rd = _tmp.toPlainText()
    strg = str(rd)
    stff = strg.splitlines()
    for i in stff:
       cmwrt.write(i)
       cmwrt.write('\n')


def smp4vidBTTN():
    print('\npyGUI MusicVideoPlayer EXECUTING...')
    vid = VideoPlayer()
    fm.setWidget(vid)

def resetBTTN():
    rst = QWidget();rst.setStyleSheet("background-color: white")
    for i in reversed(range(fm1.count()-1)): 
        fm1.itemAt(i).widget().deleteLater()
    fm.setWidget(rst)
    #tmp = QTextEdit();tmp.setFont(font2);tmp.setAlignment(Qt.AlignCenter)
    #fm2.removeWidget(tmp);
    print("\npyGUI Reset...")
    












#Displays message on win32 pop up which also inisializes the program
print('\nTHE SONGE ATTRIBUTES ARE GROUPED \nTHEN LISTED IN POP UP:\n')
class instruction():
    def do():
        print('Pop Up Activated...\nif you do not see pop up \ncheck behind opened applications', end=' ')
        check = win32ui.MessageBox('PLEASE TAKE NOTE THAT THE FOLLOWING POPUP LIST ALL VARIABLE OBJECTS \
        \n[songtitle, genre, album] \n[ artist, ft_artist, artist_pic, ft_artist_pic] \
        \n[year, month, day,duration] \n[locatoin] \
        \n[numberofletters, numberofwords, numberoflines] \n[lyrics] \n[mp4vid] \n\n\n\n\n \
        \nto continue to pyGUI press OK \notherwise press "Close" or "Cancel" button to quit program', '<<TOKEN POP UP: PLEASE READ!!>>',1)
        if check ==  1:
            print(' .. .')
        else:
            print('\n\nProgram Terminated...');sys.exit();
popUP = instruction.do()

class SongUI(QMainWindow):
    #Starts QAppliction and passes reusd objects
    #All widgets are independent and only simulate hierchy within class
    #Widgets are recreated are re assigned parents and children every time code is executed
    def startUP():
        global gui_width, gui_height, w, h, app
        app = QApplication(sys.argv)
        print('\npyGUI EXECUTING...', end=' ')
        scrnSZ = ctypes.windll.user32
        gui_width, gui_height = scrnSZ.GetSystemMetrics(0), scrnSZ.GetSystemMetrics(1)
        w, h = int (gui_width/2), int(gui_height/2)

    #Creates the parent widget though independent will house all other widgets
    # passed on previous function attributes
    def sFRAME(): 
        global frame;
        SongUI.startUP()
        frame = QMainWindow()
        frame.centralWidget()
        frame.setGeometry(int(gui_width/3), int(gui_height/4),w, h)
        frame.setFixedSize(w, h);frame.setWindowTitle('--\//\ PySong_GUI /\\\/--')
        frame.setStyleSheet("background-color: lightBlue;")


    #Create the three types of fonts to be used in Widget constructs
    #As well as creating widget title
    # passed on previous function attributes
    def tBAR():
        global font, font3, font2, l_title, f1
        SongUI.sFRAME()
       # SIZE = frame.frameSize();print('\n\n\n The size is',SIZE)
        font = QFont();font.setFamily('Times');font.setWeight(QFont.Bold);font.setPixelSize(84)
        font2 = QFont();font2.setFamily('Times');font2.setWeight(QFont.Bold);font2.setPixelSize(22)
        font3 = QFont();font3.setFamily('Times');font3.setWeight(QFont.Bold);font3.setPixelSize(54)

        l_title = QLabel('Python First GUI HW#1');l_title.setFont(font);l_title.setAlignment(Qt.AlignCenter)
        l_title.setStyleSheet("background-color: orange");l_title.setFixedHeight(int(h/7))


    #Creates all buttons that will later connect to functions
    # passed on previous function attributes
    def sBTTN():
        global b1, b2, b3, b4, b5, b6, b7, b8, blist
        SongUI.tBAR()
        
        b1, b2, b3, b4, b5, b6, b7, b8 \
        = QPushButton('Song Description'), QPushButton('Song Time Details'), QPushButton(' Artist details') \
        , QPushButton('Full Lyrics'), QPushButton('Lyric details'), QPushButton('Song Logistics')\
        , QPushButton('Song MP4 vid'), QPushButton('Reset Button')
        blist = [b1,b2,b3,b4,b5,b6,b7,b8]
        
        for i in blist:
            if i is b8:
                i.setMinimumHeight(int (h/5))
                i.setFont(font3)
            else:
                i.setFont(font2);i.setMinimumHeight(int(h/17))
            i.setStyleSheet("background-color: lightBlue")
    #Overlays Qwidgets to place over child widgets
    # passed on previous function attributes
    def sBTTN2():
        global f0,f1,hBOX,p
        SongUI.sBTTN()

        f0 = QVBoxLayout();f0.setAlignment(Qt.AlignLeft)
        f1 = QWidget();f1.setLayout(f0);
        p = QLabel('Button Selection');p.setFont(font2);p.setStyleSheet("background-color: lightGrey");p.setFixedWidth(int(w/3));p.setAlignment(Qt.AlignCenter)
        for i in blist:
            f0.addWidget(i);
    #Sets fixed size of overlayed QWidget Objects
    # passed on previous function attributes
    def dWNDOW():
        global ff, f3, fter, hBOX, fb4, fm, fm1
        SongUI.sBTTN2()
        
        fm1 = QStackedLayout() # Used for reset and to keep exactly one single widet visable in parent window
        fm = QScrollArea(); fm.setStyleSheet("background-color: white;") # allows larger sized widgets to be placed in Qwidget area
        fm.setFixedWidth(int(w*(13/23)));fm.setLayout(fm1)
        fter = QVBoxLayout(); fter.addWidget(fm)
        
        f3 = QComboBox(); f3.setStyleSheet("background-color: lightBlue;");
        f3.setFixedHeight(int(h*(11/15)))
        f3.setLayout(fter)
        f3.setFixedWidth(int(w*(2/3)))
        
        ff = QHBoxLayout();ff.addWidget(f1);ff.addWidget(f3)
        fb4 = QWidget()
        fb4.setLayout(ff)
        
        hBOX = QVBoxLayout()
        hBOX.addWidget(l_title);hBOX.addWidget(fb4)
        
    #makes Qmainwindow parent of all widgets
    # passed on previous function attributes
    def fWNDOW():
        global fwndow
        SongUI.dWNDOW()
        
        fwndow = QGroupBox();fwndow.setLayout(hBOX)
        fwndow.setFixedSize(int(w*(117/118)), int(h* (27/28)))
        fwndow.setStyleSheet("background-color: orange;")
        frame.setCentralWidget(fwndow)
    #connect functions to occure when buttons clicked
    # passed on previous function attributes
    def bttnSWITCHES():
        SongUI.fWNDOW()
        b1.clicked.connect(sdiscripBTTN)
        b2.clicked.connect(stm_dtlsBTTN)
        b3.clicked.connect(a_ftBTTN)
        b4.clicked.connect(flyrcBTTN)
        b5.clicked.connect(lyrcdtlsBTTN)
        b6.clicked.connect(slogiBTTN)
        b7.clicked.connect(smp4vidBTTN)
        b8.clicked.connect(resetBTTN)
        
    
        print(' .. . ')
        
    def run():
        SongUI.bttnSWITCHES()
        frame.show()
        app.exec_()
        print('\npyGUI TERMINATING...')
        sys.exit()
SongUI.run()

'''
Resource1: http://zetcode.com/gui/pyqt5/layout/
Resource2: https://pythonspot.com/pyqt5-colors/
Resource3: https://www.learnpyqt.com/tutorials/creating-your-first-window/
Resource4:https://www.codespeedy.com/call-a-function-from-another-function-in-python/
Resource5: A WHOLE LOT OF STACKOVERFLOW SUGGESTIONS
Probs 5 more Resources that I lost track of that were similar to those above
'''
    
    
    
    
    