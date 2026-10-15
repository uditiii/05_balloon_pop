"""
GameEngine: owns all balloons, spawns new ones, and handles clicks.

Features: three balloon types (normal / bonus / penalty), a 3-lives
system, and a 30-second timed round with a game-over screen and restart.
"""

import random

from game.balloon import Balloon, BALLOON_TYPES
from game.click_detection import check_pop
from game.renderer import WIDTH, HEIGHT

FPS = 60
SPAWN_INTERVAL_FRAMES = 45
STARTING_LIVES = 3
ROUND_SECONDS = 30
ROUND_FRAMES = ROUND_SECONDS * FPS
# Short pause after game over so a frantic last click doesn't restart instantly.
RESTART_DELAY_FRAMES = 30


class GameEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        self.balloons = []
        self.frames_until_spawn = 0
        self.score = 0
        self.lives = STARTING_LIVES
        self.frames_left = ROUND_FRAMES
        self.game_over = False
        self.end_reason = ""
        self.frames_since_game_over = 0

    def _spawn_balloon(self):
        radius = random.randint(16, 44)
        x = random.randint(radius + 10, WIDTH - radius - 10)
        speed = random.uniform(1.5, 3.0)
        kinds = list(BALLOON_TYPES.keys())
        weights = [BALLOON_TYPES[k]["weight"] for k in kinds]
        kind = random.choices(kinds, weights=weights, k=1)[0]
        self.balloons.append(
            Balloon(x=x, y=-radius, radius=radius, speed=speed, kind=kind)
        )

    def _end_round(self, reason):
        self.game_over = True
        self.end_reason = reason
        self.frames_since_game_over = 0

    def try_restart(self):
        """Start a new round, but only if the current one is over."""
        if self.game_over and self.frames_since_game_over >= RESTART_DELAY_FRAMES:
            self.reset()

    def handle_click(self, pos):
        if self.game_over:
            self.try_restart()
            return
        popped = check_pop(self.balloons, pos)
        if popped is not None:
            self.balloons.remove(popped)
            # Score never drops below zero.
            self.score = max(0, self.score + popped.points)

    def update(self):
        if self.game_over:
            self.frames_since_game_over += 1
            return

        self.frames_until_spawn -= 1
        if self.frames_until_spawn <= 0:
            self._spawn_balloon()
            self.frames_until_spawn = SPAWN_INTERVAL_FRAMES

        for b in self.balloons:
            b.update()

        # Any balloon (of any type) that reaches the bottom costs one life.
        missed = [b for b in self.balloons if b.is_past_bottom(HEIGHT)]
        self.lives -= len(missed)
        self.balloons = [b for b in self.balloons if not b.is_past_bottom(HEIGHT)]

        self.frames_left -= 1

        if self.lives <= 0:
            self.lives = 0
            self._end_round("Out of lives!")
        elif self.frames_left <= 0:
            self.frames_left = 0
            self._end_round("Time's up!")

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_scene(surface, self.balloons)
        renderer.draw_text(surface, font, f"Score: {self.score}", (10, 10))
        renderer.draw_text(surface, font, f"Lives: {self.lives}", (10, 38))

        seconds_left = (self.frames_left + FPS - 1) // FPS
        timer_text = f"Time: {seconds_left}"
        timer_w = font.size(timer_text)[0]
        renderer.draw_text(surface, font, timer_text, (WIDTH - timer_w - 10, 10))

        if self.game_over:
            renderer.draw_banner(
                surface, font, f"{self.end_reason}  Final Score: {self.score}"
            )
            if self.frames_since_game_over >= RESTART_DELAY_FRAMES:
                hint = "Click or press R to play again"
                hint_w = font.size(hint)[0]
                renderer.draw_text(
                    surface, font, hint, ((WIDTH - hint_w) // 2, HEIGHT // 2 + 30)
                )
