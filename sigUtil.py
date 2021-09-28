# Utility functions for radar class lab 1
# Michael Christoffersen
# January 2020

import numpy as np

def arangeT(start, stop, fs):
    # Function to generate set of 
    # Args are start time, stop time, sampling frequency
    # Generates times within the closed interval [start, stop] at 1/fs spacing
    # Double precision floating point
    
    if(fs <= 0):
        raise ValueError("Sampling frequency must be greater than 0")
        
    if(stop < start):
        raise ValueError("Stop time must be greater than start time")
    
    # Slow way to do this, but probably fine for the homework
    seq = np.array([]).astype(np.double)
    c = start
    while c <= stop:
        seq = np.append(seq,c)
        c += 1/fs
        
    return seq

def arangeN(nsamp,fs):
    # Generate an nsamp length array with samples at fs frequency
    if(nsamp <= 0):
        raise ValueError("Number of samples must be greater than 0")
        
    if(fs <= 0):
        raise ValueError("Sampling frequency must be greater than 0")
        
    seq = np.zeros(nsamp).astype(np.double)
    c = 0
    
    for i in range(nsamp):
        seq[i] = c
        c += 1/fs
    
    return seq

def chirp(tlen,fstart,fstop,phase,fs):
    # Function to generate a linear chirp
    # Amplitude of 1, flat window
    
    t = arangeT(0,tlen,fs)
    b = (fstop-fstart)/tlen
    
    # Change what it returns
    return [0]

def corr(a,b):
    # Function to calculate circular correlation between two series
    # Make output array
    olen = max(len(a),len(b))
    xc = np.zeros(olen)
    
    # Arrange loops based on length of signals
    if(olen == len(a)):
        p = a
        s = b
    else:
        p = b
        s = a
        
    # Do corr
    for i in range(len(p)):
        for j in range(len(s)):
            k = i+j
            # Implement circular corr
            if(k >= len(p)):
                k -= len(p) 
            
            xc[i] += p[k] * s[j]

    return xc

def corrFFT(a,b):
    # Frequency domain circular correlation
    # Make output array
    # Arrange based on length of signals

    return [0]
    
def loadData(path):
    # Reads in 20180819-215243 trace file, returns as 2D array
    data = np.fromfile(path, dtype=np.float32)
    data = np.reshape(data, (1750, 4525), order='F')
    
    return data
    