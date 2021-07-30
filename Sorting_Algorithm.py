import pygame
import random as r
from opensimplex import OpenSimplex
import os.path
print(os.path.dirname(__file__))


# initializing pygame
pygame.init()

# ------------------------------------------------
#   Setting global variables
# ------------------------------------------------

#   setting window size
winX = 1000
winY = 600

#   width of bars
width = 2

#   defining surface
win = pygame.display.set_mode((winX, winY))
pygame.display.set_caption('Sorting Algorithm Visualizer')

#   defining clock
clock = pygame.time.Clock()

#   list of random ints
list = []

#   Global tick
tick = 0

# Variable used to define wave or rand.
Option = 1

# ------------------------------------------------
#   Loading Images
# ------------------------------------------------

filepath = os.path.dirname(__file__)
bg_random = pygame.image.load(os.path.join(filepath, "imgs/Menu.png"))
bg_waves = pygame.image.load(os.path.join(filepath, "imgs/Menu_waves.png"))


# ------------------------------------------------
#   Drawing Objects
# ------------------------------------------------

class ButtonHitbox(object):

    def __init__(self, x, x2, y, y2, color, action=0):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.action = action


    def draw(self, win):
        # drawing button
        pygame.draw.rect(win, self.color, (self.x, self.y, (self.x2-self.x), (self.y2-self.y)),1)

class Text(object):

    def __init__(self,  text, x, y, size, textColor):
        self.x = x
        self.y = y
        self.textColor = textColor
        self.text = text
        self.size = size


    def draw(self, win):
        # drawing Text
        font = pygame.font.SysFont('comicsans', self.size)
        text = font.render(self.text, 1, self.textColor)
        win.blit(text, (int(self.x), int(self.y-text.get_height()/2)))

# ------------------------------------------------
#   Main loop
# ------------------------------------------------

def mainLoop():
    global tick
    run = True
    while run:
        check = click()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_ESCAPE]:
                run = False

        if keys[pygame.K_2] or check == 4:
            randomizeList(Option)
            quickSort(list, 0, len(list) - 1)
            pause()
        elif keys[pygame.K_1] or check == 3:
            randomizeList(Option)
            bubbleSort(list)
        elif keys[pygame.K_3] or check == 5:
            randomizeList(Option)
            mergeSort(list, 0, len(list)-1)
            pause()
        draw(win)


        if 1 <= tick < 20:
            tick+=1
        else:
            tick=0

    pygame.quit()


# ------------------------------------------------
#   Bubble sort
# ------------------------------------------------

def bubbleSort(list):
    i = 0
    while i < len(list):
        j = 0
        while j < len(list) - i:

            # check for X out or go back to menu
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if keys[pygame.K_SPACE]:
                    return

            # check for X out or go back to menu
            if i != 0:
                if list[j] > list[j + 1]:
                    swap(list, j, j + 1)
                drawBubble(list, j)
            j += 1
        # drawBubble(list,0)
        i += 1
    pause()


def drawBubble(list, j):
    #   SetsBackround
    win.fill((255, 255, 255))

    #   draws every rectangle
    k = 0
    for item in list:
        pygame.draw.rect(win, (0, 0, 0), (int(k * width), int(winY - item), int(width), int(item)))
        k += 1

    #   Draws the current rectangle comparison
    pygame.draw.rect(win, (255, 0, 0), (int(j * width), int(winY - list[j]), int(width), int(list[j])))
    pygame.draw.rect(win, (255, 0, 0),
                     (int((j + 1) * width), int(winY - list[(j + 1)]), int(width), int(list[(j + 1)])))

    #   Updates screen
    pygame.display.update()


# ------------------------------------------------
#   Quick sort
# ------------------------------------------------

def quickSort(arr, start, end):
    keys = pygame.key.get_pressed()
    if start >= end:
        return True
    elif keys[pygame.K_SPACE]:
        return False

    index = partition(arr, start, end)

    if index == 2000:
        return False

    check = quickSort(arr, start, index - 1)

    if not (check):
        return False

    check = quickSort(arr, index + 1, end)

    if not (check):
        return False

    return True


def partition(arr, start, end):
    pivotValue = arr[end]
    pivotIndex = start

    i = start
    while i < end:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if keys[pygame.K_SPACE]:
            return 2000
        if arr[i] <= pivotValue:
            swap(arr, i, pivotIndex)
            pivotIndex += 1
        i += 1
        drawQuicksort(arr, pivotIndex)
    swap(arr, pivotIndex, end)

    return pivotIndex


def drawQuicksort(list, pivotIndex):
    win.fill((255, 255, 255))
    k = 0
    for item in list:
        pygame.draw.rect(win, (0, 0, 0), (int(k * width), int(winY - item), int(width), int(item)))
        # pygame.draw.rect(win, (60, 60, 60), (k * width, winY - item, width, item + 10), 1)
        k += 1

    pygame.draw.rect(win, (255, 0, 0),
                     (int(pivotIndex * width), int(winY - list[pivotIndex]), int(width), int(list[pivotIndex])))
    pygame.display.update()

# ------------------------------------------------
#   Merge sort
# ------------------------------------------------

def mergeSort(arr, l, r):

    m = (l + r) // 2
    if l < r:
        check = mergeSort(arr,l,m)
        if check == 1:
            return 1
        check = mergeSort(arr,m+1,r)
        if check == 1:
            return 1
        check = merge(arr, l, m, m+1, r)
        if check == 1:
            return 1
        drawMerge2(arr)

def merge(arr, X1, Y1, X2, Y2):
    i = X1
    j = X2
    temp = []

    while i <= Y1 and j <= Y2:
        check = checkQuit()
        if check==1:
            return 1
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
        drawMerge(arr,temp, X1)

    while i <= Y1:
        check = checkQuit()
        if check == 1:
            return 1
        temp.append(arr[i])
        i += 1
        drawMerge(arr, temp, X1)
    while j <= Y2:
        check = checkQuit()
        if check == 1:
            return 1
        temp.append(arr[j])
        j += 1
        drawMerge(arr, temp, X1)

    i = X1
    for item in temp:
        check = checkQuit()
        if check == 1:
            return 1
        arr[i] = item
        i += 1

def drawMerge(arr,temp,X1):
    #   SetsBackround
    win.fill((255, 255, 255))

    #   draws every rectangle
    k = 0
    for item in arr:
        pygame.draw.rect(win, (0, 0, 0), (int(k * width), int(winY - item), int(width), int(item)))
        k += 1

    win.fill((255, 255, 255), (X1*width, 0, (len(temp))*width//2, winY))
    k = X1
    for item in temp:
        pygame.draw.rect(win, (255, 0, 0), (int(k * width), int(winY - item), int(width), int(item)))
        k += 1


    #   Updates screen
    pygame.display.update()

def drawMerge2(arr):
    #   SetsBackround
    win.fill((255, 255, 255))

    #   draws every rectangle
    k = 0
    for item in arr:
        pygame.draw.rect(win, (0, 0, 0), (int(k * width), int(winY - item), int(width), int(item)))
        k += 1

# ------------------------------------------------
#   Generic functions
# ------------------------------------------------

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def randomizeList(option):
    # list of random ints
    global list, listCopy
    list = []

    # creating noise seed
    tmp = OpenSimplex(r.randint(0, 10000))

    g = 0

    if option == 1:
        while g < winX / width:
            list.append(r.randint(0, winY))
            g += 1

    noise = 0.03  # responsible for increasing noise intervals

    if option == 2:
        while g < (winX / width) * noise:
            if tmp.noise2d(1, g) * winY < 0:
                list.append(tmp.noise2d(1, g) * winY / 2 + winY / 2)
            else:
                list.append(tmp.noise2d(1, g) * winY / 2 + winY / 2)
            g += noise

    # creating a copy of our random list
    listCopy = list

def draw(win):
    if Option == 1:
        win.blit(bg_random,(0,0))
    else:
        win.blit(bg_waves,(0,0))
    widthText = Text(str(width), 320, 140, 40, (0, 0, 0))
    widthText.draw(win)

    #   Draws hitbox for buttons
    # for button in buttons:
    #     button.draw(win)

    pygame.display.update()

def click():
    global tick, width, Option
    if pygame.mouse.get_pressed() == (1, 0, 0):
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.x < pos[0] < button.x2:
                if button.y < pos[1] < button.y2:
                    if tick == 0:
                        if button.action == 1 and width < 10:
                            width += 1
                        if button.action == 2 and width > 1:
                            width -= 1
                        if button.action == 3:
                            return 3
                        if button.action == 4:
                            return 4
                        if button.action == 5:
                            return 5
                        if button.action == 6:
                            Option = 1
                        if button.action == 7:
                            Option = 2
                        tick +=1
    return 0

def pause():
    run = False
    while not (run):

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if keys[pygame.K_SPACE]:
            return

        font = pygame.font.SysFont('comicsans', 50)
        pressSpace = font.render('[press SPACE to go back to menu]', 1, (255, 255, 255))
        win.blit(pressSpace,
                 (int(winX / 2 - pressSpace.get_width() / 2), int(winY - pressSpace.get_height() - 30)))

        pygame.display.update()
        clock.tick(15)

def checkQuit():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if keys[pygame.K_SPACE]:
        return 1


# ------------------------------------------------
#   creating MENU with object class
# ------------------------------------------------

#   Text class (text , x, y, size, textColor)
widthText = Text(str(width), 342, 140, 40, (0, 0, 0))

#   button class (x, x2, y, y2, color, action=0)
plusButton = ButtonHitbox(378, 483, 112, 169, (255, 0, 0), 1)
minusButton = ButtonHitbox(490, 596, 112, 169, (255, 0, 0), 2)
randomButton = ButtonHitbox(603, 709, 112, 169, (255, 0, 0), 6)
wavesButton = ButtonHitbox(716, 821, 112, 169, (255, 0, 0), 7)
BubbleButton = ButtonHitbox(58, 342, 197, 589, (255, 0, 0), 3)
QuickButton = ButtonHitbox(358, 643, 197, 589, (255, 0, 0), 4)
MergeButton = ButtonHitbox(658, 943, 197, 589, (255, 0, 0), 5)



buttons = [plusButton, minusButton, BubbleButton, QuickButton, MergeButton, randomButton, wavesButton]

# ------------------------------------------------
#   running program
# ------------------------------------------------

if __name__=="__main__":
    mainLoop()
