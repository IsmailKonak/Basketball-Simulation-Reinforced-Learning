import math
import pygame
import time


# Basketball game simulation.
class Simulation():
    def __init__(self):
        width, height = 640,480
        self.background = pygame.image.load("Images/basket.png")
        self.screen = pygame.display.set_mode((width, height))
        self.screen.blit(self.background,(0,0))
        pygame.display.set_caption("Basketball Game Simulation")
        
        self.ball = pygame.image.load("Images/ball.png")
        self.ball = pygame.transform.scale(self.ball,(40,40))
        self.curry = pygame.image.load("Images/curry.png")
        self.curry = pygame.transform.scale(self.curry, (150,200))
    
    # Physical calculations of the game.
    def calculations(self,alpha):
        self.V = 110
        self.g = 10
        self.angle = math.radians(alpha)
        self.Vx = self.V * math.cos(self.angle)
        self.Vy = self.V * math.sin(self.angle)
        self.max_h = round((self.Vy**2)/(2*self.g))
        self.t = ((2*self.max_h)/(self.g))**(1/2)
        self.max_x = round(self.Vx*self.t)
        self.fpsx = self.t/self.max_x+(0.11)
        
    # Calculation of the parabola the ball will travel.    
    def parabole(self,x):
        a = (self.max_h/(self.max_x/2 - 0)*(self.max_x/2 - self.max_x))**-1
        return -a*(x)*(x-self.max_x)
    
    def main(self,angle):
        angle = 90 - angle        
        self.calculations(angle)
        centerx = 50
        for x in range(50,self.max_x+50,1):
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.curry,(-10,350))
            self.calculations(angle)
            centerx = x
            centery = 420+int(self.parabole(x))
            time.sleep(self.fpsx/100)
            self.screen.blit(self.ball, (centerx,centery))
            pygame.display.update()
        
            
    def info(self):
        print("Angle: "+str(math.degrees(self.angle)))
        print("Vx Speed: "+str(self.Vx))
        print("Vy Speed: "+str(self.Vy))
        print("Max X: "+str(self.max_x-60))
        print("Max Height: "+str(self.max_h-30))
        print("Time: "+str(self.t))
        print("\n")
        
    def quite(self):
        pygame.quit()
        
sim = Simulation()
throw_angle = 48 
sim.main(throw_angle)
sim.info()
sim.quite()