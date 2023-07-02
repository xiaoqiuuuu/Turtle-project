from turtle import RawTurtle

class Myturtle(RawTurtle):
    _flag = False
    def __init__(self, screen):
        if not Myturtle._flag:
            super().__init__(screen)
            red = 69
            green = 149
            blue = 199
            self.shape("turtle")
            self.color(f"#{red:02x}{green:02x}{blue:02x}")
            Myturtle._flag = True

    def __del__(self):
        Myturtle._flag = False
        # self.screen.resetscreen()
        self.screen.tracer(20) # 关闭画布的刷新
        self.screen.clearscreen()
        self.screen.bgcolor(f"#{138:02x}{189:02x}{221:02x}")
        self.screen.update() # 打开画布刷新 ，让关闭动画更加流畅
        pass




