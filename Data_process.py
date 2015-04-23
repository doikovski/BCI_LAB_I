import mne

# ======= NOTE =======


# ======= BDF file =======

# File path and reading
Recording = 'Process/Recording.bdf'
execfile('Process/bdf_read.py')

# Low-pass filter at 40 Hz, use only for visualisation of raw data
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
tmin, tmax = 0, 5

# Events and epochs
execfile('Process/events.py')
execfile('Process/epochs.py')

# ======= Feature extraction =======

execfile('Process/frequency.py')

# ======= Classifer =======