import pygame
import pygame.locals


class PygameController:
    """ Base Controller """

    def _run_loop(self):
        """ Base loop for any controller that needs it """
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    exit()
                elif event.type == pygame.locals.KEYDOWN:
                    return event.key
                elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return event.pos
