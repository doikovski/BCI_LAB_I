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

# Raw plot
    # raw.plot()

# Save file
    # Used to avoid reloading data
    # raw.save('raw_recordings.fif', tmin=tmin, tmax=tmax, picks=picks, overwrite=True) 

#raw.plot_psds(tmin=100.0,tmax=101.0,fmin=1,fmax=40,picks=picks,n_fft=2048)