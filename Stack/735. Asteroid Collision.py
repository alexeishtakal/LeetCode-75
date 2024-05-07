class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        new_asteroids = []
        while asteroids:
            a = asteroids.pop()
            if len(new_asteroids)>0:
                n = new_asteroids.pop()
                if (a>0 and n<0):
                    if abs(a) < abs(n):
                        new_asteroids.append(n)
                    elif abs(a) > abs(n):
                        asteroids.append(a)
                else:
                    new_asteroids.append(n)
                    new_asteroids.append(a)
            else:
                new_asteroids.append(a)
        new_asteroids.reverse()
        return new_asteroids