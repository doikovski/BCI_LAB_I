print('\n\t============ Events ============\n')

# Extract events
events = mne.find_events(raw, 
                         stim_channel='STI 014')
print(events)
print('\n')

# Read and write events to avoid recalculating
    # mne.write_events('events.fif', events)
    # events = mne.read_events('events.fif')

# Plot raw EEG data with event markers
fig_rawdata = raw.plot(events=events,block=False)

event_id = {'INIT': 255,
	    'CUE': 254, 
	    'BLANK': 252, 
	    'STAND_READY': 241, 
	    'STAND_GO': 240,
	    'SIT_READY': 239,
	    'SIT_GO': 238}
#'WALK_READY':237
#'WALK_GO':236

# Event times
print 'EVENTS TIMES:'
event_sit_go_time = []
event_stand_go_time = []
event_sit_go_time_total = 0
event_stand_go_time_total = 0
for i in range(len(events[:,0])):
    if events[i,2] == 238:
        print i, 'Event SIT_GO from time', events[i,0]/2048
        event_sit_go_time.append([events[i,0]/2048,events[i+1,0]/2048])
        event_sit_go_time_total += (events[i+1,0] - events[i,0])/2048
    elif events[i,2] == 240:
        print i, 'Event STAND_GO at time', events[i,0]/2048
        event_stand_go_time.append([events[i,0]/2048,events[i+1,0]/2048])
        event_stand_go_time_total += (events[i+1,0] - events[i,0])/2048

print 'Total Sitting time:', event_sit_go_time_total, 'seconds'
print 'Total Standing time:', event_stand_go_time_total, 'seconds'
print '\n'

# Plot events
fig_events = mne.viz.plot_events(events, 
				  raw.info['sfreq'], 
				  raw.first_samp, 
				  event_id=event_id) # could add show=false
