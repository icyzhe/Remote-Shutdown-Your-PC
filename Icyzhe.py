import os
import time
import sys,ctypes
import schedule


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    os.popen("shutdownPC.exe")

else:
    if sys.version_info[0] == 3:
        # print("无管理员权限")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
