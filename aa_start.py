from aa_gui import fMain
import wx 

from numpy import arange, sin, pi
import matplotlib

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar
from matplotlib.figure import Figure

class myGui(fMain):
    def __init__(self, parent):
        # If we overload __init__ we still need to make sure the parent
        # is initialized.
        fMain.__init__(self, parent)
        #super(myGui, self).__init__(parent)
        #self.m_staticText41.Hide()
        self.panel = CanvasPanel(self.panelPlot)
        self.panel.draw()
        return
    def btStartClick(self, event):
        self.statusBar.SetStatusText("test")
        return
    def cbText(self, event):
        self.statusBar.SetStatusText(self.comboBMeasType.GetStringSelection())
        
        myList = [ "test1" , "test2" ]
        self.comboBMeasUnits.Clear()
        self.comboBMeasUnits.Set(myList)
        self.comboBMeasUnits.SetValue(myList[0])
        return
    def OnQuit(self, event):
        self.Close()

    def OnDemo(self, event):
        if self.checkDemo.GetValue():
           self.panelSetup.Enable()
           self.panelMeas.Enable()
        else:
           self.panelSetup.Disable()
           self.panelMeas.Disable()

    def OnSize(self, event):
        self.Layout()
        self.statusBar.SetStatusText("niak")


class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        sizerPanel = wx.BoxSizer(wx.VERTICAL)

        wx.Panel.__init__(self, parent,size=wx.Size(806, 450))
        sizerPlot = wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour("red")

        self.GetParent().SetSizer(sizerPanel)
        sizerPanel.Add(self, 1, wx.EXPAND | wx.ALL | wx.GROW )
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        #cursor event connection to function
        self.canvas.mpl_connect('motion_notify_event', self.UpdateStatusBar)

        self.toolbar = NavigationToolbar(self.canvas)
        sizerPlot.Add(self.canvas ,1, wx.EXPAND | wx.ALL | wx.GROW )
        sizerPlot.Add(self.toolbar, 0, wx.EXPAND | wx.ALL | wx.GROW )
        self.SetSizer(sizerPlot)

    def UpdateStatusBar(self, event):
        if event.inaxes:
            #self.GetParent().GetParent().statusBar.SetStatusText("x={}  y={}".format(event.xdata, event.ydata))
            self.GetParent().GetParent().tOutput1.SetValue(str(round(event.xdata,3)))
            self.GetParent().GetParent().tOutput2.SetValue(str(round(event.ydata,3)))
    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.set(xlabel='time (s)', 
                      ylabel='voltage (mV)',
                      title='About as simple as it gets, folks')
        self.axes.format_coord = lambda x, y: "({0:f}, ".format(y) +  "{0:f})".format(x)
        self.axes.grid()
        self.axes.plot(t, s)
#        self.figure.savefig("test.png")
#        self.canvas.draw()
        #self.figure.savefig('test.png')
        self.figure.tight_layout()




if __name__ == '__main__':
    app = wx.App()
    frame = myGui(None)
    #frame.drawPlot()
    frame.Show()
    app.MainLoop()
    
    
    
