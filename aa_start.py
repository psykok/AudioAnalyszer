from aa_gui import fMain
import wx 

from numpy import random,arange, sin, pi
import matplotlib
import numpy as np
import math

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx as NavigationToolbar
from matplotlib.figure import Figure

import pyvisa
import string


colorlist= ['blue','red','orange','yellow','purple']


class myGui(fMain):
    def __init__(self, parent):
        # If we overload __init__ we still need to make sure the parent
        # is initialized.
        fMain.__init__(self, parent)
        #super(myGui, self).__init__(parent)
        #self.m_staticText41.Hide()
        self.panel = CanvasPanel(self.panelPlot)
        #self.panel.draw()
        
        # populate gpib combo
        self.GetGPIBDevices()
 
        # populate measurment type combobox
        self.meas_dict = {0: "THD+n",
                          1: "Frequency Response",
                          2: "THD+n (Ratio)",
                          3: "Frequency Response (Ratio)",
                          4: "Ouput Level"}

        self.meas_conf = { "title" : "THD mesure",
                           "type" : 0, 
                           "unit": 0,
                           "axe_type": "freq",
                           "color": "blue"
                }

        # control setup : freq,freq_sweep,amp,amp_sweep
        self.meas_control_setup = [{"freq": 0, "freq_sweep": 1, "amp": 1, "amp_sweep": 0}, #THD
                                   {"freq": 0, "freq_sweep": 1, "amp": 1, "amp_sweep": 0}, #Frequency Response
                                   {"freq": 1, "freq_sweep": 1, "amp": 1, "amp_sweep": 0}, #THD (Ratio)
                                   {"freq": 1, "freq_sweep": 1, "amp": 1, "amp_sweep": 0}, #Frequency Response (Ratio)
                                   {"freq": 1, "freq_sweep": 0, "amp": 0, "amp_sweep": 1} #Ouput Level
                ]
        self.meas_unit = [["%","dB"],  #THD
                          ["V","dBm"], #Frequency Response
                          ["%","dB"],  #THD (Ratio)
                          ["%","dB"],  #Frequency Response (Ratio)
                          ["V","dBm"] #Ouput Level
                ]
        
        self.meas_filters = ["30 kHz Low Pass",
                             "80 kHz Low Pass",
                             "Left Plug-in Filter",
                             "Right Plug-in Filter"]

        myList=[]
        myList=self.Dict2List(self.meas_dict)
        self.comboBMeasType.Clear()
        self.comboBMeasType.Set(myList)
        self.comboBMeasType.SetValue(myList[0])

        self.setPanelConfig()

        self.build_filter_list()

        self.panel.axes.set_title(self.txtMeasTitle.GetValue())
        self.UpdateAxes()
    
    def build_filter_list(self):
        sizerFilter = wx.BoxSizer(wx.VERTICAL)

        pos=0
        self.radioFilter=[]
        for filterTag in self.meas_filters:
            self.radioFilter.append( wx.RadioButton(self.panelFilter, wx.ID_ANY,filterTag,wx.DefaultPosition,wx.DefaultSize,0))
            sizerFilter.Add(self.radioFilter[pos], 0,wx.EXPAND | wx.ALL | wx.GROW )
            pos+=1
        self.panelFilter.SetSizer(sizerFilter)
        self.panelFilter.Layout()

    def setup_gpib(self):
        gpib_model = self.comboInstrument.GetStringSelection()
        gpib_mydevice = self.comboGPIBAddr.GetStringSelection()

        if gpib_mydevice.startswith('GPIB'):
           print('MODEL:' + gpib_mydevice)
           self.gpib_dev = VISA_GPIB(gpib_mydevice)

           print('NAME:' + self.gpib_dev.name())
           self.gpib_dev.open()
           print(self.gpib_dev.read()) 

           # Enable measurement controls
           self.GPIBStatus.SetBitmap(wx.Bitmap( "icon/connected.png") )
        else:
            print("Failed to use GPIB device")
            print("Verify hardware setup and try to connect again")
            return(False)

    def GetGPIBDevices(self):
        GPIBDevList = []
        rm = pyvisa.ResourceManager()
        devices = rm.list_resources()
        
        for g_dev in devices:
            if "GPIB" in g_dev:
               GPIBDevList.append(g_dev)
        if len(GPIBDevList):
            self.comboGPIBAddr.Clear()
            self.comboGPIBAddr.Set(GPIBDevList)
            self.comboGPIBAddr.SetSelection(0)
        return

    def getPanelConfigValue(self,meas,index):
        panelConf = self.meas_control_setup[meas]
        return panelConf[index]

    def setPanelConfig(self):
        panelConf = self.meas_control_setup[self.meas_conf["type"]]
        if panelConf["freq"]:
            self.panelFreq.Enable()
        else:
            self.panelFreq.Disable()

        if panelConf["freq_sweep"]:
            self.panelFreqSweep.Enable()
        else:
            self.panelFreqSweep.Disable()

        if panelConf["amp"]:
            self.panelAmp.Enable()
        else:
            self.panelAmp.Disable()

        if panelConf["amp_sweep"]:
            self.panelAmpSweep.Enable()
        else:
            self.panelAmpSweep.Disable()

    def SetCombo(self,wx,myDic):
        myCombo.clear()

        mylist=Dict2List(myDic)
        myCambo.Set(mylist)
        myCambo.SetValue(mylist[0])

    def Dict2List(self,mydic):
        mylist = []
        for k,v in mydic.items():
            mylist.append(v)
        return mylist
   
    def onColor(self, event):
        rb = event.GetEventObject() 
        self.meas_conf["color"]=colorlist[int(rb.GetLabel())]

    def OnStart(self, event):
        self.statusBar.SetStatusText("start measurment")
        
        # results storage
        self.x = []
        self.y = []

        

        lsteps = []
        vsteps = [] 
        
        if self.meas_conf["axe_type"] == "freq":
            strtf = self.startFreq.GetValue()
            stopf = self.stopFreq.GetValue()
            num_steps = self.stepFreq.GetValue()

            decs = math.log10(stopf/strtf)
            npoints = (int(decs*num_steps)+1)

           # for n in range(npoints + 1):
           #     #lsteps.append(round(strtf*10.0**(float(n)/float(num_steps))))
           #     lsteps.append(strtf*10.0**(float(n)/float(num_steps)))
            lsteps=np.logspace(math.log10(strtf),math.log10(stopf),npoints,True)
            print(npoints)

        elif self.meas_conf["axe_type"] == "io":
            start_amp = self.startAmp.GetValue()
            stop_amp = self.stopAmp.GetValue()

            num_steps = self.stepAmp.GetValue() 
            lsteps = np.linspace(start_amp, stop_amp, num_steps)

            amp_buf = ((stop_amp - start_amp)*0.1)/2.0
            print(amp_buf)
            self.panel.axes.set_xlim(((start_amp - amp_buf), (stop_amp + amp_buf)))

        self.plt = self.panel.axes.plot(marker = 'x')


        for i in lsteps: 
            meas_point = random.randint(1, 10)

            self.x.append(float(i))
            self.y.append(float(meas_point))
          
            self.update_plot(self.x, self.y)

    def onClear(self, event):
        self.panel.clear()
        self.UpdateAxes()

    def update_plot(self, x, y):
        #print("ploter selected color : " + self.plot_color)
        #if (len(self.plt) < 1):
        #self.plt = self.a.plot(x, y, color=self.plot_color,marker = 'o',label=self.plot_color)
        self.plt = self.panel.axes.plot(x, y, self.meas_conf["color"],marker = 'o',label="toto")
        self.plt[0].set_data(x, y)
        ymin = min(y)
        ymax = max(y)
        
        # if (ymin == 0.0):
        #     ymin = -0.01
        # if (ymax == 0.0):
        #     ymax = 0.01
        sep = abs(ymax - ymin)
        sep = sep/10.0

        if (sep == 0.0):
            sep = 0.01

        #self.a.set_ylim((ymin - abs(ymin*0.10), ymax + abs(ymax*0.10)))
        self.panel.axes.set_ylim((ymin - abs(sep), ymax + abs(sep)))
        self.panel.canvas.draw()

    def onMeasChange(self, event):
        measID=self.comboBMeasType.GetCurrentSelection()
        measName=self.comboBMeasType.GetStringSelection()
        self.statusBar.SetStatusText(str(measID) + ": " + measName)
       

        self.meas_conf['axe_type'] = "freq"
        
        if (self.getPanelConfigValue(measID,'amp_sweep') == 1):
            self.meas_conf['axe_type'] = "io"

        self.SetControlConf(self.meas_unit[measID],self.meas_conf['axe_type'])
        
        #save meas type
        self.meas_conf['type'] = measID

        self.setPanelConfig()

        return

    def onGPIBConnect(self, event):
        self.setup_gpib()
        #self.GPIBStatus.SetBitmap(wx.Bitmap( "icon/connected.png") )

        return

    def onUnitChange(self, event):
        unit=self.comboBMeasUnits.GetStringSelection()
        self.meas_conf['unit'] = unit
        self.UpdateAxes()

    def SetControlConf(self,mylist,axesTag):
        self.comboBMeasUnits.Set(mylist)
        self.comboBMeasUnits.SetSelection(0)
        
        self.UpdateAxes()
    def onTitleChange(self, event):
        self.panel.axes.set_title(self.txtMeasTitle.GetValue())
        self.panel.canvas.draw()

    def UpdateAxes(self):
        unit=self.comboBMeasUnits.GetStringSelection()
        tag=self.comboBMeasType.GetStringSelection()

        axesTag = self.meas_conf['axe_type']
        
        if axesTag == "freq":
            self.panel.axes.set_xscale('log')
            self.panel.axes.set_ylabel(tag + " (" + unit +")")
            self.panel.axes.set_xlabel("Frequency (Hz)")
            self.LOutputTag.SetLabel( unit )
            xmin=strtf = self.startFreq.GetValue()
            xmax=self.stopFreq.GetValue()

        elif axesTag == "io":
            self.panel.axes.set_xscale('linear')
            self.panel.axes.set_ylabel("Input (" + unit +")")
            self.panel.axes.set_xlabel("Output (" + unit +")")
            self.LOutputTag.SetLabel( unit )
            self.ROutputTag.SetLabel( unit )
            xmin = self.startAmp.GetValue()
            xmax = self.stopAmp.GetValue()
        
        self.panel.axes.grid(True)

        self.panel.axes.set_xlim(xmin,xmax)
        self.panel.canvas.draw()

    def onSave(self,event):
        self.statusBar.SetStatusText("Saved")

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

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        sizerPanel = wx.BoxSizer(wx.VERTICAL)

        wx.Panel.__init__(self, parent,size=wx.Size(806, 450))
        sizerPlot = wx.BoxSizer(wx.VERTICAL)
        #self.SetBackgroundColour("red")

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
            self.GetParent().GetParent().ROutput.SetValue(str(round(event.xdata,3)))
            self.GetParent().GetParent().LOutput.SetValue(str(round(event.ydata,3)))
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

    def clear(self):
       self.plot_new=True

       #clear everything
       self.axes.cla()

       self.axes.grid(True)
       #self.a.lines[0].remove()
       self.canvas.draw()

class VISA_GPIB():
    def __init__(self,mydevice):
        self.rm = None
        self.inst = None
        self.mydevice = mydevice

    def open(self):

        print("Connecting to: %s" % self.mydevice)

        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(self.mydevice)

    def write(self, data):
        ret = self.inst.write(data)


    def read(self):
        output = self.inst.read_bytes(40)
        for line in str(output).split("\\r\\n"):
            if len(line) >= 10:
                result = line
        print(result)
        return (True,result)

    def test(self):
        # Not much to do on this device...
        return(self.is_open())

    def name(self):
        return("Visa GPIB Device")


if __name__ == '__main__':
    app = wx.App()
    frame = myGui(None)
    #frame.drawPlot()
    frame.Show()
    app.MainLoop()
    
    
    
