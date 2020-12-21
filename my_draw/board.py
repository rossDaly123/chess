import turtle, time

def blank_board():
    '''
    Here we will create a blank chess board
    '''
    # initalisation
    turtle.title("Chess Board")
    screen = turtle.getscreen()
    board_turtle = turtle.Turtle()
    square_size = 20
    board_turtle.fillcolor("orange")

    # Debug tool
    # board_turtle.speed(1)   # slow draw
    board_turtle.speed(10)   # fast draw

    # loop for drawing and filling board
    for box_per_column in range(8):
        for box_per_row in range(8):
            if (box_per_row%2 == 0 and box_per_column%2 == 0):  # catch first row
                board_turtle.fillcolor("gray")
            elif (box_per_row%2 == 1 and box_per_column%2 == 1): # catch second row
                board_turtle.fillcolor("gray")
            else:
                board_turtle.fillcolor("white")
            board_turtle.begin_fill()
            for square in range(4):
                board_turtle.fd(square_size)
                board_turtle.rt(90)
            board_turtle.end_fill()
            board_turtle.fd(square_size)
        board_turtle.penup()
        board_turtle.home() #finish row, return to centre
        board_turtle.lt(90) #point North
        board_turtle.fd((box_per_column+1)*square_size)
        board_turtle.rt(90)
        board_turtle.pendown() # ready in next position

if __name__ == "__main__":
    # add doctest
    blank_board()
    time.sleep(4)