from random import randint
from datetime import datetime
import keyboard
import os
import time

# high score: 474

fps = 9 # fps to display the game in
key_delay = 0.2 # deley between checking key press
solid_spawn_speed = 0.25
solid_move_speed = 0.25

row_1 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_2 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_3 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_4 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_5 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_6 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_7 = {1:'empty',2:'empty',3:'empty',4:'player',5:'empty',6:'empty',7:'empty'} # player placed in the middle as standard

row_character_1 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_character_2 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_character_3 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_character_4 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_character_5 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_character_6 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}
row_character_7 = {1:'empty',2:'empty',3:'empty',4:'empty',5:'empty',6:'empty',7:'empty'}

leftc = datetime.now()
rightc = datetime.now()
framec = datetime.now()
solidc = datetime.now()
solidmc = datetime.now()

score = 0

render_delay = 1 / fps

def move_player(direction):
    for i in row_7:
        if row_7[i] == 'player':
            if direction == 'Left' and i > 1:
                row_7[i] = 'empty'
                row_7[i - 1] = 'player'
                return
            elif direction == 'Right' and i < 7:
                row_7[i] = 'empty'
                row_7[i + 1] = 'player'
                return

while(1):
    leftc_d = datetime.now() - leftc
    rightc_d = datetime.now() - rightc
    framec_d = datetime.now() - framec
    solidc_d = datetime.now() - solidc
    solidmc_d = datetime.now() - solidmc

    # controls
    if keyboard.is_pressed('Left') and leftc_d.total_seconds() > key_delay: # on left key
        leftc = datetime.now()
        move_player('Left')
    elif keyboard.is_pressed('Right') and rightc_d.total_seconds() > key_delay: # on right key
        rightc = datetime.now()
        move_player('Right')

    # move solid
    if solidmc_d.total_seconds() > solid_move_speed:
        solidmc = datetime.now()
        score += 1

        for i in row_7:
            if row_7[i] == 'solid':
                row_7[i] = 'empty'

        for i in row_6:
            if row_6[i] == 'solid':

                if row_7[i] == 'player':
                    print(f'Game Over, score:{score}')
                    quit()
                
                row_6[i] = 'empty'
                row_7[i] = 'solid'

        for i in row_5:
            if row_5[i] == 'solid':
                row_5[i] = 'empty'
                row_6[i] = 'solid'

        for i in row_4:
            if row_4[i] == 'solid':
                row_4[i] = 'empty'
                row_5[i] = 'solid'

        for i in row_3:
            if row_3[i] == 'solid':
                row_3[i] = 'empty'
                row_4[i] = 'solid'

        for i in row_2:
            if row_2[i] == 'solid':
                row_2[i] = 'empty'
                row_3[i] = 'solid'

        for i in row_1:
            if row_1[i] == 'solid':
                row_1[i] = 'empty'
                row_2[i] = 'solid'

    # spawn solid
    if solidc_d.total_seconds() > solid_spawn_speed:
        solidc = datetime.now()
        spawn_column = randint(1,7)
        row_1[spawn_column] = 'solid'

    # render start
    if framec_d.total_seconds() > render_delay:
        framec = datetime.now()
        def p_row_1():
            for i in row_1:
                if (row_1[i] == 'empty'):
                    row_character_1[i] = '▒'
                elif (row_1[i] == 'solid'):
                    row_character_1[i] = '█'
                elif (row_1[i] == 'player'):
                    row_character_1[i] = '▲'
                else:
                    print('Data error!')
                    quit()
                
            return f'{row_character_1[1]} {row_character_1[2]} {row_character_1[3]} {row_character_1[4]} {row_character_1[5]} {row_character_1[6]} {row_character_1[7]}'

        def p_row_2():
            for i in row_2:
                if (row_2[i] == 'empty'):
                    row_character_2[i] = '▒'
                elif (row_2[i] == 'solid'):
                    row_character_2[i] = '█'
                elif (row_2[i] == 'player'):
                    row_character_2[i] = '▲'
                else:
                    print('Data error!')
                    quit()

            return f'{row_character_2[1]} {row_character_2[2]} {row_character_2[3]} {row_character_2[4]} {row_character_2[5]} {row_character_2[6]} {row_character_2[7]}'

        def p_row_3():
            for i in row_3:
                if (row_3[i] == 'empty'):
                    row_character_3[i] = '▒'
                elif (row_3[i] == 'solid'):
                    row_character_3[i] = '█'
                elif (row_3[i] == 'player'):
                    row_character_3[i] = '▲'
                else:
                    print('Data error!')
                    quit()

            return f'{row_character_3[1]} {row_character_3[2]} {row_character_3[3]} {row_character_3[4]} {row_character_3[5]} {row_character_3[6]} {row_character_3[7]}'

        def p_row_4():
            for i in row_4:
                if (row_4[i] == 'empty'):
                    row_character_4[i] = '▒'
                elif (row_4[i] == 'solid'):
                    row_character_4[i] = '█'
                elif (row_4[i] == 'player'):
                    row_character_4[i] = '▲'
                else:
                    print('Data error!')
                    quit()

            return f'{row_character_4[1]} {row_character_4[2]} {row_character_4[3]} {row_character_4[4]} {row_character_4[5]} {row_character_4[6]} {row_character_4[7]}'

        def p_row_5():
            for i in row_5:
                if (row_5[i] == 'empty'):
                    row_character_5[i] = '▒'
                elif (row_5[i] == 'solid'):
                    row_character_5[i] = '█'
                elif (row_5[i] == 'player'):
                    row_character_5[i] = '▲'
                else:
                    print('Data error!')
                    quit()

            return f'{row_character_5[1]} {row_character_5[2]} {row_character_5[3]} {row_character_5[4]} {row_character_5[5]} {row_character_5[6]} {row_character_5[7]}'

        def p_row_6():
            for i in row_6:
                if (row_6[i] == 'empty'):
                    row_character_6[i] = '▒'
                elif (row_6[i] == 'solid'):
                    row_character_6[i] = '█'
                elif (row_6[i] == 'player'):
                    row_character_6[i] = '▲'
                else:
                    print('Data error!')
                    quit()

            return f'{row_character_6[1]} {row_character_6[2]} {row_character_6[3]} {row_character_6[4]} {row_character_6[5]} {row_character_6[6]} {row_character_6[7]}'

        def p_row_7():
            for i in row_7:
                if (row_7[i] == 'empty'):
                    row_character_7[i] = '▒'
                elif (row_7[i] == 'solid'):
                    row_character_7[i] = '█'
                elif (row_7[i] == 'player'):
                    row_character_7[i] = '▲'
                else:
                    print('Data error!')
                    quit()

            return f'{row_character_7[1]} {row_character_7[2]} {row_character_7[3]} {row_character_7[4]} {row_character_7[5]} {row_character_7[6]} {row_character_7[7]}'

        # clear and then print
        os.system('cls')
        print(f'{p_row_1()}\n{p_row_2()}\n{p_row_3()}\n{p_row_4()}\n{p_row_5()}\n{p_row_6()}\n{p_row_7()}')
        #print(f'{row_7[1]}\n{row_7[2]}\n{row_7[3]}\n{row_7[4]}\n{row_7[5]}\n{row_7[6]}\n{row_7[7]}') # player debug