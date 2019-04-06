import threading
import time
import turtle

def draw_image(t,x,y):
    t.speed(5)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

if __name__ == "__main__":
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    # 画布
    screen = turtle.Screen()



    #创建新的线程画布
    t11 = threading.Thread(target=draw_image,args=(t1,-200,0))
    t12 = threading.Thread(target=draw_image, args=(t2, -0, 0))
    t13 = threading.Thread(target=draw_image, args=(t3, 200, 0))

    t11.start()
    t12.start()
    t13.start()

    # 事件循环
    screen.mainloop()


