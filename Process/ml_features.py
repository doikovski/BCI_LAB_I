print('\n\t============ Machine learning - Features ============\n') 

PSDE_sit_transform[0][0] # [Numnber of event iterations (10)][Pick (Electrode)][Amplitides]

#data_ml = []

#sit_data_ml = [[None for i in range(len(PSDE_sit_transform[0])*len(PSDE_sit_transform[0][0]))] for j in range(len(PSDE_sit_transform))]

#stand_data_ml = [[None for i in range(len(PSDE_stand_transform[0])*len(PSDE_stand_transform[0][0]))] for j in range(len(PSDE_stand_transform))]

#for i in range(len(PSDE_sit_transform)):
    #for j in range(len(PSDE_sit_transform[0])):
        #for k in range(len(PSDE_sit_transform[0][0])):
            #sit_data_ml[i][j*len(PSDE_sit_transform[0][0])+k] = PSDE_sit_transform[i][j][k]
    #data_ml.append(sit_data_ml[i])

#for i in range(len(PSDE_stand_transform)):
    #for j in range(len(PSDE_stand_transform[0])):
        #for k in range(len(PSDE_stand_transform[0][0])):
            #stand_data_ml[i][j*len(PSDE_stand_transform[0][0])+k] = PSDE_stand_transform[i][j][k]
    #data_ml.append(stand_data_ml[i])

#data_ml = np.append(PSDE_sit_transform.reshape((10,5*30)),PSDE_stand_transform.reshape((10,5*30))).reshape(20,150)
s0 = len(PSDE_sit_transform)
s1 = len(PSDE_sit_transform[0])
s2 = len(PSDE_sit_transform[0][0])
data_ml = np.concatenate((PSDE_sit_transform.reshape((s0,s1*s2)),PSDE_stand_transform.reshape((s0,s1*s2))))
#data_ml = np.append(a,b).reshape((20,5*30))
#print data_ml

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

#data /= np.std(data)

for axis in range(5):
    plt.figure()
    for i in range(10):
        for j in range(4): # 4 for 4 files
            k = 10*j + i
            plt.plot(data[i,axis],data[k,axis+1],'bo')
    for i in range(10):
        for j in range(4): # 4 for 4 files
            k = 40+10*j+i # 40 (instead of first 10) for 4 files
            plt.plot(data[i,axis],data[k,axis+1],'ro')
    plt.show(block=False)