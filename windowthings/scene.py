from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Filename


class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        winfile = "E:\\pythongeneral\\physics engine -me\\model\\treckter.obj"
        pandafile = Filename.fromOsSpecific(winfile)
        print(pandafile)
        self.disableMouse()
        
        #self.set_background_color(g=1,b=1,r=1,a=1)
        model= self.loader.loadModel(pandafile)


        model.set_pos(0,10,0)
        model.reparentTo(self.render)    



app = MyApp()
app.run()