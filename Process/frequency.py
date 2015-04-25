print('\n\t============ Frequency analysis ============\n')

# TFR Morlet
print('Caclculating TFR Morlet')
power_sit, itc_sit = mne.time_frequency.tfr_morlet(epochs=epoch_sit, 
                                                   freqs=frequencies, 
                                                   n_cycles=n_cycles,
                                                   use_fft=True)

power_stand, itc_stand = mne.time_frequency.tfr_morlet(epochs=epoch_stand, 
                                                   freqs=frequencies, 
                                                   n_cycles=n_cycles,
                                                   use_fft=True)
print('DONE: calculating power & itc')

# Plots
power_sit.plot([0], baseline=(-0.5, 0), mode=None)
plt.title('S-transform (power)')

itc_sit.plot([0], baseline=None, mode=None)
plt.title('S-transform (ITC)')


print('Done plotting power & itc\n')


# PSD estimator (Alternative to TFR Morlet)
    #mne.decoding.PSDEstimator(sfreq=Fs, 
                            #fmin=0, fmax=40, 
                            #bandwidth=None, 
                            #adaptive=False, 
                            #low_bias=True, 
                            #n_jobs=1, 
                            #normalization='length', 
                            #verbose=None)
