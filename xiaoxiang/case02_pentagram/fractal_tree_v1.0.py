"""
    作者：praise
    功能：利用递归绘制分形树
    版本：1.0
    日期：01/03/2019
"""
import turtle


def draw_branch(length, angle, delta, end):
    """

    画分形树的分支
    """
    if length > end:
        # 左分支
        turtle.fd(length)
        print('前进   ', length)
        turtle.left(angle)
        print('左转', angle)
        draw_branch(length-delta, angle, delta, end)
        # 右分支
        turtle.right(angle*2)
        print('右转', angle*2)
        draw_branch(length-delta, angle, delta, end)
        # 回到上一个分叉点
        turtle.left(angle)
        print('左转', angle)
        turtle.back(length)
        print('后退   ', length)


def main():
    """

    主函数
    """
    # 设置画笔初始值
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.color('brown')
    draw_branch(100, 40, 20, 0)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
