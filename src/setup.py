from os import mkdir, getlogin
from win32com.client import Dispatch
from win32ui import MessageBox
from requests import get
try:
    mkdir("C:/SdBomber")
except FileExistsError:
    pass
try:
    r = get("https://sametdrs.me/pages/api/SdBomber/V2/main.exe")
    with open("C:/SdBomber/main.exe", "wb") as f:
        f.write(r.content)
    r = get("https://sametdrs.me/pages/api/SdBomber/V2/style.css")
    with open("C:/SdBomber/style.css", "wb") as f:
        f.write(r.content)
    r = get("https://sametdrs.me/pages/api/SdBomber/V2/SdBomber.ico")
    with open("C:/SdBomber/SdBomber.ico", "wb") as f:
        f.write(r.content)
except Exception:
    MessageBox("Dosyalar indirilemedi!", "SD Bomber", 0)
    exit()
try:
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(
        f"C:/Users/{getlogin()}/Desktop/SD Bomber.lnk")
    shortcut.Targetpath = f"C:/SdBomber/main.exe"
    shortcut.iconlocation = f"C:/SdBomber/SdBomber.ico"
    shortcut.save()
except Exception:
    MessageBox("Kısayol oluşturulamadı!", "SD Bomber", 0)
MessageBox("SD Bomber başarıyla yüklendi!", "SD Bomber", 0)