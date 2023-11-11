from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import threading as thr
import zipfile
import shutil as su
import wget
import os

name = "ABLauncher"
version = "0.4"
release = "pre-release-1"
#libraries = "client/asm-all-4.1.jar;client/b1.7.3.jar;client/jinput-2.0.5.jar;client/jopt-simple-4.5.jar;client/jutils-1.0.0.jar;client/launchwrapper-1.5.jar;client/lwjgl_util-2.9.0.jar;client/lwjgl-2.9.0.jar;"
libraries = "client/minecraft.jar;client/jinput.jar;client/lwjgl_util.jar;client/lwjgl.jar;"
special_chars = ['@', "'", '"', '№', '#', '$', ';', '%', '^', ':', '&', '?', '*', '(', ')', '{', '}', '[', ']', '|', '/', ',', '`', '~', '\\', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', ' ']

def start():
    if nickname.get() == "" or " " in nickname.get():
        showerror(title="Ошибка!", message="В полях не должно быть пробелов!")
        print(nickname.get())
        print(nickname.get().isspace())
    elif any(char in nickname.get() for char in special_chars):
        showerror(title="Ошибка!", message="В полях не должно быть спец символов!")
        print(nickname.get())
        print(nickname.get().isspace())
        print(any(char in nickname.get() for char in special_chars))
    else:
        o = open("lastlogin.txt", 'w')
        o.write(nickname.get())
        o.close()
        s = open("settings.txt")
        global xms
        global xmx
        global session
        global jrebin
        xms = s.readline()
        xms = xms[:-1]
        xmx = s.readline()
        xmx = xmx[:-1]
        session = s.readline()
        session = session[:-1]
        jrebin = s.readline()
        s.close()
        print(nickname.get(), xms, xmx, session, jrebin)
        minecraftlauncher()

def minecraftlauncher():
    ml = open("minecraftlauncher.bat", 'w')
    ml.write('@echo off'+"\n"+'set APPDATA=%CD%'+"\n"+'"'+jrebin+'\javaw"'+' -Xms'+xms+'m -Xmx'+xmx+'m -Djava.library.path="client/natives" -cp "'+libraries+'" net.minecraft.client.Minecraft "'+nickname.get()+'" "'+session+'"')
    ml.close()
    print('start')
    os.system('hmcl.vbs')
def button_accept():
    s = open("settings.txt", 'w')
    s.write(Sxms.get()+"\n"+Sxmx.get()+"\n"+Ssession.get()+"\n"+Sjrebin.get())
    s.close()
    settings.destroy()
def button_reject():
    settings.destroy()
    
def Install_Java():
    try:
        os.makedirs("client/natives", exist_ok=True)
    except OSError:
        showerror(title="Ошибка", message="Создать директорию client не удалось")
    else:
        showinfo(title="Инфо", message="Ждите уведомления об окончании загрузки")
        wget.download("https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1Dlse6ruGo6p-ZK_Pr-ffeMwDdWPCkO2w")
        with zipfile.ZipFile('client.zip', 'r') as zip_c:
            zip_c.extractall('client')
        os. remove("client.zip")
        wget.download("https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1TAN4t3Rv1zcoV2EqvW_cmaFwkLV8iRUE")
        with zipfile.ZipFile('resources.zip', 'r') as zip_r:
            zip_r.extractall('.minecraft')
        os. remove("resources.zip")
        showinfo(title="Инфо", message="Загрузка завершена")
        
def create_settings_file():
    s = open("settings.txt", "w")
    s.write("512"+"\n"+"1024"+"\n"+"12345"+"\n"+r"*")
    s.close




#                    #
#    Main windows    #
#                    #
def main_code():
    root = Tk()
    root.title(name+" "+version+" "+release)
    root.geometry("400x300")
    root.resizable(False, False)
    root.iconbitmap(default="res/nya.by/favicon.ico")

    canvas = Canvas(root, bg = 'white', height = 245, width = 395)
    clck = PhotoImage(file='res/nya.by/clck.png')
    clcktPlace = canvas.create_image(315, 165, anchor=NW, image = clck)

    canvas.create_text(5, 5, text="ABLauncher EOL", fill="#FF0000", anchor=NW, font="Arial 14")
    canvas.create_text(5, 30, text="Я решил, что лаунчер который написал какао хоть и не плохой,", fill="#000000", anchor=NW, font="Arial 10")
    canvas.create_text(5, 50, text="но у него есть серьёзные проблемы с совместимостью.", fill="#000000", anchor=NW, font="Arial 10")
    canvas.create_text(5, 80, text="Поэтому, вместо того что бы мучать игроков, я сделаю форк", fill="#000000", anchor=NW, font="Arial 10")
    canvas.create_text(5, 100, text="лаунчера AnjoCaido и начну активнее развивать его,", fill="#000000", anchor=NW, font="Arial 10")
    canvas.create_text(5, 120, text="нежели ABLauncher.", fill="#000000", anchor=NW, font="Arial 10")
    canvas.create_text(5, 150, text="Следите за новостями на нашем дискорд сервере", fill="#FF0000", anchor=NW, font="Arial 10")
    canvas.create_text(5, 170, text="https://clck.ru/36RZvk", fill="#000000", anchor=NW, font="Arial 10")

    global nickname
    txtlogo = Label(root, text=name)
    nickname = Entry(root)
    startb = Button(root, text="Играть!", command=start, cursor="hand2")
    btnsettings = Button(root, text="Настройки", command=defsettings, cursor="hand2")
    btninfo = Button(root, text="Информация", command=definfo, cursor="hand2")

    try:
        s = open("settings.txt")
        ioerr = True
        s.close
    except IOError:
        ioerr = False

    if ioerr:
        pass
    else:
        create_settings_file()
            
    canvas.place(x=0, y=0)
    txtlogo.place(x=10, y=250)
    nickname.place(x=10, y=270, height=22)
    startb.place(x=140, y=270, height=22)
    btnsettings.place(x=195, y=270, height=22)
    btninfo.place(x=270, y=270, height=22)

    try:
        s = open("lastlogin.txt")
        ioerr = True
        s.close
    except IOError:
        ioerr = False
    if ioerr:
        tempNN = s.readline()
        if tempNN.isspace():
            pass
        else:
            nickname.delete(0, END)
            nickname.insert(0, tempNN)
            s.close()
    else:
        pass
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    root.mainloop()


def defsettings():
    global settings
    settings = Tk()
    settings.title("Настройки")
    settings.geometry("275x120")
    settings.resizable(False, False)
    settings.iconbitmap(default="res/nya.by/favicon.ico")

    global Sxms
    global Sxmx
    global Ssession
    global Sjrebin

    Sxms = Entry(settings)
    Sxmx = Entry(settings)
    Ssession = Entry(settings)
    Sjrebin = Entry(settings)
    xmsl = Label(settings, text="Мин. кол-во памяти:")
    xmxl = Label(settings, text="Макс. кол-во памяти:")
    sessionl = Label(settings, text="Сессия (не больно важно):")
    jrebinl = Label(settings, text="Путь до папки с javaw.exe:")

    btn_accept = Button(settings, text="Принять", command=button_accept, cursor="hand2")
    btn_reject = Button(settings, text="Отклонить", command=button_reject, cursor="hand2")

    Sxms.grid(column=1, row=0)
    Sxmx.grid(column=1, row=1)
    Ssession.grid(column=1, row=2)
    xmsl.grid(column=0, row=0)
    xmxl.grid(column=0, row=1)
    sessionl.grid(column=0, row=2)
    jrebinl.grid(column=0, row=3)  
    Sjrebin.grid(column=1, row=3)
      
    
    btn_accept.grid(column=0, row=6)
    btn_reject.grid(column=1, row=6)

    try:
        o = open("settings.txt")
        ioerr = True
    except IOError:
        ioerr = False
    if ioerr:
        tempXms = o.readline()
        tempXmx = o.readline()
        tempSess = o.readline()
        tempJrebin = o.readline()
        if tempXms.isspace() and tempXmx.isspace() and tempSess.isspace():
            print("True")
        else:
            Sxms.delete(0, END)
            Sxmx.delete(0, END)
            Ssession.delete(0, END)
            tempXms = tempXms[:-1]
            tempXmx = tempXmx[:-1]
            tempSess = tempSess[:-1]
            Sxms.insert(0, tempXms)
            Sxmx.insert(0, tempXmx)
            Ssession.insert(0, tempSess)
            Sjrebin.insert(0, tempJrebin)
            o.close()
    else:
        pass
    settings.eval('tk::PlaceWindow %s center' % settings.winfo_pathname(settings.winfo_id()))


def definfo():
    info = Tk()
    info.title("Информация")
    info.geometry("400x150")
    info.resizable(False, False)
    info.iconbitmap(default="res/nya.by/favicon.ico")
    
    info1 = Label(info, text="По всем вопросам на наш Discord сервер:")
    radmin1 = Label(info, text="discord.gg/p2qATAsGMp")
    warning = Label(info, foreground="#FF0000", text="Не верьте третьим лицам выдающим себя за владельцев AltBeta!")
    installjava = Button(info, text='Обновить клиент', command=Install_Java, cursor="hand2")
    ver = Label(info, text="Версия: "+version+" "+release)
    cr = Label(info, text="© 2023 __kakao & atarwn")

    ver.pack()
    info1.pack()
    radmin1.pack()
    warning.pack()
    installjava.pack()
    cr.pack()
    info.eval('tk::PlaceWindow %s center' % info.winfo_pathname(info.winfo_id()))

main_code()
#                    #
#      Threading     #
#                    #
#t1 = thr.Thread(target=main_code, name="LauncherStart")
#t2 = thr.Thread(target=lus, name="LauncherUpdaterStart")
#t1.start()
#t2.start()
#t1.join()
#t2.join()
