print('\n\t============ Machine learning - Classifications ============\n') 

#X = data[0:3./4.*len(data)]
X = data[0:2./3.*len(data)]
#np.concatenate((data[0:20],data[40:60])).shape
#y = [0 for i in range(3*len(data)/2/4)] + [1 for j in range(3*len(data)/2/4)] # Class
y = [0 for i in range(2*len(data)/2/3)] + [1 for j in range(2*len(data)/2/3)] # Class
#+ [0 for i in range(10)] + [1 for j in range(10)]

#svc = svm.SVC(kernel='linear', C=C).fit(X, y)
classification = svm.SVC()
print 'TRAINING'
classifier = classification.fit(X,y) # Training: X[:40]

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
res = 100  # step size in the mesh
xx, yy = np.meshgrid(np.arange(x_min, x_max, (x_max-x_min)/res),
                     np.arange(y_min, y_max,(y_max-y_min)/res))

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
#plt.subplot(2, 2, i + 1)
#plt.subplots_adjust(wspace=0.4, hspace=0.4)

testing = classifier.predict(X) # Testing: Predict for a point example: X[40:60]

print 'Test on training data:',testing, '\n'

print 'TESTING'

testing = classifier.predict(data[40:60])

print 'Test on testing data:',testing


# Put the result into a color plot
#Z = Z.reshape(xx.shape)
#plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

# Plot also the training points
#plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
#plt.xlabel('Feature 1')
#plt.ylabel('Feature 2')
#plt.xlim(xx.min(), xx.max())
#plt.ylim(yy.min(), yy.max())
#plt.xticks(())
#plt.yticks(())
#plt.title('Classification')

#plt.show()