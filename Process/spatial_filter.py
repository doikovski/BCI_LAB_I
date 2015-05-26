print('\n\t============ Spatial filter ============\n') 

def CAR_raw(timeseries):
    print 'Applying CAR for electrode:', i
    raw_filtered = raw[i][0] - CAR
    return raw_filtered[0]

raw_data = raw[pick_CAR][0] # 0 index for Voltage values
CAR = raw_data.mean(axis=0) # mean along electrodes axis

for i in picks_spatial_filter: # apply spacial filter
    raw.apply_function(CAR_raw, picks=[i], dtype=None, n_jobs=1)

del raw_data
del CAR