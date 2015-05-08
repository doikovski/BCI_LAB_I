print('\n\t============ Spatial filter ============\n') 

# raw[n_channels][amplitude or time][0][element number]

# First approach: Writing in raw file
    # NOTE; Times must still be implemented

#def Raw_Average(picks):
    #average = np.zeros(1000)
    #for i in range(1000): # len(time) to apply over all time
        #if not i%100:
            #print 'EPOCH_AVERAGE', i
        #for j in picks_spatial_filter: # Electrodes used for averaging
            #average[i] += raw[j][0][0][i]
        #average[i] /= 64
    #return average

#def CAR_raw(timeseries):
    #amplitude = np.zeros(len(timeseries)) # initialise array
    #for i in range(1000): # len(time) to apply over all time
        #amplitude[i] = raw[0][0][0][i] - raw_average[i]
    #return amplitude

#raw_average = Raw_Average(picks_spatial_filter)
#raw.apply_function(CAR_raw, picks=pick_CAR, dtype=None, n_jobs=10)

# APPLYING OPTIMIZATION

def CAR_raw(timeseries):
    print 'Applying CAR for electrode:', i
    return raw[i][0] - CAR

raw_data = raw[pick_CAR][0] # Voltage values
CAR = raw_data.mean(axis=0)
test = 10*np.ones(len(CAR))
for i in picks_spatial_filter:
    raw.apply_function(CAR_raw, picks=[i], dtype=None, n_jobs=1)


# Second approach: Using epochs instead

#def Epoch_Average(picks):
    #average = np.zeros(1000)
    #for i in range(1000): # len(time) to apply over all time
        #if not i%100:
            #print 'EPOCH_AVERAGE', i
        #for j in picks_spatial_filter: # Electrodes used for averaging
            #average[i] += raw[j][0][0][i]
        #average[i] /= 64
    #return average

#def CAR(timeseries):
    #amplitude = np.zeros(len(timeseries)) # initialise array
    #for i in range(1000): # len(time) to apply over all time
        #amplitude[i] = raw[0][0][0][i] - raw_average[i]
    #return amplitude
'''    
def CAR(timeseries):
    amplitude = np.zeros(len(timeseries)) # initialise array
    for i in range(1000): # len(time) to apply over all time
        amplitude[i] = raw[0][0][0][i] - raw_average[i]
    return amplitude

epoch_sit_data = epoch_sit.get_data() # [n_epochs, n_channels, n_times]
evoked=epoch_sit_data.mean(axis=1) # Calculate the mean over the channels

evoked = epochs['aud_l'].average()
'''
# for i in range(10): # Number of event iterations
    


