"""screens/menu_screen.py – start menu with the bonus legend."""

import pygame

from game import audio
import settings as cfg
from game import ui
from game.entities import Bonus

BONUS_DESCRIPTIONS = {
    "extend": "Wider paddle",
    "multiball": "Two extra balls",
    "laser": "Laser paddle (SPACE to shoot)",
    "extra_life": "Extra life",
    "shrink": "Narrower paddle",
    "speed_up": "Faster balls",
    "speed_down": "Slower balls",
}


def run(screen: pygame.Surface, clock: pygame.time.Clock) -> bool:
    """ Shows the start menu. Returns True to start the game, False to quit. """
    title_font = pygame.font.Font(None, 96)
    text_font = pygame.font.Font(None, 32)
    small_font = pygame.font.Font(None, 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    audio.play("bonus")
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False

        ui.draw_gradient_background(screen)
        ui.draw_frame(screen)

        # Glowing title (soft double-render for a neon effect)
        glow = title_font.render("BLOCK BLASTER", True, cfg.ACCENT)
        glow_rect = glow.get_rect(center=(cfg.WIDTH // 2 + 2, 112))
        screen.blit(glow, glow_rect)
        title = title_font.render("BLOCK BLASTER", True, cfg.GOLD)
        screen.blit(title, title.get_rect(center=(cfg.WIDTH // 2, 110)))

        # Bonus legend, shown in a two-column panel
        panel_rect = pygame.Rect(cfg.WIDTH // 2 - 220, 175, 440, 200)
        ui.draw_panel(screen, panel_rect)
        header = text_font.render("Bonuses", True, cfg.WHITE)
        screen.blit(header, header.get_rect(midtop=(panel_rect.centerx, panel_rect.top + 10)))

        col_width = panel_rect.width // 2
        items = list(Bonus.TYPES.items())
        for index, (bonus_type, props) in enumerate(items):
            col = index // 4
            row = index % 4
            x = panel_rect.left + 16 + col * col_width
            y = panel_rect.top + 50 + row * 34
            icon = pygame.Rect(x, y, 22, 22)
            pygame.draw.rect(screen, props["color"], icon, border_radius=6)
            letter = small_font.render(props["letter"], True, cfg.BLACK)
            screen.blit(letter, letter.get_rect(center=icon.center))
            line = small_font.render(BONUS_DESCRIPTIONS[bonus_type], True, cfg.WHITE)
            screen.blit(line, (icon.right + 10, y + 2))

        if pygame.time.get_ticks() % 1000 < 600:  # Blinking prompt
            prompt = text_font.render("Press ENTER to start", True, cfg.GOLD)
            screen.blit(prompt, prompt.get_rect(center=(cfg.WIDTH // 2, cfg.HEIGHT - 90)))
        hint = small_font.render(
            "Arrows: move    SPACE: laser    ESC: menu / quit", True, cfg.WHITE)
        screen.blit(hint, hint.get_rect(center=(cfg.WIDTH // 2, cfg.HEIGHT - 50)))

        pygame.display.flip()
        clock.tick(cfg.FPS)
