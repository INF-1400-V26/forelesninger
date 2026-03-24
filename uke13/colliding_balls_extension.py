import numpy as np
from colliding_balls_simulation import BLUE, GREEN, RED, Ball, Simulation


class MultipleBallSizeSimulation(Simulation):
    def __init__(
        self,
        n_balls: list[int],
        vel_range: list[float],
        ball_radius: list[int],
        ball_color: list[tuple[int, int, int]],
        fps: float = 60.0,
        width: int = 800,
        height: int = 600,
    ):
        self.fps = fps
        self.height = height
        self.width = width
        self.balls = self.create_balls(n_balls, vel_range, ball_radius, ball_color)

    def create_balls(
        self,
        n_balls: list[int],
        vel_range: list[float],
        ball_radius: list[int],
        ball_color: list[tuple[int, int, int]],
    ) -> list[Ball]:
        """Create multiple types of balls"""
        balls = []
        for nb, vr, br, bc in zip(n_balls, vel_range, ball_radius, ball_color):
            balls.extend(super().create_balls(nb, vr, br, bc))
        return balls


class MergeBallsSimulation(Simulation):
    def _merge_balls(self, ball_a: Ball, ball_b: Ball):
        """Merge balls to create new ball, conserving mass and momentum"""
        merged_position = (ball_a.pos * ball_a.radius + ball_b.pos * ball_b.radius) / (
            ball_a.radius + ball_b.radius
        )
        merged_velocity = (ball_a.vel * ball_a.mass + ball_b.vel * ball_b.mass) / (
            ball_a.mass + ball_b.mass
        )
        merged_radius = int(np.sqrt(ball_a.radius**2 + ball_b.radius**2))
        merged_mass = ball_a.mass + ball_b.mass

        self.balls.append(
            Ball(
                pos=merged_position,
                vel=merged_velocity,
                radius=merged_radius,
                mass=merged_mass,
                color=ball_a.color,
            )
        )

    def _handle_collisions(self):
        """Merge balls on collision"""
        balls_to_delete = []
        n_balls_before_merging = len(self.balls)
        for i in range(n_balls_before_merging):
            for j in range(i + 1, n_balls_before_merging):
                ball_a, ball_b = self.balls[i], self.balls[j]
                if ball_a.distance_to(ball_b) <= (ball_a.radius + ball_b.radius):
                    balls_to_delete.append(ball_a)
                    balls_to_delete.append(ball_b)
                    self._merge_balls(ball_a, ball_b)

        for ball in set(balls_to_delete):  # Use set() to get unique balls
            self.balls.remove(ball)


class SoftBall(Ball):
    def __init__(
        self,
        pos: tuple[float, float],
        vel: tuple[float, float],
        radius: int,
        mass: float,
        color: tuple[int, int],
        softness: float,
    ):
        super().__init__(pos, vel, radius, mass, color)
        self.softness = softness

    def impulse(self, other_ball: Ball, rel_vel_proj):
        """Calculate impulse, taking ball softness into account"""
        if isinstance(other_ball, SoftBall):
            coefficient_of_restitution = 1 - max(self.softness, other_ball.softness)
        else:
            coefficient_of_restitution = 1 - self.softness
        return (
            (1 + coefficient_of_restitution)
            * ((self.mass * other_ball.mass) / (self.mass + other_ball.mass))
            * rel_vel_proj
        )


class SoftBallSimulation(Simulation):
    def __init__(
        self,
        n_balls: int,
        vel_range: float,
        ball_radius: int,
        ball_color: tuple[int, int, int],
        ball_softness: float,
        fps: float = 60.0,
        width: int = 800,
        height: int = 600,
    ):
        """Initialise softball simulation object"""
        self.fps = fps
        self.height = height
        self.width = width
        self.balls = self.create_balls(n_balls, vel_range, ball_radius, ball_color, ball_softness)

    def create_balls(self, n_balls, vel_range, radius, color, softness) -> list[Ball]:
        """Create set of soft balls"""
        positions = self._random_positions(n_balls, radius)
        velocities = self._random_velocities(n_balls, vel_range)

        balls = [
            SoftBall(
                pos=pos, vel=vel, radius=radius, mass=radius**2, color=color, softness=softness
            )
            for (pos, vel) in zip(positions, velocities)
        ]
        return balls


if __name__ == "__main__":
    sim = MultipleBallSizeSimulation(
        n_balls=[5, 10, 20],
        vel_range=[5, 5, 5],
        ball_radius=[20, 10, 5],
        ball_color=[RED, GREEN, BLUE],
    )
    sim.run()

    # sim = MergeBallsSimulation(
    #     n_balls=30,
    #     vel_range=5,
    #     ball_radius=10,
    #     ball_color=RED,
    # )
    # sim.run()

    # sim = SoftBallSimulation(
    #     n_balls=30, vel_range=5, ball_radius=10, ball_color=RED, ball_softness=0.5
    # )
    # sim.run()
