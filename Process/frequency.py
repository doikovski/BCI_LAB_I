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


tmin_sit_first = event_sit_go_time[0][0] # NOTE only to obtain time
tmax_sit_first = event_sit_go_time[0][1]

# Plot TFT Morlet
print('Plotting TFT Morlet graphs')

#power_sit.plot([0], baseline=(-0.5, 0), mode=None)
#plt.title('S-transform (power)')

if FLAG_MP:
    def PlotTfrPower(power_sit, picks_tfr):
        fig_power_sit = power_sit.plot(picks=picks_tfr, # From 0 to n_electrodes_used-1
                                #tmin=tmin, tmax=tmax, 
                                #fmin=00, fmax=30, 
                                #vmin=0, vmax=0.0000001, 
                                dB=True,
                                show=False)
        plt.title('Averaged power from TFR MORLET')
        plt.show() # block=False

    plot_tfr_power = mp.Process(target=PlotTfrPower,args=[power_sit,picks_tfr])
    plot_tfr_power.start()

elif FLAG_PLOT:
    fig_power_sit = power_sit.plot(picks=picks_tfr, # From 0 to n_electrodes_used-1
                                tmin=-1, tmax=3, 
                                #fmin=00, fmax=30, 
                                #vmin=0, vmax=0.0000001, 
                                vmin=-250,vmax=-150,
                                dB=True,
                                show=False)
    plt.title('Averaged power from TFR MORLET')
    plt.show() # block=False

#itc_sit.plot([0], baseline=None, mode=None)
#plt.title('S-transform (ITC)')

if FLAG_MP:
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
elif FLAG_PLOT:
    fig_itc_sit = itc_sit.plot(picks=picks_tfr,
                        #tmin=tmin, tmax=tmax, 
                        #fmin=00, fmax=30, 
                        vmin=0,
                        show=False)
    plt.title('Intertrial coherence (ITC) from TFR MORLET')
    plt.show() # block=False

print('DONE: Calculating frequency and plotting corresponding graphs\n')

# PSD estimator (Alternative to TFR Morlet)
print('Computing PSDE\n')
PSDE = mne.decoding.PSDEstimator(sfreq=Fs, 
                            fmin=f_min, fmax=f_max, 
                            bandwidth=None, 
                            adaptive=False, 
                            low_bias=True, 
                            n_jobs=1, 
                            normalization='length', 
                            verbose=None)

PSDE_sit_fit = PSDE.fit(epoch_sit.get_data(),'SIT')
PSDE_sit_transform = PSDE.transform(epoch_sit.get_data())
PSDE_sit_transform[0][0] # [Numnber of event iterations (10)][Pick (Electrode)]

PSDE_stand_transform = PSDE.transform(epoch_stand.get_data())

if FLAG_PLOT:
    plt.figure()
    plot_freq = range(len(PSDE_sit_transform[0][0]))
    for i in range(len(PSDE_sit_transform[0][0])):
        plot_freq[i] *= 1.0
        plot_freq[i] /= float(len(plot_freq))
        plot_freq[i] *= f_max-f_min
        plot_freq[i] += f_min
    
    for i in range(len(PSDE_sit_transform)):
        plt.plot(plot_freq,PSDE_sit_transform[i][0],label=i)
    #plt.legend('1','2','3','4','5','6','7','8','9','10')
    plt.xlim([f_min,f_max])
    plt.legend()
    plt.title('Demonsration of features')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show(block=False)

print('DONE: PSDE\n')