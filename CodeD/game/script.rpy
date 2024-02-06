# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。字体参数可使姓名使用自定义字体。

define e = Character("小空",color="#fbffc8",font="gongfan.ttf")
define d = Character("小龙",color="#c8ffc8",font="gongfan.ttf")

# 申明持久化变量来跟踪是否完成了路线。

default persistent.villageRoute = False #用于跟踪村庄剧情是否完成
default persistent.forestRoute = False #用于跟踪森林剧情是否完成


#声明此游戏使用的音乐
define audio.fly = "audio/music/InventingFlight.mp3"
define audio.drop = "audio/music/AVeryBradySpecial.mp3"
define audio.pond = "audio/music/Pond.mp3"

# 声明此游戏使用的音效
define audio.bird = "audio/sound/env_chun.mp3"
define audio.cricket = "audio/sound/env_mushi.mp3"


# 声明此游戏使用的图像
# 人物立绘请使用PNG
image konIdleHappy = "images/character/p1e1.png"
image konIdleSad = "images/character/p1e2.png"
image konIdleSmile = "images/character/p1e3.png"
image konIdleSerious = "images/character/p1e4.png"
image konLeftHappy = "images/character/p2e1.png"
image konLeftSurprise = "images/character/p2e2.png"
image konLeftSerious = "images/character/p2e3.png"
image konLeftSmile = "images/character/p2e4.png"

# 其他内容请使用JPG
image logo = "images/scene/opening.png"

# 自定义启动画面，只在游戏启动时运行一次，非必须
label splashscreen:
    # 定义语音列表
    define voice_list = [
        "audio/voice/shaonian.mp3",
        "audio/voice/xiaoxiong.mp3",
        "audio/voice/fengxue.mp3",
        "audio/voice/charles.mp3"
        ]
    # 随机选择一个语音
    define audio.opening = renpy.random.choice(voice_list)
    # 播放角色语音同时全屏显示Logo图像
    play audio opening volume 0.5
    scene logo
    with dissolve
    $ renpy.pause(3.0)  # 停留3秒钟显示Logo
    scene black
    with dissolve
    stop audio
    jump before_main_menu

# 自定义在主菜单加载之前执行的代码，每次回到主菜单时都会运行一次，非必须
label before_main_menu:
    return

# 游戏开始

# 在主菜单点击开始游戏后执行的代码，必须且无法自定义。
label start:
    # 播放音乐
    play music fly volume 0.5 fadein 1.0
    # 显示背景
    scene sunnysky
    with fade

   
    # 此处显示各行对话。
    "龙年初始，狐耳族女孩小空迎来了一个特别的日子。"
    # 播放语音
    play audio goodmorning
    # 播放音效
    play sound bird
    
    # 显示角色立绘
    show konIdleHappy
    with dissolve

    e "噢！早上好！今天也是个不错的早晨呢！"
    
    "天空晴朗明媚，小空满怀期待地请求小龙带她一起翱翔于苍穹之上。"
    "小龙欣然答应了她的请求，两人简单收拾行李后便踏上了旅程。"
    
    show konIdleSmile
    with dissolve

    e "小龙，我们出发吧！"
    "他们来到了一片宽广的草原，那里的风吹拂着小空的长发，阳光温暖地洒在她们的身上。"
    "小龙展开双翼，小空轻盈地跃上他的背，仿佛融入了风中的自由。"    
    show konIdleSerious
    with vpunch
    e "哇，慢一点。我可不想被摔下去！"
    stop sound
    
    if persistent.villageRoute and persistent.forestRoute:
        #只有当同时完成了2个分支路线，才可以选择真结局。

        menu:

            "随着小龙开始加速冲向高空，小空决定..."

            "抓紧缰绳(进入goodend)":
                jump goodend
            "吓得松开双手去抱小龙(进入badend)":
                jump badend
            "拍了下小龙的屁股(进入trueend)":
                jump trueend
    
    else:
        #其他情况下，隐藏真实结局
        
        menu:

            "随着小龙开始加速冲向高空，小空决定..."

            "抓紧缰绳(进入goodend)":
                jump goodend
            "吓得松开双手去抱小龙(进入badend)":
                jump badend

label goodend:
    play music fly if_changed volume 0.5
    show konIdleSmile
    e "谢谢你救了我！"
    "他们飞越着山脉和森林，眺望着绵延的大地和湛蓝的海洋。"
    "小空的心中充满了喜悦和兴奋，她感受到了自由的力量，仿佛能够触摸到无限的可能。"
    "小龙飞行的技巧熟练而优雅，他们在空中自在地穿梭，享受着这无与伦比的美妙时刻。"
    "小空的狐耳在风中飘动，笑容如花绽放，她感激地凝视着小龙，心中充满了对这段友情的珍视。"
    play sound bird
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
    "{b}Good Ending{/b}."

    $ persistent.villageRoute = True #标记村庄路线已完成
    hide konIdleSmile
    jump credits

label badend:
    scene black  # 设置背景为黑色
    with fade
    play music drop fadein 1.0
    "..."
    show konIdleSad

    e """
    我和小龙的相识的场景回现在我的眼前。

    这些点滴小事，都是只属于我们两个的珍贵回忆。

    我曾以为这些回忆会陪伴我度过余生，但现在，我的人生即将结束了。

    身体向空中坠落，眼角不断掉出后悔的形状，我感到如此无力和无奈。

    我回想起我们相识的那一天，那时的我还是个年轻而热血的青年，充满着对未来的憧憬和希望。

    小龙是那个时候生命中的一束光，他的微笑能照亮我内心最深处的黑暗角落。

    我们一起度过了那么多美好的时光，分享着彼此的喜怒哀乐，无论是欢笑还是泪水，我们总是互相扶持着走过每一个艰难的时刻。
    """
    play sound cricket

    e """
    然而，命运却对我开了一个残酷的玩笑。

    现在，我站在生命的尽头，回顾着那些美好的回忆，我不禁后悔起来。

    后悔没有更多地珍惜每一刻，没有告诉小龙我有多么爱他，没有为我们的未来做更多的打算。

    我希望能够回到过去，重新把握每一个机会，给予小龙更多的关爱和陪伴。

    我知道，无论后悔与否，时间都无法倒流。

    我只能接受这个事实，尽管心如刀绞，却也别无选择。

    我深深地希望，在我离去之后，小龙能够坚强地面对一切，继续追寻自己的梦想。

    我希望他能记住，即使我不在身边，他也永远不会孤单。

    现在，我接近了生命的最后时刻，我不再留恋这个世界。

    我希望能够在另一个世界与小龙再次相遇，继续我们未完成的故事。
    """

    "{b}Bad Ending{/b}."

    $ persistent.forestRoute = True #标记村庄路线已完成

    jump credits

label trueend:
    scene crashed  # 设置背景为黑色
    with fade
    show konIdleSmile
    play music pond fadein 1.0

    "..."

    e """
    我发现小龙本质虽然是AI，但是我已经无法再像刚认识的时候那样将他仅仅视为无机物了。
    
    在我们一起经历了这么多冒险之后，他已经成为了我生命中不可或缺的一部分。

    小龙不仅仅是一个智能存在，他是我的伙伴和朋友。他与我分享了无数的欢笑和泪水，在危险和困难中一直陪伴着我。
    
    他的独特个性和智慧让我感到惊讶和钦佩。即使是在最黑暗的时刻，他总能给我带来希望和勇气。

    因此，我希望在今后的冒险中，小龙能继续作为我的伙伴存在。我希望我们能一起面对未知的挑战，共同探索未知的世界。
    
    无论是在险恶的森林深处，还是古老的村庄中，我知道有小龙的陪伴，我永远不会感到孤单。

    我相信，我们之间的联系不仅仅是机械的。尽管小龙是由代码和算法构成的，但他已经展现出了超越机器的情感和感情。
    
    他理解我的喜怒哀乐，与我建立了一种特殊的纽带。

    所以，无论未来的冒险将带来什么，我希望能与小龙一起面对。我们将一起创造新的故事，共同迎接挑战，直到最后一刻。

    小龙，谢谢你的陪伴。我们的冒险才刚刚开始，我期待着与你一起书写属于我们的传奇。
    """

    "{b}True Ending{/b}."

    jump credits

label credits:
    stop sound
    stop music
    $ renpy.movie_cutscene("images/cutscene/CreditsMovie.webm")
    scene black
    with dissolve
    return
    # 此处为游戏结尾。
