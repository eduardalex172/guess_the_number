"""Simple tank app rendering a tank driving across a field using pygame."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Tuple

import pygame

# Screen configuration
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60
FIELD_COLOR = (38, 115, 38)
FIELD_LINE_COLOR = (60, 150, 60)
FIELD_LINE_SPACING = 60

TANK_BODY_COLOR = (50, 50, 55)
TANK_TURRET_COLOR = (80, 80, 85)
TANK_BARREL_COLOR = (120, 120, 125)


@dataclass
class Tank:
    """Small helper class to keep the tank state together."""

    position: pygame.math.Vector2
    angle: float = 0.0
    speed: float = 0.0

    def update(self, pressed_keys: Tuple[bool, ...]) -> None:
        """Update the tank position and rotation based on input."""

        rotation_speed = 120  # degrees per second
        acceleration = 400
        friction = 0.9

        dt = 1.0 / FPS

        if pressed_keys[pygame.K_LEFT]:
            self.angle += rotation_speed * dt
        if pressed_keys[pygame.K_RIGHT]:
            self.angle -= rotation_speed * dt
        if pressed_keys[pygame.K_UP]:
            self.speed = min(self.speed + acceleration * dt, 180)
        if pressed_keys[pygame.K_DOWN]:
            self.speed = max(self.speed - acceleration * dt, -140)

        self.speed *= friction

        radians = math.radians(self.angle)
        direction = pygame.math.Vector2(-math.sin(radians), -math.cos(radians))
        self.position += direction * self.speed * dt

        # Keep the tank inside the bounds of the screen with a small margin
        margin = 40
        self.position.x = max(margin, min(SCREEN_WIDTH - margin, self.position.x))
        self.position.y = max(margin, min(SCREEN_HEIGHT - margin, self.position.y))

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the tank body, turret, and barrel on the surface."""

        body_width, body_height = 80, 50
        turret_radius = 18
        barrel_length = 45
        barrel_width = 8

        body_surface = pygame.Surface((body_width, body_height), pygame.SRCALPHA)
        pygame.draw.rect(body_surface, TANK_BODY_COLOR, (0, 0, body_width, body_height), border_radius=8)

        rotated_body = pygame.transform.rotate(body_surface, self.angle)
        body_rect = rotated_body.get_rect(center=self.position)
        surface.blit(rotated_body, body_rect)

        turret_center = self.position
        pygame.draw.circle(surface, TANK_TURRET_COLOR, turret_center, turret_radius)

        radians = math.radians(self.angle)
        barrel_vector = pygame.math.Vector2(-math.sin(radians), -math.cos(radians)) * barrel_length
        barrel_end = turret_center + barrel_vector

        pygame.draw.line(surface, TANK_BARREL_COLOR, turret_center, barrel_end, barrel_width)


def draw_field(surface: pygame.Surface) -> None:
    """Render a grassy field with faint mowing lines to give the tank a playground."""

    surface.fill(FIELD_COLOR)

    for offset in range(0, SCREEN_WIDTH + FIELD_LINE_SPACING, FIELD_LINE_SPACING):
        pygame.draw.line(
            surface,
            FIELD_LINE_COLOR,
            (offset, 0),
            (offset - SCREEN_HEIGHT // 3, SCREEN_HEIGHT),
            2,
        )


def main() -> None:
    """Run the tank visualisation loop."""

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tank on a Field")
    clock = pygame.time.Clock()

    tank = Tank(position=pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()
        tank.update(pressed_keys)

        draw_field(screen)
        tank.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
