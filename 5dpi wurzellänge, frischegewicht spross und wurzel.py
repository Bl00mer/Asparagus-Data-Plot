
import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt


e=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='Bonitur')



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

e=pandas.read_excel('PYTHON DATEN.xlsx', sheet_name='Bonitur')
e = np.array(e)
Sorten = ['B','G','V','X','L','R','S','F','C']
Variante = ['a','b','c']
e_klassen = ['Probe','Wurzelanzahl','Wurzellänge','Wurzel_frischgewicht','Spross_frischgewicht']
Gruppen = Dic1


def e_probe (sorte,protein):
    pro = e_klassen.index(protein)
    Hohe = []
    Mittel = []
    Kontrolle = []
    for q in Variante:
        if q == 'a':
            for i in Gruppen[sorte + q]:
                i -=1   
                if e[i,:][0] in Gruppen[sorte + q]:
                    Hohe.append(e[i,pro])
        if q == 'b':
            for i in Gruppen[sorte + q]:
                i -=1   
                if e[i,:][0] in Gruppen[sorte + q]:
                    Mittel.append(e[i,pro])
        if q == 'c':
            for i in Gruppen[sorte + q]:
                i -=1   
                if e[i,:][0] in Gruppen[sorte + q]:
                    Kontrolle.append(e[i,pro])

    c,b,a=np.mean(Kontrolle),np.mean(Mittel),np.mean(Hohe)
    print( sorte,' \n', b-c,a-c)
    return  Kontrolle, Mittel, Hohe    
    

def plot_gene(Test,Y_label):
    fig = plt.figure(1,(15,10))
    print(f'{Test}')
    for i in Sorten:
        #für jede sorte einen subplot anlegen
        ax = fig.add_subplot(3,3,Sorten.index(i)+1)
        
        #boxplots mit den listen von a und c
        bp = ax.boxplot(e_probe(i,Test), notch=None, vert=None, patch_artist=True, widths=None)
   #     print(e_probe(i,Test))
        colors = ['#e8e6e3', '#f5e20a', '#f50a0a']
 
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)

        # X-Achsenbeschrieftung
        if len(Variante) ==2:
            ax.set_xticklabels(['c', 'a'])
        else:
            ax.set_xticklabels(['c','b', 'a'])
        
        ax.grid(axis='y',alpha = 0.5)            
                #Median
        for median in bp['medians']:
            median.set(color ='black',linewidth = 1)
            
        # Außreiser Punkte 
        for flier in bp['fliers']:
            flier.set(marker ='D',
                  color ='#e7298a',
                  alpha = 0)# wenn ich alpha gelich null setzte kann ich die AUSREIßER entfernen
        
        # Titel
        plt.title(f'Sorte:{i}')

        plt.ylabel(Y_label)
    plt.show()
    
    
#plot_gene('Wurzellänge','[cm]')
plot_gene('Wurzel_frischgewicht','[g]')
#plot_gene('Spross_frischgewicht','[g]')