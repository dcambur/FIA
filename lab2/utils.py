import math


class Vector:
    def __init__(self, arr=None):
        if arr is None:
            arr = []

        self.vec = arr

    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self.vec))

    def __add__(self, other):
        return Vector([x + y for x, y in zip(self.vec, other.vec)])

    def __sub__(self, other):
        return Vector([x - y for x, y in zip(self.vec, other.vec)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.vec) != len(other.vec):
                raise ArithmeticError("Vectors must have the same length")
            return sum([x * y for x, y in zip(self.vec, other.vec)])

        if isinstance(other, int) or isinstance(other, float):
            return Vector([x * other for x in self.vec])
        raise TypeError(
            "Multiplication only supported with scalar or vector types")

    def __truediv__(self, other):
        return Vector([x / other for x in self.vec])

    def __str__(self):
        return str(self.vec)

    def __repr__(self):
        return str(self.vec)

    def __abs__(self):
        return Vector([abs(self.vec[0]), abs(self.vec[1])])

    def cross_2d(self, other):
        return self.vec[0] * other.vec[1] - self.vec[1] * other.vec[0]


class Boid:
    def __init__(self, sprite):
        self.sprite = sprite
        self.position = Vector(sprite.pos)
        self.velocity = Vector(sprite.vel)
        self.radius = 100
        self.alignment_factor = 3.0
        self.separation_factor = 1.0
        self.cohesion_factor = 2.0

    def get_proximity(self, other_boid):
        return abs(self.position - other_boid.position)

    def flocking(self, sprite_group):
        self.cohesion(sprite_group)
        self.separation(sprite_group)
        self.alignment(sprite_group)

    def alignment(self, sprite_group):
        align_vec = Vector([0, 0])
        proximity_len = 0
        for sprite in sprite_group:
            if self.sprite == sprite:
                continue
            other_boid = Boid(sprite)
            proximity = self.get_proximity(other_boid)
            if proximity.vec[0] <= self.radius and proximity.vec[1] <= self.radius:
                proximity_len += 1
                # sum of velocities
                align_vec += other_boid.velocity

        if proximity_len > 0:
            # average velocity
            align_vec /= proximity_len
            align_vec /= align_vec.norm()
            self.velocity += align_vec * self.alignment_factor
            self.velocity /= self.velocity.norm()

    def separation(self, sprite_group):
        separation_vector = Vector([0, 0])
        proximity_len = 0
        for sprite in sprite_group:
            if sprite == self.sprite:
                continue

            other_boid = Boid(sprite)
            proximity = self.get_proximity(other_boid)

            if proximity.vec[0] <= self.radius and proximity.vec[1] <= self.radius:
                # calculate the separation vector
                separation_vector += (self.position - other_boid.position)
                proximity_len += 1

        if proximity_len > 0:
            # average the separation vector and apply it to the velocity
            separation_vector /= proximity_len
            self.velocity += separation_vector * self.separation_factor
            self.velocity /= self.velocity.norm()

    def cohesion(self, sprite_group):
        cohesion_vec = Vector([0, 0])
        proximity_len = 0
        for sprite in sprite_group:

            if self.sprite == sprite:
                continue

            other_boid = Boid(sprite)
            proximity = self.get_proximity(other_boid)

            if proximity.vec[0] <= self.radius and proximity.vec[1] <= self.radius:
                proximity_len += 1
                # sum of positions
                cohesion_vec += other_boid.position

        if proximity_len > 0:
            # center of mass
            cohesion_vec /= proximity_len
            # cohesion vector
            cohesion_vec -= self.position
            self.velocity += cohesion_vec * self.cohesion_factor
            self.velocity /= self.velocity.norm()

    def to_sprite(self):
        self.sprite.pos = [self.position.vec[0], self.position.vec[1]]
        self.sprite.vel = [self.velocity.vec[0], self.velocity.vec[1]]

        return self.sprite

