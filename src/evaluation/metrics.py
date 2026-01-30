from sklearn.metrics import precision_score, recall_score, roc_auc_score

def evaluate(y_true,y_proba,threshold=0.4):
    y_pred = (y_proba >= threshold).astype(int)

    return{
        "precision":precision_score(y_true,y_pred),
        "recall":recall_score(y_true,y_pred),
        "roc_auc":roc_auc_score(y_true,y_pred)
    } 