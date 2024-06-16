import pygame
import random

# 花火のパーティクルを定義するクラス
class FireworkParticle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.uniform(2, 4)
        self.lifetime = random.uniform(20, 40)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.gravity = 0.05

    def update(self):
        self.vx *= 0.98
        self.vy = self.vy * 0.98 + self.gravity
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

# 花火のアニメーションを管理するクラス
class Firework:
    def __init__(self, x, y):
        self.particles = []
        self.create_particles(x, y)

    def create_particles(self, x, y):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for _ in range(50):
            self.particles.append(FireworkParticle(x, y, color))

    def update(self):
        for particle in self.particles:
            particle.update()
        self.particles = [p for p in self.particles if p.lifetime > 0]

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
