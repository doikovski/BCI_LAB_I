print('\n\t============ Frequency analysis ============\n')

import numpy as np
import matplotlib.pyplot as plt

n_cycles = 2  # number of cycles in Morlet wavelet
frequencies = np.arange(7, 30, 3)  # frequencies of interest
Fs = raw.info['sfreq']  # sampling in Hz

print('ONLY power, phase_lock LEFT')

from mne.time_frequency import induced_power

#power, phase_lock = induced_power(epoch_sit_data,
#				  Fs=Fs, 
#				  frequencies=frequencies, 
#				  n_cycles=2, 
#				  n_jobs=1)

# Function induced_power is deprecated; 
# induced_power will be removed in release 0.9. 
# Use tfr_morlet instead.

'''
tfr_morlet(epochs, freqs, n_cycles, use_fft=False, return_itc=True, decim=1, n_jobs=1)
    Compute Time-Frequency Representation (TFR) using Morlet wavelets
    
    Parameters
    ----------
    epochs : Epochs
        The epochs.
    freqs : ndarray, shape (n_freqs,)
        The frequencies in Hz.
    n_cycles : float | ndarray, shape (n_freqs,)
        The number of cycles globally or for each frequency.
    use_fft : bool
        The fft based convolution or not.
    return_itc : bool
        Return intertrial coherence (ITC) as well as averaged power.
    decim : int
        The decimation factor on the time axis. To reduce memory usage.
    n_jobs : int
        The number of jobs to run in parallel.
    
    Returns
    -------
    power : AverageTFR
        The averaged power.
    itc : AverageTFR
        The intertrial coherence (ITC). Only returned if return_itc
        is True.
'''

power, itc = mne.time_frequency.tfr_morlet(epochs=epoch_sit, 
					   freqs=frequencies, 
					   n_cycles=2)

print('Done calculating power & itc')

power.plot([0], baseline=(-0.5, 0), mode=None)
plt.title('S-transform (power)')

itc.plot([0], baseline=None, mode=None)
plt.title('S-transform (ITC)')


print('Done plotting power & itc')

'''
# PSD estimator
mne.decoding.PSDEstimator(sfreq=Fs, 
			  fmin=0, fmax=40, 
			  bandwidth=None, 
			  adaptive=False, 
			  low_bias=True, 
			  n_jobs=1, 
			  normalization='length', 
			  verbose=None)
'''

