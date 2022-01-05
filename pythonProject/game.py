from ursina import *
from ursina import entity
from ursina import hit_info
from ursina import collider
from random import randint

app = Ursina()
# =============================================================== WINDOWS =====================================================
window.fullscreen = True
window.color = color.black

#=========================================================SCORE BOARD==========================================================
# // score board (class 1) //
class scoreboard1(Button):
    def __init__(self, value):
        super().__init__(
            position = (-0.1,0.4),
            scale = (Text.size*4 , Text.size),
            text = 'Text',
        )
        self.text_entity.scale*=4
        self.value = value 
        self.text_entity.text = (f'{self.value}') 

    def update(self):
        hit_info = ball.intersects()

        if hit_info.hit:

            if hit_info.entity == line_5:
                self.value += 1
                ball.position = (0,0)
            self.value = clamp(self.value , 0 , 10)
            self.text_entity.text = f'{self.value}'
    # //  Showing Winner //
        if self.value == 10 :
            Button(text = 'Player 2 wins', position = (0,0),scale = (Text.size*10 , Text.size))
            ball.disable()

# // Score board (Class 2) //

class scoreboard2(Button):
    def __init__(self, value):
        super().__init__(
            position = (0.1,0.4),
            scale = (Text.size*4 , Text.size),
            text = 'Text',
        )
        self.text_entity.scale*=4
        self.value = value 
        self.text_entity.text = (f'{self.value}') 

    def update(self):
        hit_info = ball.intersects()

        if hit_info.hit:

            if hit_info.entity == line_4:
                self.value += 1
                ball.position = (0,0)
            self.value = clamp(self.value , 0 , 10)
            self.text_entity.text = f'{self.value}'
    # // Showing winner //
        if self.value == 10 :
            Button(text = 'Player 1 wins', position = (0,0),scale = (Text.size*4 , Text.size))
            ball.disable()

# // updating the score board //
value = 0 
score = scoreboard1(value)
score2 = scoreboard2(value)


#=====================================================ENTITES ON DE BOARD =====================================================
# // cubes //
cube = Entity(model = 'cube', position = (7,0,0), scale = (.2, 1,0), collider = 'box')
cube_2 = duplicate(cube , x = -7 )

# // De ball :) // 
ball = Entity(model = 'cube', position = (0,0,0), scale = (.2,.2,0), collider = 'box', dx = 0.085 , dy = 0.085)

# // Lines //
lines = []
line = Entity(model = 'cube', position = (0,0,0), scale = (.1,9,0))
line_2 = duplicate(line ,scale = (14,.1,0) ,position = (0,4.1,0), color = color.black, collider='box')
lines.append(line_2)
line_3 = duplicate(line ,scale = (14,.1,0) ,position = (0,-4.1,0), color = color.black, collider='box')
line_4 = duplicate(line ,scale = (.1,14,0) ,position = (-7.4,0,0), color = color.black, collider='box')
line_5 = duplicate(line ,scale = (.1,14,0) ,position = (7.4,0,0), color = color.black, collider='box')
lines.append(line_3)

# // speed of the cubes //
speed = 6

#====================================================== UPDATE FUNCTION =======================================================
def update():
    global dx , speed
    '''
    # // Some useless block of code...... Felt cute writing it , Might delete later :) //

    hit_info = ball.intersects()
    if hit_info.hit:
        dx = -dx* 1

    if hit_info.entity in lines:
        ball.y = -ball.y

    h = cube.intersects()
    if h.entity in lines:
        cube.y = False
    '''
# // moving them cubes //

    # // moving the left cube(cube) //

    col = cube.intersects()
    if held_keys['up arrow']:
        cube.y = cube.y + time.dt*speed
    if held_keys['down arrow']:
        cube.y = cube.y - time.dt*speed 

    if cube.hit.entity == line_3 :
        cube.y += 0  

    #  // Moving the right cube(cube_2) //

    if held_keys['w']:
        cube_2.y = cube_2.y + time.dt*speed
    if held_keys['s']:
        cube_2.y = cube_2.y - time.dt*speed

#  // Moving De balls :) // 
    ball.x -= ball.dx
    ball.y += ball.dy
    hit_info = ball.intersects()

    if hit_info.hit:
        
        if hit_info.entity == line_2 or hit_info.entity == line_3:
            ball.dy = -ball.dy
        if hit_info.entity == line_2 or hit_info.entity == line_3:
            ball.dx = -ball.dx

        if hit_info.entity == cube or cube_2:
            ball.dx = -ball.dx


app.run()