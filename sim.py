import pygame
from collections import deque
trail = deque(maxlen=500)
import math

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

sim_time = 0

# Constants
GRAVITATIONAL_CONSTANT = 6.674e-11 # N·m²/kg²
SCALE = 1_000_000 # 1 pixel = 1,000,000 meters
TIME_SCALE = 1000 #1 frame = 1000 seconds

# Earth and moon attributes in SI (kg, meters)
earth_color = (0, 0, 160)
earth_radius = 100
earth_mass = 5.972e24
earth_x = 960e6
earth_y = 540e6

moon_color = (148, 144, 141)
moon_radius = 25
moon_mass = 7.348e22
moon_vx = 0.0
moon_vy = 1022.0 
moon_x = 576e6
moon_y = 540e6

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Framerate Independence
    dt = TIME_SCALE

    # Space
    screen.fill((5, 9, 21))

    # Calculate r
    r = math.sqrt(pow(earth_x - moon_x, 2) + pow(earth_y - moon_y, 2))

    # Direction
    d = ((earth_x - moon_x), (earth_y - moon_y))

    d_norm = ((d[0] / r), (d[1] / r))

    # Gravitational Force
    f = GRAVITATIONAL_CONSTANT * (earth_mass * moon_mass) / pow(r, 2)

    # Moon Acceleration Magnitude
    a = f / moon_mass

    # Moon Acceleration
    moon_a = ((a * d_norm[0]), (a * d_norm[1]))
    
    # Moon Velocity
    moon_vx += moon_a[0] * dt
    moon_vy += moon_a[1] * dt

    # Moon New Position
    moon_x += moon_vx * dt
    moon_y += moon_vy * dt

    # Convert positions to pixels
    earth_x_px = earth_x / SCALE
    earth_y_px = earth_y / SCALE
    moon_x_px = moon_x / SCALE
    moon_y_px = moon_y / SCALE

    # Logging
    sim_time += dt
    if sim_time % 86400 < dt:  # roughly once per simulated day
        orbital_speed = math.sqrt(moon_vx**2 + moon_vy**2)
        ke = 0.5 * moon_mass * orbital_speed**2
        pe = -GRAVITATIONAL_CONSTANT * earth_mass * moon_mass / r
        print(f"Day {sim_time/86400:.1f} | r: {r/1e6:.0f} km | v: {orbital_speed:.1f} m/s | E: {ke+pe:.3e} J")

    # Trail
    trail.append((int(moon_x_px), int(moon_y_px)))
    for pos in trail:
        pygame.draw.circle(screen, (80, 78, 76), pos, 2)
    
    # Earth
    pygame.draw.circle(screen, earth_color, (int(earth_x_px), int(earth_y_px)), earth_radius)

    # Moon
    pygame.draw.circle(screen, moon_color, (int(moon_x_px), int(moon_y_px)), moon_radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()