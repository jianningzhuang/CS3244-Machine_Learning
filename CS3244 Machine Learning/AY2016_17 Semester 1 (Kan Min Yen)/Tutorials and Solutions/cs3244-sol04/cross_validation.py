from sklearn import svm
from sklearn import cross_validation
import numpy as np

#load data and parse to feature and label
def loadData(filename):
    file_handler = open(filename,'r')
    content = file_handler.read().splitlines()
    feature_array = []
    label_array = []
    for line in content:
        line_split = line.split('\t')
        label = int(line_split[11])
        label_array.append(label)

        feature = [0.0] * (len(line_split) - 1)
        for i in range(0, len(line_split)-1):
            feature[i] = float(line_split[i])
        # print feature
        # print label
        feature_array.append(feature)
        
    return (feature_array, label_array)

def run():
    kernel_list = ['linear', 'poly', 'rbf']
    penalty_list = [0.1, 1, 10]
    degree_list = [2] #[2,3]
    gamma_list = [0.001] #[0.001, 0.01, 0.1]

    x_train_all, y_train_all = loadData('train.txt')
    x_train_all = np.array(x_train_all)
    y_train_all = np.array(y_train_all)
    x_test, y_test = loadData('test.txt')

    max_val_accuracy = 0.0

    for kernel in kernel_list:
        for penalty in penalty_list:
            for degree in degree_list:
                for gamma in gamma_list:
                    svm_model = svm.SVC(C=penalty, kernel=kernel, degree=degree, gamma=gamma)
                    print svm_model
                    scores = cross_validation.cross_val_score(svm_model, x_train_all, y_train_all, cv=5)
                    print "accuracy for each fold = ", scores
                    print "average accuracy = ", scores.mean()
                    print " "
                    if scores.mean() > max_val_accuracy:
                        best_model = svm_model
                        max_val_accuracy = scores.mean()

    print "\n======= the best model:"
    print best_model

    print "======= max validation accuracy: ", max_val_accuracy 

    best_model.fit(x_train_all, y_train_all)
    print "======= test accuracy: ", best_model.score(x_test, y_test)


if __name__ == '__main__':
    run()
