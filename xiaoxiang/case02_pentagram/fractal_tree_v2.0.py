"""
    作者：praise
    功能：利用递归绘制分形树
    版本：2.0
    日期：04/03/2019
    新增功能：   给树枝末端绘上绿色，作为叶子
                 2.0 给分形树添上树根
"""
import turtle


def draw_branch(length, angle, delta, end):
    """

    画分形树的分支
    """
    if length > end:
        # 左分支
        if (length >= end) and (length <= end+delta):
            turtle.color('green')
            print('画笔颜色变为绿色')
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
        if length > end+delta:
            turtle.color('brown')
            print('画笔颜色变为棕色')
        turtle.back(length)
        print('后退   ', length)


def draw_root(r_length, r_angle, r_delta, r_end):
    """
    画树根
    """
    if r_length < r_end:
        # 右树根
        turtle.fd(r_length)
        print('前进', r_length)
        turtle.right(r_angle)
        draw_root(r_length+r_delta, r_angle, r_delta, r_end)
        # 左树根
        turtle.left(r_angle*2)
        draw_root(r_length+r_delta, r_angle, r_delta, r_end)
        # 后退
        turtle.right(r_angle)
        turtle.back(r_length)
        print('后退', r_length)


def main():
    """

    主函数
    """
    # 设置画笔初始值
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.pensize(20)                 # 画笔粗度
    turtle.color('brown')              # 画笔颜色
    turtle.left(180)
    turtle.bgpic('turtle_bg.gif')      # 背景图片(只能为.gif)
    draw_branch(150, 40, 20, 0)
    turtle.right(180)
    draw_root(10, 30, 20, 100)
    turtle.left(180)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
