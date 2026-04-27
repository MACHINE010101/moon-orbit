# Earth-Moon Orbit Simulation

I wanted to see if I could simulate gravity from scratch using real physics — no game engine, no shortcuts. This is the result: the Moon orbiting Earth, running on actual SI values and Newtonian mechanics. Built in my free time just to see if it would work.

## Features

- Newtonian gravity simulation using real SI values
- Symplectic Euler integration for stable orbits
- Orbital trail rendering
- Console logging of distance, velocity, and total mechanical energy

## Requirements

- Python 3.x
- Pygame

```
pip install pygame
```

## Usage

```
python sim.py
```

Close the window to exit.

## Physics

| Constant | Value |
|---|---|
| Gravitational constant | 6.674 × 10⁻¹¹ N·m²/kg² |
| Earth mass | 5.972 × 10²⁴ kg |
| Moon mass | 7.348 × 10²² kg |
| Initial orbital velocity | 1022 m/s |
| Time scale | 1000 seconds / frame |
