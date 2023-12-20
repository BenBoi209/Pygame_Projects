import pygame
pygame.init()

window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Cookie Clicker')
icon = pygame.image.load('cookie.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpeg')

clock = pygame.time.Clock()

cookie = pygame.image.load('cookie.png')

text_font = pygame.font.SysFont("Helvetica", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

def draw():
    window.blit(background, (0, 0))
    window.blit(cookie, (130, 120))
    pygame.display.update()

click = False
clickCount = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0] == True:
            click = True
            clickCount += 1
            print(clickCount)
        else:
            click = False

        draw()
        draw_text("Cookie Clicker", text_font, (0, 0, 0), 170, 10)
        draw_text("Built by: BenBoi", text_font, (0, 0, 0), 320, 450)
        draw_text(f"Clicks: {clickCount}", text_font, (0, 0, 0), 10, 450)
        pygame.display.flip()

pygame.quit()

