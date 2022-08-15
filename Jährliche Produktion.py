#Module importieren
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# FAO Daten importieren
Berechnungsdaten = pd.read_csv('FAOSTAT.csv')

#Zur einfacheren handhabung in einen array umwandeln
asp = np.array(Berechnungsdaten)

# Plot vorbereiten
plt.figure(3,(10,5))


# Produzierte menge über die Jahreszahl auftragen
plt.plot(asp[31:,8],asp[31:,11]/1000000)#.grid(True)

# Beschrieftung der Achsen und Abbildung
plt.xlabel('Jahr')
plt.ylabel('Produzierte Menge [10⁶ t]')
plt.title('Jährliche weltweite Spargelproduktion')
plt.grid(1)

# Darstellen der Abbildung
plt.show()