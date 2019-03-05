"""
    作者：praise
    功能：绘制五角星
    版本：2.0
    日期：27/02/2019
    新增功能：2.0 加入循环操作绘制重复不同大小的图形
"""
import turtle


def draw_pentagram(size):
    """

    绘制五角星
    """
    count = 1       # 计数器
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main(num):
    """

    主函数
    """
    # 设置画笔属性
    turtle.penup()
    turtle.backward(100)
    turtle.pensize(5)
    turtle.pencolor('red')
    turtle.pendown()

    init_size = 50       # 开始五角星的大小
    size = init_size + (num-1) * 20     # 最后五角星的大小
    # 通过改变五角星大小,绘制多个五角星
    while init_size <= size:
        draw_pentagram(init_size)
        init_size += 20
    turtle.done()


num_str = input('你想要画几个五角星：')
if __name__ == '__main__':
    main(eval(num_str))

