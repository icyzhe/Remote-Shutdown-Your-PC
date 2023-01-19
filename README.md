# Remote shutdown your PC 通过手机微信和电脑微信实现远程关闭你的计算机
Turn off your computer through mobile phone WeChat and computer WeChat.

其它有快捷键的通信软件理论上也完全可以。

第一步：你需要做的是将两个.py文件通过pyinstaller3.8 -F -w xxxxx.py打包成.exe格式，并将两个.exe文件放到C:\Windows\System32目录下。需要注意的是，shutdown.py中需要用到文字识别技术，需要你自己去百度注册一个通用文字识别（标准版），网址是：https://ai.baidu.com/ ，网络上有很多教程。成功之后在shutdownPC.py里面替换成你自己的AppID、API Key和Secret Key。

第二步：你需要做的是按下windows键+R，输入regedit，打开注册表，找到计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers，右键新建字符串值，修改数值名称为C:\Windows\System32\Icyzhe.exe，修改数值数据为RunAsInvoker。这会使得当我们计算机运行Icyzhe.exe程序时，不会弹出UAC用户账户控制，这将会很有用。后面会解释。

第三步：你需要做的是右键“此电脑”选择管理。看到任务计划程序了吗，点击它，选择右边的创建基本任务。名称描述随你，触发器选择每天，时间可以后面再修改，也可以在这里直接设置成你每天想要关机的时间，成功之后选择下一步，操作选择启动程序，点击浏览，选择我们的C:\Windows\System32\Icyzhe.exe，并选择完成。之后在任务计划程序库中找到你刚才创建的任务名称，双击进行修改，选择触发器这一栏，可以修改成“在每天的22:25触发后，无限期地每隔15分钟重复一次”。点击确定后如果提示不成功，那么选择常规这一栏的更改用户或组，之后选择高级，立即查找，找到你当前登录的账户，确定即可。最后，记得在常规这一栏勾选隐藏和以最高权限运行。这一步的关机时间随你设定，每个人的作息不同，我想说的是可以重复提醒而已。

到这里我们的程序设置基本完成了，你可以将任务计划程序的时间改成现在的时间并且间隔1分钟重复一次以便进行测试。注意，每隔x分钟重复一次的前提是先触发一次，所以最好设置的触发时间足够你后面操作。

程序的工作流程：假设你上面的步骤全没问题了，那么在你的电脑上登录Wechat，当然你的手机也需要登录，并且确保你设置了手机和电脑可以同时在线。让你电脑端的Wechat在后台运行(最小化窗口)。之后用手机向“文件传输助手”发送关机指令，比如：shutdown /s /t 600，此时到达你设置的任务计划程序触发时间，那么系统会运行Icyzhe.exe，而Icyzhe.exe会用管理员的身份运行shutdownPC.exe。(注：如果系统弹出UAC用户账户控制提示，说明你的第二步没有成功，这对我这样的懒人是致命的问题，假设这样一个场景，当你已经上床准备休息，却发现电脑没有关机，你不愿意再穿好鞋子下床走到电脑面前选择关机按钮，而是想通过这个程序关闭计算机，于是你通过手机向文件传输助手发送了关机命令，电脑也如期运行了程序，但是弹出了UAC用户账户控制，需要你选择“是”或“否”，windows才可以进行下一步任务，这很糟糕！这意味着你还需要下床走到电脑前，选择“是”后，躺回床上等待windows运行程序，这太蠢了。而我们在第二步的操作就是指定windows在运行Icyzhe.exe这一个程序时，不弹出UAC用户账户控制，这就解决了问题。)shutdownPC.exe会用快捷键打开微信窗口，并且搜索文件传输助手，截图并文字识别你所发送的最后一条命令——关机命令，并尝试执行它，如果成功了，你的计算机将会定时关闭，如果命令有问题则会执行失败但没有提醒，并且任务计划程序会按照间隔的时间继续运行Icyzhe.exe。

祝你使用愉快！
