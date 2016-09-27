# Python_programs
import turtle

def draw_sq(tom):
       
        x=0
        while(x < 4):
            tom.forward(100)
            tom.right(90)
            x = x + 1
        


def draw_cir():
        window = turtle.Screen()
        window.bgcolor("green")
        cat = turtle.Turtle()
        cat.color("blue")
        cat.speed(10)
        
        for i in range(1,91):
            draw_sq(cat)
            cat.right(2)
        cat.forward(150)    
            
        mice = turtle.Turtle()
        mice.color("pink")
        mice.speed(10)

        for j in range(1,91):
                draw_sq(mice)
        cat.forward(150)
        window.exitonclick()
