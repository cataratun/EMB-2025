import pygame
import random

#Inicializar pygame
pygame.init()

#Configurar pantalla completa
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

#Colores
NEGRO = (0, 0, 0)
AZUL = (0, 162, 232)

#Reloj para controlar FPS
clock = pygame.time.Clock()

#Clase para los ojos animados
class Eyes:
    def init(self):
    # Posición de los ojos
        self.x = width // 2
        self.y = height // 3
        # Tamaño de los ojos
        self.eye_width = width // 4
        self.eye_height = height // 10
        # Estado inicial
        self.state = "open"
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_speed = 50 # Ajuste de velocidad para mayor fluidez
        self.expressions = ["open", "blink", "angry", "happy", "surprised"]

def draw(self):
    """Dibuja los ojos en la pantalla dependiendo de su estado actual."""
    if self.state == "open":
        pygame.draw.rect(screen, AZUL, (self.x - self.eye_width - 30, self.y, self.eye_width, self.eye_height), border_radius=10)
        pygame.draw.rect(screen, AZUL, (self.x + 30, self.y, self.eye_width, self.eye_height), border_radius=10)
    elif self.state == "blink":
        if self.frame < 5:
            pygame.draw.rect(screen, AZUL, (self.x - self.eye_width - 30, self.y, self.eye_width, max(5, self.eye_height - self.frame * 3)), border_radius=10)
            pygame.draw.rect(screen, AZUL, (self.x + 30, self.y, self.eye_width, max(5, self.eye_height - self.frame * 3)), border_radius=10)
        else:
            self.state = "open"
            self.frame = 0
    elif self.state == "angry":
        pygame.draw.rect(screen, AZUL, (self.x - self.eye_width - 30, self.y - 10, self.eye_width, self.eye_height), border_radius=10)
        pygame.draw.rect(screen, AZUL, (self.x + 30, self.y - 10, self.eye_width, self.eye_height), border_radius=10)
    elif self.state == "happy":
        pygame.draw.rect(screen, AZUL, (self.x - self.eye_width - 30, self.y + 10, self.eye_width, self.eye_height), border_radius=10)
        pygame.draw.rect(screen, AZUL, (self.x + 30, self.y + 10, self.eye_width, self.eye_height), border_radius=10)
    elif self.state == "surprised":
        pygame.draw.rect(screen, AZUL, (self.x - self.eye_width - 30, self.y, self.eye_width, self.eye_width), border_radius=20)
        pygame.draw.rect(screen, AZUL, (self.x + 30, self.y, self.eye_width, self.eye_width), border_radius=20)

def update(self):
    """Controla la animación y los cambios de estado de los ojos."""
    now = pygame.time.get_ticks()
    if now - self.last_update > self.animation_speed:
        self.last_update = now
        if self.state == "blink":
            self.frame += 1
        elif random.random() < 0.07:  # Aumentar la probabilidad de cambiar de expresión
            self.state = random.choice(self.expressions)
            self.frame = 0

#Crear instancia de los ojos
eyes = Eyes()

#Bucle principal del programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key in [pygame.K_ESCAPE, pygame.K_q]):
            running = False

# Limpiar pantalla con color negro
screen.fill(NEGRO)

# Actualizar y dibujar ojos
eyes.update()
eyes.draw()

# Actualizar pantalla
pygame.display.flip()
clock.tick(30)
pygame.quit()

