import os
import keyboard
import time
from aip import AipOcr
from PIL import Image, ImageGrab
import sys,ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



if is_admin():

    keyboard.press_and_release('ctrl+alt+w')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+f')
    time.sleep(0.5)
    keyboard.write('文件传输助手')
    time.sleep(0.5)
    keyboard.press_and_release('enter')

    time.sleep(0.5)
    keyboard.press_and_release('alt+print screen')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+alt+w')
    time.sleep(0.5)

    # 将从屏幕获取到的截图存储到同级目录下
    image = ImageGrab.grabclipboard()
    image.save("pic.png")
    time.sleep(0.5)
    img = Image.open('pic.png')
    width, height = img.size

    left = width / 2
    top = height / 2
    right = width
    bottom = height
    im1 = img.crop((left, top, right, bottom))
    im1.save('pic.png')

    # 此处填写你的APP参数信息
    APP_ID = '29768744'
    API_KEY = 'hjSWwMo3ubTzP3ETpD0Dso47'
    SECRET_KEY = 'w03jtogaEVfG5sX8nwq3gakF2eMhVoix'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    img = open('pic.png', 'rb').read()
    message = client.basicGeneral(img)
    res = message['words_result']
    # print(res[-2]['words']) #待执行的命令
    # for i in res:
    #     print(i['words'])

    os.popen(res[-2]['words'])

else:
    if sys.version_info[0] == 3:
        # print("无管理员权限")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)