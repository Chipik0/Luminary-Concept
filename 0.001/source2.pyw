try:
    #--------------IMPORTING---#|
    import pygame as pg        #|
    import os                  #|
    from time import sleep     #|
    from random import randint #|
    import psutil              #|
    #---IMPORTING--------------#|



    pg.init()
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    pg.mixer.music.load("Audio/startsound.ogg")




    #---Perfomance-------------------------------------------#|
    cpufreq = psutil.cpu_freq()                              #|
    freq=cpufreq.max                                         #|
    cores=psutil.cpu_count(logical=False)                    #|
    ram=round(psutil.virtual_memory().total / (1024.0 **3))  #|
    #-------------------------------------------Perfomance---#|



    #---Articles------------------------------------------#|
    screen = pg.display.set_mode((1920, 1080))            #|
    white=(255,255,255)                                   #|
    black=(0,0,0)                                         #|
    red=(255,0,0)                                         #|
    green=(0,255,0)                                       #|
    blue=(0,0,255)                                        #|
    procent=0                                             #|
    pr=100                                                #|
    size1=0                                               #|
    size2=0                                               #| 
    width=1920                                            #|
    height=1080                                           #|
    text0=''                                              #|
    positionX=0                                           #|
    positionY=0                                           #|
    color=black                                           #|
    size=10                                               #|
                                                          #|
    Error=1                                               #|
    #-----------------------------------------------------#|



    def unfade(screen):
        light = 0
        while light < 255:
            screen.fill((light, light, light))
            sleep(0.03)
            pg.display.update()
            light += 10


    def fade():
        fade = pg.Surface((width, height))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            pg.display.update()
            screen.blit(fade, (0,0))
            pg.display.update()
            pg.time.delay(5)
    def txt(text0, positionX, positionY, color, size):
        font=pg.font.Font('Comfortaa.ttf', size)
        text=font.render(text0, 1, color)
        pos=text.get_rect(x=(positionX), y=(positionY))
        screen.blit(text, pos)
        pg.display.update()
    alpha=0
    alpha2=0
    sloi1=pg.Surface((1920, 1080))
    sloi2=pg.Surface((1920,1080))
    def iconImg(screen, alpha, alpha2, sloi1, sloi2):
        blur=pg.image.load('Images/backBlur.png')
        rectangle=pg.image.load('Noty/rectangle.png')
        sloi1.blit(blur, (0,0))
        while alpha!=70:
            sloi1.set_alpha(alpha)
            screen.blit(sloi1, (0,0))
            pg.display.update()
            alpha+=1
            sleep(0.01)
        sloi2.blit(blur, (0,0))
        while alpha2!=70:
            sloi2.set_alpha(alpha2)
            screen.blit(sloi2, (0,0))
            pg.display.update()
            alpha2+=1
            sleep(0.01)
        toast=pg.image.load('Noty/toastwelcome.png')
        posxx=int(-250)
        while posxx<=200:
            screen.blit(blur, (0,0))
            screen.blit(toast, (posxx,110))
            posxx+=12
            pg.display.update()
            sleep(0.01)
            print(posxx)
    def start():
        from moviepy.editor import VideoFileClip, preview
        logo=VideoFileClip('Audio/logo.mp4') 
        logo.preview(fps=60)
    bShutdown = pg.draw.rect(screen, (black), (805, 850, 330, 50))
    bRestart = pg.draw.rect(screen, (black), (805, 915, 330, 50))
    def errorload2(screen, white, info):
        error=1
        pg.display.update()
        sleep(2.0)
        x=775
        y=1065
        pg.mixer.music.load("Audio/error.mp3")
        errblur=pg.image.load('Images/errbl.png')
        if info=='ram':
            ram=pg.image.load('Noty/windowRAM.png')
            alpha5=0
            sl2=pg.Surface((1100,600))
            sl2.blit(errblur, (0,0))
            sleep(0.01)
            pg.mixer.music.play(start=0.0)
            while y>600:
                sl2.set_alpha(alpha5)
                screen.blit(sl2, (0,0))
                pg.display.update()
                screen.blit(ram, (x,y))
                y-=7
                alpha5+=0.9
                print(y)
                pg.display.update()
        if info=='cpu':
            ram=pg.image.load('Noty/windowCPU.png')
            alpha5=0
            sl2=pg.Surface((1100,600))
            sl2.blit(errblur, (0,0))
            sleep(0.01)
            pg.mixer.music.play(start=0.0)
            while y>600:
                sl2.set_alpha(alpha5)
                screen.blit(sl2, (0,0))
                pg.display.update()
                screen.blit(ram, (x,y))
                y-=7
                alpha5+=0.9
                print(y)
                pg.display.update()
    start()
    if ram<4:
        info='ram'
        errorload2(screen, white, info)
    elif freq<2.0 or cores<4:
        info='cpu'
        errorload2(screen, white, info)
    else:
        fade()
        iconImg(screen, alpha, alpha2, sloi1, sloi2)
    clock = pg.time.Clock()
    FPS = 120
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pg.mouse.get_pos()
                if bShutdown.collidepoint(pos) and Error==1:
                        exit()
                if bRestart.collidepoint(pos) and Error==1:
                        os.startfile('restart.pyw')
                        exit()
        clock.tick(FPS)












except Exception as e:
    import os
    from time import sleep
    import pygame as pg
    pg.init()
    screen1 = pg.display.set_mode((1920, 1080))
    sleep(2.0)
    errorcode=e
    print(errorcode)
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    logop=pg.image.load('Images/logop.png')
    from moviepy.editor import VideoFileClip, preview
    logo=VideoFileClip('criterror.mp4') 
    logo.preview(fps=60)
    cur=pg.image.load('Images/terminalcur.png')
    for i in range(5):
        screen1.blit(cur, (194,110))
        pg.display.update()
        sleep(0.4)
        screen1.fill([0,0,0])
        pg.display.update()
        sleep(0.4)
    font=pg.font.Font('Comfortaa.ttf', 15)
    err=str(errorcode)
    text=font.render(err, 1, (255,255,255))
    pos=text.get_rect(x=(200), y=(110))
    screen1.blit(text, pos)
    screen1.blit(logop, (1630,110))
    pg.display.update()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()