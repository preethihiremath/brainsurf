import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score

class EEGClassifier:
    def __init__(self, model_type='svm'):
        self.scaler = StandardScaler()
        self.model_type = model_type.lower()

        if self.model_type == 'svm':
            self.model = SVC(kernel='rbf', C=1.0, gamma='scale')
        elif self.model_type == 'lda':
            self.model = LinearDiscriminantAnalysis()
        else:
            raise ValueError("model_type must be 'svm' or 'lda'.")

    def train(self, X_train, y_train):
        X_train_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_train_scaled, y_train)

    def predict(self, X_test):
        X_test_scaled = self.scaler.transform(X_test)
        return self.model.predict(X_test_scaled)

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy


class LDAClassifier(EEGClassifier):
    def __init__(self):
        super().__init__(model_type='lda')
