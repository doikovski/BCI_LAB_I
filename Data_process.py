# MNE - Data aquisition
import mne

# Tools
import numpy as np
import matplotlib.pyplot as plt

# SKLEARN - Machine learning
import sklearn.decomposition as skd
import sklearn.svm as svm

# FLAGS
FLAG_PLOT = True
plt.ion()

# ======= NOTE =======

# For LaTeX fonts
    # plt.rc('text', usetex=True)
    # plt.rc('font', family='serif')

# ======= BDF file =======

# File path and reading
Recording1 = 'Process/Recording2.bdf'
    # Used paths: Process/Recording.bdf

raw = mne.io.read_raw_edf(Recording1, preload=True)
#raw2 = mne.io.read_raw_edf(Recording2, preload=True)
#raw3 = mne.io.read_raw_edf(Recording3, preload=True)
#raw4 = mne.io.read_raw_edf(Recording4, preload=True)

#raw.append(raw2,preload=True)
#raw.append(raw3,preload=True)
#raw.append(raw4,preload=True)

print('\n\t============ BDF file info ============\n')
print(raw.info)
print('\n')

#raw.plot_psds(tmin=100.0,tmax=101.0,fmin=1,fmax=40,picks=picks,n_fft=2048)



# Low-pass filter at 40 Hz, use only for visualisation of raw data (not for analysis)
    # raw.filter(None, 40)  # Low-pass filter

# Electrodes used for processing
#picks = [4,5,9,10,11,12,13,14,17,18,19,20,21,31,32,38,39,40,44,45,46,47,48,49,50,51,54,55,56,57,58] # Electrodes for motor imagery
    # picks = None # Uses all electrodes
picks = [47, 12, 48, 49, 32] # NOTE For quick development (central electrodes)
print 'Electrodes used:', picks

# Baseline
baseline = [-0.1,0] # means from the first instant to t = 0

# Event time for data analysis
    # Event Times : events[:,0]/2048
    # Event types : events[:,2]
tmin, tmax = -2, 5 # in secoonds
sampling_time = 2048

# Spatial filtering
spatial_filter = 'CAR'
pick_CAR = range(64) # Electrodes used to compute CAR for each time
picks_spatial_filter = picks # Electrodes on which spatial filtering is applied
execfile('Process/spatial_filter.py') # WIP
#raw.plot_psds(tmin=0.0, tmax=10.0, fmin=0, fmax=40, picks=[4]) # Check effect of spatial filtering

# Events and epochs
execfile('Process/events.py')
execfile('Process/epochs.py')

# ======= Frequency =======

n_cycles = 2  # number of cycles in Morlet wavelet
f_min,f_max = 2.0, 40.0
frequencies = np.arange(f_min, f_max, 2) # frequencies of interest
Fs = raw.info['sfreq']  # sampling in Hz
picks_tfr = range(len(picks)) # Electrode from picks used for graphs # From 0 to len(picks)-1

execfile('Process/frequency.py')

# ======= Machine learning =======

execfile('Process/ml_features.py')
execfile('Process/ml_classification.py')