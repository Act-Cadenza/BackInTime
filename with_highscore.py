import pygame, sys
pygame.init()

MENU_BACKGROUND_COLOR = (228, 55, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("ISOCTEUL", 30)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node



    def remove(self, position):
        if self.head == None:
            return

        temp = self.head

        if position == 1:
            self.head = temp.next
            temp = None
            return
        
        i = 0
        for i in range(i + 1,position):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None
        temp.next = next


for_high = LinkedList()

def read_from_file_and_find_highscore(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close
    high_score = 0
    high_name = ""
     
    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)
 
        if score > high_score:
            high_score = score
            high_name = name

            

    return high_name, high_score


def write_to_file(file_name, your_name, points):
    score_file = open(file_name, 'a')
    print(your_name+",", points, file=score_file)
    score_file.close()
     


def Selection_sort(lista): #selection sort in descending order
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[min_idx] < lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]





def show_top10(screen, file_name):
    
  
    bx = 700  # x-size of box
    by = 500  # y-size of box

    file = open(file_name, 'r')
    lines=file.readlines()
    box = pygame.surface.Surface((bx, by))
    box.fill(MENU_BACKGROUND_COLOR)

    all_score = []
    for line in lines:
        sep = line.index(',')
        name = line[:sep]
        score = int(line[sep+1:-1])
        all_score.append((score, name))
        for_high.add(all_score)
        
    if len(all_score) == 10:
        for_high.remove(all_score[10])


       
    file.close
    Selection_sort(all_score)
    best = all_score[:10] 
    # make the presentation box
    box = pygame.surface.Surface((bx, by))
    box.fill(MENU_BACKGROUND_COLOR)

    pygame.draw.rect(box, WHITE, (50, 12, bx-100, 35), 0)
    pygame.draw.rect(box, WHITE, (50, by-60, bx-100, 42), 0)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = font.render("HIGHSCORE", True, BLACK)  # headline
    txt_rect = txt_surf.get_rect(center=(bx//2, 30))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("Press ENTER to RETURN MENU", True, BLACK)  # bottom line
    txt_rect = txt_surf.get_rect(center=(bx//2, 360))

    box.blit(txt_surf, txt_rect)
    
    # write the top-10 data to the box
    for i, entry in enumerate(best):
        txt_surf = font.render(entry[1] + "  " + str(entry[0]), True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx//2, 30*i+60))
        box.blit(txt_surf, txt_rect)
        
        
     
    screen.blit(box, (0, 0))
    pygame.display.flip()

    while True:  # wait for user to acknowledge and return
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                return
        pygame.time.wait(20)

    return all_score
def enterbox(screen, txt):
 
    def blink(screen):
        for color in [MENU_BACKGROUND_COLOR, WHITE]:
            pygame.draw.circle(box, color, (bx//2, int(by*0.7)), 7, 0)
            screen.blit(box, (0, by//2))
            pygame.display.flip()
            pygame.time.wait(300)

    def show_name(screen, name):
        pygame.draw.rect(box, WHITE, (50, 60, bx-100, 20), 0)
        txt_surf = font.render(name, True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx//2, int(by*0.7)))
        box.blit(txt_surf, txt_rect)
        screen.blit(box, (0, by//2))
        pygame.display.flip()
    #to set size for the entry box
    bx = 700
    by = 100

    # make box
    box = pygame.surface.Surface((bx, by))
    box.fill(MENU_BACKGROUND_COLOR)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = font.render(txt, True, BLACK)
    txt_rect = txt_surf.get_rect(center=(bx//2, int(by*0.3)))
    box.blit(txt_surf, txt_rect)
 
    name = ""
    show_name(screen, name)

    #the input-loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                inkey = event.key
                if inkey in [13, 271]:  # enter/return key
                    return name
                elif inkey == 8:  # backspace key
                    name = name[:-1]
                elif inkey <= 300:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT and 122 >= inkey >= 97:
                        inkey -= 32  # handles CAPITAL input
                    name += chr(inkey)

        if name == "":
            blink(screen)
        show_name(screen, name)
#this function will check if you got a highscore then it will allow you to record your score
def record_high(screen, file_name, your_points):
    high_name, high_score = read_from_file_and_find_highscore(file_name)
    your_name = ''

    
    
    if your_points >= high_score:
        your_name = enterbox(screen, "YOU HAVE EARN A HIGH SCORE! - Enter code name:")

    elif your_points <= high_score:
        st1 = "The Highscore is "
        st2 = " made by "
        st3 = ". What's your name? "
        txt = st1 + str(high_score) + st2 + high_name + st3
        your_name = enterbox(screen, txt)

    
       
    if your_name == None or len(your_name) == 0:
       return

    write_to_file(file_name, your_name, your_points)


    
def highscore(screen, file_name, your_points):
    high_name, high_score = read_from_file_and_find_highscore(file_name)
    
   
    show_top10(screen, file_name)
    return



