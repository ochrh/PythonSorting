import pygame
import random
import time

WINDOW_SIZE = 640
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
#Colors
YELLOW = "#FFFF00"
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
GREY = (170, 170, 170)
LIGHT_BLUE = (64, 224, 208)

class Rectangle:
    def __init__(self, color, x, width, height):
        self.color = color
        self.x = x
        self.width = width
        self.height = height

    def select(self):
        self.color = BLUE

    def unselect(self):
        self.color = YELLOW

    def set_smallest(self):
        self.color = LIGHT_BLUE

    def set_sorted(self):
        self.color = GREEN

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
    start_time = time.time() #Start timing

    for i in range(num_rects): #Iterate over number of objects in _rects
        for j in range(i + 1, num_rects):
            if _rects[j].height < _rects[i].height:
                _rects[j].x, _rects[i].x = _rects[i].x, _rects[j].x
                _rects[j], _rects[i] = _rects[i], _rects[j]
            draw_rects(_rects)
            yield
    end_time = time.time()  # Stop timing
    print("Execution Time:", end_time - start_time, "seconds")


def bubble_sort(_rects):
    num_rects = len(_rects)
    start_time = time.time()  # Start timing
    for i in range(num_rects - 1):
        for j in range(num_rects - i - 1):
            rects[j].select(), rects[j+1].select()
            if _rects[j].height > _rects[j+1].height:
                _rects[j+1].x, _rects[j].x = _rects[j].x, _rects[j+1].x
                _rects[j+1], _rects[j] = _rects[j], _rects[j+1]
            rects[j].unselect()
            draw_rects(_rects)
            time.sleep(.0005)
            yield
    for k in range(num_rects):
        rects[k].set_sorted()
    end_time = time.time()  # Stop timing
    print("Execution Time:", end_time - start_time, "seconds")

if __name__ == '__main__':
    #Init Objects
    rects = create_rects(100)
    draw_rects(rects)
    sorting_generator = bubble_sort(rects)

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