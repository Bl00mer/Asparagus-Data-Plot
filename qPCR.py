

# Import der verwendeten Module
import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt


# Import der Versuchsdaten als in Form von verschiedenen Datensätzen
a=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='ac-Alle-LITERATUR_PRIMER') # liefert die erste Tabelle
b=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='abc-GBXR-PR1,PAL,POX') # liefert "Tabelle 2"
c=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='abc-GBXR-AOS,ERF1,AOC')
d=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='abc-GBXR-MS_PRIMER')



#Um die Daten der Gruppe in den einzelnen Datensätzen einfacher abrufen zu können, werden Dictionarys angelegt
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
Dic2 = {   
            'Ba': [i for i in range(1,4)],
            'Ga': [i for i in range(4,7)],
            'Xa': [i for i in range(7,10)],
            'Ra': [i for i in range(10,13)],
           
            'Bb': [i for i in range(13,16)],
            'Gb': [i for i in range(16,19)],
            'Xb': [i for i in range(19,22)],
            'Rb': [i for i in range(22,25)],
    
            'Bc': [i for i in range(25,28)],
            'Gc': [i for i in range(28,31)],
            'Xc': [i for i in range(31,34)],
            'Rc': [i for i in range(34,37)]
           
          }

##############################################

# Diese Funktion gibt abhängig vom genutzten Datensatz, der Sorte und des untersuchten Gens, Listen mit den Messergebnissen
# Kontrolle, mittlerer und hoher Sporenkonzentration aus

def probe (Sorte,protein,data):
#   um die richtige Spalte mit Daten einzulesen, indiziere ich über die Spaltenbezeichnung 
    pro = klassen.index(protein)
    # Erstellen der Listen für die Varianten a,b und c
    Hohe = []
    Mittel = []
    Kontrolle = []
    # Füllen der Listen mit den Messwerten
    for q in Variante:
        if q == 'a':
            for i in Gruppen[Sorte + q]:
                i -=1   # die -1 ist nötig da durch die Kopfzeile alle werte um eine zeile verschiebt
                if data[i,:][0] in Gruppen[Sorte + q]:
                    Hohe.append(data[i,pro])
        if q == 'b':
            for i in Gruppen[Sorte + q]:
                i -=1   
                if data[i,:][0] in Gruppen[Sorte + q]:
                    Mittel.append(data[i,pro])
        if q == 'c':
            for i in Gruppen[Sorte + q]:
                i -=1   
                if data[i,:][0] in Gruppen[Sorte + q]:
                    Kontrolle.append(data[i,pro])
    # Ausgabe der Listen, abhängig vom Datensatz       
    
    if len(Variante) ==2:
        return Kontrolle, Hohe
    else:
        return  Kontrolle, Mittel, Hohe 
    

# Diese Funktion nutzt die Listen mit den Messwerten und generiert Boxplots
def plot_gen (Gen,data):   
    print(Gen)
        
    fig = plt.figure(1,(15,11))
    for i in Sorten:
        # Mit jeder if-Abfrage wird hier zwischen den Datensätzen unterschieden, abhängig von der Anzahl der Sorten und Varianten

        #für jede Sorte einen subplot anlegen
        if len(Sorten) ==9:
            ax = fig.add_subplot(3,3,Sorten.index(i)+1)
        else:
            ax = fig.add_subplot(2,2,Sorten.index(i)+1)
        
        #Die Boxplots werden aufgrund der in der Funktion 'probe' generierten Listen erstellt
        bp = ax.boxplot(probe(i,Gen,data), notch=None, vert=None, patch_artist=True, widths=None)
        
        #hinzufügen eines horizontalen rasters
        ax.grid(axis='y',alpha = 0.3)            

        #t.test zum prüfen der signifikants
        #print(stats.ttest_ind(a=Kontrolle, b=Mittel, equal_var=True)) 

        
        # Im Grunde sind alle folgenden Zeilen bis zum Ende der for-Schleife nur kosmetischer Natur, wie dem entfernen von 
        # Außreiserpunkten und dem einfärben der verschiedenen Inokulationsvarianten
        
        # Die drei Inokulationsvarianten Kontrolle, 3*10³ und 3*10⁶ werden mit den Farben Grau, Gelb und Rot dargestellt
        if len(Variante) ==2:
            colors = ['#e8e6e3', '#f50a0a']
        else:
            colors = ['#e8e6e3', '#f5e20a', '#f50a0a']
 
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
        
        # Gibt jedem subplot den Titel der untersuchten Sorte
        plt.title(f'Sorte:{i}')
        
        # Median soll schwar sein
        for median in bp['medians']:
            median.set(color ='black',linewidth = 1)
    
        # X-Achsenbeschrieftung
        if len(Variante) ==2:
            ax.set_xticklabels(['c', 'a'])
        else:
            ax.set_xticklabels(['c','b', 'a'])
    
        # whiskers
        for whisker in bp['whiskers']:
            whisker.set(color ='#0b0a09',
                    linewidth = 1.5,
                    linestyle ="-")
        
        # Außreiser Punkte werden nicht dargestellt
        for flier in bp['fliers']:
            flier.set(marker ='D',
                  color ='#e7298a',
                  alpha = 0)# ist alfa gleich null sind die Außreiser transparent
       
        # changing color and linewidth of caps
        for cap in bp['caps']:
            cap.set(color ='#0b0a09',
                linewidth = 2)
        
        # Benennung der Y-Achse 
        plt.ylabel('∆ Cq')

    plt.show()

#######################################################################

# Für jeden Datensatz liegen andere Angaben vor daher müssen ja nach datensatz ein Paar variablen eingestellt werden

# zur einfacheren handhabung werden die Datensätze in arrays umgewandelt
a = np.array(a)
# Wahl des Dictionarys des Datensatzes
Gruppen = Dic1
# Spaltenbezeichnungen des Datensatzes
klassen = ['Probe','EF1alfa','PR1','PAL','POX','AOS','ERF1','AOC',None,'DCqPR1','DCqPAL','DCqPOX','DCqAOS','DCqERF1','DCqAOC']
# Sorten die im Datensatz untersucht wurden
Sorten = ['B','G','V','X','L','R','S','F','C']
#Inokulationsvarianten die untersucht wurden
Variante = ['a','c']    

# durch das entfernen des '#' zeichens lassen sich die Ergebnisse plotten

# plot_gen('DCqPR1',a)
# plot_gen('DCqPAL',a)
# plot_gen('DCqPOX',a)
# plot_gen('DCqAOS',a)
# plot_gen('DCqERF1',a)
# plot_gen('DCqAOC',a)


b = np.array(b)
Gruppen = Dic1
Sorten = ['B','G','X','R']
Variante = ['a','b','c']
klassen = ['Probe','EF1alfa','PR1','PAL','POX',None,'DCqPR1','DCqPAL','DCqPOX']

# plot_gen('DCqPR1',b)
# plot_gen('DCqPAL',b)
# plot_gen('DCqPOX',b)


c = np.array(c)
Gruppen = Dic2
Sorten = ['B','G','X','R']
Variante = ['a','b','c']
klassen = [None,'Probe','EF1 alfa','AOS','ERF1','AOC',None,'DCqAOS','DCqERF1','DCqAOC']

# plot_gen('DCqAOS',c)
# plot_gen('DCqERF1',c)
# plot_gen('DCqAOC',c)

d = np.array(d)
Gruppen = Dic2
Sorten = ['B','G','X','R']
Variante = ['a','b','c']
klassen = [None, 'Probe','EF1alfa','EIF5A2','LRPK','MTV1','PFK6','IDH1',None ,'DCqEIF5A2','DCqLRPK','DCqMTV1','DCqPFK6','DCqCICDH']

# plot_gen('DCqEIF5A2',d)
# plot_gen('DCqLRPK',d)
# plot_gen('DCqMTV1',d)
# plot_gen('DCqPFK6',d)
# plot_gen('DCqCICDH',d)