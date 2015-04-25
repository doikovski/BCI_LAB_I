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

# Plot TFT Morlet
tmin_sit_first = event_sit_go_time[0][0]
tmax_sit_first = event_sit_go_time[0][1]

print('Plotting TFT Morlet graphs')

#power_sit.plot([0], baseline=(-0.5, 0), mode=None)
#plt.title('S-transform (power)')

def PlotTfrPower(power_sit, picks_tfr):
    fig_power_sit = power_sit.plot(picks=picks_tfr, # From 0 to n_electrodes_used-1
                            #tmin=tmin, tmax=tmax, 
                            #fmin=00, fmax=30, 
                            #vmin=0, vmax=0.0000001, 
                            dB=True,
                            show=False)
    # NOTE: Creates issues with multiprocessing

    plt.title('Averaged power from TFR MORLET')
    plt.show() # block=False

plot_tfr_power = mp.Process(target=PlotTfrPower,args=[power_sit,picks_tfr])
plot_tfr_power.start()

#itc_sit.plot([0], baseline=None, mode=None)
#plt.title('S-transform (ITC)')

def PlotTfrItc(itc_sit, picks_tfr):
    fig_itc_sit = itc_sit.plot(picks=picks_tfr,
                    #tmin=tmin, tmax=tmax, 
                    #fmin=00, fmax=30, 
                    vmin=0,
                    show=False)
    plt.title('Intertrial coherence (ITC) from TFR MORLET')
    plt.show() # block=False

plot_tfr_itc = mp.Process(target=PlotTfrItc,args=[itc_sit,picks_tfr])
plot_tfr_itc.start()

print('DONE: Calculating frequency and plotting corresponding graphs\n')

# PSD estimator (Alternative to TFR Morlet)
    #mne.decoding.PSDEstimator(sfreq=Fs, 
                            #fmin=0, fmax=40, 
                            #bandwidth=None, 
                            #adaptive=False, 
                            #low_bias=True, 
                            #n_jobs=1, 
                            #normalization='length', 
                            #verbose=None)
