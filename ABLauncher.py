from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import threading as thr
import zipfile
import shutil as su
import wget
import os
import xml.etree.ElementTree as ET
import webbrowser


name = "ABLauncher"
version = "0.4"
release = "pr4"
build2 = '7'
libraries = "client/minecraft.jar;client/jinput.jar;client/lwjgl_util.jar;client/lwjgl.jar;"
special_chars = ['@', "'", '"', '№', '#', '$', ';', '%', '^', ':', '&', '?', '*', '(', ')', '{', '}', '[', ']', '|', '/', ',', '`', '~', '\\', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', ' ']

if not os.path.exists("res"):
    os.mkdir("res")
elif not os.path.exists("res/config"):
    os.mkdir("res/config")
    

def start():
    if nickname.get() == "" or nickname.get() == " " in nickname.get():
        showerror(title="Ошибка!", message="В полях не должно быть пробелов!")
        print(nickname.get())
        print(nickname.get().isspace())
    elif any(char in nickname.get() for char in special_chars):
        showerror(title="Ошибка!", message="В полях не должно быть спец символов!")
        print(nickname.get())
        print(nickname.get().isspace())
        print(any(char in nickname.get() for char in special_chars))
    else:
        o = open("res/config/lastlogin.txt", 'w')
        o.write(nickname.get())
        o.close()
        s = open("res/config/settings.txt")
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
    ml = open("hmcl.vbs", 'w')
    ml.write('Set WshShell = CreateObject("WScript.Shell")'+'\n'+'WshShell.Run chr(34) & "minecraftlauncher.bat" & Chr(34), 0')
    ml.close()
    os.system('hmcl.vbs')
    
def Update_Client():
    try:
        os.makedirs("client/natives", exist_ok=True)
    except OSError:
        showerror(title="Ошибка", message="Создать директорию client не удалось")
    else:
        showinfo(title="Инфо", message="Ждите уведомления об окончании загрузки")
        wget.download("https://atarwn.github.io/abl/client.zip")
        with zipfile.ZipFile('client.zip', 'r') as zip_c:
            zip_c.extractall('client')
        os. remove("client.zip")
        wget.download("https://atarwn.github.io/abl/resources.zip")
        with zipfile.ZipFile('resources.zip', 'r') as zip_r:
            zip_r.extractall('.minecraft/resources')
        os. remove("resources.zip")
        wget.download("https://atarwn.github.io/abl/resources_music.zip")
        with zipfile.ZipFile('resources_music.zip', 'r') as zip_rm:
            zip_rm.extractall('.minecraft/resources')
        os. remove("resources_music.zip")
        showinfo(title="Инфо", message="Загрузка завершена")

def Install_Java():
    try:
        o = open("res/config/settings.txt")
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
            tempXms = tempXms[:-1]
            tempXmx = tempXmx[:-1]
            tempSess = tempSess[:-1]
            tempJrebin = str(os.path.dirname(os.path.abspath(__file__)))+"\\res\\local-resources\\Java\\bin"
            o.close()
            o = open("res/config/settings.txt", "w")
            o.write(tempXms+"\n"+tempXmx+"\n"+tempSess+"\n"+tempJrebin)
            print(tempXms+"\n"+tempXmx+"\n"+tempSess+"\n"+tempJrebin)
            o.close()
    else:
        pass
    showerror(title="Упс!", message="Данная функция пока недоступна, ждите обновления!")

        
def Open_Support():
    webbrowser.open("https://atarwn.github.io/abl/")



    
#                    #
#    Main windows    #
#                    #

# окно настроек
def defsettings():
    def button_accept():
        s = open("res/config/settings.txt", 'w')
        s.write(Sxms.get()+"\n"+Sxmx.get()+"\n"+Ssession.get()+"\n"+Sjrebin.get())
        s.close()
        s = open("res/config/autoupdate.txt", 'w')
        print(au_enabled.get())
        s.write(str(au_enabled.get()))
        s.close()
        settings.destroy()
    def button_reject():
        settings.destroy()

        
    global settings
    settings = Toplevel()
    settings.title("Настройки")
    settings.geometry("275x135")
    settings.resizable(False, False)
    settings.iconbitmap(default="res/local-resources/favicon.ico")

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

    au_enabled = BooleanVar()

    btn_accept = Button(settings, text="Применить", command=button_accept, cursor="hand2")
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
        au = open("res/config/autoupdate.txt")
        ioerr = True
        au.close
    except IOError:
        ioerr = False
    if ioerr:
        au = open("res/config/autoupdate.txt")
        if au.read() == "True":
            au_enabled.set(True)
        else:
            au_enabled.set(False)
    else:
        create_config_au_file()
        check_update()
        
    autoupdatech = ttk.Checkbutton(settings, text="Включить", variable=au_enabled)
    autoupdatel = Label(settings, text="Автообновление:")
    autoupdatel.grid(column=0, row=4)
    autoupdatech.grid(column=1, row=4)


    try:
        o = open("res/config/settings.txt")
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
    

# Надо
def create_settings_file():
    s = open("res/config/settings.txt", "w")
    s.write("512"+"\n"+"1024"+"\n"+"12345"+"\n"+r"*")
    s.close
    showwarning(title="Внимание!", message="Это ваш первый запуск лаунчера, пожалуйста, выберите и скопируйте путь к папке bin в папке java!")
    defsettings()
    Sxms.insert(0, "512")
    Sxmx.insert(0, "1024")
    Ssession.insert(0, "12345")
    Sjrebin.insert(0, "ВСТАВИТЬ СЮДА")
    webbrowser.open("C:\Program Files\Java")
def create_config_au_file():
    s = open("res/config/autoupdate.txt", "w")
    s.write("False")
    s.close

# окно с информацией
def definfo():
    global info
    info = Toplevel()
    info.title("Информация")
    info.geometry("300x200")
    info.resizable(False, False)
    info.iconbitmap(default="res/local-resources/favicon.ico")
    
    info1 = Label(info, text="По всем вопросам на наш Discord сервер:")
    radmin1 = Label(info, text="discord.gg/p2qATAsGMp")
    # warning = Label(info, foreground="#FF0000", text="Не верьте третьим лицам выдающим себя за владельцев AltBeta!")    # возможно будет удалено
    updateclient = Button(info, text='Обновить клиент Minecraft', command=Update_Client, cursor="hand2")
    installjava = Button(info, text='Установить рекомендуемую Java', command=Install_Java, cursor="hand2")
    opensupport = Button(info, text='Открыть справку', command=Open_Support, cursor="hand2")
    ver = Label(info, text="Версия: "+version+" "+release)
    cr = Label(info, text="\n\n© 2024 __kakao & atarwn")

    ver.pack()
    info1.pack()
    radmin1.pack()
    # warning.pack()    # возможно будет удалено
    updateclient.pack()
    installjava.pack()
    opensupport.pack()
    cr.pack()

# обновлятор
def call_updater():
    if os.path.exists(wget.download('https://atarwn.github.io/abl/u.zip')):
        with zipfile.ZipFile('u.zip', 'r') as zip_c:
            zip_c.extractall('')
        os.remove("u.zip")
        exit()
    else:
        showwarning(title='Ой!', message='Указанный файл отсутствует на сервере, игнорируем...')
def check_update(): 
    if build1 > build2:
        downloadAccept = askyesno(title="!", message="Доступно обновление! Хотите скачать?")            
        if os.name!='nt':
            showerror(title='Упс!', message='Автоматическое обновление пока что недоступно в ващей операционной системе')
        elif downloadAccept:
            call_updater()
    elif build1 <= build2:
        showinfo(title='Ура!', message='Вы используете последнюю версию!')

####   #  ### #  #
# # # ###  #  ## #
# # # # # ### # ##
def main_code():
    def close_all_windows():
        print(root.winfo_children)
    
    root = Tk()
    root.title(name+" "+version+" "+release)
    root.geometry("400x300")
    root.resizable(False, False)
    root.iconbitmap(default="res/local-resources/favicon.ico")
    
    global build1
    if os.path.exists(wget.download('https://atarwn.github.io/abl/newupdate.xml', 'temp_bmV3dXBkYXRlLnhtbA.xml')):
        os.remove('temp_bmV3dXBkYXRlLnhtbA.xml')
        if os.path.exists('res/local-resources/newupdate.xml'):
            os.remove('res/local-resources/newupdate.xml')
        else:
            pass
        wget.download('https://atarwn.github.io/abl/newupdate.xml', 'res/local-resources/newupdate.xml')
        uxml1 = ET.parse('res/local-resources/newupdate.xml')
        root1 = uxml1.getroot()
        build1 = root1.find('build').text
    else:
        uxml1 = ET.parse('res/local-resources/newupdate.xml')
        root1 = uxml1.getroot()
        build1 = root1.find('build').text
        showwarning(title='Ой!', message='Указанный файл отсутствует на сервере, игнорируем...')

    
    try:
        au = open("res/config/autoupdate.txt")
        ioerr = True
        au.close
    except IOError:
        ioerr = False

    if ioerr:
        au = open("res/config/autoupdate.txt")
        if au.read() == "True":
            check_update()
        else:
            pass
    else:
        create_config_au_file()
        check_update()
        

    canvas = Canvas(root, bg = 'white', height = 245, width = 395)
    buildName1 = root1.find('buildname').text
    date1 = root1.find('date').text
    relnotes1 = root1.find('relnotes').text

    print('Build:', build1)
    print('Name: ', buildName1)
    print('Date:', date1)
    print('Release Notes:', relnotes1) #Max symbols: 54; Max lines: 8 

    canvas_bg = PhotoImage(file="res/local-resources/shot.png")
    canvas.create_image(1, 1, anchor=NW, image=canvas_bg)
    
    canvas.create_text(5, 5, text='Обновление '+buildName1, fill="#FFFFFF", anchor=NW, font="Arial 14")
    canvas.create_text(5, 30, text=date1, fill="#FFFFFF", anchor=NW, font="Arial 10")
    canvas.create_text(5, 45, text='Изменения:', fill="#FFFFFF", anchor=NW, font="Arial 10")
    canvas.create_text(5, 45, text=relnotes1, fill="#FFFFFF", anchor=NW, font="Arial 10")
    canvas.create_text(5, 210, text="Следите за новостями на нашем дискорд сервере", fill="#FF00FF", anchor=NW, font="Arial 10")
    
    canvas.create_text(5, 229, text="https://clck.ru/36RZvk", fill="#00FFFF", anchor=NW, font="Arial 10")


    global nickname
    txtlogo = Label(root, text=name)
    nickname = Entry(root)
    startb = Button(root, text="Играть!", command=start, cursor="hand2")
    btnsettings = Button(root, text="Настройки", command=defsettings, cursor="hand2")
    btninfo = Button(root, text="Информация", command=definfo, cursor="hand2")

    try:
        s = open("res/config/settings.txt")
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
        s = open("res/config/lastlogin.txt")
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

    root.mainloop()

#                         #
#   Resources not found   #
#                         #
def resources_out_code():
    def close_all_windows():
        print(root.winfo_children)
    
    root = Tk()
    root.title(name+" "+version+" "+release)
    root.geometry("400x300")
    root.resizable(False, False)        
    showerror(title="Ошибка!", message="Отсутствует папка или некоторые ресурсы!\nНормальный запуск лаунчера невозможен")
    
    canvas = Canvas(root, bg = 'white', height = 90, width = 395)
    
    canvas.create_text(5, 5, text='Отсутствует папка или некоторые ресурсы!', fill="#FF0000", anchor=NW, font="Arial 14")
    canvas.create_text(5, 30, text='Нормальный запуск лаунчера невозможен', fill="#FF0000", anchor=NW, font="Arial 10")
    canvas.create_text(5, 50, text="При возникновении проблем обратитесь на сервер поддержки", fill="#FF0000", anchor=NW, font="Arial 10")
    
    canvas.create_text(5, 70, text="https://clck.ru/36RZvk", fill="#000000", anchor=NW, font="Arial 10")


    global nickname
    txtlogo = Label(root, text=name)
    nickname = Entry(root)
    startb = Button(root, text="Играть!", command=start, cursor="hand2")
    #btnsettings = Button(root, text="Настройки", command=defsettings, cursor="hand2")
    #btninfo = Button(root, text="Информация", command=definfo, cursor="hand2")

    try:
        s = open("res/config/settings.txt")
        ioerr = True
        s.close
    except IOError:
        ioerr = False

    if ioerr:
        pass
    else:
        create_settings_file()
            
    canvas.place(x=0, y=158)


    #~~~ Settings ~~~#
    def button_accept():
        s = open("res/config/settings.txt", 'w')
        s.write(Sxms.get()+"\n"+Sxmx.get()+"\n"+Ssession.get()+"\n"+Sjrebin.get())
        s.close()
        s = open("res/config/autoupdate.txt", 'w')
        print(au_enabled.get())
        s.write(str(au_enabled.get()))
        s.close()

    global Sxms
    global Sxmx
    global Ssession
    global Sjrebin

    Sxms = Entry(root)
    Sxmx = Entry(root)
    Ssession = Entry(root)
    Sjrebin = Entry(root)
    xmsl = Label(root, text="Мин. кол-во памяти:")
    xmxl = Label(root, text="Макс. кол-во памяти:")
    sessionl = Label(root, text="Сессия (не больно важно):")
    jrebinl = Label(root, text="Путь до папки с javaw.exe:")

    au_enabled = BooleanVar()

    btn_accept = Button(root, text="Применить", command=button_accept, cursor="hand2")

    Sxms.grid(column=1, row=0)
    xmsl.grid(column=0, row=0)
    Sxmx.grid(column=1, row=1)
    xmxl.grid(column=0, row=1)
    Ssession.grid(column=1, row=2)
    sessionl.grid(column=0, row=2)
    jrebinl.grid(column=0, row=3)  
    Sjrebin.grid(column=1, row=3)
    
    btn_accept.grid(column=0, row=6)

    try:
        au = open("res/config/autoupdate.txt")
        ioerr = True
        au.close
    except IOError:
        ioerr = False
    if ioerr:
        au = open("res/config/autoupdate.txt")
        if au.read() == "True":
            au_enabled.set(True)
        else:
            au_enabled.set(False)
    else:
        create_config_au_file()
        check_update()
        
    autoupdatech = ttk.Checkbutton(root, text="Включить", variable=au_enabled)
    autoupdatel = Label(root, text="Автообновление:")
    autoupdatel.grid(column=0, row=4)
    autoupdatech.grid(column=1, row=4)


    try:
        o = open("res/config/settings.txt")
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
    #~~~ Settings ~~~#
    
    txtlogo.place(x=10, y=250)
    nickname.place(x=10, y=270, height=22)
    startb.place(x=140, y=270, height=22)

    try:
        s = open("res/config/lastlogin.txt")
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

    root.mainloop()
#   Resources not found   #


if not os.path.exists("res/local-resources") or not os.path.exists("res/local-resources/favicon.ico") or not os.path.exists("res/local-resources/shot.png"):
    #if not os.path.exists("res/local-resources"):
    #    os.mkdir("res/local-resources")
    resources_out_code()
else:
    main_code()
