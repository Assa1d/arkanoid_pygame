"""game/ui.py – shared drawing helpers for the new visual theme."""

import pygame

import settings as cfg


def draw_gradient_background(screen: pygame.Surface) -> None:
    """ Vertical gradient background (deep violet -> midnight blue). """
    top = cfg.BG_TOP
    bottom = cfg.BG_BOTTOM
    height = screen.get_height()
    width = screen.get_width()
    for y in range(height):
        t = y / max(1, height - 1)
        color = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        pygame.draw.line(screen, color, (0, y), (width, y))


def draw_frame(screen: pygame.Surface) -> None:
    """ Neon-style border frame around the play field. """
    rect = pygame.Rect(6, 6, screen.get_width() - 12, screen.get_height() - 12)
    pygame.draw.rect(screen, cfg.ACCENT, rect, width=3, border_radius=10)


def draw_panel(screen: pygame.Surface, rect: pygame.Rect, radius: int = 10) -> None:
    """ Semi-transparent rounded panel, used for HUD/menu backdrops. """
    panel = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(panel, cfg.PANEL_BG, panel.get_rect(), border_radius=radius)
    pygame.draw.rect(panel, cfg.ACCENT, panel.get_rect(), width=2, border_radius=radius)
    screen.blit(panel, rect.topleft)
