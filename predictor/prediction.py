import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

from sklearn.preprocessing import StandardScaler

import torch
from torch import nn
from torch.nn import functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layer_1 = nn.Linear(15, 24)
        self.layer_out = nn.Linear(24, 1)
        self.dropout1 = nn.Dropout(p=0.33444)

    def forward(self, inputs):
        x = F.relu(self.layer_1(inputs))
        x = self.dropout1(x)
        x = self.layer_out(x)

        return x


def makePrediction(user_data):
    user_data = dict(user_data)
    df = pd.DataFrame([user_data])
    chol = 240
    df['Cholesterol'] = df['Cholesterol'].fillna(chol)

    # Transform data from dataframe
    scaler = StandardScaler()
    X_test = scaler.fit_transform(df.T)
    X_test = X_test.T

    # Load best model
    DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = Net()
    model.to(DEVICE)
    model.load_state_dict(torch.load('./predictor/state_dict_final.pt'))

    # Prediction
    X_valid_batch = torch.from_numpy(X_test).float()
    output = model(X_valid_batch)
    ypred_rest = torch.sigmoid(output)
    #y_pred = torch.round(torch.sigmoid(output))
    #y_pred_label = "Positive" if y_pred[0].item() > 0.5 else "Negative"
    return str(ypred_rest[0].item())

