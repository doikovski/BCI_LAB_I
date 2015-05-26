print('\n\t============ Machine learning - Classifications ============\n') 

X = np.asarray(data)
y = [0 for i in range(40)] + [1 for j in range(40)] # Class
#+ [0 for i in range(10)] + [1 for j in range(10)]

#svc = svm.SVC(kernel='linear', C=C).fit(X, y)
classification = svm.SVC()
print 'TRAINING\n'
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

print 'TESTING\n'

testing = classifier.predict(X) # Testing: Predict for a point example: X[40:60]

print 'Test result:',testing

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