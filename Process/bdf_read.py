raw = mne.io.read_raw_edf(Recording, preload=True)

print('\n\t============ BDF file info ============\n')
print(raw.info)
print('\n')

# Raw plot
    # raw.plot()

# Save file
    # Used to avoid reloading data
    # raw.save('raw_recordings.fif', tmin=tmin, tmax=tmax, picks=picks, overwrite=True) 
