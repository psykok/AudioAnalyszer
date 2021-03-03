# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 21 2021)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class fMain
###########################################################################

class fMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Audio Analyzer Control", pos = wx.DefaultPosition, size = wx.Size( 1200,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 1200,800 ), wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.menuSave = wx.MenuItem( self.file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.menuSave )

		self.menuQuit = wx.MenuItem( self.file, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.menuQuit )

		self.m_menubar1.Append( self.file, u"File" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.GPIBToolBar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.m_staticText4 = wx.StaticText( self.GPIBToolBar, wx.ID_ANY, u"Instrument", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText4.SetLabelMarkup( u"Instrument" )
		self.m_staticText4.Wrap( -1 )

		self.GPIBToolBar.AddControl( self.m_staticText4 )
		comboInstrumentChoices = [ u"HP 8903A/B", u"VP7722" ]
		self.comboInstrument = wx.ComboBox( self.GPIBToolBar, wx.ID_ANY, u"VP7722", wx.DefaultPosition, wx.Size( 200,-1 ), comboInstrumentChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.comboInstrument.SetSelection( 0 )
		self.GPIBToolBar.AddControl( self.comboInstrument )
		self.m_staticText2 = wx.StaticText( self.GPIBToolBar, wx.ID_ANY, u"GPIB Address", wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		self.GPIBToolBar.AddControl( self.m_staticText2 )
		comboGPIBAddrChoices = []
		self.comboGPIBAddr = wx.ComboBox( self.GPIBToolBar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), comboGPIBAddrChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.GPIBToolBar.AddControl( self.comboGPIBAddr )
		self.btConnect = wx.Button( self.GPIBToolBar, wx.ID_ANY, u"connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GPIBToolBar.AddControl( self.btConnect )
		self.GPIBStatus = wx.StaticBitmap( self.GPIBToolBar, wx.ID_ANY, wx.Bitmap( u"icon/disconnected.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.GPIBToolBar.AddControl( self.GPIBStatus )
		self.GPIBToolBar.AddSeparator()

		self.checkDemo = wx.CheckBox( self.GPIBToolBar, wx.ID_ANY, u"demo mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GPIBToolBar.AddControl( self.checkDemo )
		self.GPIBToolBar.Realize()

		bSizer16.Add( self.GPIBToolBar, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer16.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer8.SetMinSize( wx.Size( 200,-1 ) )
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.panelMeas = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.panelMeas, wx.ID_ANY, u"Measurement Title" ), wx.VERTICAL )

		self.txtMeasTitle = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Title", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		sbSizer2.Add( self.txtMeasTitle, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61.Add( sbSizer2, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.panelMeas, wx.ID_ANY, u"Measurement Type" ), wx.VERTICAL )

		comboBMeasTypeChoices = [ u"THD+n", u"Fequence Response", u"Output Level" ]
		self.comboBMeasType = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Fequence Response", wx.DefaultPosition, wx.Size( 200,-1 ), comboBMeasTypeChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.comboBMeasType.SetSelection( 1 )
		sbSizer1.Add( self.comboBMeasType, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.panelMeas, wx.ID_ANY, u"Units" ), wx.VERTICAL )

		comboBMeasUnitsChoices = [ u"%", u"dB" ]
		self.comboBMeasUnits = wx.ComboBox( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), comboBMeasUnitsChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.comboBMeasUnits.SetSelection( 0 )
		sbSizer6.Add( self.comboBMeasUnits, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61.Add( sbSizer6, 0, wx.ALL|wx.EXPAND, 5 )

		rbNbLinesChoices = [ u"1", u"2", u"3", u"4" ]
		self.rbNbLines = wx.RadioBox( self.panelMeas, wx.ID_ANY, u"Number Lines", wx.DefaultPosition, wx.DefaultSize, rbNbLinesChoices, 1, wx.RA_SPECIFY_ROWS )
		self.rbNbLines.SetSelection( 0 )
		bSizer61.Add( self.rbNbLines, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.btStart = wx.Button( self.panelMeas, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer71.Add( self.btStart, 1, wx.ALL, 5 )

		self.btClear = wx.Button( self.panelMeas, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer71.Add( self.btClear, 1, wx.ALL, 5 )


		bSizer61.Add( bSizer71, 1, wx.ALL|wx.SHAPED, 5 )


		self.panelMeas.SetSizer( bSizer61 )
		self.panelMeas.Layout()
		bSizer61.Fit( self.panelMeas )
		self.m_notebook1.AddPage( self.panelMeas, u"Meas", True )
		self.panelSetup = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelSetup.SetBackgroundColour( wx.Colour( 141, 195, 229 ) )

		bSizer81 = wx.BoxSizer( wx.VERTICAL )

		self.panelFreqSweep = wx.Panel( self.panelSetup, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.panelFreqSweep.SetBackgroundColour( wx.Colour( 253, 228, 131 ) )

		sizerFreqSweep = wx.StaticBoxSizer( wx.StaticBox( self.panelFreqSweep, wx.ID_ANY, u"Frequency Sweep Control" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size( 85,-1 ), wx.ALIGN_LEFT )
		self.m_staticText41.Wrap( -1 )

		bSizer11.Add( self.m_staticText41, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.startFreq = wx.SpinCtrl( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 20, 100000, 20 )
		self.startFreq.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer11.Add( self.startFreq, 1, wx.ALL, 5 )


		sizerFreqSweep.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.Size( 85,-1 ), wx.ALIGN_LEFT )
		self.m_staticText5.Wrap( -1 )

		bSizer10.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.stopFreq = wx.SpinCtrl( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 50, 100000, 20000 )
		bSizer10.Add( self.stopFreq, 1, wx.ALL, 5 )


		sizerFreqSweep.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, u"Step by decade", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_LEFT )
		self.m_staticText3.Wrap( -1 )

		bSizer91.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.stepFreq = wx.SpinCtrl( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 50, 10 )
		bSizer91.Add( self.stepFreq, 1, wx.ALL, 5 )


		sizerFreqSweep.Add( bSizer91, 1, wx.EXPAND, 5 )


		self.panelFreqSweep.SetSizer( sizerFreqSweep )
		self.panelFreqSweep.Layout()
		sizerFreqSweep.Fit( self.panelFreqSweep )
		bSizer81.Add( self.panelFreqSweep, 0, wx.EXPAND|wx.FIXED_MINSIZE, 5 )

		self.panelFreq = wx.Panel( self.panelSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelFreq.SetBackgroundColour( wx.Colour( 242, 202, 48 ) )

		sizerFreq = wx.StaticBoxSizer( wx.StaticBox( self.panelFreq, wx.ID_ANY, u"Frequency" ), wx.HORIZONTAL )

		self.singleFreq = wx.SpinCtrl( sizerFreq.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 100, 150000, 1000 )
		sizerFreq.Add( self.singleFreq, 1, wx.ALL|wx.EXPAND, 5 )


		self.panelFreq.SetSizer( sizerFreq )
		self.panelFreq.Layout()
		sizerFreq.Fit( self.panelFreq )
		bSizer81.Add( self.panelFreq, 0, wx.EXPAND, 5 )

		self.panelAmpSweep = wx.Panel( self.panelSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerVoltSweep = wx.StaticBoxSizer( wx.StaticBox( self.panelAmpSweep, wx.ID_ANY, u"Voltage Sweep Control" ), wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer12.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.startAmp = wx.SpinCtrlDouble( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.1, 10, 0.500000, 0.1 )
		self.startAmp.SetDigits( 1 )
		bSizer12.Add( self.startAmp, 1, wx.ALL, 5 )


		sizerVoltSweep.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer13.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.stopAmp = wx.SpinCtrlDouble( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.1, 10, 10.000000, 1 )
		self.stopAmp.SetDigits( 1 )
		bSizer13.Add( self.stopAmp, 1, wx.ALL, 5 )


		sizerVoltSweep.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, u"Step by decade", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer14.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.stepAmp = wx.SpinCtrl( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 50, 10 )
		bSizer14.Add( self.stepAmp, 1, wx.ALL, 5 )


		sizerVoltSweep.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.panelAmpSweep.SetSizer( sizerVoltSweep )
		self.panelAmpSweep.Layout()
		sizerVoltSweep.Fit( self.panelAmpSweep )
		bSizer81.Add( self.panelAmpSweep, 0, wx.EXPAND |wx.ALL, 5 )

		self.panelAmp = wx.Panel( self.panelSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelAmp.SetBackgroundColour( wx.Colour( 93, 159, 202 ) )

		sizerAmp = wx.StaticBoxSizer( wx.StaticBox( self.panelAmp, wx.ID_ANY, u"Amp (V)" ), wx.HORIZONTAL )

		self.amp = wx.SpinCtrlDouble( sizerAmp.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 15, 0.5, 0.1 )
		self.amp.SetDigits( 2 )
		sizerAmp.Add( self.amp, 1, wx.ALL|wx.EXPAND, 5 )


		self.panelAmp.SetSizer( sizerAmp )
		self.panelAmp.Layout()
		sizerAmp.Fit( self.panelAmp )
		bSizer81.Add( self.panelAmp, 0, wx.EXPAND, 5 )

		self.panelFilter = wx.Panel( self.panelSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelFilter.SetBackgroundColour( wx.Colour( 212, 155, 155 ) )

		bSizer81.Add( self.panelFilter, 1, wx.EXPAND, 5 )


		self.panelSetup.SetSizer( bSizer81 )
		self.panelSetup.Layout()
		bSizer81.Fit( self.panelSetup )
		self.m_notebook1.AddPage( self.panelSetup, u"Setup", False )

		bSizer8.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( bSizer8, 0, wx.ALIGN_LEFT, 5 )

		sizerPanel = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer17.SetMinSize( wx.Size( -1,60 ) )
		self.LOutput = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.LOutput.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.LOutput.SetForegroundColour( wx.Colour( 15, 238, 24 ) )
		self.LOutput.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer17.Add( self.LOutput, 0, wx.ALL|wx.EXPAND, 5 )

		self.LOutputTag = wx.StaticText( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.Size( 80,25 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.LOutputTag.Wrap( -1 )

		self.LOutputTag.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer17.Add( self.LOutputTag, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ROutput = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.ROutput.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ROutput.SetForegroundColour( wx.Colour( 15, 238, 24 ) )
		self.ROutput.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer17.Add( self.ROutput, 0, wx.ALL|wx.EXPAND, 5 )

		self.ROutputTag = wx.StaticText( self, wx.ID_ANY, u"Hz", wx.DefaultPosition, wx.Size( 80,25 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.ROutputTag.Wrap( -1 )

		self.ROutputTag.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer17.Add( self.ROutputTag, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		sizerPanel.Add( bSizer17, 0, wx.ALIGN_CENTER|wx.SHAPED, 5 )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.panelPlot = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer161.Add( self.panelPlot, 1, wx.ALL|wx.EXPAND, 5 )


		sizerPanel.Add( bSizer161, 1, wx.EXPAND, 5 )


		bSizer7.Add( sizerPanel, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer16.Add( bSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.onSave, id = self.menuSave.GetId() )
		self.Bind( wx.EVT_MENU, self.OnQuit, id = self.menuQuit.GetId() )
		self.comboInstrument.Bind( wx.EVT_COMBOBOX, self.OnInstSelect )
		self.btConnect.Bind( wx.EVT_BUTTON, self.onGPIBConnect )
		self.checkDemo.Bind( wx.EVT_CHECKBOX, self.OnDemo )
		self.txtMeasTitle.Bind( wx.EVT_TEXT, self.onTitleChange )
		self.comboBMeasType.Bind( wx.EVT_COMBOBOX, self.onMeasChange )
		self.comboBMeasUnits.Bind( wx.EVT_COMBOBOX, self.onUnitChange )
		self.rbNbLines.Bind( wx.EVT_RADIOBOX, self.onNbLines )
		self.btStart.Bind( wx.EVT_BUTTON, self.OnStart )
		self.btClear.Bind( wx.EVT_BUTTON, self.onClear )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onSave( self, event ):
		event.Skip()

	def OnQuit( self, event ):
		event.Skip()

	def OnInstSelect( self, event ):
		event.Skip()

	def onGPIBConnect( self, event ):
		event.Skip()

	def OnDemo( self, event ):
		event.Skip()

	def onTitleChange( self, event ):
		event.Skip()

	def onMeasChange( self, event ):
		event.Skip()

	def onUnitChange( self, event ):
		event.Skip()

	def onNbLines( self, event ):
		event.Skip()

	def OnStart( self, event ):
		event.Skip()

	def onClear( self, event ):
		event.Skip()


