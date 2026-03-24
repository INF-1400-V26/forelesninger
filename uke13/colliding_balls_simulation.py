"""
Simulation of colliding balls with Pygame.

An initial draft was made using Claude Haiku 4.5.

Extension to additional classes, refactoring of methods and use of NumPy for vectors
have been done by MHS.

"""

import numpy as np

import pygame

# Initialize all pygame modules that need initializing (e.g. display)
pygame.init()

# Constants for 8-bit RGB color values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 0)
GREEN = (50, 255, 50)
BLUE = (0, 100, 255)


class Ball:
    def __init__(
        self,
        pos: tuple[float, float],
        vel: tuple[float, float],
        radius: int,
        mass: float,
        color: tuple[int, int],
    ):
        """Initialize ball"""
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.radius = radius
        self.mass = mass
        self.color = color

    def update(self, width: int, height: int):
        """Update position, handle potential wall bounces"""
        self.pos += self.vel  # s = s0 + v*dt
        self.wall_bounce(width, height)

    def wall_bounce(self, width: int, height: int, coefficient_of_restituion: float = 1.0):
        """Check for wall collisions and update velocity accordingly

        Parameters
        ----------
        width, height : int
            Width and height of "world" (screen)
        coefficient_of_restituion : float, optional
            Number between 0 (soft) and 1 (hard)
        """
        x, y = self.pos
        if (x - self.radius) < 0 or (x + self.radius) > width:
            self.vel[0] = -self.vel[0] * coefficient_of_restituion  # Flip horizontal vel.
        if (y - self.radius) < 0 or (y + self.radius) > height:
            self.vel[1] = -self.vel[1] * coefficient_of_restituion  # Flip vertical vel.

    def draw(self, surface: pygame.Surface):
        """Draw ball on surface"""
        pygame.draw.circle(surface, self.color, self.pos.astype(int), self.radius)  # type:ignore

    def distance_to(self, other_ball: "Ball") -> float:
        """Calculate relative distance to another ball"""
        return np.sqrt(np.sum((other_ball.pos - self.pos) ** 2))  # Pythagorean distance

    def impulse(self, other_ball: "Ball", rel_vel_proj: float) -> float:
        """Impulse for elastic collision"""
        return 2 * ((self.mass * other_ball.mass) / (self.mass + other_ball.mass)) * rel_vel_proj

    def collide(self, other_ball: "Ball"):
        """Collide with other ball - update velocities for both balls"""
        dist = self.distance_to(other_ball)
        if dist == 0:
            return  # Zero distance

        # Calc. normal (unit) vector pointing from self to other
        norm_vec = (other_ball.pos - self.pos) / dist

        # Calculate relative velocity along normal
        rel_vel_proj = (other_ball.vel - self.vel) @ norm_vec  # Dot product
        if rel_vel_proj > 0:
            return  # Balls are already moving apart, don't change velocity

        # Calculate impulse, i.e. change in momentum
        # See https://en.wikipedia.org/wiki/Inelastic_collision#Formula
        impulse = self.impulse(other_ball, float(rel_vel_proj))

        # Update velocities - add/subtract velocity component along normal vector
        self.vel += (impulse / self.mass) * (norm_vec)
        other_ball.vel -= (impulse / other_ball.mass) * (norm_vec)


class Simulation:
    def __init__(
        self,
        n_balls: int,
        vel_range: float,
        ball_radius: int,
        ball_color: tuple[int, int, int] = BLUE,
        fps: float = 60.0,
        width: int = 800,
        height: int = 600,
    ):
        """Initialize simulation object"""
        self.fps = fps
        self.height = height
        self.width = width
        self.balls = self.create_balls(n_balls, vel_range, ball_radius, ball_color)

    def _random_positions(self, n_balls, ball_radius):
        """Create random valid ball posiitions"""
        rng = np.random.default_rng()
        x = rng.uniform(low=ball_radius, high=self.width - ball_radius, size=(n_balls, 1))
        y = rng.uniform(low=ball_radius, high=self.height - ball_radius, size=(n_balls, 1))
        return np.hstack((x, y))

    def _random_velocities(self, n_balls, vel_range):
        """Create random velocities within specified velocity range"""
        return np.random.uniform(low=-vel_range, high=vel_range, size=(n_balls, 2))

    def create_balls(
        self, n_balls: int, vel_range: float, radius: int, color: tuple[int, int, int]
    ) -> list[Ball]:
        """Create balls for simulation

        Parameters
        ----------
        n_balls : int
            Number of balls
        vel_range : float
            Maximum absolute value of velocity along one axis
        radius : int
            Radius of each ball
        color : tuple[int,int,int]
            RGB values describing ball color

        Returns
        -------
        list[Ball]
        """
        positions = self._random_positions(n_balls, radius)
        velocities = self._random_velocities(n_balls, vel_range)

        balls = [
            Ball(pos=pos, vel=vel, radius=radius, mass=radius**2, color=color)
            for (pos, vel) in zip(positions, velocities)
        ]
        return balls

    def update(self):
        """Update all balls and handle collisions between balls"""
        for ball in self.balls:
            ball.update(self.width, self.height)
        self._handle_collisions()

    def _handle_collisions(self):
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball_a, ball_b = self.balls[i], self.balls[j]
                if ball_a.distance_to(ball_b) <= (ball_a.radius + ball_b.radius):
                    ball_a.collide(ball_b)

    def draw(self):
        """Draw surface and all balls"""
        self.surface.fill(WHITE)
        for ball in self.balls:
            ball.draw(self.surface)

    def run(self):
        """Initialize pygame components and run simulation in loop"""
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ball Collision Simulation")
        self.clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.draw()
            pygame.display.flip()  # Update entire screen
            self.clock.tick(self.fps)

        pygame.quit()


if __name__ == "__main__":
    sim = Simulation(n_balls=30, vel_range=5, ball_radius=10)
    sim.run()
