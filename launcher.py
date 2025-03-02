from subprocess import Popen
from pyautogui import moveTo, click, hotkey
from win32gui import FindWindow, SetWindowPos
from time import sleep
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW


def popen_launcher():
    # 启动程序
    launcher = Popen(["E:\webcast_mate\直播伴侣 Launcher.exe"])
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
    # SetWindowPos(hwnd_launcher, HWND_TOPMOST, 0, 0, 1920, 1080, SWP_SHOWWINDOW)  # 调整窗口大小并置顶
    moveTo(1370, 800)
    click()



def popen_obs():
    # 启动OBS
    Popen(["D:\obs-studio\bin\64bit\obs64.exe"])
    sleep(2)  # 等待OBS启动并加载窗口
    while True:
        # 如果不知道窗口类名，可以将其设为None，查找窗口标题
        hwnd_launcher = FindWindow("Chrome_WidgetWin_1", "直播伴侣")
        if hwnd_launcher:
            break
        else:
            print("未找到窗口，等待1秒...")
            sleep(1)
    print("窗口找到！")
    SetWindowPos(hwnd_launcher, HWND_TOPMOST, 0, 0, 1623, 1135, SWP_SHOWWINDOW)  # 调整窗口大小并置顶

    moveTo(809, 419)








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
    # 等待获取推流码
    sleep(1)
    moveTo(250,90)
    click()
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    moveTo(250,175)
    click()
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    # 关闭webcast_mate
    caster.kill()


# popen_obs()
popen_webcast_mate()
# popen_launcher()

    
