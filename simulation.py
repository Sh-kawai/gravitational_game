import pygame
import random
import math
from constants import *

class ParticleA:
    def __init__(self, x, y, mass=A_MASS):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = A_RADIUS
    
    def update_position(self):
        self.x, self.y = pygame.mouse.get_pos()

    def draw(self, screen):
        pygame.draw.circle(screen, POINT_A_COLOR, (int(self.x), int(self.y)), self.radius)

class ParticleB:
    def __init__(self, x, y, vx, vy, mass=B_MASS):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.trail = []
        self.radius = B_RADIUS

    def update(self, ax, ay):
        # 速度全体を減衰
        if math.hypot(self.vx, self.vy) > DAMP_MIN_SPEED:
            self.vx *= DAMPING_FACTOR
            self.vy *= DAMPING_FACTOR

        # 速度更新
        self.vx += ax
        self.vy += ay
        self.x += self.vx
        self.y += self.vy
        
        if self.x <= 0 or self.x >= WIDTH:
            self.vx = -self.vx
        if self.y <= 0 or self.y >= HEIGHT:
            self.vy = -self.vy

        # 軌跡の更新
        self.trail.append((self.x, self.y))
        if len(self.trail) > TRAIL_LENGTH:
            self.trail.pop(0)

    def draw(self, screen):
        for i in range(len(self.trail) - 1):
            alpha = (i + 1) / TRAIL_LENGTH
            color = (
                int(POINT_B_COLOR[0] * alpha + BACKGROUND_COLOR[0] * (1 - alpha)),
                int(POINT_B_COLOR[1] * alpha + BACKGROUND_COLOR[1] * (1 - alpha)),
                int(POINT_B_COLOR[2] * alpha + BACKGROUND_COLOR[2] * (1 - alpha)),
            )
            pygame.draw.aaline(screen, color, self.trail[i], self.trail[i + 1])
        pygame.draw.circle(screen, POINT_B_COLOR, (int(self.x), int(self.y)), self.radius)

class Simulation:
    def __init__(self, num_particles_a, num_particles_b, game_time=GAME_TIME, a_mass=A_MASS, damping_factor=DAMPING_FACTOR):
        self.particles_a = []
        self.particles_b = []
        self.num_particles_b = num_particles_b
        self.score = 0
        self.game_over = False
        self.game_time = game_time
        self.start_time = 0  # ゲーム開始時刻
        self.elapsed_time = 0  # 経過時間
        self.a_mass = a_mass
        self.damping_factor = damping_factor

        self.create_particles_a(num_particles_a)
        self.create_particles_b()

    def create_particles_a(self, num=1):
        for _ in range(num):
            self.particles_a.append(ParticleA(random.uniform(WIDTH // 4, 3 * WIDTH // 4),random.uniform(HEIGHT // 4, 3 * HEIGHT // 4), mass=self.a_mass))

    def create_particles_b(self):
        self.particles_b = []
        for _ in range(self.num_particles_b):
            self.particles_b.append(self._create_particle_b())

    def _create_particle_b(self):
        b_x = random.uniform(0, WIDTH)
        b_y = random.uniform(0, HEIGHT)
        b_vx = random.uniform(-2, 2)
        b_vy = random.uniform(-2, 2)
        return ParticleB(b_x, b_y, b_vx, b_vy)

    def update(self):
        if not self.game_over:
            self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000

            if self.elapsed_time >= self.game_time or not self.particles_b:
                self.game_over = True

            for particle_a in self.particles_a:
                particle_a.update_position()
            
            for particle_b in self.particles_b[:]:
                ax, ay = 0, 0
                for particle_a in self.particles_a:
                    dx = particle_a.x - particle_b.x
                    dy = particle_a.y - particle_b.y
                    distance = math.hypot(dx, dy)

                    if distance < CONSUME_DISTANCE:
                        particle_a.mass += particle_b.mass  # 質点Aの質量を増加
                        self.particles_b.remove(particle_b)
                        self.score += 1  # スコアを増やす
                        break
                    else:
                        if distance > 0:
                            force = G * particle_a.mass * particle_b.mass / distance**2
                            ax += force * dx / distance / particle_b.mass
                            ay += force * dy / distance / particle_b.mass

                particle_b.update(ax, ay)

    def draw(self, screen):
        for particle_a in self.particles_a:
            particle_a.draw(screen)
        for particle_b in self.particles_b:
            particle_b.draw(screen)
