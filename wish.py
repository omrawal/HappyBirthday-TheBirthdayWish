import turtle
import random

bobo = turtle.Turtle()

bobo.width(8)
bobo.color('#d700d7')
new = turtle.getscreen()
new.bgcolor("lightblue")
color_lst = ['yellow', 'red', 'brown', 'blue', 'orange', 'cyan', 'green']
back_lst = ['#daf9d7', '#9fd7e7', '#c5d107', '#9cd4d2', '#e8e4c6']

# go to start of page 
def goto_start():  
    bobo.penup()
    bobo.left(90)
    bobo.forward(300)
    bobo.left(90)
    bobo.forward(330)
    bobo.left(90)

# give a space
def space():
    bobo.right(90)
    bobo.forward(30)
    bobo.left(90)

# got to next line just below
def nextline():
    bobo.right(180)
    bobo.forward(60)
    bobo.left(180)

# select a new line point to left 
def new_line(n=0):
    bobo.setpos(0, 0)
    bobo.forward(100)
    bobo.left(90)
    bobo.forward(300)
    bobo.left(90)
    bobo.forward(n)
    bobo.right(90)
    bobo.right(90)

# my initials
def by_omrawal():
    bobo.color('red')
    bobo.width(6)
    bobo.setpos(0, 0)
    bobo.left(180)
    bobo.forward(250)
    bobo.right(90)
    bobo.forward(250)
    bobo.right(90)

    bobo.forward(5)
    bobo.right(90)
    bobo.pendown()
    bobo.forward(10)
    bobo.penup()
    bobo.right(90)
    bobo.forward(10)
    bobo.left(90)
    bobo.forward(10)
    bobo.left(90)

    bobo.penup()
    bobo.right(90)
    bobo.forward(40)
    bobo.pendown()
    bobo.circle(17)
    bobo.penup()
    # bobo.right(180)
    bobo.forward(34)
    bobo.left(90)

    bobo.pendown()
    bobo.forward(34)
    bobo.right(150)
    bobo.forward(17)
    bobo.left(120)
    bobo.forward(17)
    bobo.right(150)
    bobo.forward(34)
    bobo.penup()
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)


# start writing happy
def h1():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(180)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(15)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(180)
    bobo.forward(40)
    bobo.penup()
    bobo.right(180)
    bobo.forward(40)
    bobo.right(270)
    bobo.forward(20)
    bobo.right(270)

# a
def a():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(15)
    bobo.right(180)
    bobo.forward(15)
    bobo.right(90)
    bobo.forward(20)
    bobo.penup()
    bobo.right(270)
    bobo.forward(20)
    bobo.right(270)

# b
def b():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.left(180)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.penup()
    bobo.right(180)
    bobo.forward(40)
    bobo.left(90)

# c
def c():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(180)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.penup()
    bobo.forward(20)
    bobo.left(90)

# d
def d():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(15)
    bobo.right(30)
    bobo.forward(10)
    bobo.right(60)
    bobo.forward(25)
    bobo.right(30)
    bobo.forward(10)
    bobo.right(60)
    bobo.forward(15)
    bobo.penup()
    bobo.right(180)
    bobo.forward(35)
    bobo.left(90)

# e
def e():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.setheading(180)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(15)
    bobo.setheading(180)
    bobo.forward(15)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(20)
    bobo.penup()
    bobo.forward(20)
    bobo.left(90)

# f
def f():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.penup()
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.pendown()
    bobo.forward(20)
    bobo.left(180)
    bobo.penup()
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(180)
    bobo.forward(40)
    bobo.left(90)

# g
def g():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(180)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(18)
    bobo.left(90)
    bobo.forward(8)
    bobo.penup()
    bobo.right(180)
    bobo.forward(8)
    bobo.right(90)
    bobo.forward(18)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)


# h
def h():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(180)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(15)
    bobo.left(90)
    bobo.forward(20)
    bobo.right(180)
    bobo.forward(40)
    bobo.penup()
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# i
def i():
    bobo.right(90)
    bobo.pendown()
    bobo.forward(20)
    bobo.left(180)
    bobo.forward(10)
    bobo.right(90)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(10)
    bobo.left(180)
    bobo.forward(20)
    bobo.penup()
    bobo.left(180)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(30)
    bobo.forward(10)
    bobo.left(90)

# j
def j():
    bobo.right(90)
    bobo.pendown()
    bobo.forward(10)
    bobo.left(90)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(10)
    bobo.right(180)
    bobo.forward(20)
    bobo.penup()
    bobo.left(180)
    bobo.forward(10)
    bobo.left(90)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# k
def k():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(180)
    bobo.forward(20)
    bobo.left(90)
    bobo.left(30)
    bobo.forward(30)
    bobo.right(180)
    bobo.forward(30)
    bobo.left(110)
    bobo.forward(30)
    bobo.penup()
    bobo.setheading(0)
    bobo.forward(20)
    bobo.left(90)

# l
def l():
    bobo.forward(40)
    bobo.pendown()
    bobo.right(180)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.penup()
    bobo.left(90)
    bobo.forward(40)
    bobo.right(180)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# m
def m():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(150)
    bobo.forward(20)
    bobo.left(110)
    bobo.forward(20)
    bobo.setheading(270)
    bobo.forward(40)
    bobo.penup()
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# n
def n():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(180)
    bobo.left(30)
    bobo.forward(40)
    bobo.setheading(90)
    bobo.forward(40)
    bobo.penup()
    bobo.right(180)
    bobo.forward(45)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# o
def o():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.penup()
    bobo.right(180)
    bobo.forward(40)
    bobo.left(90)

# p
def p():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.left(90)
    bobo.penup()
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(40)
    bobo.left(90)

# r
def r():
    bobo.pendown()
    bobo.forward(40)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.left(90)
    bobo.setheading(315)
    bobo.forward(25)
    bobo.penup()
    bobo.setheading(0)
    bobo.forward(20)
    bobo.left(90)

# s
def s():
    bobo.pendown()
    bobo.right(90)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.right(90)
    bobo.forward(20)
    bobo.penup()
    bobo.right(90)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# t
def t():
    bobo.right(90)
    bobo.forward(5)
    bobo.left(90)
    bobo.pendown()
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(10)
    bobo.right(180)
    bobo.forward(20)
    bobo.penup()
    bobo.left(180)
    bobo.forward(10)
    bobo.left(90)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# u
def u():
    bobo.forward(40)
    bobo.pendown()
    bobo.right(180)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(40)
    bobo.penup()
    bobo.right(180)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# v
def v():
    bobo.forward(40)
    bobo.pendown()
    bobo.right(180)
    bobo.left(20)
    bobo.forward(45)
    bobo.setheading(70)
    bobo.forward(45)
    bobo.penup()
    bobo.setheading(270)
    bobo.forward(40)
    bobo.left(90)
    bobo.forward(20)
    bobo.left(90)

# y
def y():
    bobo.right(90)
    bobo.forward(10)
    bobo.left(90)
    bobo.pendown()
    bobo.forward(20)
    bobo.left(30)
    bobo.forward(25)
    bobo.right(180)
    bobo.forward(25)
    bobo.left(110)
    bobo.forward(25)
    bobo.right(180)
    bobo.forward(25)
    bobo.penup()
    bobo.setheading(270)
    bobo.forward(20)
    bobo.left(90)
    bobo.forward(30)
    bobo.left(90)












































goto_start()
bobo.color(random.choice(color_lst))
new.bgcolor(random.choice(back_lst))
h1()
bobo.color(random.choice(color_lst))
new.bgcolor(random.choice(back_lst))
a()
bobo.color(random.choice(color_lst))
new.bgcolor(random.choice(back_lst))
# p()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# p()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# y()
# nextline()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# b()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# i()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# r()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# t()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# h()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# d()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# a()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# y()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# new_line(0)
# new.bgcolor(random.choice(back_lst))
g()
bobo.color(random.choice(color_lst))
new.bgcolor(random.choice(back_lst))
# r()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# k()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
d()
bobo.color(random.choice(color_lst))
new.bgcolor(random.choice(back_lst))
# d()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# h()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# i()
# bobo.color(random.choice(color_lst))
# new.bgcolor(random.choice(back_lst))
# by_omrawal()
# new.bgcolor(random.choice(back_lst))


bobo.home()
bobo.forward(200)
bobo.pendown()
bobo.color("hotpink")
bobo.width(3)
bobo.speed(0)


def squre(length, angle):

    bobo.forward(length)
    bobo.right(angle)
    bobo.forward(length)
    bobo.right(angle)

    bobo.forward(length)
    bobo.right(angle)
    bobo.forward(length)
    bobo.right(angle)


# squre(80, 90)

# for i in range(36):
#     bobo.right(10)
#     squre(80, 90)


turtle.done()
