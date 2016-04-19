"""
FinalProject.py
Author: Avery Wallis
Sources: Hayden Hatfield

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
skin =Color(0xFCD15B, 1.0)
wall=Color(0xE8E8E8, 1.0)
orange=Color(0xFFa500,1.0)
plat=Color(0xB9BDBB,1.0)
gooy=Color(0xCDF238,1.0)
white=Color(0xFFFFFF,1.0)
darkblue=Color(0x052099,1.0)

thinline= LineStyle(1, black)
thickline= LineStyle(5, black)
thickishline= LineStyle(2.5, black)
noline=LineStyle(0, black)
portalline=LineStyle(1, blue)
portalline2=LineStyle(1, orange)

wall=RectangleAsset(500,500, noline, wall)
blueportal=EllipseAsset(27, 60, noline, blue)
orangeportal=EllipseAsset(27, 60, noline, orange)
innerportal=EllipseAsset(24, 57, noline, white)
exit=CircleAsset(70, thinline, plat)
exit2=CircleAsset(20, thinline, plat)
plat=RectangleAsset(250, 50, noline, plat)
doorline=LineAsset(0, 120, thinline)
goo=PolygonAsset([(0,500),(800,500),(800,600,),(0,600)],noline,gooy)

class Chell(Sprite):
    asset = ImageAsset("images/Chell.png")
    def __init__(self, position):
        super().__init__(Chell.asset, position)
        self.visible = True
        self.x = 250
        self.y = 250
        self.click = 0
        self.mright = 0
        PortalGame.listenKeyEvent("keydown", "d", self.rightOn)
        PortalGame.listenKeyEvent("keyup", "d", self.rightOff)
        PortalGame.listenKeyEvent("keydown", "a", self.leftOn)
        PortalGame.listenKeyEvent("keyup", "a", self.leftOff)
        PortalGame.listenMouseEvent("click", self.ClickOn)
        
    def step(self):
        if self.click == 1:
            self.x = 500
            self.y = 500
        if self.mright == 1:
            self.x += 1
            self.y = self.y
        if self.mright == 0:
            self.x =self.x
            self.y=self.y
            
    def ClickOn(self,event):
        self.click = 1
    def rightOn(self,event):
        self.mright = 1
    def rightOff(self,event):
        self.mright = 0
    def leftOn(self,event):
        self.mleft = 1
    def leftOff(self,event):
        self.mleft = 0

class PortalGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Sprite(wall, (400,20))
        Sprite(wall, (100,20))
        Sprite(exit, (800,100))
        Sprite(exit2, (800, 100))
        Sprite(doorline, (800, 30))
        Sprite(plat, (100,400))
        Sprite(plat, (650, 150))
        Sprite(orangeportal, (700,90))
        Sprite(innerportal, (700,90))
        Sprite(blueportal, (200,340))
        Sprite(innerportal, (200,340))
        Sprite(goo, (100,0))
        Chell((0,0))
        
    def step(self):
        for chell in self.getSpritesbyClass(Chell):
            chell.step()
            
myapp = PortalGame(1000,750)
myapp.run()