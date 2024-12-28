# AI雀魂python脚本
我称之为 雀魂最高牌效全自动放炮机！<br>
## 使用指南
下载项目文件后，请在安装了以下库的虚拟环境下运行：<br>
PyAutoGUI,<br>selenium,<br>opencv-python<br><br>

运行程序时，为保证雀魂界面的识别准确性，请勿让其他窗口遮盖雀魂游戏窗口。此外，请将雀魂调整至1080p分辨率。
效果演示视频见b站[https://www.bilibili.com/video/BV1k26pY3E8J/](https://www.bilibili.com/video/BV1k26pY3E8J/)

## 实现原理
使用opencv库进行牌面识别，使用pyautogui库进行鼠标的控制。出牌逻辑通过网页爬虫获取。
