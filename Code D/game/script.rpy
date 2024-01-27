# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene sunny sky

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show riding happy

    # 此处显示各行对话。

    e "小龙，我们出发吧！"

    #全屏播放动画后3秒后继续剧情

    $ renpy.movie_cutscene("/images/cutscene/riding_happy.webm",delay=3.0)
    
    e "哇，慢一点。我可不想被摔下去！"

    menu:
        "抓紧缰绳(进入goodend)":
            jump goodend  # 结束游戏
        "吓得松开双手去抱小龙(进入badend)":
            jump badend  # 开始游戏

label goodend:
    e "谢谢你救了我！"
    jump credits

label badend:
    hide riding happy
    "你向空中坠落，眼角不断掉出后悔的形状..."
    jump credits

label credits:
    scene black  # 设置背景为黑色
    pause 1.0  # 等待1秒钟
    "制作团队"  # 第一行文本
    pause 1.0  # 每行文字显示后暂停1秒钟
    "编剧: 熊超"  # 第二行文本
    pause 1.0
    "美术设计: Bing Create、Pika.art"  # 第三行文本
    pause 1.0
    "音乐: 暂无"  # 第四行文本
    pause 1.0
    "特别感谢: 家人和朋友"  # 第五行文本
    pause 1.0
    "Ren'Py引擎"  # 第六行文本

    return
    # 此处为游戏结尾。