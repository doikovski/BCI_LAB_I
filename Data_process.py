# MNE - Data aquisition
import mne

# Tools
import numpy as np
import matplotlib.pyplot as plt

# SKLEARN - Machine learning
    # import sklearn as sk

# Optional packages
FLAG_MP = False # Flag used to plot figures using multiprocessing, not for Windows or iOS
if FLAG_MP:
    import multiprocessing as mp

# FLAGS
FLAG_PLOT = False

if FLAG_PLOT and FLAG_MP:
    import sys
    sys.exit("ERROR, FLAG_PLOT and FLAG_MP cannot be both used at the same time")

# ======= NOTE =======

# Multiprocessing
    # Multiprocessing is used when FLAG_MP is True and allows to continue processing
    # while plotting
    # The alternative is to use the FLAG_PLOT (True) to plot without using multiprocessing, 
    # but the execution will stop at each plot until the windows is closed

# For LaTeX fonts
    # plt.rc('text', usetex=True)
    # plt.rc('font', family='serif')

# ======= BDF file =======

# File path and reading
Recording = 'Process/Recording.bdf'
    # Used paths: Process/Recording.bdf
execfile('Process/bdf_read.py')

# Low-pass filter at 40 Hz, use only for visualisation of raw data (not for analysis)
    # raw.filter(None, 40)  # Low-pass filter

# Electrodes used for processing
    # picks = [4,5,9,10,11,12,13,14,17,18,19,20,21,31,32,38,39,40,44,45,46,47,48,49,50,51,54,55,56,57,58] # Electrodes for motor imagery
    # picks = None # Uses all electrodes
picks = [4,5,9] # For quick development
print 'Electrodes used:', picks

# Baseline
baseline = None # means from the first instant to t = 0

# Event time for data analysis
    # Event Times : events[:,0]/2048
    # Event types : events[:,2]
tmin, tmax = -2, 5 # in secoonds
sampling_time = 2048

# Events and epochs
execfile('Process/events.py')
execfile('Process/epochs.py')

# Spatial filtering
execfile('Process/spatial_filter.py') # WIP
#raw.plot_psds(tmin=0.0, tmax=10.0, fmin=0, fmax=40, picks=[0]) # Check effect of spatial filtering

# ======= Frequency =======

n_cycles = 2  # number of cycles in Morlet wavelet
frequencies = np.arange(2, 40, 2) # frequencies of interest
Fs = raw.info['sfreq']  # sampling in Hz
picks_tfr = [0] # Electrode from picks used for graphs # From 0 to len(picks)-1

execfile('Process/frequency.py')

# ======= Machine learning =======

execfile('Process/ml_features.py')
execfile('Process/ml_classification.py')
