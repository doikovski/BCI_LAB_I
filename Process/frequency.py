print('\n\t============ Frequency analysis ============\n')

# TFR Morlet
print('Caclculating TFR Morlet')
power_sit, itc_sit = mne.time_frequency.tfr_morlet(inst=epoch_sit, 
                                                   freqs=frequencies, 
                                                   n_cycles=n_cycles,
                                                   use_fft=True)

power_stand, itc_stand = mne.time_frequency.tfr_morlet(inst=epoch_stand, 
                                                   freqs=frequencies, 
                                                   n_cycles=n_cycles,
                                                   use_fft=True)
print('DONE: calculating power & itc')


# Plot TFT Morlet
print('Plotting TFT Morlet graphs')

#power_sit.plot([0], baseline=(-0.5, 0), mode=None)
#plt.title('S-transform (power)')

if FLAG_PLOT:
    fig_power_sit = power_sit.plot(picks=picks_tfr, # From 0 to n_electrodes_used-1
                                #tmin=-1, tmax=3, 
                                #fmin=00, fmax=30, 
                                #vmin=0, vmax=0.0000001, 
                                vmin=-250,vmax=-150,
                                dB=True,
                                show=False)
    plt.title('Averaged power from TFR MORLET')
    plt.show() # block=False

if FLAG_PLOT:
    fig_itc_sit = itc_sit.plot(picks=picks_tfr,
                        #tmin=tmin, tmax=tmax, 
                        #fmin=00, fmax=30, 
                        vmin=0,
                        show=False)
    plt.title('Intertrial coherence (ITC) from TFR MORLET')
    plt.show() # block=False

print('DONE: Calculating frequency and plotting corresponding graphs\n')

# PSD estimator 
print('Computing PSDE\n')
PSDE = mne.decoding.PSDEstimator(sfreq=Fs, 
                            fmin=f_min, fmax=f_max, 
                            bandwidth=None, 
                            adaptive=False, 
                            low_bias=False, 
                            n_jobs=1, 
                            normalization='length', 
                            verbose=None)

epoch_sit_data = epoch_sit.get_data()
epoch_stand_data = epoch_stand.get_data()

epoch_sit_padded=np.pad(epoch_sit_data, ((0,0),(0,0),(0,1000)), 'constant')
epoch_stand_padded=np.pad(epoch_stand_data, ((0,0),(0,0),(0,1000)), 'constant')

#PSDE_sit_fit = PSDE.fit(epoch_sit.get_data(),'SIT')
PSDE_sit_transform = PSDE.transform(epoch_sit_padded) # [Numnber of event iterations (10)][Pick (Electrode)][amplitude] 

PSDE_stand_transform = PSDE.transform(epoch_stand_padded)

###Nomalisation
#for i in range(len(PSDE_sit_transform)):
   #for j in range(len(picks)):
       #PSDE_sit_transform[i][j] /= PSDE_sit_transform[i][j].std()
       
#for i in range(len(PSDE_stand_transform)):
   #for j in range(len(picks)):
       #PSDE_stand_transform[i][j] /= PSDE_stand_transform[i][j].std()

if True: #FLAG_PLOT:
    for j in range(len(picks)):
        plt.figure()
        plot_freq = range(len(PSDE_sit_transform[0][0]))
        for i in range(len(PSDE_sit_transform[0][0])):
            plot_freq[i] *= 1.0
            plot_freq[i] /= float(len(plot_freq))
            plot_freq[i] *= f_max-f_min
            plot_freq[i] += f_min
        
        for i in range(len(PSDE_sit_transform)):
            plt.plot(plot_freq,PSDE_sit_transform[i][j],label=i)
        
        plt.xlim([f_min,f_max])
        plt.legend()
        plt.title('Sit PSDE for electrode %i' %j)
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        plt.show(block=False)

print('DONE: PSDE\n')

# General matrix containing all data
# PSDE_sit[Events][Windows_size][Steps][Electrode][Freq amplitude]

# PSDE_sit[Events][Electrode][Freq amplitude][Windows_size][Steps]

epoch_sit_data = epoch_sit.get_data()
PSDE_sit = [[None for i in range(steps)] for j in range(len(t_window))]

window_n = 0

for window in t_window:
    for step in range(steps):
        
        # Times
        start = int( (np.abs(tmin) + step*t_step ) * Fs)
        end = int( (np.abs(tmin) + step*t_step + window ) * Fs)
        
        # Crop time
        epoch_sit_data_crop = epoch_sit_data[:,:,start:end]
        epoch_stand_data_crop = epoch_stand_data[:,:,start:end]
        
        # Padding
        epoch_sit_padded = np.pad(epoch_sit_data_crop, ((0,0),(0,0),(0,1000)), 'constant')
        epoch_stand_padded = np.pad(epoch_sit_data_crop, ((0,0),(0,0),(0,1000)), 'constant')
        
        # PSDE
        PSDE_sit_transform = PSDE.transform(epoch_sit_padded)
        PSDE_stand_transform = PSDE.transform(epoch_sit_padded)
        
        # Storage
        PSDE_sit[window_n][step]= PSDE_sit_transform
        
    window_n += 1

PSDE_sit = np.asarray(PSDE_sit)
