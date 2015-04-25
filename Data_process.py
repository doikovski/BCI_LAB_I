# MNE - Data aquisition
import mne

# Tools
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

# SKLEARN - Machine learning
    # import sklearn as sk

# ======= NOTE =======

# Multiprocessing required to continue with execution while keeping graphs

# For LaTeX fonts
    # plt.rc('text', usetex=True)
    # plt.rc('font', family='serif')

# ======= BDF file =======

# File path and reading
Recording = 'Process/Recording.bdf'
execfile('Process/bdf_read.py')

# Low-pass filter at 40 Hz, use only for visualisation of raw data (not for analysis)
    # raw.filter(None, 40)  # Low-pass filter

# Electrodes used for processing
    # picks = [4,5,9,10,11,12,13,14,17,18,19,20,21,31,32,38,39,40,44,45,46,47,48,49,50,51,54,55,56,57,58] # Electrodes for motor imagery
    # picks = None # Uses all electrodes
picks = [2,3,4] # For quick development
print 'Electrodes used:', picks

# Baseline
baseline = None # means from the first instant to t = 0

# Event time for data analysis
    # Event Times : events[:,0]/2048
    # Event types : events[:,2]
tmin, tmax = -2, 5

# Events and epochs
execfile('Process/events.py')
execfile('Process/epochs.py')

# ======= Frequency =======

n_cycles = 2  # number of cycles in Morlet wavelet
frequencies = np.arange(2, 40, 2) # frequencies of interest
Fs = raw.info['sfreq']  # sampling in Hz

# Electrode from picks used for graphs
picks_tfr = [0]

execfile('Process/frequency.py')

# ======= Machine learning =======

execfile('Process/ml_features.py')
execfile('Process/ml_classification.py')