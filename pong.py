import pygame

WIDTH = 720
HEIGHT = 560

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
frame_rate = 90

pong = pygame.Rect((WIDTH // 2) - 10, (HEIGHT // 2) - 10, 20, 20)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 45, 10, 90)
opponent = pygame.Rect(10, HEIGHT // 2 - 45, 10, 90)

pong_x = 3
pong_y = 3
player_vel = 5
opponent_vel = 5

bgcolor = pygame.Color('grey12')
light_grey = (200, 200, 200)


def pong_physics():
    global pong_x, pong_y
    pong.x += pong_x
    pong.y += pong_y

    if pong.x <= 0 or pong.x >= WIDTH - 15:
        pong.x, pong.y = (WIDTH // 2) - 15, (HEIGHT // 2) - 10
        
    if pong.y <= 0 or pong.y >= HEIGHT - 15:
        pong_y *= -1

    if pong.colliderect(player) or pong.colliderect(opponent):
        pong_x *= -1


def main():
    global pong_x, pong_y, player_vel
    run = True
    clock = pygame.time.Clock()

    while run:
        display.fill(bgcolor)
        clock.tick(frame_rate)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_UP]:
            player.y -= player_vel
            if player.y <= 0:
                player.y = 5

        if keys[pygame.K_DOWN]:
            player.y += player_vel
            if player.y + player.height >= HEIGHT:
                player.y = HEIGHT - player.height- 5

        if opponent.y < pong.y:
            opponent.y += opponent_vel
        if opponent.y > pong.y:
            opponent.y -= opponent_vel
        if opponent.y <= 0:
            opponent.y = 5
        if opponent.y + opponent.height >= HEIGHT:
            opponent.y = HEIGHT - opponent.height - 5

        pong_physics()

        pygame.draw.line(display, light_grey, (WIDTH // 2, 0),
                         (WIDTH // 2, HEIGHT))
        pygame.draw.rect(display, light_grey, player)
        pygame.draw.rect(display, light_grey, opponent)
        pygame.draw.ellipse(display, light_grey, pong)

        pygame.display.flip()


if __name__ == '__main__':
    main()
