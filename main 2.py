import turtle #importing library

my_wn = turtle.Screen()
my_wn.bgcolor("light blue")


my_pen = turtle.Turtle()

size = 100 
while size > 0:
  for i in range(4):
    my_pen.fd(size) # Move forward by 'size' 
    my_pen.left(90)
  size -=10 

my_pen.hideturtle()
my_wn.mainloop()