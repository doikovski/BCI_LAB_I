print('\n\t============ Spatial filter ============\n') 

# raw[n_channels][amplitude or time][0][element number]

spatial_filter = 'CAR'
picks_spatial_filter = picks # Electrodes on which spatial filtering is applied
pick_CAR = [0,1,2,3,4,5,6,7,8,9,10] # Electrodes used to average signal for a specific time

# First approach: Writing in raw file
    # NOTE; Times must still be implemented

def Raw_Average(picks):
    average = np.zeros(1000)
    for i in range(1000): # len(time) to apply over all time
        if not i%100:
            print 'EPOCH_AVERAGE', i
        for j in picks_spatial_filter: # Electrodes used for averaging
            average[i] += raw[j][0][0][i]
        average[i] /= 64
    return average

def CAR_raw(timeseries):
    amplitude = np.zeros(len(timeseries)) # initialise array
    for i in range(1000): # len(time) to apply over all time
        amplitude[i] = raw[0][0][0][i] - raw_average[i]
    return amplitude

raw_average = Raw_Average(picks_spatial_filter)
raw.apply_function(CAR_raw, picks=pick_CAR, dtype=None, n_jobs=10)

# Second approach: Using epochs instead

def Epoch_Average(picks):
    average = np.zeros(1000)
    for i in range(1000): # len(time) to apply over all time
        if not i%100:
            print 'EPOCH_AVERAGE', i
        for j in picks_spatial_filter: # Electrodes used for averaging
            average[i] += raw[j][0][0][i]
        average[i] /= 64
    return average

def CAR(timeseries):
    amplitude = np.zeros(len(timeseries)) # initialise array
    for i in range(1000): # len(time) to apply over all time
        amplitude[i] = raw[0][0][0][i] - raw_average[i]
    return amplitude

#epoch_sit_data = epoch_sit.get_data() # [n_epochs, n_channels, n_times]
