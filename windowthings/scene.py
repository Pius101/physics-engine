from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        
        self.teapot = self.loader.loadModel("models/teapot")
        self.teapot.reparentTo(self.render)
        self.teapot.setPos(0,10, -1)
        self.teapot.setScale(0.5)

        # Camera setup
        self.camera.setPos(0, 10, -1)
        self.camera.lookAt(0, 10, 0)
        




app = MyApp()
app.run()