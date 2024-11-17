import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        molpos=mole_image.get_rect(topleft=(0, 0))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if molpos.collidepoint(mouse_pos):
                        molpos.center = (random.randrange(16, 641, 32), random.randrange(16, 513, 32))
                #elif event.type==pygame.MOUSEBUTTONDOWN:
                    #print(event.pos)
                    #x=random.randrange(0, 640, 32)
                    #y=random.randrange(0, 512,32)
                    #screen.blit(mole_image.image(x,y))
                    #screen.blit(mole_image, mole_image.get_rect(center=(x, y)))
                    #molpos.center=(random.randrange(16, 641,32),random.randrange(16, 512,32))
            screen.fill("light green")
            #pygame.draw.line(screen, "dark blue", (32, 0), (32, 512))
            for i in range(0, 640, 32):
                pygame.draw.line(screen, "dark blue", (i, 0), (i, 512))
            for i in range(0, 512, 32):
                pygame.draw.line(screen, "dark blue", (0, i), (640, i))
            #screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            #screen.blit(mole_image, mole_image.get_rect(center=(random.randrange(0, 640), random.randrange(0, 512))))
            screen.blit(mole_image, molpos)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
