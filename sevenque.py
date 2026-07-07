import pygame
from tkinter import messagebox

class UpsMonitor:
    def __init__(self, start_charge):
        self.charge = float(start_charge)
        
    def start_animation(self):
        pygame.init()
        screen = pygame.display.set_mode((300, 400))
        pygame.display.set_caption("Индикатор заряда")
        clock = pygame.time.Clock()
        
        DECREASE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(DECREASE_EVENT, 1000)
        
        is_running = True
        flash_visible = True
        flash_timer = 0

        while is_running:
            dt = clock.tick(60) 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                
                if event.type == DECREASE_EVENT and self.charge > 0:
                    self.charge -= 5
                    if self.charge <= 0:
                        self.charge = 0
                        messagebox.showwarning("Внимание", "Аккумулятор полностью разряжен!")

            if self.charge < 20:
                flash_timer += dt
                if flash_timer >= 500:
                    flash_visible = not flash_visible
                    flash_timer = 0
            else:
                flash_visible = True

            if self.charge > 50:
                color = (0, 255, 0)      
            elif 20 <= self.charge <= 50:
                color = (255, 255, 0)  
            else:
                color = (255, 0, 0) if flash_visible else (240, 240, 240)

            screen.fill((240, 240, 240))

            pygame.draw.rect(screen, (0, 0, 0), (100, 80, 100, 250), 5)
            pygame.draw.rect(screen, (0, 0, 0), (130, 60, 40, 20))

            if self.charge > 0:
                fill_height = int((self.charge / 100) * 240)
                fill_y = 85 + (240 - fill_height)
                pygame.draw.rect(screen, color, (105, fill_y, 90, fill_height))

            pygame.display.flip()

        pygame.quit()
