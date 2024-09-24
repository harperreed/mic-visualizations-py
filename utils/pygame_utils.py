import pygame

def add_glow_effect(screen):
    surf = pygame.Surface(screen.get_size())
    surf.set_colorkey((0, 0, 0))
    surf.set_alpha(20)
    pygame.draw.rect(surf, (20, 20, 20), surf.get_rect())
    screen.blit(surf, (0, 0), special_flags=pygame.BLEND_RGB_ADD)