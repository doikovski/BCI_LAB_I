print('\n\t============ Events ============\n')

events = mne.find_events(raw, stim_channel='STI 014') # Extract events # ADDED STIM_CHANNEL
print(events)
print('\n')

# Read and write events to avoid recalculating
# mne.write_events('events.fif', events)
# events = mne.read_events('events.fif')

# Plot raw EEG data with event markers
# fig_rawdata = raw.plot(events=events,block=False)

event_id = {'INIT': 255,
	    'CUE': 254, 
	    'BLANK': 252, 
	    'STAND_READY': 241, 
	    'STAND_GO': 240,
	    'SIT_READY': 239,
	    'SIT_GO': 238}

#'WALK_READY':237
#'WALK_GO':236

#for ind, before, after in events[:5]:
#    print("At sample %d stim channel went from %d to %d"
#          % (ind, before, after))

# Plot the events to get an idea of the paradigm
# Specify colors and an event_id dictionary for the legend.
#color = {1: 'green', 2: 'yellow', 3: 'red', 4: 'c', 5: 'black', 32: 'blue'}

# Plot events

fig_events = mne.viz.plot_events(events, 
				  raw.info['sfreq'], 
				  raw.first_samp, 
				  event_id=event_id) # could add show=false
