from subprocess import Popen
from pyautogui import moveTo, click, hotkey,locateOnScreen,ImageNotFoundException
from win32gui import FindWindow, SetWindowPos
from time import sleep
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW
from os import system
import share

def popen_launcher():
    # 启动程序
    share.launcher = Popen(["E:\webcast_mate\直播伴侣 Launcher.exe"])
    sleep(5)  # 等待程序启动并加载窗口

    # 查找窗口句柄，确保类名和标题都正确
    while True:
        hwnd_launcher = FindWindow("Chrome_WidgetWin_1", "直播伴侣")  # 如果不知道窗口类名，可以将其设为None，查找窗口标题
        if hwnd_launcher:
            break
        else:
            print("未找到窗口，等待1秒...")
            sleep(1)

    print("窗口找到！")
    sleep(1)
    SetWindowPos(hwnd_launcher, HWND_TOPMOST, 0, 0, 1920, 1080, SWP_SHOWWINDOW)  # 调整窗口大小并置顶
    sleep(1)
    while True:
        try:
            auto1 = locateOnScreen('img/1.png', confidence=0.95)
            moveTo(auto1)
            click()
        except ImageNotFoundException:
            print("未找到图片，等待1秒...")
            sleep(1)
        try:
            auto4 = locateOnScreen('img/4.png', confidence=0.8)
            moveTo(auto4)
            click()
        except ImageNotFoundException:
            print("未找到恢复画面，等待1秒...")
            sleep(1)
        try:
            locateOnScreen('img/5.png', confidence=0.8)
            break
        except ImageNotFoundException:
            print("未找到关播，等待1秒...")
            sleep(1)
    sleep(5)


def popen_obs():
    
    # 启动OBS
    # 指定工作目录
    obs_path = r"D:\obs-studio\bin\64bit\obs64.exe"
    working_dir = r"D:\obs-studio\bin\64bit"
    Popen([obs_path], cwd=working_dir)
    sleep(3)  # 等待OBS启动并加载窗口

    while True:
        # 如果不知道窗口类名，可以将其设为None，查找窗口标题
        hwnd_launcher = FindWindow("Qt663QWindowIcon", "OBS 31.0.1 - 配置文件: 1212 - 场景: a1")
        if hwnd_launcher:
            break
        else:
            print("未找到窗口，等待1秒...")
            sleep(1)
    print("窗口找到！")
    SetWindowPos(hwnd_launcher, HWND_TOPMOST, 0, 0, 1623, 1135, SWP_SHOWWINDOW)  # 调整窗口大小并置顶
    sleep(1.5)
    moveTo(809, 419)
    click()
    sleep(2)
    moveTo(150,192)
    click()
    while True:
        try:
            auto2 = locateOnScreen('img/2.png', confidence=0.8)
            moveTo(auto2.left + 100, auto2.top)
            click()
            break
        except ImageNotFoundException:
            print("未找到图片，等待1秒...")
            sleep(1)
    hotkey('ctrl', 'a')
    sleep(0.2)
    hotkey('ctrl', 'v')
    sleep(1)
    moveTo(auto2.left + 100, auto2.top + 80)
    click()
    hotkey('ctrl', 'a')
    hotkey('win', 'v')
    sleep(1)
    while True:
        try:
            auto3 = locateOnScreen('img/3.png', confidence=0.8)
            moveTo(auto3.left + 100, auto3.top + 230)
            click()
            break
        except ImageNotFoundException:
            print("未找到图片，等待1秒...")
            sleep(1)
    sleep(1)
    moveTo(1273,1100)
    click()
    sleep(1)
    moveTo(811,150)
    click()










def popen_webcast_mate():
    # 启动webcast_mate
    caster = Popen(["E:\webcast_mate\推流码获取工具.exe"])
    sleep(1)  # 等待webcast_mate启动并加载窗口
    moveTo(1284,819)
    click()
    sleep(1) 
    while True:
        # 如果不知道窗口类名，可以将其设为None，查找窗口标题
        hwnd_tool = FindWindow("TfrmMain", "推流小助手 v1.1")
        if hwnd_tool:
            break
        else:
            print("未找到窗口，等待1秒...")
            sleep(1)
    print("窗口找到！")
    SetWindowPos(hwnd_tool, HWND_TOPMOST, 0, 0, 1280, 900, SWP_SHOWWINDOW)
    sleep(0.5)
    moveTo(1207,90)
    click()
    sleep(3)
    # 等待获取推流码
    while True:
        try:
            auto6 = locateOnScreen('img/6.png', confidence=0.8)
            break
        except ImageNotFoundException:
            print("未找到图片，等待1秒...")
            sleep(1)
    sleep(0.5)
    moveTo(250,175)
    click()
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    sleep(0.8)
    moveTo(250, 90)
    click()
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    # 关闭webcast_mate
    caster.kill()

    system('taskkill /F /IM "直播伴侣.exe"')

