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

plt.plot([laengeZA,laengeZB,laengeZC],[tZA1mhz,tZB1mhz,tZC1mhz])
plt.show()
plt.plot([laengeZA,laengeZB,laengeZC],[tZA2mhz,tZB2mhz,tZC2mhz])
plt.show()

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

