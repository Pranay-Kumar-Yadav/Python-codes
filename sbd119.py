#confusion matrix calculation
def confusion_matrix_calc(y_true, y_pred):
    TP = TN = FP = FN = 0

    for actual, predicted in zip(y_true, y_pred):
        if actual == 1 and predicted == 1:
            TP += 1
        elif actual == 0 and predicted == 0:
            TN += 1
        elif actual == 0 and predicted == 1:
            FP += 1
        elif actual == 1 and predicted == 0:
            FN += 1

    return TP, TN, FP, FN


y_true = [1, 0, 1, 1, 0, 0, 1]
y_pred = [1, 0, 1, 0, 0, 1, 1]

TP, TN, FP, FN = confusion_matrix_calc(y_true, y_pred)

print("TP:", TP)
print("TN:", TN)
print("FP:", FP)
print("FN:", FN)