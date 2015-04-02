print('\n\t============ Epochs ============\n')

# Epochs
epochs = mne.Epochs(raw,
		    events=events, 
		    event_id=event_id, 
		    tmin=tmin, 
		    tmax=tmax, 
		    # baseline=baseline, # (None, 0) # Could be changed to baseline, changed
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

# VERY LONG, DOESN'T WORK
# epochs = mne.Epochs(raw, events, event_id, tmin, tmax)

# Save epochs to avoid recalculating later
# epochs.save('epochs.fif')
# saved_epochs = mne.read_epochs('sample-epo.fif')

print('\n')
print(epochs)
print('\n\n')


# QUESTION: WHAT ARE EVOKES AND ARE THEY NECESSARY?

epoch_sit = epochs['SIT_GO']
# epoch_stand = epochs['STAND_GO'].average()

print(epoch_sit)

# Removed because FFT plot uses previous variable
# epoch_sit_data = epoch_sit.get_data()
# print(epoch_sit_data)

'''
evoked_sit = epoch_sit.average()
print(evoked_sit)
evoked_sit.plot()
'''

'''
evoked = epochs.average() # Average to create Evoked 
cov = mne.compute_covariance(epochs, tmax=0)  # Calculate baseline covariance 
forward = mne.make_forward_solution(evoked.info, mri, src, bem, mindist=5.0)  
inverse = mne.minimum_norm.make_inverse_operator(evoked.info, forward, cov)  
stc = mne.minimum_norm.apply_inverse(evoked, inverse,  
                                         lambda2=1. / 9.)  # Source estimates 
'''
'''
events2 = mne.find_events(raw, stim_channel='STI 014')
print(events[:5])
event_id2 = dict(ST_READY=1, SIT_GO=2)
'''

