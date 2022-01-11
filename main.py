import turtle
window=turtle.Screen()
window.title("Pong Game Done By Raneem")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)
rectCors = ((-60,10),(60,10),(60,-10),(-60,-10));
window.register_shape('rectangle',rectCors);



# Plyer 1
player_1=turtle.Turtle()
rectCors = ((-60,10),(60,10),(60,-10),(-60,-10));
window.register_shape('rectangle',rectCors);
player_1.shape("rectangle")
player_1.fillcolor("red")
player_1.penup()
player_1.pencolor("white")
player_1.forward(350)

# Player 2

player_2=turtle.Turtle()
rectCors = ((-60,10),(60,10),(60,-10),(-60,-10));
window.register_shape('rectangle',rectCors);
player_2.shape("rectangle")
player_2.fillcolor("blue")
player_2.penup()
player_2.pencolor("white")

player_2.backward(350)


# Ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.pencolor("white")














while True :
    window.update()