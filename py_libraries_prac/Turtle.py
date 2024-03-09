import turtle

#python class name follows the convention of Pascal Casing
my_turtle = turtle.Turtle() #my_turtle is an object created from the Turtle class
my_turtle.shape("turtle")
my_turtle.color("DarkTurquoise")
my_turtle.forward(100)

my_screen = turtle.Screen()
my_screen.exitonclick() #after this method is called, the screen only terminates its execution after the user has clicked on it