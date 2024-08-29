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

n = int(input("n= "))
numbers = []
print("Enter n numbers:")
for i in range(n):
    num = int(input())
    numbers.append(num)
target = int(input("target= "))
numbers.sort()



def draw_boxes(numbers, low, high, mid, target_index=None):
    box_width = 50
    box_height = 25
    margin = 10
    x_start = (screen_width-(box_width+margin)*n)//2
    y_start = screen_height//2-box_height//2
    for i, number in enumerate(numbers):
        x = x_start+i*(box_width + margin)
        y = y_start
        if i == target_index:
            color = target_color
        elif i == low or i == high:
            color = low_high_color
        elif i == mid:
            color = mid_color
        else:
            color = box_color
        pygame.draw.rect(screen, color, (x, y, box_width, box_height))
        text_surface = font.render(str(number), True, text_color)
        text_rect = text_surface.get_rect(center=(x+box_width//2,y+box_height//2))
        screen.blit(text_surface, text_rect)

def binary_search(numbers, target):
    low = 0
    high = len(numbers)-1
    while low <= high:
        mid = (low + high) // 2
        draw_boxes(numbers, low, high, mid, target_index)
        pygame.display.flip()
        if numbers[mid] == target:
            target_index = mid
            break
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    draw_boxes(numbers, low, high, mid, target_index)
    pygame.display.flip()
    return target_index

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
