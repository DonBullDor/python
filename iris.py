from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    br = '\n'
    iris = datasets.load_iris()  # load dataset
    keys = iris.keys()  # get keys from the dataset
    print(keys, br)
    X = iris.data  # the feature array
    y = iris.target  # the target variable
    print('features shape:', X.shape)
    print('target shape:', y.shape, br)

    features = iris.feature_names
    targets = iris.target_names
    print('feature set:')
    print(features, br)
    print('targets:')
    print(targets, br)
    print(iris.DESCR[525:900], br)

    rnd_clf = RandomForestClassifier(random_state=0,
                                     n_estimators=100)
    # RandomForestClassifier is an ensemble learning method that
    # constructs a multitude of decision trees at training time and outputs the class that is the mode of the classes

    rnd_clf.fit(X, y)  # fit the classifier to the data
    rnd_name = rnd_clf.__class__.__name__
    feature_importances = rnd_clf.feature_importances_
    importance = sorted(zip(feature_importances, features), reverse=True)
    print('most important features' + ' (' + rnd_name + '):')
    [print(row) for i, row in enumerate(importance)]
