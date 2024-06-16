import pygame
from constants import GAME_TIME, A_MASS, DAMPING_FACTOR, WHITE, WIDTH, HEIGHT, POINT_A_COLOR

class Setting:
    def __init__(self):
        self.game_time_font = pygame.font.Font(None, 64)
        self.game_time_text = self.game_time_font.render(f"GAME_TIME:{GAME_TIME}", True, WHITE)
        self.game_time_rect = self.game_time_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))

        self.a_mass_font = pygame.font.Font(None, 64)
        self.a_mass_text = self.a_mass_font.render(f"A_MASS:{A_MASS}", True, WHITE)
        self.a_mass_rect = self.a_mass_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        
        self.damping_factor_font = pygame.font.Font(None, 64)
        self.damping_factor_text = self.damping_factor_font.render(f"DAMPING_FACTOR:{DAMPING_FACTOR}", True, WHITE)
        self.damping_factor_rect = self.damping_factor_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    def update(self):
        self.game_time_text = self.game_time_font.render(f"GAME_TIME:{GAME_TIME}", True, WHITE)
        self.a_mass_text = self.a_mass_font.render(f"A_MASS:{A_MASS}", True, WHITE)
        self.damping_factor_text = self.damping_factor_font.render(f"DAMPING_FACTOR:{DAMPING_FACTOR}", True, WHITE)
    def draw(self, screen):
        pygame.draw.rect(screen, POINT_A_COLOR, self.game_time_rect)
        screen.blit(self.game_time_text, self.game_time_rect.topleft)
        pygame.draw.rect(screen, POINT_A_COLOR, self.a_mass_rect)
        screen.blit(self.a_mass_text, self.a_mass_rect.topleft)
        pygame.draw.rect(screen, POINT_A_COLOR, self.damping_factor_rect)
        screen.blit(self.damping_factor_text, self.damping_factor_rect.topleft)
        
if __name__ == "__main__":
    # 設定値の表示
    print("Current Game Settings:")
    print(f"Game Time: {GAME_TIME} seconds")
    print(f"A Mass: {A_MASS}")
    print(f"Damping Factor: {DAMPING_FACTOR}")

    # 新しい設定値の入力
    GAME_TIME = int(input("Enter game time (seconds): "))
    A_MASS = int(input("Enter mass of particle A: "))
    DAMPING_FACTOR = float(input("Enter damping factor: "))

    # 設定値の表示
    print("RESET Game Settings:")
    print(f"Game Time: {GAME_TIME} seconds")
    print(f"A Mass: {A_MASS}")
    print(f"Damping Factor: {DAMPING_FACTOR}")