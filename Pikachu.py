from turtle import *

t = Turtle()
t.speed(40)
side =10
numsqueare = 21

def drawsquare(color):
  t.color(color)
  t.begin_fill()
  for i in range(4):
    t.forward(side)
    t.right(90)
  t.end_fill()
  t.forward(side)

def nextRow():
  t.penup()
  t.backward(numsqueare * side)
  t.left(90)
  t.forward(side)
  t.right(90)
  t.pendown()

def drawRow(colors, numbers):
  for j in range(len(colors)):
    for k in range(numbers[j]):
      drawsquare(colors[j])
  nextRow()

color = ["white", "black", "white"]
number = [10, 2, 9]
drawRow(color, number)

color = ["white", "black", "gold", "black", "white"]
number = [9, 2, 1, 1, 8]
drawRow(color, number)

color = ["white", "black", "gold", "black", "white"]
number = [6, 3, 4, 1, 7]
drawRow(color, number)

color = ["white", "black", "goldenrod", "gold", "dimgrey", "black", "white"]
number = [5, 1, 2, 5, 1, 1, 6]
drawRow(color, number)

color = ["white", "black", "goldenrod", "gold", "dimgrey", "gold", "black", "white"]
number = [4, 1, 2, 1, 2, 4, 1, 6]
drawRow(color, number)

color = ["white", "black", "goldenrod", "dimgrey", "gold", "dimgrey", "gold", "saddlebrown", "dimgrey", "black", "white"]
number = [4, 1, 2, 1, 2, 1, 2, 1, 1, 1, 5]
drawRow(color, number)

color = ["white", "black", "goldenrod", "gold", "dimgrey", "gold", "dimgrey","saddlebrown", "black","white"]
number = [1, 3, 2, 2, 1, 5, 1, 1,1,4]
drawRow(color, number)

color = ["black","goldenrod","dimgrey","goldenrod","gold","red","gold","saddlebrown","dimgrey","saddlebrown","black","white"]
number = [1,1,1,1,3,2,3,1,1,1,1,5]
drawRow(color, number)

color = ["white","black","gold","red","gold","black","goldenrod","black","white"]
number = [1,1,5,2,4,1,2,1,4]
drawRow(color, number)

color = ["black","gold","darkgoldenrod","gold","black","dimgrey","gold","black","white","black","goldenrod","black","white"]
number = [1,1,1,3,1,1,4,1,1,1,2,1,3]
drawRow(color, number)

color = ["black","gold","goldenrod","white","black","gold","black","white","black","goldenrod","black","white"]
number = [1,4,1,1,1,3,1,1,1,3,1,3]
drawRow(color, number)

color = ["white","black","gold","goldenrod","gold","darkgoldenrod","black","goldenrod","black","white"]
number = [1,1,4,1,3,1,2,3,1,4]
drawRow(color, number)

color = ["white","black","gold","darkgoldenrod","gold","dimgrey","goldenrod","black","white"]
number = [1,1,6,1,2,1,5,1,3]
drawRow(color, number)

color = ["white","black","goldenrod","gold","black","gold","dimgrey","goldenrod","black","white"]
number = [2,1,1,3,2,3,1,5,1,2]
drawRow(color, number)

color = ["white","black","goldenrod","black","white","black","gold","grey","goldenrod","black","white"]
number = [3,2,1,1,2,1,2,2,5,1,1]
drawRow(color, number)

color = ["white","black","goldenrod","darkgoldenrod","black","white","black","grey","gold","goldenrod","black"]
number = [4,1,1,1,1,2,2,3,1,4,1]
drawRow(color, number)

color = ["white","black","goldenrod","black","white","black","gold","goldenrod","black"]
number = [4,1,2,1,4,4,1,3,1]
drawRow(color, number)

color = ["white","black","grey","black","white","black","gold","goldenrod","black","white"]
number = [5,1,1,1,8,1,1,1,1,1]
drawRow(color, number)

color = ["white","black","grey","black","white","black","white",]
number = [5,1,1,1,9,2,2]
drawRow(color, number)

color = ["white","black","white"]
number = [6,2,13]
drawRow(color, number)