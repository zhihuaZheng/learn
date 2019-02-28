"""
    作者：郑致华
    功能：绘制五角星
    版本：2.0
    日期：27/02/2019
    新增功能：加入循环操作绘制重复不同大小的图形
"""
import turtle


def single_side(distance, angle, increment):
    """

    单条边绘制
    """
    turtle.forward(distance + increment)
    turtle.right(angle)


def main(num):
    timer0 = 0      # 绘制五角星边数计数器
    timer1 = 0      # 绘制五角星个数计数器
    while timer1 < num:
        timer1 += 1
        while timer0 < 5:
            timer0 += 1
            single_side(50, 144, (timer1-1) * 20)
        timer0 = 0
    turtle.exitonclick()


num_str = input('你想画几个五角星：')
if __name__ == '__main__':
    main(eval(num_str))
