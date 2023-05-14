import numpy as np

class RNN:
    def __init__(self, input_dim, hidden_dim, output_dim, seq_length):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.seq_length = seq_length

        self.Wxh = np.random.randn(hidden_dim, input_dim) * 0.01
        self.Whh = np.random.randn(hidden_dim, hidden_dim) * 0.01
        self.Why = np.random.randn(output_dim, hidden_dim) * 0.01
        self.bh = np.zeros((hidden_dim, 1))
        self.by = np.zeros((output_dim, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, inputs):
        self.hidden_states = np.zeros((self.hidden_dim, self.seq_length))
        self.outputs = np.zeros((self.output_dim, self.seq_length))

        h_prev = np.zeros((self.hidden_dim, 1))

        for t in range(self.seq_length):
            x_t = inputs[:, t].reshape(-1, 1)
            a_t = np.dot(self.Wxh, x_t) + np.dot(self.Whh, h_prev) + self.bh
            h_t = np.tanh(a_t)
            o_t = np.dot(self.Why, h_t) + self.by
            y_t = self.sigmoid(o_t)

            self.hidden_states[:, t] = h_t.reshape(-1)
            self.outputs[:, t] = y_t.reshape(-1)
            h_prev = h_t

        return self.outputs

    def backward(self, inputs, targets, learning_rate=0.1):
        dWxh = np.zeros_like(self.Wxh)
        dWhh = np.zeros_like(self.Whh)
        dWhy = np.zeros_like(self.Why)
        dbh = np.zeros_like(self.bh)
        dby = np.zeros_like(self.by)
        dh_next = np.zeros((self.hidden_dim, 1))

        for t in reversed(range(self.seq_length)):
            x_t = inputs[:, t].reshape(-1, 1)
            y_t = self.outputs[:, t].reshape(-1, 1)
            t_t = targets[:, t].reshape(-1, 1)
            h_t = self.hidden_states[:, t].reshape(-1, 1)

            do_t = y_t - t_t
            dWhy += np.dot(do_t, h_t.T)
            dby += do_t

            dh_t = np.dot(self.Why.T, do_t) + dh_next
            da_t = (1 - h_t * h_t) * dh_t
            dbh += da_t
            dWxh += np.dot(da_t, x_t.T)
            dWhh += np.dot(da_t, self.hidden_states[:, t-1].reshape(-1, 1).T)
            dh_next = np.dot(self.Whh.T, da_t)

        self.Wxh -= learning_rate * dWxh
        self.Whh -= learning_rate * dWhh
        self.Why -= learning_rate * dWhy
        self.bh -= learning_rate * dbh
        self.by -= learning_rate * dby


