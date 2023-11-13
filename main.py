#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from multiprocessing import Queue
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from subprocess import PIPE, run
import time
import subprocess
import shutil
import shlex
from PyQt5 import uic                         # added
import glob
import os.path
from os import path
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

#**file_ = open('style_sheet') ##### style_sheet
#**file_ = file_.read()   ##### style_sheet

class Application(QtWidgets.QMainWindow):
    def __init__(self, title= "Default", parent=None):  
        super(Application, self).__init__(parent)
        self.title = title
        #self.ui = Ui_MainWindow()                    # commented
        #self.ui.setupUi(self)                        # commented
        uic.loadUi("gui.ui", self)            # added
        #self.setWindowTitle(self.title)              # commented
        #**self.setStyleSheet(file_)   ##### style_sheet
        self._initButtons()
        self.lineEdit_2.setText(" ")
        self.lineEdit_4.setText(" ")
        self.lineEdit_5.setText(" ")
        self.lineEdit_6.setText(" ")
        self.lineEdit_7.setText("")
        self.lineEdit.setText(" ")
        self.lineEdit_8.setText(" ")
        self.lineEdit_9.setText(" ")
        self.lineEdit_10.setText(" ")
        self.lineEdit_12.setText(" ")
        self.lineEdit_13.setText(" ")
        self.lineEdit_14.setText(" ")
        
        
        self.lineEdit_17.setText(" ")
        self.lineEdit_16.setText(" ")
        self.lineEdit_15.setText(" ")
        self.lineEdit_18.setText(" ")
        self.lineEdit_19.setText(" ")
        self.lineEdit_20.setText(" ")
        self.lineEdit_21.setText(" ")
        self.lineEdit_22.setText(" ")
        self.lineEdit_23.setText(" ")
        
        self.lineEdit_3.setText(" ")
        self.lineEdit_24.setText(" ")
        self.lineEdit_25.setText(" ")
        self.lineEdit_26.setText(" ")
        self.lineEdit_27.setText(" ")
        self.lineEdit_28.setText(" ")
        self.lineEdit_29.setText(" ")
        self.lineEdit_31.setText(" ")
        self.lineEdit_32.setText(" ")

    def _initButtons(self): 
        self.pushButton_2.clicked.connect(self.Run)
        self.pushButton.clicked.connect(self.Plot)
        self.actionExit_2.triggered.connect(self.Exit)
        self.actionClear_2.triggered.connect(self.Clear)
        
    def Clear(self): 
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        
        
        self.lineEdit_17.clear()
        self.lineEdit_16.clear()
        self.lineEdit_15.clear()
        self.lineEdit_18.clear()
        self.lineEdit_19.clear()
        self.lineEdit_20.clear()
        self.lineEdit_21.clear()
        self.lineEdit_22.clear()
        self.lineEdit_23.clear()
        
        self.lineEdit_3.clear()
        self.lineEdit_24.clear()
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        self.lineEdit_27.clear()
        self.lineEdit_28.clear()
        self.lineEdit_29.clear()
        self.lineEdit_31.clear()
        self.lineEdit_32.clear()

        
    def Exit(self):
        """Generate 'question' dialog on clicking 'X' button in title bar.
        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(self, "Message",
            "Are you sure you want to quit ?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            qapp.quit()
        else:
            pass 

        
    def Plot(self):
        if self.checkBox.isChecked():
            fig = plt.figure(1)
            plt.plot (self.T, self.z, 'm',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel (' Temperature ($^\circ$C) ' ,fontsize=16)
            plt.ylabel ('Axial Height',fontsize=16)
            plt.title ('Graph of axial temp. distribution in the coolant')
            plt.savefig('Axial temp. distribution in the coolant.png', dpi=600)
            plt.show()
        
            fig = plt.figure(2)
            plt.plot (self.Tc ,self.z, 'b-.',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel ('Temperature ($^\circ$C)',fontsize=16 ) 
            plt.ylabel ('Axial Height',fontsize=16)
            plt.title ('Graph of temp. distribution in the outer surface of the cladding')
            plt.savefig('Axial temp. distribution in the outer surface of the cladding.png', dpi=600)
            plt.show()
            
            fig = plt.figure(3)
            plt.plot (self.Tf ,self.z, 'g--',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel ('Temperature ($^\circ$C)',fontsize=16 )
            plt.ylabel ('Axial Height',fontsize=16)
            plt.title ('Graph of temp. distribution in the fuel surface')
            plt.savefig('Axial temp. distribution in the fuel surface.png', dpi=600)
            plt.show()
           
            fig = plt.figure(4)
            plt.plot (self.To ,self.z, 'r-',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel ('Temperature ($^\circ$C)',fontsize=16 )
            plt.ylabel ('Axial Height',fontsize=16)
            plt.title ('Graph of temp. distribution in the fuel center')
            plt.savefig('Axial temp. distribution in the fuel center.png', dpi=600)
            plt.show()

            fig = plt.figure(5)
            plt.plot (self.T, self.z,"m", self.Tc, self.z,'b-.', self.Tf, self.z,'g--', self.To, self.z,'r-',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel ('Temperature ($^\circ$C)',fontsize=16 )
            plt.ylabel ('Height of Reactor Core (m)',fontsize=16)
            #plt.title('Combined temp. distribution in the coolant, outer surface of the cladding, fuel surface, fuel center')
            plt.gca().legend(('Coolant','Outer Surface of Cladding', 'Fuel Surface','Fuel Centerline'))
            plt.savefig('Axial temperature distribution.png', dpi=600)  
            plt.show()
        else:
            pass
        if self.checkBox_2.isChecked():
            fig = plt.figure(6)
            plt.plot(self.ri,self.Tff,'r',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel('Radial distance (mm)',fontsize=16)
            plt.ylabel('Temperature ($^\circ$C)',fontsize=16)
            plt.title ('Graph of radial temp. distribution in the fuel')
            plt.savefig('Radial temp. distribution in the fuel.png', dpi=600)
            plt.show()
        
            fig = plt.figure(7)
            plt.plot(self.rj,self.Td,'g--',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel('Radial distance (mm)',fontsize=16) 
            plt.ylabel('Temperature ($^\circ$C)',fontsize=16)
            plt.title('Graph of radial temp. distribution in the sheath(cladding)')
            plt.savefig('Radial temp. distribution in the sheath(cladding).png', dpi=600)
            plt.show()
        
            fig = plt.figure(8)
            plt.plot(self.rk,self.Th,'b-',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel('Radial distance (mm)',fontsize=16)
            plt.ylabel('Temperature ($^\circ$C)',fontsize=16)
            plt.title ('Graph of radial temp. distribution in the coolant')
            plt.savefig('Radial temp. distribution in the coolant.png', dpi=600)
            plt.show()
        
            fig = plt.figure(9)
            plt.plot(self.ri, self.Tff, 'r', self.rj, self.Td,'g--', self.rk, self.Th,'b-',linewidth = 2.5)
            plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            plt.xlabel('Radial Distance (mm)',fontsize=16)
            plt.ylabel('Temperature ($^\circ$C)',fontsize=16)
            #plt.title ('Combined radial temp. distribution demarcating clearly each region')
            plt.gca().legend(('Fuel Rod','Cladding','Coolant'))
            plt.savefig('Radial temperature distribution.png', dpi=600)  
            plt.show()
        else:
            pass
         
        #%************************************************************************************
	#Python code for axial temperature profile
	# initialization of thermal-hydraulic parameters used in simulating in the axial direction.
	#%************************************************************************************   
    
    def Run(self):
        if self.checkBox.isChecked():
            Ti = eval(self.lineEdit_2.text())   # inlet temperature 
            Te = eval(self.lineEdit_7.text())    # exit temperature
            pc = eval(self.lineEdit.text())      # total channel power
            cp = eval(self.lineEdit_8.text())   # specific heat at constant pressure
            m  = eval(self.lineEdit_9.text())    # mass flow rate
            H  = eval(self.lineEdit_10.text())   # core height/pin cell 
            HH = eval(self.lineEdit_12.text())    # height including the reflector.
            hc = eval(self.lineEdit_13.text())   # heat transfer coefficient
            s = eval(self.lineEdit_14.text())    # heated perimeter
            z1 = eval(self.lineEdit_4.text()); z2 = eval(self.lineEdit_5.text()); z3 = eval(self.lineEdit_6.text())
            self.z  = np.arange(float(z1),  float(z2), float(z3))
            beta = 3.14*H/(2*HH)
            print (beta)
        
            #%************************************************************************************
            # Computing terms in the main equation
            # MATLAB codes for the equations in the axial direction
            VAL1 = (pc / 2 * m * cp)
            VAL2 = np.sin(2*beta * self.z/H) / np.sin(beta + 1)
            #%************************************************************************************
            self.T = Ti + VAL1*VAL2
            f = open("Axial temp. distribution in the coolant.text", "w")
            for i in range(len(self.T)):
                f.write("%10.5f %15.5f\n" % (self.T[i], self.z[i]))
            f.close()

            #%************************************************************************************
            VAL3 = (Ti+Te)/2
            VAL4 = (Te-Ti)/2* np.sin (beta)
            VAL5 = np.sin(2*beta*self.z/H)
            VAL6 = (pc*beta* np.cos (2*beta*self.z/H))/ (hc*s*H*np.sin (beta))
            #%************************************************************************************
            #%************************************************************************************
            self.Tc= VAL3+VAL4*VAL5+VAL6
            f = open("Axial temp. distribution in the outer surface of the cladding.text", "w")
            for i in range(len(self.Tc)):
                f.write("%10.5f %15.5f\n" % (self.Tc[i], self.z[i]))
            f.close()
            #%************************************************************************************
            VAL7 = (1.4581*pc*np.cos (2*beta*self.z/H))/ (H*(Te-Ti))
            #%************************************************************************************
            #%************************************************************************************
            self.Tf= VAL3+VAL4*(VAL5+VAL7)
            f = open("Axial temp. distribution in the fuel surface.text", "w")
            for i in range(len(self.Tf)):
                f.write("%10.5f %15.5f\n" % (self.Tf[i], self.z[i]))
            f.close()

            VAL8 = (2.4720*pc*np.cos (2*beta * self.z/H))/ (H*(Te-Ti))
            #%************************************************************************************
            self.To= VAL3+VAL4*(VAL5+VAL8)
            f = open("Axial temp. distribution in the fuel center.text", "w")
            for i in range(len(self.To)):
                f.write("%10.5f %15.5f\n" % (self.To[i], self.z[i]))
            f.close()
        else:
            pass
        if self.checkBox_2.isChecked():
            #%************************************************************************************
            #%The thermal-hydraulic parameters used in simulating in the radial direction.
            #%ri, rj and rk are distances from fuel element center (m).
            #%************************************************************************************
            ri1 = eval(self.lineEdit_17.text())
            ri2 = eval(self.lineEdit_16.text())
            ri3 = eval(self.lineEdit_15.text())
            self.ri  = np.arange(float(ri1),  float(ri2), float(ri3)) # range and interval for the fuel meat of radius

            rj1 = eval(self.lineEdit_18.text())
            rj2 = eval(self.lineEdit_19.text())
            rj3 = eval(self.lineEdit_20.text())
            self.rj  = np.arange(float(rj1),  float(rj2), float(rj3)) #range and interval from the inner to  outer  surfaces  of cladding

            rk1 = eval(self.lineEdit_21.text())
            rk2 = eval(self.lineEdit_22.text())
            rk3 = eval(self.lineEdit_23.text())
            self.rk  = np.arange(float(rk1),  float(rk2), float(rk3)) # width of the coolant channel

            h = eval(self.lineEdit_3.text())      # heat transfer coefficient
            rf = eval(self.lineEdit_24.text())    # radius of the fuel
            rc = eval(self.lineEdit_25.text())    # width of the cladding
            kf = eval(self.lineEdit_26.text())    # conductivity of the fuel
            kc = eval(self.lineEdit_27.text())    # conductivity of the cladding
            q = eval(self.lineEdit_28.text())     # heat flux
            Q = eval(self.lineEdit_29.text())     # power density
            Ta = eval(self.lineEdit_31.text())    # temperature at inner surface of cladding
            Tb = eval(self.lineEdit_32.text())    # temperature at the outer surface of cladding
            #%************************************************************************************
            self.Tff = Ta + (Q / (4*kf))*(rf**2 - self.ri**2)
            f = open("Radial temp. distribution in the fuel.text", "w")
            for i in range(len(self.ri)):
                f.write("%10.5f  %15.5f\n" % (self.ri[i], self.Tff[i]))
            f.close()

            self.Td = Ta-((rf*q)* np.log (self.rj/rf)/kc)
            f = open("Radial temp. distribution in the sheath(cladding).text", "w")
            for i in range(len(self.rj)):
                f.write("%10.5f  %15.5f\n" % (self.rj[i], self.Td[i]))
            f.close()

            self.Th = Tb -(Q*self.rk**2)/(2*h*rc)
            f = open("Radial temp. distribution in the coolant.text", "w")
            for i in range(len(self.rk)):
                f.write("%10.5f  %15.5f\n" % (self.rk[i], self.Td[i]))
            f.close()
        else:
            pass
        
       
       
qapp = QApplication(sys.argv)  
app  = Application(u'Thermal Hydraulic')
qapp.setStyleSheet("QFrame, QPushButton { background-color: palegoldenrod; border-width: 2px; border-color: darkkhaki}"
                   "QGroupBox { background-color: darkkhaki; border-width: 2px; border-color: darkkhaki}"
                   "QFrame { border: 2px solid #1EAE3D}"
                   #"QLabel, QAbstractButton { font: bold }"
                   "QStatusBar QLabel { font: normal }"
                   "QStatusBar::item { border-width: 1; border-color: darkkhaki; border-style: solid; border-radius: 2;}"
                   "QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView { background-color: cornsilk; selection - color: #0a214c}"
                   "QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView { selection-background-color:  #C19A6B;}"
                   "QLineEdit, QFrame { border-width: 1px; border-style: solid; border-color: darkkhaki; border-radius: 2px}"
                   "QLabel { border: none; padding: 0; background: none; }")                  
                    #"QPlainTextEdit {font-family: Monospace; font-size: 13px; background:  #E2E2E2; color:  #202020; border: 1px solid #1EAE3D;}")
#qApp.setStyleSheet("QLineEdit { background-color: red }")



app.show()
desktop = qapp.desktop()                                    # added
resolution = desktop.availableGeometry()                    # added 
app.move(resolution.center() - app.rect().center())         # added 
qapp.exec_()

