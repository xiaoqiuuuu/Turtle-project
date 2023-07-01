# 中华人民共和国国旗是五星红旗，中华人民共和国的象征和标志。中华人民共和国国旗的设计者是曾联松，
# 旗面为红色，长方形，其长与高为三与二之比，旗面左上方缀黄色五角星五颗。
# 一星较大，其外接圆直径为旗高十分之三，居左；四星较小，其外接圆直径为旗高十分之一，环拱于大星之右。
# 中华人民共和国国旗于1949年7月14日至8月15日开始征求国旗图案。
# 1949年8月20日，国旗国徽评选委员会共收到了2992幅（一说为3012幅）国旗图案。
# 1949年9月27日，全国政协第一届全体会议代表通过了以五星红旗为国旗的议案。
# 1949年10月1日，第一面中华人民共和国国旗由毛泽东在天安门广场首次升起。
# 中华人民共和国国旗的红色象征革命。旗上的五颗五角星及其相互关系象征共产党领导下的革命人民大团结。
# 五角星用黄色是为了在红地上显出光明，四颗小五角星各有一尖正对着大星的中心点，表示围绕着一个中心而团结
import turtle
import time

turtle.speed(10)
turtle.screensize(canvheight=200,canvwidth=200,bg="cyan")
# width 与 height 为小数时表示占据屏幕的比例
# turtle.setup(width=0.5,height=0.5)

turtle.up()
turtle.goto(-200,200)
turtle.down()
turtle.fillcolor("red")
turtle.color("red")

turtle.begin_fill()
turtle.forward(480)
turtle.right(90)
turtle.forward(320)
turtle.left(90)
turtle.backward(480)
turtle.right(90)
turtle.backward(320)
turtle.end_fill()

turtle.up()
turtle.forward(64)
turtle.left(90)
turtle.forward(32)
turtle.down()

# 大五角星
a=96
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(2)
turtle.end_fill()

#无需使用移动指针 直接使用goto更方便
turtle.up()
# 移动到五角星右顶点
turtle.forward(96)
# 向左边转动°(度数)
turtle.left(53)
turtle.forward(36)
turtle.down()

# 第一个小五角星
a=32
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(5)
turtle.end_fill()

turtle.up()
turtle.right(80)
turtle.forward(42)
turtle.left(55)

# 第二个小五角星
a=32
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(5)
turtle.end_fill()

turtle.up()
turtle.right(96)
turtle.forward(32)

# 第三个小五角星
a=32
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(5)
turtle.end_fill()

turtle.up()
turtle.right(54)
turtle.forward(45)
turtle.right(30)

# 最后一个小五角星
a=32
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(2)
turtle.end_fill()
turtle.ht()

turtle.done()
