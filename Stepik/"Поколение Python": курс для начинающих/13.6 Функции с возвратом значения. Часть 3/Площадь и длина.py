def get_circle(radius):
    import math
    return 2 * radius * math.pi, radius ** 2 * math.pi

print(get_circle(1.5))