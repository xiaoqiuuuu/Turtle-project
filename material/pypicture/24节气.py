# 案例5：24节气倒计时（代码参考1）

### ① 程序初始化设置
import turtle  # 导入turtle库（模块）

turtle.bgcolor("#ffff55")  # 设置背景颜色为#ffff55，一种浅黄色
turtle.speed(5)  # 设置海龟的绘图速度，参数为0时最快
turtle.delay(0)  # 设置海龟绘图的延迟时间，参数为0时，表示绘图没有延迟

### ② 变量初始化设置
# 创建列表name，存放24节气中文名称
name = ["雨水", "惊蛰", "春风",
        "清明", "谷雨", "立夏",
        "小满", "芒种", "夏至",
        "小暑", "大暑", "立秋",
        "处暑", "白露", "秋风",
        "寒露", "霜降", "立冬",
        "小雪", "大雪", "冬至",
        "小寒", "大寒", "立春"]

# 创建列表en_name，存放24节气英文名称
en_name = ["Rain Water", "Awakening of Insects", "Spring Equinox",
           "Pure Brightness", "Grain Rain", "Beginning of Summer",
           "Grain Buds", "Grain in Ear", "Summer Solstice",
           "Minor Heat", "Major Heat", "Beginning of Autumn",
           "End of Heat", "White Dew", "Autumn Equinox",
           "Cold Dew", "Frost's Descent", "Beginning of Winter",
           "Minor Snow", "Major Snow", "Winter Solstice",
           "Minor Cold", "Major Cold", "Beginning of Spring"]

# 创建列表poem，存放诗词
# 没有对应的诗词，就定义为空字符串。如果不定义，调用时会报错
poem = ["随风潜入夜 润物细无声", "春雷响 万物长", "春风如贵客 一到便繁华",
        "清明时节雨纷纷", "风吹雨洗一城花", "天地始交 万物并秀",
        "物至于此 小得盈满", "家家麦饭美 处处菱歌长", "绿筠尚含粉 圆荷始散芳",
        "荷风送香气 竹露滴清响", "桂轮开子夜 萤火照空时", "天阶夜色凉如水 坐看牵牛织女星",
        "春种一粒粟 秋收万颗子", "露从今夜白 月是故乡明", "",
        "", "", "",
        "", "", "",
        "", "", ""]

# 定义变量n，作为累加器
n = 0


### ③ 自定义函数fun()
# fun()的功能是，写一个倒计时数字，以及一个节气的名称、英文名称和对应的诗词
def fun():
    global n  # 强制n是全局变量的n(即声明本函数体内的变量n为主函数中的那个全局变量n)
    turtle.clear()  # 清除屏幕中的已有绘图。（如果不用clear()，5个数字会重叠在一起）
    turtle.dot(500, "#b1352b")  # 画一个直径为500，颜色为#b1352b（一种红色）的圆点，作为背景装饰
    turtle.penup()  # 海龟抬脚，移动时不会留下痕迹，但是仍然可以写字，所以后面无需再写pendown()
    turtle.setheading(-90)  # 让海龟头部向下

    turtle.backward(10)  # 海龟向上移动10像素，准备写字.（如果不向上移动10像素，海龟写出的几行字会偏下）
    turtle.write(24 - n, align="center", font=("黑体", 120))  # 写倒计时数字（第1行）
    turtle.forward(50)  # 海龟向下移动50像素，准备写字
    turtle.write(name[n], align="center", font=("黑体", 30))  # 写节气中文名称（第2行）
    turtle.forward(50)  # 海龟再向下移动50像素，准备写字
    turtle.write(en_name[n], align="center", font=("Arial", 25))  # 写节气英文名称（第3行）
    turtle.forward(50)  # 海龟再向下移动50像素，准备写字
    turtle.write(poem[n], align="center", font=("隶书", 20))  # 写节气对于诗词（第4行）

    turtle.home()  # 海龟返回原点，回到初始位置
    n = n + 1  # 累加器n加1


### ④ 主程序
# 显示两行引导文字
turtle.pencolor("black")  # 设置画笔颜色为黑色black
turtle.penup()  # 海龟抬脚，移动时不会留下痕迹，但是仍然可以写字，所以后面无需再写pendown()
turtle.setheading(-90)  # 让海龟头部向下
turtle.backward(30)  # 海龟向上移动30像素（步），准备写字.（如果不向上移动30像素，海龟写出的两行字会偏下）
turtle.write("让我们一起倒计时，迎接春的到来", align="center", font=("黑体", 20))  # 写中文引导语
turtle.forward(60)  # 海龟再向下移动60像素（步），准备写字
turtle.write("Let's greet the arrival of spring with a countdown", align="center", font=("Arial", 20))  # 写英文引导语
turtle.home()  # 海龟返回原点，回到初始位置

# 24秒倒计时开始
turtle.pencolor("white")  # 设置画笔颜色为白色white
for i in range(24):  # 每次调用fun()写4行文字，要循环24次
    # 调用自定义函数fun()
    turtle.ontimer(fun, t=1000 * (i + 1))  # 安装一个计时器，t毫秒后调用fun()函数

### ⑤ 海龟绘图结束，隐藏海龟
turtle.hideturtle()
turtle.done()