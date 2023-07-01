# 绘制党旗，党旗尺寸为120cmx80cm，此处等比例放大5倍
# 导入第三方库
import turtle as t

t.screensize(10 , 20)

# 绘制党旗红色背景
# 设置画笔颜色为红色，后期填充也是红色
t.color("red")
# 抬起画笔
t.penup()
# 选择起始点
t.goto(-300, 200)
# 放下画笔用于绘图
t.pendown()
# 开始绘画填充
t.begin_fill()
t.forward(600)
t.right(90)
t.forward(400)
t.right(90)
t.forward(600)
t.right(90)
t.forward(400)
t.end_fill()

# 绘制镰刀和斧头
# 设置画笔颜色为黄色
# 绘制斧头
t.color("yellow")
t.penup()
t.goto(-220, 100)
t.pendown()
# 开始填充
t.begin_fill()
t.right(45)
t.forward(50)
t.right(60)
t.circle(50, 15)
t.right(45)
t.forward(13)
t.right(90)
t.forward(18)
t.left(90)
t.forward(100)
t.right(90)
t.forward(22)
t.right(90)
t.forward(100)
t.left(90)
t.forward(18)
t.right(90)
t.forward(22)
# 完成填充
t.end_fill()

# 开始绘制镰刀
t.penup()
# 确定镰刀绘制开始点
t.goto(-148, 156)
t.right(180)
t.pendown()
# 开始绘制镰刀并填充
t.begin_fill()
t.circle(-85, 35)
t.circle(-60, 150)
t.left(90)
t.forward(22)
t.left(90)
t.circle(83, 86)
t.circle(71, 121)
t.penup()
t.end_fill()

# 完善镰刀细节
t.goto(-216, 28)
t.right(15)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# 防止最后绘图窗口一闪而过
t.done()

