import pygame

pygame.init()
screen_size = (screen_width,screen_height) = (1280,720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True

background_color = pygame.Color("#00ADB5")
box_color = pygame.Color("#222831")
low_high_color = "red"
mid_color = "yellow"
target_color = "green"
text_color = pygame.Color("#EEEEEE")
font = pygame.font.Font("FiraCode-Regular.ttf", 24)

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
        self.n = 6
        self.numbers = [1,2,3,4,5,6]
        self.target = 6
        self.low = 0
        self.high = self.n-1
        self.mid = 0
        self.finished = False

    def Draw(self):
        box_width = 50
        box_height = 25
        margin = 10
        x_start = (screen_width-(box_width+margin)*self.n)//2
        y_start = screen_height//2-box_height//2
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
            pygame.draw.rect(screen, color, (x, y, box_width, box_height))
            text_surface = font.render(str(self.numbers[i]), True, text_color)
            text_rect = text_surface.get_rect(center=(x+box_width//2,y+box_height//2))
            screen.blit(text_surface, text_rect)

    def OneStepBinarySearch(self):
        if not self.finished:
            self.mid = self.low+(self.high-self.low)//2
            if self.numbers[self.mid] == self.target:
                self.finished=True
            elif self.numbers[self.mid] < self.target:
                self.low = self.mid+1
            else:
                self.high = self.mid-1

    def Stop(self):
        return self.finished or self.low>self.high

BSV = Visualizer()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)
    if not BSV.Stop():
        BSV.OneStepBinarySearch()
    BSV.Draw()
    pygame.display.flip()

    clock.tick(1)

pygame.quit()
