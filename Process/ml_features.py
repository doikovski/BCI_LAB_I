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




