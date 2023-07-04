# 案例1：中国结雪花（固定位置）
# 程序初始化设置
import turtle  # 导入turtle库（模块）
import random  # 导入random随机库（模块）

turtle.speed(3)  # 设置海龟的绘图速度，参数为0时最快
turtle.delay(1)  # 设置海龟绘图的延迟时间，参数为0时表示延迟时间为0
turtle.bgcolor("#000000")  # 设置背景颜色为#0d93b8，一种蓝色
turtle.pencolor("#ffffff")  # 设置画笔颜色为#ffffff，纯白色，也就是white
turtle.pensize(3)  # 设置画笔的粗细为3


# 自定义函数draw(times)
def draw(times):
    turtle.penup()
    turtle.goto(20 * times, 20 * times)
    turtle.pendown()

    for i in range(6):
        turtle.forward(10 * times)
        turtle.circle(2 * times, 180)

        turtle.forward(14 * times)
        turtle.circle(-4 * times, 60)
        turtle.forward(4 * times)
        turtle.circle(2 * times, 180)
        turtle.forward(4 * times)
        turtle.circle(8 * times, 60)

        turtle.forward(14 * times)
        turtle.circle(2 * times, 180)
        turtle.forward(12 * times)
        turtle.circle(-2 * times, 180)
        turtle.forward(12 * times)
        turtle.circle(2 * times, 270)
        turtle.forward(12 * times)
        turtle.circle(-2 * times, 180)
        turtle.forward(12 * times)
        turtle.circle(2 * times, 180)

        turtle.forward(14 * times)
        turtle.circle(8 * times, 60)
        turtle.forward(4 * times)
        turtle.circle(2 * times, 180)
        turtle.forward(4 * times)
        turtle.circle(-4 * times, 60)
        turtle.forward(4 * times)
        turtle.left(180)
        turtle.forward(4 * times)
        turtle.circle(4 * times, 60)
        turtle.forward(4 * times)
        turtle.circle(-2 * times, 180)
        turtle.left(180)
        turtle.circle(2 * times, 270)
        turtle.forward(4 * times)
        turtle.circle(8 * times, 60)
        turtle.forward(4 * times)


# 调用自定义函数draw(times)
draw(4)  # 参数4可以控制雪花的大小，数字越大，绘制出的雪花越大

# 海龟绘图结束，隐藏海龟
turtle.hideturtle()
turtle.done()