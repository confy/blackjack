import pygame
import pygame.locals

class PygameController:
    def _run_loop(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    exit()
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.locals.K_ESCAPE:
                        return False
                elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                    return event.pos
