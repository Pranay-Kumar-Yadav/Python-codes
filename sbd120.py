#train test split manually
def train_test_split_manual(X, y, test_size=0.2):
    split_index = int(len(X) * (1 - test_size))

    X_train = X[:split_index]
    X_test = X[split_index:]

    y_train = y[:split_index]
    y_test = y[split_index:]

    return X_train, X_test, y_train, y_test


X = [1,2,3,4,5,6,7,8,9,10]
y = [0,1,0,1,0,1,0,1,0,1]

X_train, X_test, y_train, y_test = train_test_split_manual(X, y, test_size=0.3)

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train)
print("y_test:", y_test)