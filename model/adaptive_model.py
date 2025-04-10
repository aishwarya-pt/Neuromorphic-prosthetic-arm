import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

class AdaptiveThresholdModel:
    def __init__(self, threshold=0.5):
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.threshold = threshold

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def update_threshold(self, feedback_accuracy):
        if feedback_accuracy < 0.7:
            self.threshold -= 0.05
        else:
            self.threshold += 0.05
        self.threshold = min(max(self.threshold, 0.1), 0.9)
