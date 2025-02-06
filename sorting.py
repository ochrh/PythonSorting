import pygame
import random

WINDOW_SIZE = 640
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
#Colors
YELLOW = "#FFFF00"
BLACK = (0,0,0)
WHITE = (0,0,0)

class Rectangle:
    def __init__(self, color, x, width, height):
        self.color = color
        self.x = x
        self.width = width
        self.height = height

# FUNCTIONS
def create_rects(num_rects):
    rectangles = [] #list of rects obj
    heights = [] #list of rect obj.height
    rect_width =  ((WINDOW_SIZE - 16) // num_rects)
    gap = 8
    print(rect_width)

    for i in range(num_rects):
        height = random.randint(10,500)
        while height in heights:
            height = random.randint(8, 256)

        heights.append(height)

        rect = Rectangle(YELLOW, gap + (i * rect_width), rect_width, height)
        rectangles.append(rect)
    return rectangles

def draw_rects(_rects):
    WINDOW.fill((255,255,255))

    for rect in _rects:
        pygame.draw.rect(WINDOW, rect.color, (rect.x, WINDOW_SIZE-rect.height, rect.width, rect.height))
        pygame.draw.line(WINDOW, BLACK, (rect.x, WINDOW_SIZE), (rect.x, WINDOW_SIZE-rect.height))
        pygame.draw.line(WINDOW, BLACK, (rect.x+rect.width, WINDOW_SIZE), (rect.x+rect.width, WINDOW_SIZE-rect.height))
        pygame.draw.line(WINDOW, BLACK, (rect.x, WINDOW_SIZE-rect.height), (rect.x+rect.width, WINDOW_SIZE-rect.height))

def selection_sort(_rects):
    num_rects = len(_rects)
    for i in range(num_rects): #Iterate over number of objects in _rects
        for j in range(i + 1, num_rects):
            draw_rects(_rects)
            if _rects[j].height < _rects[i].height:
                _rects[j].x, _rects[i].x = _rects[i].x, _rects[j].x
                _rects[j], _rects[i] = _rects[i], _rects[j]
            yield
    draw_rects(_rects)

if __name__ == '__main__':
    #Init Objects
    rects = create_rects(100)
    draw_rects(rects)
    sorting_generator = selection_sort(rects)

    running = True
    sorting = False
    while running:
        if sorting:
            try:
                next(sorting_generator)
            except StopIteration:
                sorting = False
        else:
            draw_rects(rects)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sorting = not sorting
        pygame.display.flip()