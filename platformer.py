import pygame

pygame.init()

W, H = 900, 700
background = (44, 200, 100)
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Платформер")

clock = pygame.time.Clock()
FPS = 60

class Player(pygame.sprite.Sprite):

    GRAVITY = 1

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.surface = pygame.Surface((width, height))
        self.color = (0, 0, 255)
        self.surface.fill(self.color)

        self.x_vel = 5
        self.y_vel = 0
        self.fall_count = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.x_vel
        if keys[pygame.K_d] and self.rect.x < W - 50:
            self.rect.x += self.x_vel

        self.y_vel += min(1, (self.fall_count / FPS) * self.GRAVITY)
        self.rect.y += self.y_vel
        self.fall_count += 1


    def draw(self):
        screen.blit(self.surface, (self.rect.x, self.rect.y))

player = Player(100, 100, 50, 50)

run_game = True
while run_game:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    player.move()
    player.draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()


