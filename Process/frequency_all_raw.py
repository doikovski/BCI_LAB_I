print('\n\t============ Frequency analysis for all data ============\n')

# raw[Electrode][0 for amplitudes, 1 for times][amplitude or time]
# epoch_sit_data[event][electrode][amplitude]

raw_data = np.zeros((1,len(picks),len(raw[0][0][0])))
for i in range(len(picks)):
    raw_data_electrode = np.asarray(raw[picks])
    raw_data[0,i] = raw_data_electrode[0][0][0]

tmin = 0
t_step = 0.1
t_window = [1.0]
steps = 10

PSDE_sit = [[None for i in range(steps)] for j in range(len(t_window))]

window_n = 0

for window in t_window:
    for step in range(steps):
        
        print 'WINDOW:', window, 'STEP:', step
        
        # Times
        start = int( ( np.abs(tmin) + step*t_step ) * Fs )
        end = int( ( np.abs(tmin) + step*t_step + window ) * Fs )
        
        # Crop time
        raw_data_crop = raw_data[:,:,start:end]
        
        # Padding
        raw_padded = np.pad(raw_data_crop, ((0,0),(0,0),(0,10000)), 'constant')
        
        # PSDE
        PSDE_sit_transform = PSDE.transform(raw_padded)
        
        # Storage
        PSDE_sit[window_n][step]= PSDE_sit_transform
        
    window_n += 1

PSDE_sit = np.asarray(PSDE_sit)

#del raw_data
#del epoch_stand_data
#del raw_padded
#del epoch_stand_padded