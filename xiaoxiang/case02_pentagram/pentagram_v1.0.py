"""
    作者：praise
    功能：五角星的绘制
    版本：1.0
    日期：26/02/2019
"""
import turtle
# 画笔属性配置
turtle.pencolor('green')


def main():
    """
    主函数
    """
    # 计数器
    timer = 0
    while timer < 5:
        timer += 1
        single_side(100, 144)
        # # 第二条边
        # turtle.forward(50)
        # turtle.right(144)
        # # 第三条边
        # turtle.forward(50)
        # turtle.right(144)
        # # 第四条边
        # turtle.forward(50)
        # turtle.right(144)
        # # 第五条边
        # turtle.forward(50)
        # turtle.right(144)

    # 关闭窗口
    turtle.exitonclick()


def single_side(distance, angle):
    # 第一条边
    turtle.forward(distance)
    turtle.right(angle)


if __name__ == '__main__':
    main()
