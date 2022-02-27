import random 
from re import X
from tablaVerdad import *
import numpy as np
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import matplotlib.lines as mlines

import matplotlib.pyplot as plt


# n1 = 0.4
# n2 = 0.6
# n3 = 0.9
# n4 = 0.10

class index(QMainWindow):
    def __init__(self):
        super().__init__()
        self.listaErrores = []
        self.listaGeneraciones = []

        # self.w1 = 0
        # self.w2 = 0
        # self.w3 = 0
        # self.w4 = 0
        # self.w5 = 0

        # self.n1 = 0
        # self.n2 = 0
        # self.n3 = 0
        # self.n4 = 0
        # self.n5 = 0
        
        uic.loadUi("vista.ui", self)
        self.boton.clicked.connect(self.definirDatos)
      

    def definirDatos(self):
        listaW = []
        listaN = []
        valor_w1_aux = self.w1_.text() 
        valor_w1 = llenarW(valor_w1_aux)

        valor_w2_aux = self.w2_.text() 
        valor_w2 = llenarW(valor_w2_aux)

        valor_w3_aux = self.w3_.text() 
        valor_w3 = llenarW(valor_w3_aux)

        valor_w4_aux = self.w4_.text() 
        valor_w4 = llenarW(valor_w4_aux)

        valor_w5_aux = self.w5_.text() 
        valor_w5 = llenarW(valor_w5_aux)

        valor_w6_aux = self.w6_.text() 
        valor_w6 = llenarW(valor_w6_aux)
        listaW.append(valor_w1)
        listaW.append(valor_w2)
        listaW.append(valor_w3)
        listaW.append(valor_w4)
        listaW.append(valor_w5)
        listaW.append(valor_w6)
        
        n1 = float(self.n1_.text())
        n2 = float(self.n2_.text())
        n3 = float(self.n3_.text())
        n4 = float(self.n4_.text())
        n5 = float(self.n5_.text())
        listaN = [n1,n2,n3,n4,n5]
        
        #neurona1
        self.listaErrores.append(neurona(n1,listaW)[0])
        self.listaGeneraciones.append(neurona(n1,listaW)[1])
        #neurona2   
        self.listaErrores.append(neurona(n2,listaW)[0])
        self.listaGeneraciones.append(neurona(n2,listaW)[1])
        #neurona3  
        self.listaErrores.append(neurona(n3,listaW)[0])
        self.listaGeneraciones.append(neurona(n3,listaW)[1])
        #neurona4
        self.listaErrores.append(neurona(n4,listaW)[0])
        self.listaGeneraciones.append(neurona(n4,listaW)[1])
        #neurona5  
        self.listaErrores.append(neurona(n5,listaW)[0])
        self.listaGeneraciones.append(neurona(n5,listaW)[1])

        print(self.listaErrores)
        print(self.listaGeneraciones)
        
        figure1 = plt.figure(figsize=(15, 10))

        ax = plt.subplot(1,1,1)


        ax.set_title('Graficas')
        for x in range(5):
            ax.plot( self.listaGeneraciones[x], self.listaErrores[x], marker='o',label=f'N={listaN[x]}')

        ax.legend()

        plt.show()

        


      

def llenarW(valor_aux):
    if len(valor_aux) == 0:
        valor = round(random.uniform(0,1),3)
    elif len(valor_aux) >0:
        valor = float(valor_aux) 
    return valor


def neurona(n,lista_w):
    contador = 1
  
    listaError = []
    listaK = []
    #y_C_aux en lista
    y_c_aux = []
    #y_c_k en array
    y_c_k = []

    w_k = []

    w_k = lista_w
    while(True):
        u_k = np.dot(w_k,x)

        for u in u_k:
            if u < 0:
                y_c_aux.append(0)
            elif u >= 0:
                y_c_aux.append(1)

        y_c_k = np.array(y_c_aux)
        e_k = y_d - y_c_k
        
        formula_multiplicacion = np.dot(e_k,x.transpose())
  
        n_x_e_k = np.dot(n,formula_multiplicacion)

        wk_1 = w_k + n_x_e_k

    
    
        llego = np.all(y_d== y_c_k)

        errorTemporal = 0
        for i in range(len(e_k)):
            errorTemporal += e_k[i] ** 2
        error = np.sqrt(errorTemporal)
        listaError.append(error)

        # print('K: ',contador)
        listaK.append(contador)

        # print(f'datos Wk: {w_k}\n'+f'datos Uk: {u_k}\n'+f'Y deseada: {y_d}\n'+f'Y_coseguida: {y_c_k}\n'+f'error: {e_k}\n'+f' WK_1: {wk_1}\n'+
        # f'errorNoRaiz: {errorTemporal}\n'+f'errorRaiz: {error}\n'+f'N: {n}')
        # print('---------------------')
        contador = contador +1
        w_k = wk_1    
        y_c_aux.clear()
        y_c_k = []
        if  llego == True:
            break

    # print(listaError)
    return listaError,listaK




# neurona(n4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    sys.exit(app.exec_())








