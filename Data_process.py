import mne

# ===================================== BDF file =====================================

# File path and reading
Recording = '../Measures/120315-DK-JA/120315-VT-DK1.bdf'
execfile('Process/bdf_read.py')

# Low-pass filter at 40 Hz
raw.filter(None, 40)  # Low-pass filter

# Data parameters
picks = mne.pick_types(raw.info, meg=False, eeg=True, eog=False, stim=False, exclude='bads')
# ORIGINAL: picks = mne.pick_types(raw.info, meg=True, eeg=True, eog=True, stim=False, exclude='bads')
baseline = (None, 0) # means from the first instant to t = 0

# Time for data analysis
tmin = 0
tmax = 30 # t_max = 398 for thos file

# Events and epochs
execfile('Process/events.py')
execfile('Process/epochs.py')

# ===================================== Feature extraction =====================================

execfile('Process/frequency.py')
# ===================================== Classifer =====================================