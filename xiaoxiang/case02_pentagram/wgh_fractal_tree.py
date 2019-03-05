"""
    作者：wgh
    功能：利用递归绘制分形树
    版本：1.0
    日期：03/03/2019
"""
import turtle
# import time


def draw_branch(length, delt, angle, end):
    """

    画分形树的分支
    """
    if length > end:
        turtle.forward(length)
        print('前进', length)
        turtle.right(angle)
        print('右转', angle)
        draw_branch(length - delt, delt, angle, end)
        if length-delt <= end:
            turtle.forward(length-delt)
            print('前进', length-delt)
            turtle.backward(length-delt)
            print('后退', length-delt)
        # time.sleep(1)       # 停止目前线程调用1秒，用于调试
        turtle.left(2*angle)
        print('左转', 2*angle)
        turtle.forward(length-delt)
        print('前进', length-delt)
        turtle.backward(length-delt)
        print('后退', length-delt)
        draw_branch(length - delt, delt, angle, end)
        turtle.right(angle)
        print('右转', angle)
        turtle.backward(length)
        print('后退', length)


def main():
    """

    主函数
    """
    # 设置画笔初始值
    turtle.penup()
    turtle.left(90)
    turtle.back(300)
    turtle.pendown()
    turtle.delay(120)       # 延迟turtle爬行速度，用于调试
    turtle.color('brown')
    draw_branch(50, 20, 30, 10)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
