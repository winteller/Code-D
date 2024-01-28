﻿# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("小空",color="#fbffc8",font="gongfan.ttf")
define d = Character("小龙",color="#c8ffc8",font="gongfan.ttf")

#声明此游戏使用的音乐
define audio.fly = "audio/music/InventingFlight.mp3"
define audio.drop = "audio/music/A Very Brady Special.mp3"

# 声明此游戏使用的音效
define audio.birdChirp = "audio/sound/env_chun.mp3"
define audio.cricketCall = "audio/sound/env_mushi.mp3"

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添""加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    play music fly
    scene sunny sky
    with fade
    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。


    # 此处显示各行对话。
    "龙年初始，狐耳族女孩小空迎来了一个特别的日子。"
    # 播放台词语音
    play audio goodmorning
    play sound birdChirp
    e "噢！早上好！今天也是个不错的早晨呢！"
    "天空晴朗明媚，小空满怀期待地请求小龙带她一起翱翔于苍穹之上。"
    "小龙欣然答应了她的请求，两人简单收拾行李后便踏上了旅程。"
    
    show riding happy
    with dissolve
    e "小龙，我们出发吧！"
    "他们来到了一片宽广的草原，那里的风吹拂着小空的长发，阳光温暖地洒在她们的身上。"
    "小龙展开双翼，小空轻盈地跃上他的背，仿佛融入了风中的自由。"    
    e "哇，慢一点。我可不想被摔下去！"
    stop sound
    menu:

        "随着小龙开始加速冲向高空，小空决定..."

        "抓紧缰绳(进入goodend)":
            jump goodend  # 结束游戏
        "吓得松开双手去抱小龙(进入badend)":
            jump badend  # 开始游戏

label goodend:
    play music fly if_changed
    e "谢谢你救了我！"
    "他们飞越着山脉和森林，眺望着绵延的大地和湛蓝的海洋。"
    "小空的心中充满了喜悦和兴奋，她感受到了自由的力量，仿佛能够触摸到无限的可能。"
    "小龙飞行的技巧熟练而优雅，他们在空中自在地穿梭，享受着这无与伦比的美妙时刻。"
    "小空的狐耳在风中飘动，笑容如花绽放，她感激地凝视着小龙，心中充满了对这段友情的珍视。"
    play sound birdChirp
    "他们降落在一片花海之中，绚烂的花朵散发出迷人的香气。"
    "小空跳下小龙的背，她向四周张望，发现了一朵特别美丽的花。"
    "她小心翼翼地摘下它，轻轻握在手中。"
    "小空转过身，看着小龙。"
    e "小龙，今天的飞行真是太棒了！"
    e "我感受到了自由与快乐，这是我永远难以忘怀的回忆。"
    "小龙微笑着点头，温柔地回答"
    d "小空，你是我遇到的最特别的朋友，和你一起飞翔是我最开心的时刻。我们的友谊将永远在我心中珍藏。"
    "小空抬起手中的花，轻轻递给小龙"
    e "这朵花是我为你准备的，它象征着我们纯真而美好的友情。"
    e "无论未来如何，我们都会一直支持彼此，一起面对困难，分享喜悦。"
    "小龙接过花朵，感动地看着小空"
    d "谢谢你，小空。这朵花将永远在我的心中绽放，它代表着我们的友情，无论时间如何流转，它都不会凋谢。"
    "他们相视而笑，心中充满了对未来的期许。"
    "在这个特殊的龙年开始之际，小空和小龙的友谊将继续在天空中翱翔，见证彼此成长与坚强。"
    "他们深信，无论遇到什么困难，他们都会相互扶持，一同勇往直前，创造更多美好的回忆。"
    "于是，他们继续踏上了未知的旅程，一起探索这个广阔的世界，留下属于他们友情的故事，在每个龙年的开始都继续绽放。"
    stop sound
    stop music fadeout 1.0
    "{b}Good Ending{/b}."
    jump credits

label badend:
    scene black  # 设置背景为黑色
    with fade
    hide riding happy
    play music drop fadein 1.0
    "..."
    e "我和小龙的相识的场景回现在我的眼前"
    e "这些点滴小事，都是只属于我们两个的珍贵回忆。"
    e "我曾以为这些回忆会陪伴我度过余生，但现在，我的人生即将结束了。"
    e "身体向空中坠落，眼角不断掉出后悔的形状，我感到如此无力和无奈。"
    e "我回想起我们相识的那一天，那时的我还是个年轻而热血的青年，充满着对未来的憧憬和希望。"
    e "小龙是那个时候生命中的一束光，他的微笑能照亮我内心最深处的黑暗角落。"
    e "我们一起度过了那么多美好的时光，分享着彼此的喜怒哀乐，无论是欢笑还是泪水，我们总是互相扶持着走过每一个艰难的时刻。"
    play sound cricketCall
    e "然而，命运却对我开了一个残酷的玩笑。"
    e "现在，我站在生命的尽头，回顾着那些美好的回忆，我不禁后悔起来。"
    e "后悔没有更多地珍惜每一刻，没有告诉小龙我有多么爱他，没有为我们的未来做更多的打算。"
    e "我希望能够回到过去，重新把握每一个机会，给予小龙更多的关爱和陪伴。"
    e "我知道，无论后悔与否，时间都无法倒流。"
    e "我只能接受这个事实，尽管心如刀绞，却也别无选择。"
    e "我深深地希望，在我离去之后，小龙能够坚强地面对一切，继续追寻自己的梦想。"
    e "我希望他能记住，即使我不在身边，他也永远不会孤单。"
    e "现在，我接近了生命的最后时刻，我不再留恋这个世界。"
    e "我希望能够在另一个世界与小龙再次相遇，继续我们未完成的故事。"
    "{b}Bad Ending{/b}."
    jump credits

label credits:
    hide riding happy
    stop sound
    stop music fadeout 1.0
    $ renpy.movie_cutscene("images/cutscene/CreditsMovie.webm")
    scene black
    with fade
    return
    # 此处为游戏结尾。
