import turtle
import time

print("----Turtle Kütüphanesi----")
ok = turtle.Turtle()
ok.forward(100)
ok.right(90)
time.sleep(1)
ok.forward(100)
ok.right(90)
time.sleep(1)
ok.forward(100)
ok.right(90)
time.sleep(1)
ok.forward(100)
ok.right(90)
time.sleep(1)
ok.penup()
ok.forward(110)
ok.pendown()

for _ in range(3):
    ok.forward(150)
    ok.right(120)
    time.sleep(1)

ekran = turtle.Screen()
ekran.bgcolor("blue")
ekran.exitonclick()