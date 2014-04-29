'''
Created on 16.04.2014

@author: martin
'''
from numpy import *
from uncertainties import ufloat
import matplotlib.pyplot as plt


def make_LaTeX_table(data,header, flip= 'false', onedim = 'false'):
    output = '\\begin{table}\n\\centering\n\\begin{tabular}{'
    #Get dimensions
    if(onedim == 'true'):
        if(flip == 'false'):
        
            data = array([[i] for i in data])
        
        else:
            data = array([data])
    
    row_cnt, col_cnt = data.shape
    header_cnt = len(header)
    
    if(header_cnt == col_cnt and flip== 'false'):
        #Make Format
        
        for i in range(col_cnt):
            output += 'S'
        output += '}\n\\toprule\n{'+ header[0]
        for i in range (1,col_cnt):
            output += '} &{ ' + header[i]
        output += ' }\\\\\n\\midrule\n'
        for i in data:
            if(isinstance(i[0],(int,float,int32))):
                output += str( i[0] )
            else:
                output += ' ${:L}$ '.format(i[0])
            for j in range(1,col_cnt):
                if(isinstance(i[j],(int,float,int32))):
                    output += ' & ' + str( i[j])
                else:
                    output += ' & ' + str( i[j]).replace('/','')
                
            output += '\\\\\n'
        output += '\\bottomrule\n\\end{tabular}\n\\label{}\n\\caption{}\n\\end{table}\n'
                            
        return output

    else:
        return 'ERROR'



    
def err(data):
    mean = data.mean()
    N = len(data)
    err = 0
    for i in data:
        err += (i - mean)**2
    err = sqrt(err/((N-1)*N))
    return ufloat(mean,err)


def lin_reg(x,y):
    N = len(x)
    sumx = x.sum()
    sumy = y.sum()
    sumxx = (x*x).sum()
    sumxy = (x*y).sum()
    m = (sumxy - sumx*sumy/N)/(sumxx- sumx**2/N)
    b = sumy/N - m*sumx/N
    
    sy = sqrt(((y - m*x - b)**2).sum()/(N-1))
    m_err = sy *sqrt(N/(N*sumxx - sumx**2))
    b_err= m_err * sqrt(sumxx/N)
    return ufloat(m,m_err), ufloat(b,b_err)
  
    
    
laengeZA = 0.0397
laengeZB = 0.0804
laengeZC = 0.1205

#Teil A:

tZC2mhz = 0.0000887
tZB2mhz = 0.0000597
tZA2mhz = 0.0000299

tZC1mhz = 0.000090
tZB1mhz = 0.0000609
tZA1mhz = 0.000031

vZC2mhz = 2*laengeZC/tZC2mhz
vZB2mhz = 2*laengeZB/tZB2mhz
vZA2mhz = 2*laengeZA/tZA2mhz

vZC1mhz = 2*laengeZC/tZC1mhz
vZB1mhz = 2*laengeZB/tZB1mhz
vZA1mhz = 2*laengeZA/tZA1mhz

print "A-Scan mit Impuls-Echo-Verfahren:"
print "vZC2mhz: "
print vZC2mhz
print "vZB2mhz: "
print vZB2mhz
print "vZA2mhz: "
print vZA2mhz
print "vZC1mhz: "
print vZC1mhz
print "vZB1mhz: "
print vZB1mhz
print "vZA1mhz: "
print vZA1mhz


laengen=array([2*laengeZA,2*laengeZB,2*laengeZC])
zeiten=array([tZA1mhz,tZB1mhz,tZC1mhz])
zeiten2=array([tZA2mhz,tZB2mhz,tZC2mhz])
m1, b1 = lin_reg(laengen,zeiten) ## Werte besser in Variablen speichern. 
m2, b2 = lin_reg(laengen,zeiten2)
print "m und b aus linearer Regression der 1 MHz Sonde: m=%s, b=%s" % (m1,b1) # so wird schoener formatiert und GERUNDET
print "m und b aus linearer Regression der 2 MHz Sonde: m=%s, b=%s"% (m2,b2) 




plt.plot([2*laengeZA,2*laengeZB,2*laengeZC],[tZA1mhz,tZB1mhz,tZC1mhz],'x')

x=linspace(0,0.25)

plt.plot(x,x*m1.n+b1.n) ## Hier musst du als erstes Argument nocheinmal 'x' angeben !!!!! 

plt.xlabel("Zylinderlaenge (Hin- und Rueckweg) [m]")
plt.ylabel("Laufzeit [10^(-6)sec]")
plt.xlim(0, 0.25)
plt.ylim(0, 0.0001)
plt.savefig("Fig1.png")
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet


plt.plot([2*laengeZA,2*laengeZB,2*laengeZC],[tZA2mhz,tZB2mhz,tZC2mhz],'x')

x=linspace(0,0.25)

plt.plot(x,x*m2.n+b2.n) ## Hier musst du als erstes Argument nocheinmal 'x' angeben !!!!! 

plt.xlabel("Zylinderlaenge (Hin- und Rueckweg) [m]")
plt.ylabel("Laufzeit [10^(-6)sec]")
plt.xlim(0, 0.25)
plt.ylim(0, 0.0001)
plt.savefig("Fig2.png")
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet



print "Errechnete Schallgeschwindigkeiten aus m:"
print 1/0.0003651045527787822
print 1/0.0003638669517641943
print "Wellenlaufzeit durch Schutzschicht:"
print "1 MHz:"
print 2.070563067616667e-06
print "2 MHz:"
print 1.0690742703565743e-06
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
print sAuge

