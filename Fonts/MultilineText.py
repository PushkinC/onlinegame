import pygame



def render_multiline_text(font: pygame.font.Font, text: list[str], smoothing: bool, color: tuple[str, str, str], interval=5) -> pygame.Surface:
    surfaces: list[pygame.Surface] = []
    for i in text:
        surfaces.append(font.render(i, smoothing, color))

    w = max([i.get_rect().w for i in surfaces])
    h = surfaces[0].get_rect().h
    surface = pygame.Surface((w, len(surfaces) * h + (len(surfaces) - 1) * interval), flags=pygame.SRCALPHA)
    surface.fill((0, 0, 0, 0))

    for i in range(len(surfaces)):
        surface.blit(surfaces[i], (0, i * (h + interval)))

    return surface


