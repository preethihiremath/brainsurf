import numpy as np
import pandas as pd

class RNN():
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.W_hh = np.random.randn(hidden_dim, hidden_dim)
        self.W_xh = np.random.randn(input_dim, hidden_dim)
        self.W_hy = np.random.randn(hidden_dim, output_dim)
        self.b_h = np.zeros((1, hidden_dim))
        self.b_y = np.zeros((1, output_dim))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        T = len(x)
        h = np.zeros((T + 1, self.hidden_dim))
        y_pred = np.zeros((T, self.output_dim))
        for t in range(T):
            h[t] = self.sigmoid(np.dot(x[t], self.W_xh) + np.dot(h[t-1], self.W_hh) + self.b_h)
            y_pred[t] = np.dot(h[t], self.W_hy) + self.b_y
        return y_pred

    def loss(self, x, y_true):
        y_pred = self.forward(x)
        return np.mean((y_pred - y_true) ** 2)

    def backward(self, x, y_true):
        T = len(x)
        dW_hh = np.zeros_like(self.W_hh)
        dW_xh = np.zeros_like(self.W_xh)
        dW_hy = np.zeros_like(self.W_hy)
        db_h = np.zeros_like(self.b_h)
        db_y = np.zeros_like(self.b_y)
        dh_next = np.zeros((1, self.hidden_dim))
        for t in reversed(range(T)):
            dy = 2 * (self.forward(x)[t] - y_true[t])
            dW_hy += np.dot(self.sigmoid(np.dot(x[t], self.W_xh) + np.dot(h[t-1], self.W_hh) + self.b_h).T, dy)
            db_y += dy
            dh = np.dot(dy, self.W_hy.T) + dh_next
            dh_raw = (1 - self.sigmoid(np.dot(x[t], self.W_xh) + np.dot(h[t-1], self.W_hh) + self.b_h)) * self.sigmoid(np.dot(x[t], self.W_xh) + np.dot(h[t-1], self.W_hh) + self.b_h) * dh
            db_h += dh_raw
            dW_xh += np.dot(x[t].reshape(self.input_dim, 1), dh_raw.reshape(1, self.hidden_dim))
            dW_hh += np.dot(h[t-1].reshape(self.hidden_dim, 1), dh_raw.reshape(1, self.hidden_dim))
            dh_next = np.dot(dh_raw, self.W_hh.T)
        return dW_xh, dW_hh, dW_hy, db_h, db_y

    def fit(self, X, Y, epochs=10, learning_rate=0.01):
        for i in range(epochs):
            loss = 0
            for j in range(len(X)):
                x = X[j]
                y_true = Y[j]
                dW_xh, dW_hh, dW_hy, db_h, db_y = self.backward(x,y)
