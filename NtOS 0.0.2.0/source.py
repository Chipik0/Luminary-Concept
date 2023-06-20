# Дорогой программист
# Когда я писал этот код, только бог и я знали как он работает
# Теперь знает только бог
# 
# Тем не менее если ты попытаешься что то оптимизировать и у тебя не получится (вероятнее всего)
# Увеличь значение этого счетчика как предупреждение для следующего человека:

potrachenno_grebannyh_chasov=285

stop2=1


try:
    #Запуск и пасхалки
    def start():
        if check1==True:
            with open('chuck.txt') as f:
                if 'Chuck Review' in f.read():
                    startchuck()
        elif check2==True:
            with open('Quietly_rule.txt') as f:
                info=f.read()
                if "I don't follow the rules of silence" in info or "i don't follow the rules of silence" in info:
                    logo=VideoFileClip('Media/536634/logo3.mp4')
                    clip_resized = logo.resize(height=YM)
                    clip_resized.preview(fps=30)
                    pg.quit()
                    sys.exit()
                elif 'I follow the rules of silence' in info or 'i follow the rules of silence' in info:
                    welcome2v(unblur, barmat, bar, screen, YM)
                else:
                    welcome2v(unblur, barmat, bar, screen, YM)
        else:
            welcome2v(unblur, barmat, bar, screen, YM)
            info="Приветик"
            power1=0
            Thread(target = notify, args=(screen, info,  power1)).start()
            
    #-----------------------------------------------------------------------------------IMPORTING---#|
    import pygame as pg
    import os
    from time import sleep
    import psutil
    import datetime
    from win32api import GetSystemMetrics
    from moviepy.editor import VideoFileClip, preview
    import sys
    import cv2
    from threading import Thread
    from PIL import ImageFilter, Image
    import pyscreenshot
    import shutil
    from random import choice
    #---IMPORTING-----------------------------------------------------------------------------------#|

    pg.init()
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)

    #InitData
    matcolor2=open('Media/color.txt', 'r')
    matcolor=matcolor2.read()
    matcolor3=matcolor.replace('(', '')
    matcolor4=matcolor3.replace(')', '')
    matcolor = tuple(map(int, matcolor4.split(',')))
    
    def lerp(a, b, t):
        return a + (b - a) * t
    
    def anim():
        a1=pg.draw.rect(screen, (255,0,0), (0, 0, 40, 40))
        a2=pg.draw.rect(screen, (255,0,0), (50, 0, 40, 40))
        a3=pg.draw.rect(screen, (255,0,0), (100, 0, 40, 40))
        a4=pg.draw.rect(screen, (255,0,0), (150, 0, 40, 40))
        a5=pg.draw.rect(screen, (255,0,0), (200, 0, 40, 40))
        screen.blit(vir, (0,250))


    def startchuck():
        pg.mixer.music.load('Media/536634/logo2.mp3')
        pg.mixer.music.play()
        w=(255, 255, 255)
        g=(26, 26, 26)
        b=(0,0,0)
        screen.fill([0,0,0])

        sleep(1.220)
        font=pg.font.Font('Comfortaa.ttf', 25)
        text=font.render('luminary', 1, (26,26,26))
        screen.blit(text, text.get_rect(center = screen.get_rect().center))
        pg.display.update()
        sleep(2.168-1.220)

        text = "luminary"
        x2, y2=screen.get_rect().center
        x3, y3=font.size(text)
        x3=x3/2
        y3=y3/2
        text_rect = pg.Rect(x2-x3, y2-y3, XM, YM)
        list=[g, w]
        colors = []

        for i in range(6):
            colors = []
            screen.fill(b)
            for  i in range(len(text)):
                r=choice(list)
                colors.append(r)
            letters = [font.render(letter, True, colors[i % len(colors)]) for i, letter in enumerate(text)]
            x, y = text_rect.topleft
            for letter_surface in letters:
                screen.blit(letter_surface, (x, y))
                x += letter_surface.get_width()
                pg.display.update()
            sleep(0.1)
        screen.fill(b)
        text2=font.render(text, 1, w)
        screen.blit(text2, text2.get_rect(center = screen.get_rect().center))
        pg.display.update()
        sleep(3.500-3.100)

        for i in range(4):
            colors = []
            screen.fill(b)
            for  i in range(len(text)):
                r=choice(list)
                colors.append(r)
            letters = [font.render(letter, True, colors[i % len(colors)]) for i, letter in enumerate(text)]
            x, y = text_rect.topleft
            for letter_surface in letters:
                screen.blit(letter_surface, (x, y))
                x += letter_surface.get_width()
                pg.display.update()
            sleep(0.180)
        sleep(0.7)
        screen.fill(b)
        text=font.render(text, 1, w)
        screen.blit(text, text.get_rect(center = screen.get_rect().center))
        pg.display.update()

        sleep(0.75)

        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        hour = current_time.hour
        minute = current_time.minute
        font=pg.font.Font('Comfortaa.ttf', 22)
        text=font.render(f"{hour:02d}:{minute:02d}", 1, (255,255,255))
        YYM=YM-53
        x, y, b, b=bar.get_rect(center = screen.get_rect().center)
        powerlayer3.blit(unblur, unblur.get_rect(center = screen.get_rect().center))
        powerlayer3.blit(barmat, (x, YYM))
        powerlayer3.blit(bar, (x, YYM))
        x, y, b, b=text.get_rect(center = screen.get_rect().center)
        x-=89
        y=YM-37
        powerlayer3.blit(text, (x, y))

        for alpha in range(0, 150):
                powerlayer3.set_alpha(alpha)
                screen.blit(powerlayer3, (0,0))
                pg.display.update()
                pg.time.delay(2)
        sleep(0.5)
        




    check09=os.path.exists('Comfortaa.ttf')
    check10=os.path.exists('config.txt')

    if check09==True and check10==True:

        bar=pg.image.load('Media/Images/bar.png')
        barmat=pg.image.load('Media/Images/barMaterialU.png')
        unblur=pg.image.load('Cache/backunBlur.png')
        blur=pg.image.load('Cache/blurscreen.png')


        #---Perfomance-------------------------------------------#|
        cpufreq = psutil.cpu_freq()                              #|
        freq=cpufreq.max                                         #|
        cores=psutil.cpu_count(logical=False)                    #|
        ram=round(psutil.virtual_memory().total / (1024.0 **3))  #|
        #-------------------------------------------Perfomance---#|
        
        def cvtopg(opencv_image):
            opencv_image = opencv_image[:,:,::-1]
            shape = opencv_image.shape[1::-1]
            pygame_image = pg.image.frombuffer(opencv_image.tostring(), shape, 'RGB')
            return pygame_image

        def back(screen, barmat, unblur, bar):
            for alpha in range(0, 130):
                backgr.set_alpha(alpha)
                screen.blit(backgr, (0,0))
                pg.display.update()
                pg.time.delay(5)
        def choose_shut(screen):
            backgr.blit(screen, (0,0))
            screenimg2=pg.image.load('Media/Images/shutdown.png').convert_alpha()
            XXM=XM
            ratio = XM / YM
            XXM += 30
            YYM = XXM / ratio
            layer.fill(matcolor)
            for alpha in range(0, 110):
                layer.set_alpha(alpha)
                screen.blit(layer, (0,0))
                pg.display.update()
                pg.time.delay(3)
            target = 0
            current = 30
            pg.mixer.music.load('Media/Notify/notify.wav')
            pg.mixer.music.play()
            for i in range(100):
                screenimg22=pg.transform.scale(screenimg2, (XXM,YYM))
                fade.fill(matcolor)
                fade.blit(screenimg22, screenimg22.get_rect(center = screen.get_rect().center))
                fade.set_alpha(alpha)
                screen.fill(matcolor)
                screen.blit(fade, fade.get_rect(center=screen.get_rect().center))
                ratio = XM / YM
                current = lerp(current, target, 0.08)
                XXM -= current
                YYM = XXM / ratio
                alpha+=1
                pg.display.update()
                sleep(0.001)
            power1=1
            x, y=screen.get_rect().center
            pg.display.update()

        def notify(screen, info, power1):
            if power1!=1:
                font=pg.font.Font('Comfortaa.ttf', 16)
                text=font.render(info, 1, (0,0,0))
                target = 200
                current = -10
                pg.mixer.music.load('Media/Notify/notify.wav')
                pg.mixer.music.play()
                sleep(0.2)
                screen_copy = pg.Surface(screen.get_size())
                screen_copy.blit(screen, (0, 0))
                for i in range(100):
                  current = lerp(current, target, 0.08)
                  pg.draw.rect(surf, (255,255,255), (-10, 80, current, 50))
                  surf.blit(text, (current-190, 97))
                  screen.blit(surf, (0,0))
                  pg.display.update()
                  sleep(0.01)
                sleep(3)
                target = -10
                current = 200
                for i in range(100):
                  surf.blit(screen_copy, (0,0))
                  font=pg.font.Font('Comfortaa.ttf', 16)
                  text=font.render(info, 1, (0,0,0))
                  current = lerp(current, target, 0.08)
                  pg.draw.rect(surf, (255,255,255), (-10, 80, current, 50))
                  surf.blit(text, (current-190, 97))
                  screen.blit(surf, (0,0))
                  pg.display.update()
                  sleep(0.01)

        def shutdown(screen, stat):

            screenimg2=pg.image.load('Media/Images/shutdown_screen.png').convert_alpha()
            XXM=XM
            ratio = XM / YM
            XXM += 30
            YYM = XXM / ratio
            layer.fill(matcolor)
            for alpha in range(0, 110):
                layer.set_alpha(alpha)
                screen.blit(layer, (0,0))
                pg.display.update()
                pg.time.delay(3)
            target = 0
            current = 30
            pg.mixer.music.load('Media/shutdown.wav')
            pg.mixer.music.play()

            for i in range(100):
                screenimg22=pg.transform.scale(screenimg2, (XXM,YYM))
                fade.fill(matcolor)
                fade.blit(screenimg22, screenimg22.get_rect(center = screen.get_rect().center))
                fade.set_alpha(alpha)
                screen.fill(matcolor)
                screen.blit(fade, fade.get_rect(center=screen.get_rect().center))
                ratio = XM / YM
                current = lerp(current, target, 0.07)
                XXM -= current
                YYM = XXM / ratio
                alpha+=1
                pg.display.update()
                sleep(0.001)

            sleep(3)
            layer.blit(screenimg22, screenimg22.get_rect(center = screen.get_rect().center))

            for alpha in range(0, 150):
                layer.set_alpha(alpha)
                screen.blit(layer, (0,0))
                pg.display.update()
                pg.time.delay(30)
            sleep(1.0)
            screen.fill([0,0,0])
            pg.display.update()

            if stat=='on':
                os.startfile('Start.py')
                pg.quit()
                sys.exit()
            else:
                pg.quit()
                sys.exit()

        def erroreffect(screen, sloiError2, sloiError):
                pg.image.save(screen, 'monitor-1.png')
                originalImage = cv2.imread('monitor-1.png')
                orimage=pg.image.load('monitor-1.png')
                grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
                (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
                sloiError2.blit(orimage, (0,0))
                cv2.imwrite('bw.png', grayImage)
                blwh=pg.image.load('bw.png')
                sloiError.blit(blwh, (0,0))
                pg.mixer.music.load("Media/ui/erroreffect.wav")
                pg.mixer.music.play()
                alphae=0
                alphaee=0
                while alphae<=100:
                    alphae+=6
                    blwh.set_alpha(alphae)
                    screen.blit(blwh, (0,0))
                    pg.display.update()
                while alphaee!=200:
                    alphaee+=10
                    sloiError2.set_alpha(alphaee)
                    screen.blit(sloiError2, (0,0))
                    pg.display.update()


        def effecterrorload(image):
            Error=1
            screen.fill([0,0,0])
            screenimg2=pg.image.load(image).convert_alpha()
            XXM=XM
            ratio = XM / YM
            XXM += 30
            YYM = XXM / ratio
            layer.fill(matcolor)
            for alpha in range(0, 110):
                layer.set_alpha(alpha)
                screen.blit(layer, (0,0))
                pg.display.update()
                pg.time.delay(3)
            target = 0
            current = 30
            pg.mixer.music.load('Media/Notify/notify.wav')
            pg.mixer.music.play()
            for i in range(100):
                screenimg22=pg.transform.scale(screenimg2, (XXM,YYM))
                fade.fill(matcolor)
                fade.blit(screenimg22, screenimg22.get_rect(center = screen.get_rect().center))
                fade.set_alpha(alpha)
                screen.fill(matcolor)
                screen.blit(fade, fade.get_rect(center=screen.get_rect().center))
                ratio = XM / YM
                current = lerp(current, target, 0.08)
                XXM -= current
                YYM = XXM / ratio
                alpha+=1
                pg.display.update()
                sleep(0.001)

        def errorload2(info):
                if info=='ram':
                    effecterrorload('Media/Images/ram.png')
                if info=='cpu':
                    effecterrorload('Media/Images/cpu.png')

        def fade(screen):
                fade = pg.Surface((XM, YM))
                for alpha in range(0, 100):
                    fade.set_alpha(alpha)
                    pg.display.update()
                    screen.blit(fade, (0,0))
                    pg.display.update()
                    pg.time.delay(5)

        def scale(screen, XM, YM):
            a=100 * float(60)/float(XM)
            b=100 * float(60)/float(YM)-5
            int(a)
            int(b)
            print(a, b)
            image = pyscreenshot.grab()
            image.save("Cache/screen.png")
            img=Image.open('Cache/screen.png')
            imgg=img.filter(ImageFilter.GaussianBlur(100))
            imgg.save('Cache/screen.png')
            image=pg.image.load('Cache/screen.png')
            aa=pg.transform.scale(image, (XM, YM))
            fade.blit(aa, aa.get_rect(center = screen.get_rect().center))
            pg.mixer.music.load('Media/ui/battery.wav')
            pg.mixer.music.play()
            for alpha in range(0, 90):
                fade.set_alpha(alpha)
                screen.blit(fade, (0,0))
                pg.display.update()
                pg.time.delay(5)
            for i in range(30):
                screen.fill([0,0,0])
                XM-=a
                YM-=b
                aa=pg.transform.scale(image, (XM, YM))
                screen.blit(aa, aa.get_rect(center = screen.get_rect().center))
                pg.display.update()
            XM=GetSystemMetrics(0)
            YM=GetSystemMetrics(1)

        def powerUSB(powerup, powerdown, screen, XM, YM, unblur, bar, barmat, blur):
                image = pyscreenshot.grab()
                image.save("Cache/screen.png")
                original_image=Image.open('Cache/screen.png')
                blurred_image = original_image.filter(ImageFilter.GaussianBlur(150))
                blurred_image.save('Cache/blur.png')
                blur=pg.image.load('Cache/blur.png')
                blur2=pg.transform.scale(blur, (XM,YM))
                usb=pg.image.load('Media/Images/usb.png')
                layerUSBP.blit(blur2, blur2.get_rect(center = screen.get_rect().center))
                layerUSBP.blit(usb, usb.get_rect(center = screen.get_rect().center))
                layerUSBP2.blit(unblur, unblur.get_rect(center = screen.get_rect().center))
                layerUSBP2.blit(barmat, (0, 918))
                layerUSBP2.blit(bar, (0, 918))
                if powerdown==1:
                    pg.mixer.music.load('Media/ui/uncharge.wav')
                    pg.mixer.music.play(start=0)
                if powerup==1:
                    pg.mixer.music.load('Media/ui/charge.wav')
                    pg.mixer.music.play(start=0)
                for alpha in range(0, 100):
                    layerUSBP.set_alpha(alpha)
                    screen.blit(layerUSBP, (0,0))
                    pg.display.update()
                    pg.time.delay(5)
                sleep(1)
                for alpha in range(0, 100):
                    layerUSBP2.set_alpha(alpha)
                    screen.blit(layerUSBP2, (0,0))
                    pg.display.update()
                    pg.time.delay(5)
                powerup=0
                powerdown=0

        def welcome(alpha2, alpha3, sloi2, sloi3, screen, bar, barmat, unblur, blur):
                sloi2.blit(blur, (0,0))
                sloi2.blit(barmat, (0,918))
                sloi2.blit(bar, (0,918))
                def sloi3blit():
                    sloi3.blit(unblur, unblur.get_rect(center = screen.get_rect().center))
                    sloi3.blit(barmat, (0, 918))
                    sloi3.blit(bar, (0, 918))
                while alpha2!=50:
                    sloi2.set_alpha(alpha2)
                    screen.blit(sloi2, (0,0))
                    pg.display.update()
                    alpha2+=1
                    sleep(0.01)
                posyy=int(-200)
                pg.mixer.music.load("Media/ui/welcome.wav")
                pg.mixer.music.play()
                while posyy<=75:
                    posyy+=5
                    pg.display.update()
                    sleep(0.004)
                sleep(1.0)
                sloi3blit()
                while alpha3<=50:
                    sloi3.set_alpha(alpha2)
                    screen.blit(sloi3, (0,0))
                    pg.display.update()
                    alpha3+=1
                    sleep(0.06)
                posy2=75
                while posy2>=-45:
                    screen.blit(unblur, unblur.get_rect(center = screen.get_rect().center))
                    screen.blit(barmat, (0,918))
                    screen.blit(bar, (0,918))
                    posy2-=3
                    pg.display.update()

        def welcome2v(unblur, barmat, bar, screen, YM):
            current_date_time = datetime.datetime.now()
            current_time = current_date_time.time()
            hour = current_time.hour
            minute = current_time.minute
            font=pg.font.Font('Comfortaa.ttf', 22)
            text=font.render(f"{hour:02d}:{minute:02d}", 1, (255,255,255))
            YYM=YM-53
            x, y, b, b=bar.get_rect(center = screen.get_rect().center)
            powerlayer3.blit(unblur, unblur.get_rect(center = screen.get_rect().center))
            powerlayer3.blit(barmat, (x, YYM))
            powerlayer3.blit(bar, (x, YYM))
            powerlayer2.blit(unblur, unblur.get_rect(center = screen.get_rect().center))
            powerlayer2.blit(barmat, (x, YYM))
            powerlayer2.blit(bar, (x, YYM))
            x, y, b, b=text.get_rect(center = screen.get_rect().center)
            x-=89
            y=YM-37
            powerlayer2.blit(text, (x, y))
            powerlayer3.blit(text, (x, y))
            font=pg.font.Font('Comfortaa.ttf', 25)
            text=font.render('luminary', 1, (255,255,255))
            powerlayer2.blit(text, text.get_rect(center = screen.get_rect().center))
            powerlayer.blit(text, text.get_rect(center = screen.get_rect().center))
            current_date_time = datetime.datetime.now()
            screen.blit(powerlayer, (0,0))
            pg.mixer.music.load('Media/startsound.ogg')
            pg.display.update()
            pg.mixer.music.play(start=0)
            sleep(2)
            pg.mixer.music.load('Media/ui/startsound2.mp3')
            pg.mixer.music.play(start=0)
            sleep(0.1)
            for alpha in range(0, 100):
                powerlayer2.set_alpha(alpha)
                screen.blit(powerlayer2, (0,0))
                pg.display.update()
                pg.time.delay(5)
            sleep(1)
            for alpha in range(0, 150):
                powerlayer3.set_alpha(alpha)
                screen.blit(powerlayer3, (0,0))
                pg.display.update()
                pg.time.delay(2)


        #---Articles--------------------------------------------------#|

        #screen
        XM=GetSystemMetrics(0)            
        YM=GetSystemMetrics(1)
        FPS = 60
        clock = pg.time.Clock()
   
        #variables
        power1=0
        alpha2=0
        alpha3=0
        stop=0
        Error=0
        powerdown=''
        
        #layers
        layer=pg.Surface((XM,YM))
        fade = pg.Surface((XM, YM))
        sloi2=pg.Surface((XM,YM))
        sloi3=pg.Surface((XM,YM))
        sloiError=pg.Surface((XM,YM))
        sloiError2=pg.Surface((XM,YM))
        layer2=pg.Surface((XM,YM))
        surf=pg.Surface((XM, YM), pg.SRCALPHA)
        layerUSBP=pg.Surface((XM,YM))
        layerUSBP2=pg.Surface((XM,YM))
        powerlayer=pg.Surface((XM,YM))
        powerlayer2=pg.Surface((XM,YM))
        powerlayer3=pg.Surface((XM,YM))
        backgr=pg.Surface((XM,YM))
        powerlayer=pg.Surface((XM,YM))
        screen = pg.display.set_mode((XM, YM))

        #lists
        songlist=[]
        songlist2=[]
        
        #config
        config = open('config.txt','r')
        b=config.read()
        
        #buttons
        bShutdown = pg.draw.rect(screen, (0,0,0), (805, 850, 330, 50))
        bRestart = pg.draw.rect(screen, (0,0,0), (805, 915, 330, 50))
        #-------------------------------------------------------------#|

        #---Secrets-------------------------------------------#|
        check1=os.path.exists('chuck.txt')
        check2=os.path.exists('Quietly_rule.txt')
        #---Secrets-------------------------------------------#|

        vir=pg.image.load('Media/Images/virus.png')
        x,y=screen.get_rect().center
        YYM=YM-45
        XXM=x-45
        chrome=pg.draw.rect(screen, (255,0,0), (XXM, YYM, 40, 40))
        YYM=YM-45
        XXM=x+5
        games=pg.draw.rect(screen, (255,0,0), (XXM, YYM, 40, 40))
        YYM=YM-45
        XXM=x+53
        settings=pg.draw.rect(screen, (255,0,0), (XXM, YYM, 40, 40))
        YYM=YM-45
        XXM=x+100
        music=pg.draw.rect(screen, (255,0,0), (XXM, YYM, 40, 40))
        YYM=YM-45
        XXM=x+148
        explorer=pg.draw.rect(screen, (255,0,0), (XXM, YYM, 40, 40))
        YYM=YM-45
        XXM=x-222
        power=pg.draw.rect(screen, (255,0,0), (XXM, YYM, 40, 40))
        YYM=YM-45
        XXM=x-177
        save=pg.draw.rect(screen, (255,0,0), (XXM, YYM, 40, 40))
        stdn=pg.draw.rect(screen, (255,0,0), (x-225/2, y-57, 225, 40))
        rst=pg.draw.rect(screen, (255,0,0), (x-225/2, y+9, 225, 40))
        back_button=pg.draw.rect(screen, (255,0,0), (x-225/2, y+70,  225, 40))
        virico=pg.draw.rect(screen, (255,0,0), (250, 0, 60, 58))    
            


        #pg.mouse.set_visible(False)
        #cursor_img=pg.image.load('')
        #cursor_img_rect = cursor_img.get_rect()



        def diff(list1, list2):
            list_difference = [item for item in list1 if item not in list2]
            return list_difference
    


        def scale2v():
            XM=GetSystemMetrics(0)
            YM=GetSystemMetrics(1)  
            image = pyscreenshot.grab()
            image.save("Cache/screen.png")
            unblur=pg.image.load('Cache/screen.png')
            img=Image.open('Cache/screen.png')
            imgg=img.filter(ImageFilter.GaussianBlur(30))
            imgg.save('Cache/screen2.png')
            image=pg.image.load('Cache/screen2.png')
            blur=pg.transform.scale(image, (XM, YM))
            fade.blit(blur, blur.get_rect(center = screen.get_rect().center))
            msg=pg.image.load('Media/Images/message.png')
            pg.mixer.music.load('Media/ui//battery2.wav')
            pg.mixer.music.play()
            stat=0
            alpha=0
            target = 0
            current = 15
            target2 = YM-100
            current2 = YM+250
            for i in range(30):
                XXM=XM
                print(pos)
                current = lerp(current, target, 0.1)
                current2 = lerp(current2, target2, 0.1)
                stat+=current
                alpha+=11
                ratio = XM / YM
                XXM -= stat
                YYM = XXM / ratio
                screen.fill([0,0,0])
                fade.fill([0,0,0])
                unblur=pg.transform.scale(unblur, (XXM, YYM))
                blur=pg.transform.scale(image, (XXM, YYM))
                fade.blit(blur, blur.get_rect(center = screen.get_rect().center))
                fade.set_alpha(alpha)
                cenx,ceny, a,a=msg.get_rect(center = screen.get_rect().center)
                print(cenx-250)
                screen.blit(unblur, unblur.get_rect(center = screen.get_rect().center))
                screen.blit(fade, (0,0))
                screen.blit(msg, (cenx, current2))
                pg.display.update()
            XM=GetSystemMetrics(0)
            YM=GetSystemMetrics(1)            



        def rom():
            stop=1
            total_size2=0
            from os.path import getsize, join
            for root, dirs, files in os.walk('.'):
                total_size = sum(getsize(join(root, name)) for name in files)
                total_size2+=total_size
            B = float(total_size2)
            KB = float(B/1024)
            total_size2 = float(KB // 1024)
            YM=GetSystemMetrics(1)
            image = pyscreenshot.grab()
            image.save("Cache/screen.png")
            image=Image.open('Cache/screen.png')
            newimg=image.filter(ImageFilter.GaussianBlur(70))
            newimg.save('Cache/screen.png')
            img=pg.image.load('Cache/screen.png')
            img=pg.transform.scale(img, (XM,YM))
            for path, subdirs, files in os.walk(r'.'):
                for filename in files:
                    print('')
            layer.blit(img, img.get_rect(center = screen.get_rect().center))
            total, used, free = shutil.disk_usage("/")
            total=total // (2**30)
            used=used // (2**30)
            free=free // (2**30)
            height1 = int(YM * (used / total))
            height2 = int(YM * (free / total))
            a=0
            for alpha in range(0, 120):
                layer.set_alpha(alpha)
                screen.blit(layer, (0,0))
                pg.display.update()
            if height1<45:
                height1=45
            if height2<45:
                YYM=YM-45
                height2=45+YYM
            for i in range(20):
                a+=3
                rom1=pg.draw.rect(screen, (128,128,128), (0, 0, a, height2))
                rom2=pg.draw.rect(screen, (58,200,246), (0, height2, a, height1))
                rom3=pg.draw.rect(screen, (255,255,0), (0, YM-45, a, 45))
                pg.display.update()
            font=pg.font.Font('Comfortaa.ttf', 15)
            text=font.render('Свободное место', 1, (255,255,255))
            XXM=75
            YYM=15
            total, used, free = shutil.disk_usage("/")
            total=total // (2**30)
            used=used // (2**30)
            free=free // (2**30)
            str(free)
            str(used)
            str(total_size)
            screen.blit(text, (XXM, YYM))
            free=str(free)+'GB'
            text=font.render(free, 1, (255,255,255))
            XXM=235
            YYM=15
            screen.blit(text, (XXM, YYM))
            text=font.render('Данные NoteOS', 1, (255,255,255))
            XXM=75
            YYM=YM-30
            screen.blit(text, (XXM, YYM))
            total_size2=str(total_size2)+'MB'
            text2=font.render(total_size2, 1, (255,255,255))
            XXM=210
            YYM=YM-30
            screen.blit(text2, (XXM,YYM))
            text=font.render('Другие данные', 1, (255,255,255))
            XXM=75
            YYM=YM-75
            screen.blit(text, (XXM, YYM))
            used=str(used)+'GB'
            text=font.render(used, 1, (255,255,255))
            XXM=210
            YYM=YM-75
            screen.blit(text, (XXM, YYM))
            pg.display.update()

        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------

        #Check system
        if ram<4:
            Error=1
            info='ram'
            errorload2(info)
        elif freq<2.0 or cores<4:
            Error=1
            info='cpu'
            errorload2(info)
        else:
            start()

        def checkUSB(drives, dl):
            uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            x = diff(uncheckeddrives, drives)
            if x:
                powerup=1
                powerUSB(powerup, powerdown, screen, XM, YM, unblur, bar, barmat, blur)
            x = diff(drives, uncheckeddrives)
            if x:
                powerdown=1
                powerUSB(powerup, powerdown, screen, XM, YM, unblur, bar, barmat, blur)
            drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        stop2=0
        def time():
                YYM=YM-53
                x, y, bla,bla=bar.get_rect(center = screen.get_rect().center)
                if stop2!=1:
                    screen.blit(unblur, unblur.get_rect(center = screen.get_rect().center))
                    screen.blit(barmat, (x, YYM))
                    screen.blit(bar, (x, YYM))
                    current_date_time = datetime.datetime.now()
                    current_time = current_date_time.time()
                    hour = current_time.hour
                    minute = current_time.minute
                    second = current_time.second
                    text0=f"{hour:02d}:{minute:02d}"
                    font=pg.font.Font('Comfortaa.ttf', 22)
                    text=font.render(f"{hour:02d}:{minute:02d}", 1, (255,255,255))
                    x, y, bla, bla2=text.get_rect(center = screen.get_rect().center)
                    x-=89
                    y=YM-37
                    screen.blit(text, (x, y))
                    pg.display.update()
            
        def tactic_sound():
            pg.mixer.music.load('Media/ui/choose.wav')
            pg.mixer.music.play()
        def lerp(a, b, t):
            return a + (b - a) * t
        def an():
            sleep(1)
            back(screen, barmat, unblur, bar)
            anim()
            pg.display.update()

        #Work
        touchtactic=1
        stop2=1
        while True:
            screen.blit(vir, (250, 0))
            a1=pg.draw.rect(screen, (255,0,0), (0, 0, 40, 40))
            a2=pg.draw.rect(screen, (255,0,0), (50, 0, 40, 40))
            a3=pg.draw.rect(screen, (255,0,0), (100, 0, 40, 40))
            a4=pg.draw.rect(screen, (255,0,0), (150, 0, 40, 40))
            a5=pg.draw.rect(screen, (255,0,0), (200, 0, 40, 40))
            if stop==0 and stop2==0 and power1!=1:
                time()
            checkUSB(drives, dl)
            for event in pg.event.get():
                pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type ==pg.MOUSEWHEEL:
                    print(event.y)
                elif explorer.collidepoint(pos) and touchtactic==1:
                    rom()
                else:
                    touchtactic=1
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1 and Error!=1:
                        if power.collidepoint(pos):
                            power1=1
                            choose_shut(screen)
                        elif stdn.collidepoint(pos) and power1==1:
                            shutdown(screen, stat='off')
                        elif back_button.collidepoint(pos) and power1==1:
                            back(screen, barmat, unblur, bar)
                            power1=0
                        elif rst.collidepoint(pos) and power1==1:
                            print('...')
                            shutdown(screen, 'on')
                        elif a1.collidepoint(pos):
                            scale(screen, XM, YM)
                            an()
                        elif a2.collidepoint(pos):
                            powerup=1
                            powerUSB(powerup, powerdown, screen, XM, YM, unblur, bar, barmat, blur)
                            an()
                        elif a3.collidepoint(pos):
                            scale2v()
                            an()
                        elif a4.collidepoint(pos):
                            rom()
                            an()
                        elif a5.collidepoint(pos):
                            erroreffect(screen, sloiError2, sloiError)
                            an()
                        elif virico.collidepoint(pos):
                            file=open('Cache/virus.txt', 'w')
                            file.close()
                            sleep(3)
                            shutdown(screen, 'on')
            clock.tick(FPS)
        
#Verb for exceptions
except Exception as e:
    import os
    from time import sleep
    import pygame as pg
    matcolor2=open('Media/color.txt', 'r')

    XM=GetSystemMetrics(0)
    YM=GetSystemMetrics(1)              


    pg.init()
    sleep(2.0)
    errorcode=e
    print(errorcode)
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)

    matcolor2=open('Media/color.txt', 'r')
    matcolor=matcolor2.read()
    matcolor3=matcolor.replace('(', '')
    matcolor4=matcolor3.replace(')', '')
    matcolor = tuple(map(int, matcolor4.split(',')))

    screen=pg.display.set_mode((XM, YM))

    layer=pg.Surface((XM,YM))
    layer2=pg.Surface((XM,YM))
    fade = pg.Surface((XM, YM))
    screenimg2=pg.image.load('Media/Images/sww.png').convert_alpha()
    XXM=XM
    ratio = XM / YM
    XXM += 30
    YYM = XXM / ratio
    font=pg.font.Font('Comfortaa.ttf', 22)
    err=str(errorcode)
    text=font.render(err, 1, (255,255,255))
    x,y,b,b=text.get_rect(center = screen.get_rect().center)
    layer2.fill(matcolor)
    layer2.blit(text, text.get_rect(center=layer2.get_rect().center))
    layer.fill(matcolor)
    for alpha in range(0, 110):
        layer.set_alpha(alpha)
        screen.blit(layer, (0,0))
        pg.display.update()
        pg.time.delay(3)
    target = 0
    current = 30
    for i in range(100):
        screenimg22=pg.transform.scale(screenimg2, (XXM,YYM))
        fade.fill(matcolor)
        fade.blit(screenimg22, screenimg22.get_rect(center = screen.get_rect().center))
        fade.set_alpha(alpha)
        screen.fill(matcolor)
        screen.blit(fade, fade.get_rect(center=screen.get_rect().center))
        ratio = XM / YM
        current = lerp(current, target, 0.07)
        XXM -= current
        YYM = XXM / ratio
        alpha+=1
        pg.display.update()
        sleep(0.001)
    sleep(1)
    for alpha in range(0, 110):
        layer2.set_alpha(alpha)
        screen.blit(layer2, (0,0))
        pg.display.update()
        pg.time.delay(15)

    pg.display.update()
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()