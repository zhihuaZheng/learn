"""
    作者：praise
    功能：绘制五角星
    版本：2.0
    日期：27/02/2019
    新增功能：2.0 加入循环操作绘制重复不同大小的图形
              3.0 使用递归函数绘制重复不同大小的图形
"""
import turtle


def draw_recursive_pentagram(size):
    """

    递归绘制五角星
    """
    count = 1       # 计数器
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    size += 20
    if size <= 130:
        draw_recursive_pentagram(size)


def main():
    # 画笔属性设置
    turtle.pencolor('red')
    turtle.pensize(3)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    draw_recursive_pentagram(50)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
