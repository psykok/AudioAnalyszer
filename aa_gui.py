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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Audio Analyzer Control", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 1200,700 ), wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.menuQuit = wx.MenuItem( self.file, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.menuQuit )

		self.m_menubar1.Append( self.file, u"File" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_toolBar2 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.m_staticText4 = wx.StaticText( self.m_toolBar2, wx.ID_ANY, u"Instrument", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText4.SetLabelMarkup( u"Instrument" )
		self.m_staticText4.Wrap( -1 )

		self.m_toolBar2.AddControl( self.m_staticText4 )
		comboInstrumentChoices = [ u"HP 8903A/B", u"VP7722" ]
		self.comboInstrument = wx.ComboBox( self.m_toolBar2, wx.ID_ANY, u"VP7722", wx.DefaultPosition, wx.Size( 200,-1 ), comboInstrumentChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.comboInstrument.SetSelection( 1 )
		self.m_toolBar2.AddControl( self.comboInstrument )
		self.m_staticText2 = wx.StaticText( self.m_toolBar2, wx.ID_ANY, u"GPIB Address", wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		self.m_toolBar2.AddControl( self.m_staticText2 )
		comboGPIBAddrChoices = []
		self.comboGPIBAddr = wx.ComboBox( self.m_toolBar2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), comboGPIBAddrChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.m_toolBar2.AddControl( self.comboGPIBAddr )
		self.btConnect = wx.Button( self.m_toolBar2, wx.ID_ANY, u"connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toolBar2.AddControl( self.btConnect )
		self.m_bitmap1 = wx.StaticBitmap( self.m_toolBar2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toolBar2.AddControl( self.m_bitmap1 )
		self.m_toolBar2.AddSeparator()

		self.checkDemo = wx.CheckBox( self.m_toolBar2, wx.ID_ANY, u"demo mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toolBar2.AddControl( self.checkDemo )
		self.m_toolBar2.Realize()

		bSizer16.Add( self.m_toolBar2, 0, wx.EXPAND, 5 )

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

		self.txtMeasTitle = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"My Measure", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		sbSizer2.Add( self.txtMeasTitle, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer61.Add( sbSizer2, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.panelMeas, wx.ID_ANY, u"Measurement Type" ), wx.VERTICAL )

		comboBMeasTypeChoices = [ u"THD+n", u"Fequence Response", u"Output Level" ]
		self.comboBMeasType = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"THD+n", wx.DefaultPosition, wx.Size( 200,-1 ), comboBMeasTypeChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.comboBMeasType.SetSelection( 0 )
		sbSizer1.Add( self.comboBMeasType, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61.Add( sbSizer1, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.panelMeas, wx.ID_ANY, u"Units" ), wx.VERTICAL )

		comboBMeasUnitsChoices = [ u"%", u"dB" ]
		self.comboBMeasUnits = wx.ComboBox( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), comboBMeasUnitsChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.comboBMeasUnits.SetSelection( 0 )
		sbSizer6.Add( self.comboBMeasUnits, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer61.Add( sbSizer6, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.panelMeas, wx.ID_ANY, u"Plot Number" ), wx.HORIZONTAL )

		self.radioBtn1 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.radioBtn1, 1, wx.ALL, 5 )

		self.radioBtn2 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.radioBtn2, 1, wx.ALL, 5 )

		self.radioBtn3 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.radioBtn3, 1, wx.ALL, 5 )

		self.radioBtn4 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.radioBtn4, 1, wx.ALL, 5 )


		bSizer61.Add( sbSizer4, 1, wx.ALL|wx.EXPAND|wx.SHAPED, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.btStart = wx.Button( self.panelMeas, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer71.Add( self.btStart, 1, wx.ALL, 5 )

		self.btClear = wx.Button( self.panelMeas, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer71.Add( self.btClear, 1, wx.ALL, 5 )


		bSizer61.Add( bSizer71, 1, wx.ALL|wx.SHAPED, 5 )


		self.panelMeas.SetSizer( bSizer61 )
		self.panelMeas.Layout()
		bSizer61.Fit( self.panelMeas )
		self.m_notebook1.AddPage( self.panelMeas, u"Meas", False )
		self.panelSetup = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelSetup.SetBackgroundColour( wx.Colour( 141, 195, 229 ) )

		bSizer81 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self.panelSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 253, 228, 131 ) )

		sizerFreqSweep = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Frequency Sweep Control" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size( 85,-1 ), wx.ALIGN_LEFT )
		self.m_staticText41.Wrap( -1 )

		bSizer11.Add( self.m_staticText41, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 20, 100000, 0 )
		self.m_spinCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer11.Add( self.m_spinCtrl1, 1, wx.ALL, 5 )


		sizerFreqSweep.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.Size( 85,-1 ), wx.ALIGN_LEFT )
		self.m_staticText5.Wrap( -1 )

		bSizer10.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_spinCtrl3 = wx.SpinCtrl( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 50, 100000, 20000 )
		bSizer10.Add( self.m_spinCtrl3, 1, wx.ALL, 5 )


		sizerFreqSweep.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, u"Step by decade", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_LEFT )
		self.m_staticText3.Wrap( -1 )

		bSizer91.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_spinCtrl4 = wx.SpinCtrl( sizerFreqSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 50, 10 )
		bSizer91.Add( self.m_spinCtrl4, 1, wx.ALL, 5 )


		sizerFreqSweep.Add( bSizer91, 1, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( sizerFreqSweep )
		self.m_panel4.Layout()
		sizerFreqSweep.Fit( self.m_panel4 )
		bSizer81.Add( self.m_panel4, 1, wx.EXPAND, 5 )

		self.m_panel5 = wx.Panel( self.panelSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.Colour( 242, 202, 48 ) )

		sizerFreq = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, u"Frequency" ), wx.HORIZONTAL )

		self.m_spinCtrl5 = wx.SpinCtrl( sizerFreq.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 100, 150000, 1000 )
		sizerFreq.Add( self.m_spinCtrl5, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel5.SetSizer( sizerFreq )
		self.m_panel5.Layout()
		sizerFreq.Fit( self.m_panel5 )
		bSizer81.Add( self.m_panel5, 0, wx.EXPAND, 5 )

		sizerVoltSweep = wx.StaticBoxSizer( wx.StaticBox( self.panelSetup, wx.ID_ANY, u"Voltage Sweep Control" ), wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer12.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.1, 10, 0.500000, 0.1 )
		self.m_spinCtrlDouble1.SetDigits( 1 )
		bSizer12.Add( self.m_spinCtrlDouble1, 1, wx.ALL, 5 )


		sizerVoltSweep.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer13.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_spinCtrlDouble2 = wx.SpinCtrlDouble( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.1, 10, 10.000000, 1 )
		self.m_spinCtrlDouble2.SetDigits( 1 )
		bSizer13.Add( self.m_spinCtrlDouble2, 1, wx.ALL, 5 )


		sizerVoltSweep.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, u"Step by decade", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer14.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_spinCtrl6 = wx.SpinCtrl( sizerVoltSweep.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 50, 10 )
		bSizer14.Add( self.m_spinCtrl6, 1, wx.ALL, 5 )


		sizerVoltSweep.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer81.Add( sizerVoltSweep, 1, wx.EXPAND|wx.TOP, 5 )

		self.m_panel51 = wx.Panel( self.panelSetup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel51.SetBackgroundColour( wx.Colour( 93, 159, 202 ) )

		sizerAmp = wx.StaticBoxSizer( wx.StaticBox( self.m_panel51, wx.ID_ANY, u"Amp (V)" ), wx.HORIZONTAL )

		self.m_spinCtrlDouble3 = wx.SpinCtrlDouble( sizerAmp.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 15, 0.5, 0.1 )
		self.m_spinCtrlDouble3.SetDigits( 2 )
		sizerAmp.Add( self.m_spinCtrlDouble3, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel51.SetSizer( sizerAmp )
		self.m_panel51.Layout()
		sizerAmp.Fit( self.m_panel51 )
		bSizer81.Add( self.m_panel51, 0, wx.EXPAND, 5 )


		self.panelSetup.SetSizer( bSizer81 )
		self.panelSetup.Layout()
		bSizer81.Fit( self.panelSetup )
		self.m_notebook1.AddPage( self.panelSetup, u"Setup", True )

		bSizer8.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( bSizer8, 0, wx.ALIGN_LEFT, 5 )

		sizerPanel = wx.BoxSizer( wx.VERTICAL )

		self.m_toolBar21 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TB_HORIZONTAL )
		self.lOUtput1 = wx.StaticText( self.m_toolBar21, wx.ID_ANY, u"THD (%)", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.lOUtput1.Wrap( -1 )

		self.lOUtput1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_toolBar21.AddControl( self.lOUtput1 )
		self.tOutput1 = wx.TextCtrl( self.m_toolBar21, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.tOutput1.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.tOutput1.SetForegroundColour( wx.Colour( 15, 238, 24 ) )
		self.tOutput1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		self.m_toolBar21.AddControl( self.tOutput1 )
		self.m_toolBar21.AddSeparator()

		self.lOutput2 = wx.StaticText( self.m_toolBar21, wx.ID_ANY, u"Freq(Hz)", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.lOutput2.Wrap( -1 )

		self.lOutput2.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_toolBar21.AddControl( self.lOutput2 )
		self.tOutput2 = wx.TextCtrl( self.m_toolBar21, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.tOutput2.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.tOutput2.SetForegroundColour( wx.Colour( 15, 238, 24 ) )
		self.tOutput2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		self.m_toolBar21.AddControl( self.tOutput2 )
		self.m_toolBar21.Realize()

		sizerPanel.Add( self.m_toolBar21, 0, wx.EXPAND, 5 )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.panelPlot = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer161.Add( self.panelPlot, 1, wx.EXPAND |wx.ALL, 5 )


		sizerPanel.Add( bSizer161, 1, wx.EXPAND, 5 )


		bSizer7.Add( sizerPanel, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer16.Add( bSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()
		bSizer16.Fit( self )
		self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.OnSize )
		self.Bind( wx.EVT_MENU, self.OnQuit, id = self.menuQuit.GetId() )
		self.comboInstrument.Bind( wx.EVT_COMBOBOX, self.OnInstSelect )
		self.btConnect.Bind( wx.EVT_BUTTON, self.OnGPIBConnect )
		self.checkDemo.Bind( wx.EVT_CHECKBOX, self.OnDemo )
		self.comboBMeasType.Bind( wx.EVT_COMBOBOX, self.cbText )
		self.btStart.Bind( wx.EVT_BUTTON, self.OnStart )
		self.btClear.Bind( wx.EVT_BUTTON, self.OnClear )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnSize( self, event ):
		event.Skip()

	def OnQuit( self, event ):
		event.Skip()

	def OnInstSelect( self, event ):
		event.Skip()

	def OnGPIBConnect( self, event ):
		event.Skip()

	def OnDemo( self, event ):
		event.Skip()

	def cbText( self, event ):
		event.Skip()

	def OnStart( self, event ):
		event.Skip()

	def OnClear( self, event ):
		event.Skip()


