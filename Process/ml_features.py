print('\n\t============ Machine learning - Features ============\n') 

# Example to use the obtained data
    # Plot amplitude in function of frequencies
if FLAG_MP:
    def PlotPowerSit(power_sit):
        for i in range(3):
            for j in range(19):
                for k in range(0,10241,1000):
                    # power.data[j][k][l]: j:n_channels, k:n_freqs, l:n_times
                    plt.plot(frequencies[j],power_sit.data[i][j][k],'bx-')
        plt.title('Demonsration of features')
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        #plt.ylim([0,1e-8])
        plt.show()

    plot_power_sit = mp.Process(target=PlotPowerSit,args=[power_sit])
    plot_power_sit.start()

elif FLAG_PLOT:
    plt.figure()
    for i in range(3):
            for j in range(19):
                for k in range(0,10241,1000):
                    # power.data[j][k][l]: j:n_channels, k:n_freqs, l:n_times
                    plt.plot(frequencies[j],power_sit.data[i][j][k],'bx-')
    plt.title('Demonsration of features')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    #plt.ylim([0,1e-8])
    plt.show(block=False)

# Sample:
    # (40)*64 features
        # 40 frequencies
        # 64 electrodes

# sample_sit[n_channel][freq]=amplitude

# USE ICA -> Indpendent extraction
#mne.preprocessing.ICA.fit(inst, 
                          #picks=picks, 
                          #start=None, 
                          #stop=None, 
                          #decim=None, 
                          #reject=None, 
                          #flat=None, 
                          #tstep=2.0, 
                          #verbose=None)

PSDE_sit_transform[0][0] # [Numnber of event iterations (10)][Pick (Electrode)][Amplitides]

#sklearn.decomposition.FastICA(n_components=None, 
                              #algorithm='parallel', 
                              #whiten=True, 
                              #fun='logcosh', 
                              #fun_args=None, 
                              #max_iter=200, 
                              #tol=0.0001, 
                              #w_init=None, 
                              #random_state=None)

data_ml = []

sit_data_ml = [[None for i in range(len(PSDE_sit_transform[0])*len(PSDE_sit_transform[0][0]))] for j in range(len(PSDE_sit_transform))]

stand_data_ml = [[None for i in range(len(PSDE_stand_transform[0])*len(PSDE_stand_transform[0][0]))] for j in range(len(PSDE_stand_transform))]

for i in range(len(PSDE_sit_transform)):
    for j in range(len(PSDE_sit_transform[0])):
        for k in range(len(PSDE_sit_transform[0][0])):
            sit_data_ml[i][j*len(PSDE_sit_transform[0][0])+k] = PSDE_sit_transform[i][j][k]
    data_ml.append(sit_data_ml[i])

for i in range(len(PSDE_stand_transform)):
    for j in range(len(PSDE_stand_transform[0])):
        for k in range(len(PSDE_stand_transform[0][0])):
            stand_data_ml[i][j*len(PSDE_stand_transform[0][0])+k] = PSDE_stand_transform[i][j][k]
    data_ml.append(stand_data_ml[i])

ica = skd.FastICA(random_state=0) # random_state was added else the result changes every time the code is executed

#ica = skd.PCA() # TEST PCA

#features_sit = ica.fit_transform(sit_data_ml)
#features_stand = ica.fit_transform(stand_data_ml)
data = ica.fit_transform(data_ml)

data /= data.std(axis=0)

#plt.figure('Features')
#for i in range(10):
    #plt.plot(features_sit[i,0],features_sit[i,1],'bo')
    #plt.plot(features_stand[i,0],features_stand[i,1],'ro')
#plt.show(block=False)

data /= np.std(data)

for axis in range(5):
    plt.figure()
    for i in range(10):
        for j in range(1): # 4 for 4 files
            k = 10*j + i
            plt.plot(data[i,axis],data[k,axis+1],'bo')
    for i in range(10):
        for j in range(1): # 4 for 4 files
            k = 10+10*j+i # 40 (instead of first 10) for 4 files
            plt.plot(data[i,axis],data[k,axis+1],'ro')
    plt.show(block=False)

    