"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.yu
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
emojis = [":)","^-^",":D","^o^","*^*","-_-",":/",":(","=_=","!_!","X.X","~_~","o_o",">_<","._.",";)",":3",":v","o.O","8)","^.^","+.+",":D","·u·","$_$","7_7","<3","r.r","ç_ç","#.#","€_€","¬.¬"]
tiles = emojis * 2
state = {'mark': None}
hide = [True] * 64
nTaps = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global nTaps 
    nTaps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    

    
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
        else: 
            # Game Finished: win
            if True not in hide:
                goto(0,0)
                color('white')
                write("YOU WIN!", font=('Arial', 30, 'normal'), align='center')
                goto(0,-20)
                write(f"Taps: {nTaps}", font=('Arial', 10, 'normal'), align='center')
                print("You win!")
                return
            pass
            

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #if tiles[mark] < 10:
           # goto(x + 15, y+2)
        #else:
         #   goto(x + 3, y+2)
        goto(x + 3, y+2)
        color('black')

        write(tiles[mark], font=('Arial', 26, 'normal'))
    up()
    goto(0, -190)
    write(f"Taps: {nTaps}", align="center",font=('Arial', 10, 'normal'))
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
