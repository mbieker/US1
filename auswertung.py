'''
Created on 16.04.2014

@author: martin
'''
from numpy import *
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize.minpack import curve_fit
from Tools import *
    

laenge = array([0.0397,0.0804,0.1205])*2
#Teil A:

t2MHz = array([29.9,59.7,88.7])*1e-6
t1MHz = array([31.0,60.9,90.0])*1e-6

v2MHz = laenge/t2MHz

v1MHz = laenge/t1MHz

print "A-Scan mit Impuls-Echo-Verfahren:"
print v2MHz
print v1MHz


m1, b1 = lin_reg(laenge,t1MHz) ## Werte besser in Variablen speichern. 
m2, b2 = lin_reg(laenge,t2MHz)
print "m und b aus linearer Regression der 1 MHz Sonde: m=%s, b=%s" % (m1,b1) # so wird schoener formatiert und GERUNDET
print "m und b aus linearer Regression der 2 MHz Sonde: m=%s, b=%s"% (m2,b2) 
# Das ganze nochmal mit Curve Fit

def y(x,m,b):
    return x*m + b
params, cov = curve_fit(y,laenge, t1MHz)
m1_ = ufloat(params[0],sqrt(cov[0][0]))
b1_ = ufloat(params[1],sqrt(cov[1][1]))

print "Mit curve_fit : m1=  %s und b1 = %s" %  (m1_,b1_)

params, cov = curve_fit(y,laenge, t2MHz)
m2_ = ufloat(params[0],sqrt(cov[0][0]))
b2_ = ufloat(params[1],sqrt(cov[1][1]))

print "Mit curve_fit : m2=  %s und b2 = %s" %  (m2_,b2_)



plt.plot(laenge,t1MHz*1e6,'x')

x=linspace(0,0.25)

plt.plot(x,(x*m1.n+b1.n)*1e6) ## Hier musst du als erstes Argument nocheinmal 'x' angeben !!!!! 


plt.xlabel("Zylinderlaenge (Hin- und Rueckweg) [m]")
plt.ylabel(r"Laufzeit [$\mu s$]")
plt.savefig("Fig1.png")
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet


plt.plot(laenge,t2MHz*1e6,'x')

plt.plot(x,(x*m2.n+b2.n)*1e6) ## Hier musst du als erstes Argument nocheinmal 'x' angeben !!!!! 
 

plt.savefig("Fig2.png")

plt.close() 



print "Errechnete Schallgeschwindigkeiten aus m (linear):"
print (1/m1)
print (1/m2)

print "Errechnete Schallgeschwindigkeiten aus m_ (nonlinear):"
print str(1/m1_)
print str(1/m2_)


#Teil B:

  
tdZC = 0.0000451
tdZB = 0.0000307
tdZA = 0.0000159

vdZC = laengeZC/tdZC
vdZB = laengeZB/tdZB
vdZA = laengeZA/tdZA

print ""
print "Durchschallverfahren:"
print "vdZC:"
print vdZC
print "vdZB:"
print vdZB
print "vdZA:"
print vdZA

#Teil C:
#
tvonuntenx=array([45.0,46.1,11.7,17.9,24.1,30.4,36.2,42.0,47.8,0.00,13.2])
tvonobenx =array([16.1,14.9,43.6,40.8,35.6,30.0,24.4,18.3,12.2,6.5,41.7])
tvonunten=tvonuntenx/1000000
tvonoben=tvonobenx/1000000
svonunten=0.5*(tvonunten-2.070563067616667e-06)*(0.5*(2738.94146865+2748.25728237))
svonoben=0.5*(tvonoben-2.070563067616667e-06)*(0.5*(2738.94146865+2748.25728237))
print "Ermittelte Abstaende der Loecher zur Oberflaeche von unten:"
print svonunten
print "Ermittelte Abstaende der Loecher zur Oberflaeche von oben:"
print svonoben
lochdicke=0.08-svonunten-svonoben
print "Dicke der Loecher:"
print lochdicke


#Teil D:
print "Untersuchung des Augenmodells:"
zeitenmikrosec=array([11.7,18.3,25.3,69.8])
zeiten=zeitenmikrosec/1000000
cL=2500
cGK=1410
sIris=0.5*(zeiten[0]-b2)*cGK
print "sIris:"
print sIris
sLinse1=0.5*(zeiten[1]-b2)*cGK
print "sLinse1:"
print sLinse1
sLinse2=sLinse1+0.5*(zeiten[2]-zeiten[1])*cL
print "sLinse2:"
print sLinse2
sAuge=sLinse2+0.5*(zeiten[3]-zeiten[2])*cGK
print "sAuge:"
print sAuge"""
