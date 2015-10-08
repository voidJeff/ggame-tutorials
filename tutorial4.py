from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position, angle):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.lrOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rrOff)
        self.fxcenter = self.fycenter = 0.5
        self.angle = angle = 0
        
    def step(self):
        self.x -= self.vx
        self.y -= self.vy
        self.rotation += self.vr
        self.angle += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            self.x -= 2
            self.y -= 2
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        
    def thrustOn(self, event):
        self.thrust = 1
        self.vx = cos(math.pi * self.angle)

    def thrustOff(self, event):
        self.thrust = 0
        self.vx = 0
        
    def rotateLeft(self, event):
        self.vr = 0.01
        
    def lrOff(self,  event):
        self.vr = 0
        
    def rotateRight(self, event):
        self.vr = -0.01
        
    def rrOff(self,  event):
        self.vr = 0
class SpaceGame(App):
    def __init__(self, width, height, angle):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
