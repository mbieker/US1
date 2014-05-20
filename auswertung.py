'''
Created on 16.04.2014

@author: Julian Surmann & Martin Bieker
'''
from numpy import *
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize.minpack import curve_fit
from Tools import *
    

laenge = array([0.0397,0.0804,0.1205])*2
#Teil A:


t1MHz = array([31.0,60.9,90.0])*1e-6
t2MHz = array([29.9,59.7,88.7])*1e-6
v2MHz = laenge/t2MHz

v1MHz = laenge/t1MHz

print "A-Scan mit Impuls-Echo-Verfahren:"
print v2MHz
print v1MHz


m1, b1 = lin_reg(laenge,t1MHz) 
m2, b2 = lin_reg(laenge,t2MHz)
print "lineare Regression 1 MHz : m=%s, b=%s" % (m1,b1)
print "lineare Regression 2 MHz: m=%s, b=%s"% (m2,b2) 
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

plt.plot(x,(x*m1.n+b1.n)*1e6) 


plt.xlabel("Zylinderlaenge (Hin- und Rueckweg) [m]")
plt.ylabel(r"Laufzeit [$\mu s$]")
plt.savefig("Fig1.png")
plt.close() 


plt.plot(laenge,t2MHz*1e6,'x')

plt.plot(x,(x*m2.n+b2.n)*1e6)

plt.xlabel("Zylinderlaenge (Hin- und Rueckweg) [m]")
plt.ylabel(r"Laufzeit [$\mu s$]")
plt.savefig("Fig2.png")
plt.close() 


#Regressionsdaten als Tabelle ausgeben

c_1 = 1/m1
c_2 = 1/m2
data = array([[1,2],[b1,b2],[m1,m2],[c_1,c_2]])
print make_LaTeX_table(data.T, 
                       [r'$f/\si{\mega\hertz}$}', 'dt', 'm', 'c'])

#Durchschnitt berechnen

c = 0.5*(c_1+c_2)
print "Mittelwert c = %s" % c 
#Teil B:


tD = array([15.9,30.7,45.1])*1e-6

m3, b3 = lin_reg(laenge/2,tD) 
print """Durchschallung lineare Regression2 MHz :
     m=%s, b=%s""" % (m3,b3)


# Das ganze nochmal mit Curve Fit


params, cov = curve_fit(y,laenge/2, tD)
m3_ = ufloat(params[0],sqrt(cov[0][0]))
b3_ = ufloat(params[1],sqrt(cov[1][1]))
print "Mit curve_fit : m1=  %s und b1 = %s" %  (m3_,b3_)

# Durchschallungsverfahren plotten

plt.plot(laenge/2, tD*1e6,'x')

x= linspace(0,0.13)

plt.plot(x,(m3.nominal_value*x+b3.nominal_value)*1e6)
plt.xlabel("Zylinderlaenge [m]")
plt.ylabel(r"Laufzeit [$\mu s$]")
plt.savefig("Fig3.png")


print """m und b aus linearer Regression 
        der 1 MHz Sonde: m=%s, b=%s""" % (m3,b3)
print "Errechnete Durchschallverf. aus m (linear):"
print (1/m3)


#Teil C:
#
t_unten = array([45.0,46.1,11.7,17.9,24.1,30.4,
                 36.2,42.0,47.8,0.00,13.2])*1e-6
t_oben  = array([16.1,14.9,43.6,40.8,35.6,30.0,
                 24.4,18.3,12.2,6.5,41.7])*1e-6

t_unten = t_unten-b1_
t_oben  = t_oben -b1_


s_unten = 0.5*t_unten*c  
s_oben = 0.5*t_oben*c

d = 0.08 - s_unten-s_oben

data = array([range(1,12),s_oben*1e2,
               s_unten*1e2, d*1e2 ])# Laengen in centimetern

print make_LaTeX_table(data.T, ['n','so','su', 'd'])

#Teil D:
print "Untersuchung des Augenmodells:"
zeiten =array([11.7,18.3,25.3,69.8])*1e-6

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
print sAuge
