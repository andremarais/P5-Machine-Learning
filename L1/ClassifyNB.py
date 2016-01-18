import pprint

def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!

    from sklearn.naive_bayes import GaussianNB
    from prep_terrain_data import makeTerrainData
    a = makeTerrainData()
    clf = GaussianNB()
    clf.fit(a[0],a[1])

    return clf




def test():
    import numpy as np
    x = np.array([[-1,1], [-2, 1], [-3, -2], [1, 1],[2, 1],[3, 2]])
    y = np.array([1, 1, 1, 2, 2, 2])
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(x,y)
    print(clf.predict([-0.8, -1]))
    from prep_terrain_data import makeTerrainData
    a = makeTerrainData()
    print len(a[3])



