import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('white')
t.pencolor('orange')
t.speed(0)

for i in range(150):
	t.circle(190-i,90)
	t.lt(50)
	t.circle(190+i,20)
	t.lt(10)
s.exitonclick