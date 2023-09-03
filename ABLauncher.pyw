from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import os

version = "0.3"
libraries = "client/asm-all-4.1.jar;client/b1.7.3.jar;client/jinput-2.0.5.jar;client/jopt-simple-4.5.jar;client/jutils-1.0.0.jar;client/launchwrapper-1.5.jar;client/lwjgl_util-2.9.0.jar;client/lwjgl-2.9.0.jar;"

def start():
    if nickname.get().isspace():
        showerror(title="Ошибка!", message="В полях не должно быть пробелов!")
        print(nickname.get())
        print(nickname.get().isspace())
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
    ml.write('@echo off'+"\n"+'set APPDATA=%CD%'+"\n"+'"'+jrebin+'\javaw.exe"'' -Xms'+xms+'m -Xmx'+xmx+'m -Djava.library.path="client/natives" -cp "'+libraries+'" net.minecraft.client.Minecraft "'+nickname.get()+'" "'+session+'"')
    ml.close()
    print('@echo off'+"\n"+'set APPDATA=%CD%'+"\n"+'"'+jrebin+'\javaw.exe"'' -Xms'+xms+'m -Xmx'+xmx+'m -Djava.library.path="client/natives" -cp "'+libraries+'" net.minecraft.client.Minecraft "'+nickname.get()+'" "'+session+'"')
    os.system('hmcl.vbs')
def button_accept():
    s = open("settings.txt", 'w')
    s.write(Sxms.get()+"\n"+Sxmx.get()+"\n"+Ssession.get()+"\n"+Sjrebin.get())
    s.close()
    settings.destroy()
def button_reject():
    settings.destroy()

def defsettings():
    global settings
    settings = Tk()
    settings.title("Настройки")
    settings.geometry("275x120")
    settings.resizable(False, False)
    root.iconbitmap(default="favicon.ico")

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
    sessionl = Label(settings, text="Сессия:")
    jrebinl = Label(settings, text="Путь до папки с javaw.exe:")

    btn_accept = Button(settings, text="Принять", command=button_accept)
    btn_reject = Button(settings, text="Отклонить", command=button_reject)

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
            print("тут есть пробелы!")
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

def definfo():
    info = Tk()
    info.title("Информация")
    info.geometry("400x150")
    info.resizable(False, False)
    root.iconbitmap(default="favicon.ico")
    
    info1 = Label(info, text="По всем вопросам в дискорд к __kakao")
    radmin1 = Label(info, text="Наш дискорд сервер:")
    radmin2 = Label(info, text="discord.gg/p2qATAsGMp")
    infoip = Label(info, text="IP сервера (на момент 02.09.23) - недоступен")
    warning = Label(info, foreground="#FF0000", text="Не верьте третьим лицам выдающим себя за владельцев альтбеты!")

    info1.pack()
    radmin1.pack()
    radmin2.pack()
    infoip.pack()
    warning.pack()

def create_settings_file():
    s = open("settings.txt", "w")
    s.write("512"+"\n"+"1024"+"\n"+"12345"+"\n"+"C:\ProgramData\Oracle\Java\javapath")
    s.close
    
#main code

root = Tk()
root.title("ABLauncher.py "+version)
root.geometry("400x300")
root.resizable(False, False)
root.iconbitmap(default="favicon.ico")

canvas = Canvas(root, bg = 'black', height = 245, width = 395)
shot = PhotoImage(file='shot.png')
shotPlace = canvas.create_image(2, 2, anchor=NW, image = shot)

txtlogo = Label(root, text="ABLauncher.py "+version)
nickname = Entry(root)
start = Button(root, text="Играть!", command=start)
btnsettings = Button(root, text="Настройки", command=defsettings)
btninfo = Button(root, text="Информация", command=definfo)

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
start.place(x=135, y=270, height=22)
btnsettings.place(x=189, y=270, height=22)
btninfo.place(x=261, y=270, height=22)

try:
    s = open("lastlogin.txt")
    ioerr = True
    s.close
except IOError:
    ioerr = False
if ioerr:
    tempNN = o.readline()
    if tempNN.isspace():
        pass
    else:
        nickname.delete(0, END)
        nickname.insert(0, tempNN)
        s.close()
else:
    pass

root.mainloop()

