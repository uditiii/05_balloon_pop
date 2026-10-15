"""
Balloon Pop (Lab Starter)

Run with:  python3 main.py

Click balloons to pop them before they reach the bottom.
"""

import pygame

from game.game_engine import GameEngine, FPS
from game.renderer import WINDOW_SIZE


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Balloon Pop")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 22)

    engine = GameEngine()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                engine.handle_click(event.pos)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                engine.try_restart()

        engine.update()
        engine.draw(screen, font)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
