# import der Module
import pandas as pd, pandas
import numpy as np
import matplotlib.pyplot as plt

#import der datensätze
e=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='Bonitur')
f=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='7dpi Bonitur')
g=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='12dpi Bonitur')


#Um die Daten der Gruppe einfacher aufrufen zu können, werden zwei Dictionarys angelegt
Dic1 = {
            'Ba': [i for i in range(1,10)],
            'Ga': [i for i in range(10,19)],
            'Va': [i for i in range(19,28)],
            'Xa': [i for i in range(28,37)],
            'La': [i for i in range(37,46)],
            'Ra': [i for i in range(46,55)],
            'Sa': [i for i in range(55,64)],
            'Fa': [i for i in range(64,73)],
            'Ca': [i for i in range(73,82)],
           
            'Bb': [i for i in range(82,91)],
            'Gb': [i for i in range(91,100)],
            'Vb': [i for i in range(100,109)],
            'Xb': [i for i in range(109,118)],
            'Lb': [i for i in range(118,127)],
            'Rb': [i for i in range(127,136)],
            'Sb': [i for i in range(136,145)],
            'Fb': [i for i in range(145,154)],
            'Cb': [i for i in range(154,163)],
    
    
            'Bc': [i for i in range(163,172)],
            'Gc': [i for i in range(172,181)],
            'Vc': [i for i in range(181,190)],
            'Xc': [i for i in range(190,199)],
            'Lc': [i for i in range(199,208)],
            'Rc': [i for i in range(208,217)],
            'Sc': [i for i in range(217,226)],
            'Fc': [i for i in range(226,235)],
            'Cc': [i for i in range(235,244)]
           
          }


Dic3 = {
            'B': [i for i in range(1,16)],
            'G': [i for i in range(16,31)],
            'V': [i for i in range(31,46)],
            'X': [i for i in range(46,61)],
            'L': [i for i in range(61,76)],
            'R': [i for i in range(76,91)],
            'S': [i for i in range(91,106)],
            'F': [i for i in range(106,121)],
            'C': [i for i in range(121,136)],}

e = np.array(e)
f = np.array(f)
g = np.array(g)

Sorten = ['B','G','V','X','L','R','S','F','C']
Variante = ['a','b','c']

def probe_e(Sorte,header):
    Gruppen = Dic1
    klassen = ['Probe','Wurzelanzahl','Wurzellänge','Wurzel_frischgewicht','Spross_frischgewicht','Sproßanzahl']
    pro = klassen.index(header)
    # Erstellen der Listen
    Hohe = []
    Mittel = []
    Kontrolle = []
    # Füllen der Listen
    for q in Variante:
        if q == 'a':
            for i in Gruppen[Sorte + q]:
                i -=1   
                if e[i,:][0] in Gruppen[Sorte + q]:
                    Hohe.append(e[i,pro])
        if q == 'b':
            for i in Gruppen[Sorte + q]:
                i -=1   
                if e[i,:][0] in Gruppen[Sorte + q]:
                    Mittel.append(e[i,pro])
        if q == 'c':
            for i in Gruppen[Sorte + q]:
                i -=1   
                if e[i,:][0] in Gruppen[Sorte + q]:
                    Kontrolle.append(e[i,pro])
    return Kontrolle, Mittel, Hohe
#print(probe_e('B'))



def probe_fg(Sorte,data,header1, header2, header3):
    Gruppen = Dic3
    klassen = [None,'Sorte','Inokulum','Anzahl Wurzeln a','Sproßzahl a','Inokulum','Anzahl Wurzeln b',
               'Sproßzahl b','Inokulum','Anzahl Wurzeln c','Sproßzahl c']
    # Erstellen der Listen
    Hohe = []
    Mittel = []
    Kontrolle = []
    # Füllen der Listen
    for q in Variante:
        if q == 'a':
            for i in Gruppen[Sorte]:
                i -=1   
                if data[i,:][0] in Gruppen[Sorte]:
                    Hohe.append(data[i,klassen.index(header1)])
        if q == 'b':
            for i in Gruppen[Sorte]:
                i -=1   
                if data[i,:][0] in Gruppen[Sorte]:
                    Mittel.append(data[i,klassen.index(header2)])
        if q == 'c':
            for i in Gruppen[Sorte]:
                i -=1   
                if data[i,:][0] in Gruppen[Sorte]:
                    Kontrolle.append(data[i,klassen.index(header3)])
    return Kontrolle, Mittel, Hohe




# fünf_dpi_c, fünf_dpi_b, fünf_dpi_a = probe_e('B')
# sieben_dpi_c, sieben_dpi_b, sieben_dpi_a = probe_fg('B',f,'Anzahl Wurzeln a','Anzahl Wurzeln b','Anzahl Wurzeln c')
# zwölf_dpi_c, zwölf_dpi_b, zwölf_dpi_a = probe_fg('B',g,'Anzahl Wurzeln a','Anzahl Wurzeln b','Anzahl Wurzeln c')



# vorbereiten des Plots 
fig, axes = plt.subplots(nrows=3, ncols=3)# bei panda läuft das mit den subplots anders


print('wurzelanzahl')
#die sorten werden nacheinander durch gegagen und nacheinander in den Plot eingesetzt
for i,j,k in zip(Sorten,[0,0,0,1,1,1,2,2,2],[0,1,2,0,1,2,0,1,2]):
    
    # für jede sorte werden die Daten der drei Varianten für die drei Probentage in variablen gespeichert
    fünf_dpi_c, fünf_dpi_b, fünf_dpi_a = probe_e(i,'Wurzelanzahl')
    sieben_dpi_c, sieben_dpi_b, sieben_dpi_a = probe_fg(i,f,'Anzahl Wurzeln a','Anzahl Wurzeln b','Anzahl Wurzeln c')
    zwölf_dpi_c, zwölf_dpi_b, zwölf_dpi_a = probe_fg(i,g,'Anzahl Wurzeln a','Anzahl Wurzeln b','Anzahl Wurzeln c')
    
    
    # die pandas funktion braucht zum plotten der grafiken die daten in form eines Dictionary
    plotdata = pd.DataFrame({
        "Kontrolle":[np.mean(fünf_dpi_c), 0, np.mean(zwölf_dpi_c)], #  kontrolle 7di fehlt  #np.mean(sieben_dpi_c)
        "Mittlere Sporenkonzentration":[np.mean(fünf_dpi_b), np.mean(sieben_dpi_b), np.mean(zwölf_dpi_b)],
        "Hohe Sporenkonzentration":[np.mean(fünf_dpi_a), np.mean(sieben_dpi_a), np.mean(zwölf_dpi_a)]}, 
        index=["5dpi", "7dpi", "12dpi"] )
    
#    print(i,plotdata)
    color1 =['#e8e6e3', '#f5e20a', '#f50a0a']
    #Plotten der ergebnisse in die subplots, die y-achse hat immer den gleichen bereich
    dt = plotdata.plot(kind="bar", legend=False, color=color1, ax=axes[j, k], figsize = (13, 13), title = f'Sorte:{i}',rot =0,
                     ylim = (0,2.25)).grid(axis='y',alpha = 0.5)#
    #dt.set_ylim(0, 2)

    
    




#%%  # trennzeichen, somit wird nur ein teil des programms ausgeführt
fig, axes = plt.subplots(nrows=3, ncols=3)# bei panda läuft das mit den subplots anders


print('Sproßanzahl')
for i,j,k in zip(Sorten,[0,0,0,1,1,1,2,2,2],[0,1,2,0,1,2,0,1,2]):
    
    fünf_dpi_c, fünf_dpi_b, fünf_dpi_a = probe_e(i,'Sproßanzahl')
    sieben_dpi_c, sieben_dpi_b, sieben_dpi_a = probe_fg(i,f,'Sproßzahl a','Sproßzahl b','Sproßzahl c')
    zwölf_dpi_c, zwölf_dpi_b, zwölf_dpi_a = probe_fg(i,g,'Sproßzahl a','Sproßzahl b','Sproßzahl c')


    plotdata = pd.DataFrame({
        "Kontrolle":[np.mean(fünf_dpi_c), 0, np.mean(zwölf_dpi_c)], #  kontrolle 7di fehlt  #np.mean(sieben_dpi_c)
        "Mittlere Sporenkonzentration":[np.mean(fünf_dpi_b), np.mean(sieben_dpi_b), np.mean(zwölf_dpi_b)],
        "Hohe Sporenkonzentration":[np.mean(fünf_dpi_a), np.mean(sieben_dpi_a), np.mean(zwölf_dpi_a)]}, 
        index=["5dpi", "7dpi", "12dpi"] )
    
    
#    print(i,plotdata)
    color1 =['#e8e6e3', '#f5e20a', '#f50a0a']
    plotdata.plot(kind="bar", legend=False, color=color1, ax=axes[j, k], figsize = (13, 13), title = f'Sorte:{i}',rot =0,
                     ylim = (0,2)).grid(axis='y')#

