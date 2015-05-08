raw = mne.io.read_raw_edf(Recording, preload=True)

print('\n\t============ BDF file info ============\n')
print(raw.info)
print('\n')

# Raw plot
    # raw.plot()

# Save file
    # Used to avoid reloading data
    # raw.save('raw_recordings.fif', tmin=tmin, tmax=tmax, picks=picks, overwrite=True) 

#raw.plot_psds(tmin=100.0,tmax=101.0,fmin=1,fmax=40,picks=picks,n_fft=2048)