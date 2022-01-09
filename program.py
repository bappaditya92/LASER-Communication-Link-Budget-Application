#program to calculate receieved power of laser intercom system
import numpy as np
import math
import matplotlib.pyplot as plt 

def calc():
    Pt = 2
    r = 0.05
    D = 2*r
    f = 0.20 
    Area = 3.14*(r*r)
    div = 4e-3

    T = 1
    V = 1 
    lam = 0.808

    rtf = 0.9
    L = (3.91/V) * (np.power((0.55/lam),(0.585*(np.power(V,0.3333)))))

    c = 3*(np.power(10,8))
    e = 1.6e-19

    h = 6.626 * (1e-34)
    sb = 0.1
    FOV = D/f
    solid = (3.14/4)*(np.power(FOV,2))
    kB = 1.38e-23
    Temp = 300

    id = 3e-6
    BW = 10e8
    RL = 10e3
    respon = 0.55

    R1 = range(2000)
    l = len(R1)

    solar = np.zeros(l)
    A1 = np.zeros(l)
    ip = np.zeros(l)
    iS = np.zeros(l)
    iDark = np.zeros(l)
    iShot = np.zeros(l)
    ither = np.zeros(l)
    snr = np.zeros(l)
    A = np.zeros(l)
    P1 = np.zeros(l)


    for j in range(1,l):
        solar[j] = sb*solid*Area*10
        A1[j] = 3.14*(np.power((R1[j]*div),2))/4
        P1[j] = Pt*rtf*T*(Area/A1[j])*(np.exp(-(L)*R1[j]/1000))

        ip[j] = P1[j]*respon
        iS[j] = ip[j]+solar[j]*respon
        iDark[j] = np.power((2*e*BW*id),0.5)
        iShot[j] = np.power((2*e*BW*iS[j]),0.5)
        ither[j] = np.power((4*kB*Temp*BW/RL),0.5)

        #snr
        snr[j] = ip[j]/np.power(((np.power(iShot[j],2))+(np.power(iDark[j],2))+(np.power(ither[j],2))),0.5)
        #ber
        A[j] = 0.5*(1-np.power(((snr[j])/(2+snr[j])),0.5))
        A1[j] = math.erfc(snr[j]/1.414)


    '''
    # plot with various axes scales
    plt.figure()

    # linear
    plt.subplot(241)
    plt.plot(A1, R1)
    #plt.yscale('linear')
    plt.title('BER 2')
    plt.grid(True)


    # log
    plt.subplot(242)
    plt.plot(P1, R1)
    #plt.yscale('log')
    plt.title('Power Received')
    plt.grid(True)


    # symmetric log
    plt.subplot(243)
    plt.plot(ip,R1)
    #plt.yscale('symlog', linthreshy=0.01)
    plt.title('Photon current due to signal')
    plt.grid(True)

    plt.subplot(244)
    plt.plot(iS,R1)
    #plt.yscale('symlog', linthreshy=0.01)
    plt.title('Current due to signal and solar')
    plt.grid(True)

    plt.subplot(245)
    plt.plot(iDark,R1)
    #plt.yscale('symlog', linthreshy=0.01)
    plt.title('Dark current')
    plt.grid(True)

    plt.subplot(246)
    plt.plot(iShot,R1)
    #plt.yscale('symlog', linthreshy=0.01)
    plt.title('Shot Current')
    plt.grid(True)

    plt.subplot(247)
    plt.plot(snr,R1)
    #plt.yscale('symlog', linthreshy=0.01)
    plt.title('SNR')
    plt.grid(True)

    plt.subplot(248)
    plt.plot(ither,R1)
    #plt.yscale('symlog', linthreshy=0.01)
    plt.title('Thermal')
    plt.grid(True)

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)
    '''
    plt.subplot(211)
    plt.plot(A,R1)
    plt.grid(True)

    plt.subplot(212)
    plt.plot(snr,R1)

    plt.show()