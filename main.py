import pygame

pygame.init()
screen_size = (screen_width,screen_height) = (1280,720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True

background_color = pygame.Color("#A0FF00")
box_color = "white"
low_high_color = pygame.Color("#FF0000")
mid_color = "yellow"
target_color = pygame.Color("#00FFFF")
text_color = pygame.Color("#5F00FF")
font = pygame.font.Font("FiraCode-Regular.ttf", 14)

class Button:
    def __init__(self,text,x,y,width,height):
        self.text = text
        self.rect = pygame.Rect(x,y,width,height)
        self.color = pygame.Color("#393E46")
        self.hover_color = pygame.Color("#555B6E")
        self.text_color = pygame.Color("#EEEEEE")

    def draw(self, surface):
        screen.fill(background_color)
        pygame.draw.rect(surface, box_color,self.rect)
        text_surface = font.render(self.text,True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        pygame.display.flip()

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def click(self):
        return self.is_hovered() and pygame.mouse.get_pressed()[0]

class Visualizer:
    def __init__(self):
        # self.n = int(input("n= "))
        # self.numbers = []
        # print("Enter n numbers:")
        # for i in range(self.n):
        #     num = int(input())
        #     self.numbers.append(num)
        # self.target = int(input("target= "))
        # self.numbers.sort()
        self.n = 15
        self.numbers = [1,5,8,12,15,21,24,30,35,42,47,53,59,63,68]
        self.target = 42
        self.low = 0
        self.high = self.n-1
        self.mid = self.low+(self.high-self.low)//2
        self.start = False
        self.finished = False

    def Draw(self):
        box_width = 50
        box_height = 25
        margin = 10
        x_start = (screen_width-(box_width+margin)*self.n)//2
        y_start = screen_height//2-box_height//2
        screen.fill(background_color)
        for i in range(self.n):
            x = x_start+i*(box_width + margin)
            y = y_start
            if i == self.mid:
                if self.finished:
                    color = target_color
                else:
                    color = mid_color
            elif i == self.low or i == self.high:
                color = low_high_color
            else:
                color = box_color
            pygame.draw.rect(screen,color,(x,y,box_width,box_height))
            text_surface = font.render(str(self.numbers[i]),True,text_color)
            text_rect = text_surface.get_rect(center=(x+box_width//2,y+box_height//2))
            screen.blit(text_surface,text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)

    def BinarySearchMidUpdate(self):
        self.mid = self.low+(self.high-self.low)//2

    def BinarySearchLowHighUpdate(self):
        if self.numbers[self.mid] == self.target:
            self.finished=True
        elif self.numbers[self.mid] < self.target:
            self.low = self.mid+1
        else:
            self.high = self.mid-1

    def Stop(self):
        return self.finished or self.low>self.high

BSV = Visualizer()
start_button = Button("Start",screen_width//2-50,screen_height//2+100,100,50)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill(background_color)
    if not BSV.start:
        start_button.draw(screen)
        
        if start_button.click():
            BSV.start = True
            screen.fill(background_color)
            # BSV.Draw()
            # pygame.display.flip()
            # pygame.time.delay(1000)
    else:
        if not BSV.Stop():
            BSV.Draw()
            BSV.BinarySearchMidUpdate()
            BSV.Draw()
            BSV.BinarySearchLowHighUpdate()
            # pygame.display.flip()
            # pygame.time.delay(1000)
            # BSV.OneStepBinarySearch()
            # pygame.time.delay(1000)
        # screen.fill(background_color)
        BSV.Draw()
        # pygame.time.delay(1000)
    # pygame.display.flip()

    clock.tick(60)

pygame.quit()
