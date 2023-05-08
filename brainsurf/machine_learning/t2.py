import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data


def split_data(data):
    """
    Split the data into training and testing sets.
    """
    X = data[:, :-1]
    y = data[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train the linear regression model on the training data.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the performance of the trained model on the testing data.
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("MSE: {:.2f}".format(mse))
    print("R2 score: {:.2f}".format(r2))

def calculate_levels(model, X_point):
    """
    Predict the alpha, beta, delta, and theta levels for a single data point using the trained model.
    """
    levels = model.predict(X_point.reshape(1, -1))
    return levels

# Example usage
data = load_data('C:/Users/Preethi V Hiremath/OneDrive/Desktop/Projects/esp/brainsurf/data/eeg_data/sample_data.csv');

X_train, X_test, y_train, y_test = split_data(data)
model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test)

# Calculate alpha, beta, delta, and theta levels for a single point
X_point = np.array([2.44,-9.51538,-0.458429,-0.300244])
levels = calculate_levels(model, X_point)
print("Alpha level: {:.2f}".format(levels[0, 0]))
print("Beta level: {:.2f}".format(levels[0, 1]))
print("Delta level: {:.2f}".format(levels[0, 2]))
print("Theta level: {:.2f}".format(levels[0, 3]))


# if __name__ == '__main__':

    # preprocessed_data = preprocess_data(data)
    # X_train, X_test, y_train, y_test = split_data(preprocessed_data)
    # model = train_model(X_train, y_train)
    # evaluate_model(model, X_test, y_test)