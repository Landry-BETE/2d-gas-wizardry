from itertools import *

import pygame

from particle import *

STARTING_BLUE_PARTICLES = 100

WIDTH = 700
HEIGHT = 700
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monoatomic Bidimensional Gas")
clock = pygame.time.Clock()


def colliding(particle, particle2):
    """checks if particles are overlaping & moving closer to one another to trigger bouncing & avoid agglomeration"""
    return np.linalg.norm(particle.pos - particle2.pos) < particle.size + particle2.size and np.inner(
        particle.speed - particle2.speed, particle.pos - particle2.pos) < 0


def energy(particles):
    """total kinetic energy up to a constant multiplier"""
    return np.sum([particle.size ** 2 * np.linalg.norm(particle.speed) ** 2 for particle in particles])


def momentum(particles):
    """total momentum up to a constant multiplier"""
    return np.sum([particle.speed * particle.size ** 2 for particle in particles], axis=0)


def elastic_collision(particle, particle2):
    """makes use of colliding() to compute speeds after eventual collision"""
    corr = np.inner(particle.speed - particle2.speed, particle.pos - particle2.pos) * (particle.pos - particle2.pos)
    corr = 2 * corr / ((particle.size ** 2 + particle2.size ** 2) * np.linalg.norm(particle.pos - particle2.pos) ** 2)
    particle.speed = particle.speed - particle2.size ** 2 * corr
    particle2.speed = particle2.speed + particle.size ** 2 * corr


def draw_environment(particles):
    """the drawing of the frame"""
    momentum_gas = momentum(particles)
    # print("U: {} | P: {} | P_wall: {}".format(energy(particles), momentum_gas, momentum_ini - momentum_gas))

    game_display.fill(WHITE)
    for particle_pair in combinations(particles, 2):
        if colliding(*particle_pair):
            elastic_collision(*particle_pair)
    for particle in particles:
        pygame.draw.circle(game_display, particle.color, np.rint(particle.pos).astype('int64'), particle.size)
        particle.move()

    pygame.display.update()


def main():
    """the game, the largest scope before global"""
    global momentum_ini
    particles = [Particle(WIDTH, HEIGHT) for i in range(STARTING_BLUE_PARTICLES)]
    momentum_ini = momentum(particles)
    print("momentum ini: {}".format(momentum_ini))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(particles)
        clock.tick(60)


if __name__ == '__main__':
    main()
