# 画奥运五环标志（标准颜色+五环套接）

import turtle

turtle.speed(3)
### 设置半径与画笔粗细
# r=float(input("请输入五环的半径："))   # input()函数接收到的是字符串，float()可以将其转换为浮点型数字
r = 80  # 暂时设置一个固定值，方便调试程序
pensize = r / 6  # 改动半径，环的粗细以及环与环的间距会等比例缩放
turtle.pensize(pensize)  # 设置画笔的粗细为pensize

### 【1】画五个环
s1 = 2 * r + 2 * pensize  # 左右两环的圆心到中间环圆心的距离是s
s2 = r + pensize  # 左右两环的圆心到y轴的距离是s

# ① 画中间的黑环，起点坐标为(0，0)，即海龟的默认坐标
turtle.pencolor("#000000")  # #000000是黑色，也就是blake
turtle.circle(r)  # 海龟画半径为r的圆

# ② 画左上的蓝环，起点坐标为(-s1,0)
turtle.pencolor("#0081C8")  # #0081C8是一种蓝色，切记不是blue
turtle.penup()  # 海龟抬笔，没有移动（绘画）痕迹
turtle.goto(-s1, 0)  # 让海龟移至坐标(-s1,0)
turtle.pendown()  # 海龟落笔，移动（绘画）有痕迹
turtle.circle(r)

# ③ 画右上的红环，起点坐标为(s1,0)
turtle.pencolor("#EE334E")  # #EE334E是一种红色，切记不是red
turtle.penup()
turtle.goto(s1, 0)  # 让海龟移至坐标(s1,0)
turtle.pendown()
turtle.circle(r)

# ④ 画左下的黄环，起点坐标为(-s2,-r)
turtle.pencolor("#FCB131")  # #FCB131是一种黄色，切记不是yellow
turtle.penup()
turtle.goto(-s2, -r)  # 让海龟移至坐标(-s2,-r)
turtle.pendown()
turtle.circle(r)

# ⑤ 画右下的绿环，起点坐标为(s2,-r)
turtle.pencolor("#00A651")  # #00A651是一种绿色，切记不是green
turtle.penup()
turtle.goto(s2, -r)  # 让海龟移至坐标(s2,-r)
turtle.pendown()
turtle.circle(r)

### 【2】 实现五环套连

# ① 黑环压黄环，移至黑环起点坐标(0,0)
turtle.pencolor("#000000")  # #000000是黑色
turtle.penup()
turtle.goto(0, 0)  # 海龟移至黑环起点坐标(0,0)
turtle.pendown()
turtle.circle(r, -20)  # 海龟画半径为r，度数为-20的圆弧

# ② 红环压绿环，移至红环起点坐标(s1,0)
turtle.pencolor("#EE334E")  # #EE334E是一种红色
turtle.penup()
turtle.goto(s1, 0)  # 海龟移至红环起点坐标(s1,0)
turtle.setheading(0)  # 因为海龟刚刚画过圆弧，方向发生了改变，所以要重新设置方向
turtle.pendown()
turtle.circle(r, -20)  # 海龟画半径为r，度数为-20的圆弧

# ③ 黑环压绿环，移至黑环的上端坐标(0,2*r)
turtle.pencolor("#000000")  # #000000是黑色
turtle.penup()
turtle.goto(0, 2 * r)  # 海龟移至黑环上端坐标(0,2*r)
turtle.setheading(0)  # 因为海龟刚刚画过圆弧，方向发生了改变，所以要重新设置方向
turtle.pendown()
turtle.circle(-r, 100)  # 海龟画半径为-r，度数为100的圆弧

# ④ 蓝环压黄环，移到蓝环的上端坐标(-s1,2*r)
turtle.pencolor("#0081C8")  # #0081C8是一种蓝色
turtle.penup()
turtle.goto(-s1, 2 * r)  # 海龟移至蓝环上端坐标(-s1,2*r)
turtle.setheading(0)  # 因为海龟刚刚画过圆弧，方向发生了改变，所以要重新设置方向
turtle.pendown()
turtle.circle(-r, 100)  # 海龟画半径为-r，度数为100的圆弧

### 绘图结束，隐藏海龟
turtle.hideturtle()

turtle.done()