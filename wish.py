import turtle
import random

# pointer = turtle.Turtle()


# set the name here
NAME = "Google"


# go to start of page
def goto_start():
    global pointer
    pointer.penup()
    pointer.left(90)
    pointer.forward(300)
    pointer.left(90)
    pointer.forward(330)
    pointer.left(90)

# give a space


def space():
    global pointer
    pointer.right(90)
    pointer.forward(30)
    pointer.left(90)

# got to next line just below


def nextline():
    global pointer
    pointer.right(180)
    pointer.forward(60)
    pointer.left(180)

# select a new line point to left


def new_line(n=0):
    global pointer
    pointer.setpos(0, 0)
    pointer.forward(100)
    pointer.left(90)
    pointer.forward(300)
    pointer.left(90)
    pointer.forward(n)
    pointer.right(90)
    pointer.right(90)

# my initials


def by_omrawal():
    global pointer
    pointer.color('red')
    pointer.width(6)
    pointer.setpos(0, 0)
    pointer.left(180)
    pointer.forward(250)
    pointer.right(90)
    pointer.forward(250)
    pointer.right(90)

    pointer.forward(5)
    pointer.right(90)
    pointer.pendown()
    pointer.forward(10)
    pointer.penup()
    pointer.right(90)
    pointer.forward(10)
    pointer.left(90)
    pointer.forward(10)
    pointer.left(90)

    pointer.penup()
    pointer.right(90)
    pointer.forward(40)
    pointer.pendown()
    pointer.circle(17)
    pointer.penup()
    # pointer.right(180)
    pointer.forward(34)
    pointer.left(90)

    pointer.pendown()
    pointer.forward(34)
    pointer.right(150)
    pointer.forward(17)
    pointer.left(120)
    pointer.forward(17)
    pointer.right(150)
    pointer.forward(34)
    pointer.penup()
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)


# start writing happy
def h1():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(180)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(15)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(180)
    pointer.forward(40)
    pointer.penup()
    pointer.right(180)
    pointer.forward(40)
    pointer.right(270)
    pointer.forward(20)
    pointer.right(270)

# a


def a():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(15)
    pointer.right(180)
    pointer.forward(15)
    pointer.right(90)
    pointer.forward(20)
    pointer.penup()
    pointer.right(270)
    pointer.forward(20)
    pointer.right(270)

# b


def b():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.left(180)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.penup()
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)

# c


def c():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(180)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.penup()
    pointer.forward(20)
    pointer.left(90)

# d


def d():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(15)
    pointer.right(30)
    pointer.forward(10)
    pointer.right(60)
    pointer.forward(25)
    pointer.right(30)
    pointer.forward(10)
    pointer.right(60)
    pointer.forward(15)
    pointer.penup()
    pointer.right(180)
    pointer.forward(35)
    pointer.left(90)

# e


def e():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.setheading(180)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(15)
    pointer.setheading(180)
    pointer.forward(15)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(20)
    pointer.penup()
    pointer.forward(20)
    pointer.left(90)

# f


def f():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.penup()
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.pendown()
    pointer.forward(20)
    pointer.left(180)
    pointer.penup()
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)

# g


def g():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(180)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(18)
    pointer.left(90)
    pointer.forward(8)
    pointer.penup()
    pointer.right(180)
    pointer.forward(8)
    pointer.right(90)
    pointer.forward(18)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)


# h
def h():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(180)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(15)
    pointer.left(90)
    pointer.forward(20)
    pointer.right(180)
    pointer.forward(40)
    pointer.penup()
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# i


def i():
    global pointer
    pointer.right(90)
    pointer.pendown()
    pointer.forward(20)
    pointer.left(180)
    pointer.forward(10)
    pointer.right(90)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(10)
    pointer.left(180)
    pointer.forward(20)
    pointer.penup()
    pointer.left(180)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(30)
    pointer.forward(10)
    pointer.left(90)

# j


def j():
    global pointer
    pointer.right(90)
    pointer.pendown()
    pointer.forward(10)
    pointer.left(90)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(10)
    pointer.right(180)
    pointer.forward(20)
    pointer.penup()
    pointer.left(180)
    pointer.forward(10)
    pointer.left(90)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# k


def k():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(180)
    pointer.forward(20)
    pointer.left(90)
    pointer.left(30)
    pointer.forward(30)
    pointer.right(180)
    pointer.forward(30)
    pointer.left(110)
    pointer.forward(30)
    pointer.penup()
    pointer.setheading(0)
    pointer.forward(20)
    pointer.left(90)

# l


def l():
    global pointer
    pointer.forward(40)
    pointer.pendown()
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.penup()
    pointer.left(90)
    pointer.forward(40)
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# m


def m():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(150)
    pointer.forward(20)
    pointer.left(110)
    pointer.forward(20)
    pointer.setheading(270)
    pointer.forward(40)
    pointer.penup()
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# n


def n():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(180)
    pointer.left(30)
    pointer.forward(40)
    pointer.setheading(90)
    pointer.forward(40)
    pointer.penup()
    pointer.right(180)
    pointer.forward(45)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# o


def o():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.penup()
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)

# p


def p():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.left(90)
    pointer.penup()
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(40)
    pointer.left(90)

# q


def q():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.penup()

    pointer.right(135)
    pointer.forward(15)
    pointer.right(90)
    pointer.pendown()
    pointer.forward(15)
    pointer.left(45)
    pointer.penup()
    pointer.forward(25)
    pointer.left(90)


# r
def r():
    global pointer
    pointer.pendown()
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.left(90)
    pointer.setheading(315)
    pointer.forward(25)
    pointer.penup()
    pointer.setheading(0)
    pointer.forward(20)
    pointer.left(90)

# s


def s():
    global pointer
    pointer.pendown()
    pointer.right(90)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.penup()
    pointer.right(90)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# t


def t():
    global pointer
    pointer.right(90)
    pointer.forward(5)
    pointer.left(90)
    pointer.pendown()
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(10)
    pointer.right(180)
    pointer.forward(20)
    pointer.penup()
    pointer.left(180)
    pointer.forward(10)
    pointer.left(90)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# u


def u():
    global pointer
    pointer.forward(40)
    pointer.pendown()
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(40)
    pointer.penup()
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# v


def v():
    global pointer
    pointer.forward(40)
    pointer.pendown()
    pointer.right(180)
    pointer.left(20)
    pointer.forward(45)
    pointer.setheading(70)
    pointer.forward(45)
    pointer.penup()
    pointer.setheading(270)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)

# w


def w():
    global pointer
    pointer.forward(40)
    pointer.pendown()
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(15)
    pointer.left(90)
    pointer.forward(20)
    pointer.right(180)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(15)
    pointer.left(90)
    pointer.forward(40)
    pointer.penup()
    pointer.right(180)
    pointer.forward(40)
    pointer.left(90)
    pointer.forward(20)
    pointer.left(90)


# x
def x():
    global pointer
    pointer.pendown()
    pointer.right(45)
    pointer.forward(40)
    pointer.left(180)
    pointer.forward(20)
    pointer.right(90)
    pointer.forward(20)
    pointer.left(180)
    pointer.forward(40)

    pointer.left(45)
    pointer.penup()
    pointer.setheading(0)
    pointer.forward(20)
    pointer.left(90)


# y


def y():
    global pointer
    pointer.right(90)
    pointer.forward(10)
    pointer.left(90)
    pointer.pendown()
    pointer.forward(20)
    pointer.left(30)
    pointer.forward(25)
    pointer.right(180)
    pointer.forward(25)
    pointer.left(110)
    pointer.forward(25)
    pointer.right(180)
    pointer.forward(25)
    pointer.penup()
    pointer.setheading(270)
    pointer.forward(20)
    pointer.left(90)
    pointer.forward(30)
    pointer.left(90)

# z


def z():
    global pointer
    pointer.forward(40)
    pointer.pendown()
    pointer.right(90)
    pointer.forward(20)
    pointer.right(120)
    pointer.forward(45)
    pointer.left(120)
    pointer.forward(20)
    pointer.penup()
    pointer.forward(20)
    pointer.left(90)


def changeColors():
    global pointer
    pointer.color(random.choice(color_lst))
    screen_color.bgcolor(random.choice(back_lst))


def drawCake():
    global pointer
    pointer.home()
    pointer.forward(200)
    pointer.pendown()
    pointer.color("hotpink")
    pointer.width(3)
    pointer.speed(0)
    square(80, 90)
    for i in range(36):
        pointer.right(10)
        square(80, 90)


def square(length, angle):
    global pointer
    pointer.forward(length)
    pointer.right(angle)
    pointer.forward(length)
    pointer.right(angle)
    pointer.forward(length)
    pointer.right(angle)
    pointer.forward(length)
    pointer.right(angle)


def checkWord(word):

    if word == 'a':
        a()
    elif word == 'b':
        b()
    elif word == 'c':
        c()
    elif word == 'd':
        d()
    elif word == 'e':
        e()
    elif word == 'f':
        f()
    elif word == 'g':
        g()
    elif word == 'h':
        h()
    elif word == 'i':
        i()
    elif word == 'j':
        j()
    elif word == 'g':
        g()
    elif word == 'h':
        h()
    elif word == 'i':
        i()
    elif word == 'j':
        j()
    elif word == 'k':
        k()
    elif word == 'l':
        l()
    elif word == 'm':
        m()
    elif word == 'n':
        n()
    elif word == 'o':
        o()
    elif word == 'p':
        p()
    elif word == 'q':
        q()
    elif word == 'r':
        r()
    elif word == 's':
        s()
    elif word == 't':
        t()
    elif word == 'u':
        u()
    elif word == 'v':
        v()
    elif word == 'w':
        w()
    elif word == 'x':
        x()
    elif word == 'y':
        y()
    elif word == 'z':
        z()
    else:
        print('Some Error Occured')


pointer = turtle.Turtle()
pointer.width(8)
pointer.color('#d700d7')
screen_color = turtle.getscreen()
screen_color.bgcolor("lightblue")
color_lst = ['yellow', 'red', 'brown', 'blue', 'orange', 'cyan', 'green']
back_lst = ['#daf9d7', '#9fd7e7', '#c5d107', '#9cd4d2', '#e8e4c6']
goto_start()
changeColors()
h1()
changeColors()
a()
changeColors()
p()
changeColors()
p()
changeColors()
y()
nextline()
changeColors()
b()
changeColors()
i()
changeColors()
r()
changeColors()
t()
changeColors()
h()
changeColors()
d()
changeColors()
a()
changeColors()
y()
changeColors()
new_line(0)
changeColors()

for word in list(NAME.lower()):
    print(word, " is the word")
    checkWord(word)
    changeColors()

changeColors()
by_omrawal()
changeColors()
drawCake()
turtle.done()
