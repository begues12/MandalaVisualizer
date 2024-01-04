from Particle import Particle
from Console import Console

class ParticleManager:
    def __init__(self, particle_config, screen_size, num_particles=10):
        Console.log("Loading particles file: " + particle_config + "\n")
        self.particles = [Particle(particle_config, screen_size) for _ in range(num_particles)]
        self.screen_size = screen_size
        Console.log("Particles loaded.")
        
    def update(self, volume_level):
        for particle in self.particles:
            particle.update(volume_level)
            
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
