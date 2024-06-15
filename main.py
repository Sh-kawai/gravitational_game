import pygame
from simulation import Simulation
from constants import WIDTH, HEIGHT, BACKGROUND_COLOR, POINT_A_COLOR, WHITE, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravitational Game")
    clock = pygame.time.Clock()

    start_button_font = pygame.font.Font(None, 64)
    start_button_text = start_button_font.render("START", True, WHITE)
    start_button_rect = start_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    restart_button_font = pygame.font.Font(None, 64)
    restart_button_text = restart_button_font.render("RESTART", True, WHITE)
    restart_button_rect = restart_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    running = True
    game_started = False
    sim = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
                if start_button_rect.collidepoint(event.pos):
                    game_started = True
                    sim = Simulation(1, 100)
                    sim.start_time = pygame.time.get_ticks()
            elif event.type == pygame.MOUSEBUTTONDOWN and game_started and sim.game_over:
                if restart_button_rect.collidepoint(event.pos):
                    game_started = True
                    sim = Simulation(1, 100)
                    sim.start_time = pygame.time.get_ticks()

        if sim:
            sim.update()

        screen.fill(BACKGROUND_COLOR)
        if not game_started:
            pygame.draw.rect(screen, POINT_A_COLOR, start_button_rect)
            screen.blit(start_button_text, start_button_rect.topleft)
        else:
            sim.draw(screen)
            if sim.game_over:
                game_over_font = pygame.font.Font(None, 72)
                game_over_text = game_over_font.render("GAME OVER", True, WHITE)
                game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
                final_score_text = restart_button_font.render(f"Final Score: {sim.score}", True, WHITE)
                final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))

                screen.blit(game_over_text, game_over_rect.topleft)
                screen.blit(final_score_text, final_score_rect.topleft)
                pygame.draw.rect(screen, POINT_A_COLOR, restart_button_rect)
                screen.blit(restart_button_text, restart_button_rect.topleft)
            else:
                font = pygame.font.Font(None, 36)
                score_text = font.render(f"Score: {sim.score}", True, WHITE)
                time_text = font.render(f"Time: {int(sim.game_time - sim.elapsed_time)}", True, WHITE)
                screen.blit(score_text, (20, 20))
                screen.blit(time_text, (20, 60))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
