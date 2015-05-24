print('\n\t============ Epochs ============\n')

# Epochs
epochs = mne.Epochs(raw,
		    events=events, 
		    event_id=event_id, 
		    tmin=tmin, 
		    tmax=tmax, 
		    baseline=baseline, # (None, 0) # Could be changed to baseline, changed
		    picks=picks, # Changed from None to picks
		    name='Unknown', 
		    preload=False, # Changed to True - Changed back to false or 52 baselines are calculated
		    reject=None, 
		    flat=None, 
		    proj=True, 
		    decim=1, 
		    reject_tmin=None,
		    reject_tmax=None, 
		    detrend=None, 
		    add_eeg_ref=True, 
		    on_missing='error', 
		    verbose=None)

print('\n')
print(epochs)
print('\n\n')

epoch_sit = epochs['SIT_GO']
epoch_stand = epochs['STAND_GO']

print(epoch_sit)
