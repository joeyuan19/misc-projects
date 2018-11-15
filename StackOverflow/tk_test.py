import sys, Tkinter
sys.modules['tkinter'] = Tkinter
import Pmw

class Print:

	def __init__(self, text):
		self.text = text

	def __call__(self):
		print self.text

class mainWindow:

		def __init__(self,parent):
			self.parent = parent
			self.balloon = Pmw.Balloon(parent)

			def Quit():
				root.destroy()

			menuBar = Pmw.MenuBar(parent,hull_relief = 'raised',hull_borderwidth = 1,balloon = self.balloon)
			menuBar.pack(fill = 'x')

			menuBar.addmenu('Run Control','Calibration,Download Configuration,Number of Triggers,Data Output File,Upload Configuration,Start DAQ,Quit')
			menuBar.addcascademenu('Run Control','Calibration','View and/or change the calibration',traverseSpec = 'z',tearoff = 1)
			menuBar.addmenuitem('Calibration','command','Display the DAC calibration',command = Print('display the DAC calibration'),label = 'Display DAC Calibration')

			menuBar.addmenuitem('Calibration','command','Display the calibration mask',command = Print('display the calibration mask'),label = 'Display Calibration Mask')
			menuBar.addmenuitem('Calibration','command','Change the DAC calibration',command = Print('change the DAC calibration'),label = 'Change DAC Calibration')
			menuBar.addmenuitem('Calibration','command','Change the calibration mask',command = Print('change the calibration mask'),label = 'Change Calibration Mask')

			menuBar.addmenuitem('Run Control','command','Download a configuration',command = Print('download configuration'),label = 'Download Configuration')

			menuBar.addmenuitem('Run Control','command','Set the number of triggers',command = Print('set number of triggers'),label = 'Number of Triggers')
			menuBar.addmenuitem('Run Control','command','Change the file where the data will be sent to',command = Print('set data output file'),label = 'Data Output File')
			menuBar.addmenuitem('Run Control','command','Upload a configuration',command = Print('upload a configuration'),label = 'Upload Configuration')

			menuBar.addmenuitem('Run Control','command','Start the data aquisition',command = Print('start data aquisition'),label = 'Start DAQ')
			menuBar.addmenuitem('Run Control','separator')
			menuBar.addmenuitem('Run Control','command','Close the GUI',command = Quit,label = 'Quit')

			mainPart = Tkinter.Label(parent,text = 'GUI',background = 'white',foreground = 'white',padx = 100,pady = 100)
			mainPart.pack(fill = 'both', expand = 1)

			buttonBox = Pmw.ButtonBox(parent)
			buttonBox.pack(fill = 'x')
			buttonBox.add('Start\nRoot', command = Print('start root'))
			
			self.menuBar = menuBar
			self.mainPart = mainPart
			self.buttonBox = buttonBox

if __name__ == '__main__':
	root = Tkinter.Tk()
	parent = Pmw.initialise(root)
	root.title('pCT GUI')
	derp = mainWindow(root) 
	root.mainloop()


