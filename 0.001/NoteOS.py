#----------------Importing---#|
import pygame as pg          #|
import os                    #|
from time import sleep       #|
from random import randint   #|
from tkinter import*         #|
#---Importing----------------#|


timecadr=1
dirname = os.path.dirname(__file__)
os.chdir(dirname)
pg.init()



#-------------------------------Articles---#|
screen = pg.display.set_mode((500, 250))   #|
clock = pg.time.Clock()                    #|
FPS = 60                                   #|
red=(255, 0, 0)                            #|
green=(0, 255, 0)                          #|
blue=(0,0,255)                             #|
white=(255,255,255)                        #|
black=(0,0,0)                              #|
screen.fill([255, 255, 255])               #|
text0=''                                   #|
positionX=0                                #|
positionY=0                                #|
color=black                                #|
size=10                                    #|
#---Articles-------------------------------#|



rectangleStart = pg.draw.rect(screen, (white), (5, 200, 53, 20))
rectangleExit = pg.draw.rect(screen, (white), (65, 200, 53, 20))
rectangleLI=pg.draw.rect(screen, (white), (5, 200, 100, 20))
rectangleYes = pg.draw.rect(screen, (white), (5, 200, 80, 20))
rectangleNo = pg.draw.rect(screen, (white), (90, 200, 140, 20))
rectangle = pg.draw.rect(screen, (white), (5, 200, 80, 20))



def unpack():
    os.mkdir('NoteOS_Beta')
    os.chdir('NoteOS_Beta')
    MainNTOS = open("NoteOS_Beta.py", "w+")
    MainNTOS.write('''
''')
    MainNTOS.close()
    os.chdir('..')



def txt(text0, positionX, positionY, color, size):
    font=pg.font.Font('Comfortaa.ttf', size)
    text=font.render(text0, 1, color)
    pos=text.get_rect(x=(positionX), y=(positionY))
    screen.blit(text, pos)
    pg.display.update()



def cadr1START():
    size=200
    text0='Note'
    positionX=-70
    positionY=-70
    color=(235,235,235)
    txt(text0, positionX, positionY, color, size)
    size=14
    text0='''Добро пожаловать в программу бета тестирования NoteOS'''
    positionX=5
    positionY=227
    color=black
    txt(text0, positionX, positionY, color, size)
    text0='Начать'
    positionX=7
    positionY=204
    color=black
    size=12
    txt(text0, positionX, positionY, color, size)
    pg.display.update()



def cadr2PRPOL():
    screen.fill([255,255,255])
    positionX=-70
    positionY=-70
    color=(235,235,235)
    size=175
    text0='privacy policy'
    txt(text0, positionX, positionY, color, size)
    size=14
    text0='''Прочитайте лицензионное соглашение'''
    positionX=5
    positionY=227
    color=black
    txt(text0, positionX, positionY, color, size)
    text0='Принять'
    size=12
    positionX=7
    positionY=205
    txt(text0, positionX, positionY, color, size)
    text0='Отказаться и выйти'
    color=red
    positionX=80
    positionY=205
    txt(text0, positionX, positionY, color, size)
    pg.display.update()
    os.startfile('PrivacyPolicy.txt')



def cadr5SET():
    screen.fill([255,255,255])
    size=200
    text0='setting'
    color=(235,235,235)
    positionX=-70
    positionY=-70
    txt(text0, positionX, positionY, color, size)
    text0='''Всё готово к установке NoteOS в папку NtOS'''
    size=14
    positionX=5
    positionY=227
    color=black
    txt(text0, positionX, positionY, color, size)
    text0='Старт'
    size=12
    positionX=7
    positionY=205
    txt(text0, positionX, positionY, color, size)
    text0='Выход'
    color=red
    positionX=65
    positionY=205
    txt(text0, positionX, positionY, color, size)
    pg.display.update()



def cadr6Load():
    screen.fill([255,255,255])
    pg.display.update()
    sleep(1.0)
    light = 255
    while light > 0:
        screen.fill((light, light, light))
        sleep(0.03)
        pg.display.update()
        light -= 10
    sleep(2.0)
    def logoandProgress():
        logo = pg.image.load('logo2.png')
        screen.blit(logo, (201, 40))
        pg.display.update()
    def files():
        size=15
        text0='Распаковка файлов...'
        positionX=170
        positionY=150
        color=white
        txt(text0, positionX, positionY, color, size)
    def components():
        size=15
        text0='Установка компонентов...'
        positionX=150
        positionY=150
        color=white
        txt(text0, positionX, positionY, color, size)
        pg.display.update()
    def time():
        text0='Это не займет много времени...'
        positionX=125
        positionY=150
        size=15
        color=white
        txt(text0, positionX, positionY, color, size)
        pg.display.update()
    screen.fill([0,0,0])
    logoandProgress()
    files()
    unpack()
    pg.display.update()
    sleep(5.0)
    screen.fill([0,0,0])
    logoandProgress()
    time()
    pg.display.update()
    sleep(3.0)
    procent=0
    size1=0
    size2=0
    def line(procent, size1, size2):
        while procent!=size2: #263
            pg.draw.rect(screen, (white), (size1, 170, procent, 2))
            procent+=1
            pg.display.update()
            sleep(0.01)
    size1=125
    size2=263
    line(procent, size1, size2)
    sleep(2.0)
    screen.fill([0,0,0])
    logoandProgress()
    components()
    size1=150
    size2=220
    line(procent, size1, size2)
    sleep(1.5)
    screen.fill([0,0,0])
    text0='NoteOS успешно установлена'
    color=white
    size=16
    positionX=150
    positionY=150
    txt(text0, positionX, positionY, color, size)
    pg.display.update()





def cadr3License():
    screen.fill([255,255,255])
    size=200
    text0='license'
    color=(235,235,235)
    positionX=-70
    positionY=-70
    txt(text0, positionX, positionY, color, size)
    text0='''Введите лицензионный ключ'''
    size=14
    positionX=5
    positionY=227
    color=black
    txt(text0, positionX, positionY, color, size)
    text0='Продолжить'
    size=12
    positionX=7
    positionY=205
    txt(text0, positionX, positionY, color, size)
    root = Tk()
    root.title("Лицензионный ключ")
    root.geometry('200x20')
    from tkinter import ttk
    entry = ttk.Entry()
    entry.pack(anchor=NW, padx=0, pady=0)
    license=entry.get()
    root.mainloop()
    print(license)


    


cadr1START()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pg.mouse.get_pos()
            if rectangle.collidepoint(pos) and timecadr==1:
                cadr2PRPOL()
                timecadr=2  
            elif rectangleYes.collidepoint(pos) and timecadr==2:
                cadr3License()
                timecadr=3
            elif rectangleLI.collidepoint(pos) and timecadr==3:
                cadr5SET()
                timecadr=4
            elif rectangleStart.collidepoint(pos) and timecadr==4:
                cadr6Load()
                timecadr=5
            elif rectangleExit.collidepoint(pos) and timecadr==4:
                exit()
            elif rectangleNo.collidepoint(pos) and timecadr==2:
                exit()
    clock.tick(FPS)