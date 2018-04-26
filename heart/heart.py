#-*-coding:utf-8-*-
'''
这个程序的作用是画两颗小心心；
并且作者信息和赠送的人可以自定义；
时间可以自动获取系统时间；
'''
import turtle
import time
def add():
  
    fromname =input("请输入你喜欢的人名字:\n")
    toname = input("请输入你的人名字:\n")
    return fromname,toname
def cir():
    for i in range (200):
        turtle.right(1)
        turtle.forward(1)
def love():
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(112)
    cir()
    turtle.left(120)
    cir()
    turtle.forward(112)
    turtle.end_fill()
def pic(fromname,toname):
    turtle.setup(1000,400,150,150)
    turtle.color('red','pink')
    turtle.pensize(2)
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-350,-100)
    turtle.pendown()

    love()
    turtle.penup()
    turtle.left(140)
    turtle.fd(180)
    turtle.pendown()
    love()

    for i in range (20):
        turtle.right(7.8)
        turtle.forward(0.3)
    turtle.forward(8)
    turtle.up()
    turtle.goto(20,-30)
    turtle.write("To :{}\nFrom :{}\n{}\n关注微信号：城市共享，定制更多小程序！\n".format
    (fromname,toname,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())),font=('楷体',18,'normal'))
    turtle.hideturtle()
    turtle.done()
def numtime():
    for i in range(100):
        print("{}\r".format(i*'>'),end="")
        time.sleep(0.01)
    print("\n\n加载完成！请稍等...\n关注微信号：城市共享，定制更多小程序！\n")
    for i in range(100):
        print("{}\r".format(i*'>'),end="")
        time.sleep(0.01)
    time.sleep(3)
def main():
    athour = list(add())
    print("{:^}\n".format(100*"*"))
    print("{:^90}".format('作者：'+athour[1]))
    print("\n{:^}\n".format(100*"*"))
    numtime()
    pic(athour[0],athour[1])
main()
