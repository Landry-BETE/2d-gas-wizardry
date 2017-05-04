from itertools import *

import numpy as np
import pygame

from particle import *

STARTING_BLUE_PARTICLES = 50

WIDTH = 400
HEIGHT = 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monoatomic Bidimensional Gas")
clock = pygame.time.Clock()


def colliding(particle, other_particle):
    """checks if particles are overlaping & moving closer to one another to trigger bouncing & avoid agglomeration"""
    overlap = np.linalg.norm(
        np.array([particle.x, particle.y]) - np.array(
            [other_particle.x, other_particle.y])) - particle.size - other_particle.size
    convergence = np.inner(np.array([particle.move_x - other_particle.move_x, particle.move_y - other_particle.move_y]),
                           np.array([particle.x - other_particle.x, particle.y - other_particle.y]))
    return overlap < 0 and convergence < 0


def energy(particles):
    """total kinetic energy up to a constant multiplier"""
    return np.sum(
        np.array([np.linalg.norm(particle.size ** 2 * np.array([particle.move_x, particle.move_y])) ** 2 for particle in
                  particles]))


def momentum(particles):
    """total momentum up to a constant multiplier"""
    return np.sum([np.array([particle.move_x, particle.move_y]) * particle.size ** 2 for particle in particles], axis=0)


def elastic_collision(particle, other_particle):
    """makes use of colliding() to compute speeds after eventual collision"""
    if colliding(particle, other_particle):
        corr = 2 * np.inner(np.array([particle.move_x - other_particle.move_x,
                                      particle.move_y - other_particle.move_y]),
                            np.array([particle.x - other_particle.x,
                                      particle.y - other_particle.y]))

        corr = np.divide(corr, np.linalg.norm(np.array([particle.x - other_particle.x,
                                                        particle.y - other_particle.y])) ** 2)

        corr = corr / (particle.size ** 2 + other_particle.size ** 2)

        particle.move_x, particle.move_y = np.array([particle.move_x, particle.move_y]) \
                                           - other_particle.size ** 2 \
                                             * corr \
                                             * np.array([particle.x - other_particle.x, particle.y - other_particle.y])

        other_particle.move_x, other_particle.move_y = np.array([other_particle.move_x,
                                                                 other_particle.move_y]) \
                                                       - particle.size ** 2 \
                                                         * corr \
                                                         * np.array([other_particle.x - particle.x,
                                                                     other_particle.y - particle.y])


def draw_environment(particles):
    """the drawing of the frame"""
    momentum_gas = momentum(particles)
    print("energy: {} \n  momentum of gas: {} \n momentum absorbed by wall: {}".format(energy(particles), momentum_gas,
                                                                                       momentum_ini - momentum_gas))

    game_display.fill(WHITE)

    for particle_pair in combinations(particles, 2):
        elastic_collision(*particle_pair)
    for particle in particles:
        pygame.draw.circle(game_display, particle.color,
                           np.rint([particle.x, particle.y]).astype(int),
                           particle.size)
        particle.move()

    pygame.display.update()


def main():
    """the game, the largest scope before global"""
    global momentum_ini
    particles = [Particle(WIDTH, HEIGHT) for i in range(STARTING_BLUE_PARTICLES)]
    particles.append(Particle(WIDTH, HEIGHT, RED))
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
