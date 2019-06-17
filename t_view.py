import pygame
from mechanics import game_board

def run(game_board):
    pygame.init()
    surface = pygame.display.set_mode((600,600))
    running = True
    i = 0
    stop = False
    surface.fill(pygame.Color(250,250,250))
    draw_board()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                print(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and not stop:
                position = find_row_col(event.pos)
                res = add_mark(game_board,position,i)
                if res == True:
                    draw_element(position,i)
                    i = i +  1
        stop = check_match(game_board)
        pygame.display.flip()
        
    pygame.quit()

def draw_board():
    surface = pygame.display.get_surface()
    pygame.draw.line(surface,(4,134,248),(200,0),(200,600),3)
    pygame.draw.line(surface,(4,134,248),(400,0),(400,600),3)
    pygame.draw.line(surface,(4,134,248),(0,200),(600,200),3)
    pygame.draw.line(surface,(4,134,248),(0,400),(600,400),3)
    pygame.display.flip()
    
def check_match(game_board):
    if game_board.hor_match()[0]:
        row = game_board.hor_match()[1]
        draw_match_line('r',row)
        return True
    elif game_board.vert_match()[0]:
        col = game_board.vert_match()[1]
        draw_match_line('c',col)
        return True
    elif game_board.diag_match()[0]:
        side = game_board.diag_match()[1]
        draw_match_line('d',side)
        return True
    return False
        
def draw_match_line(mtype,position):
    surface = pygame.display.get_surface()
    if mtype == 'r':
        start_posx = 0
        start_posy = 100 + 200 * position
        end_posx = 600
        end_posy = start_posy
        pygame.draw.line(surface,(222,46,31),(start_posx,start_posy),(end_posx,end_posy),10)
    elif mtype == 'c':
        start_posx = 100 + 200 * position
        start_posy = 0
        end_posx = start_posx
        end_posy = 600
        pygame.draw.line(surface,(222,46,31),(start_posx,start_posy),(end_posx,end_posy),10)
    elif position == 'left':
        pygame.draw.line(surface,(222,46,31),(20,20),(580,580),10)
    elif position == 'right':
        pygame.draw.line(surface,(222,46,31),(20,580),(580,20),10)
        
    
def find_row_col(pos):
    if pos[0] <= 200:
        col = 0
    elif pos[0] <= 400:
        col = 1
    else:
        col = 2
    if pos[1] <= 200:
        row = 0
    elif pos[1] <= 400:
        row = 1
    else:
        row = 2
    return (row,col)
                                        
def add_mark(game_board,position,player):
    p = 'X' if player % 2 == 0 else 'O'
    res = game_board.add_element(p,position[0],position[1])
    return res

def draw_element(pos,player):
    if player % 2 == 0:
        draw_x(pos)
    else:
        draw_o(pos)
        
def draw_x(pos):
    surface = pygame.display.get_surface()
    start_posx1 = 20 + 200*pos[1]
    start_posy1 = 20 + 200*pos[0]
    end_posx1 = 180 + 200*pos[1]
    end_posy1 = 180 + 200*pos[0]
    start_posy2 = 180 + 200*pos[0]
    end_posy2 = 20 + 200*pos[0]
    pygame.draw.line(surface,(0,0,0),(start_posx1,start_posy1),(end_posx1,end_posy1),10)
    pygame.draw.line(surface,(0,0,0),(start_posx1,start_posy2),(end_posx1,end_posy2),10)

def draw_o(pos):
    surface = pygame.display.get_surface()
    centerx = 100 + 200 * pos[1]
    centery = 100 + 200 * pos[0]
    pygame.draw.circle(surface,(0,0,0),(centerx,centery),100,10)

if __name__ == '__main__':
    board = game_board()
    run(board)







