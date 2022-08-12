import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

from sklearn.preprocessing import StandardScaler

import torch
from torch import nn
from torch.nn import functional as F

data = {'Age': 37, 'Sex': 0, 'RestingBP': 300, 'Cholesterol': 400, 'FastingBS': 0,
        'MaxHR': 120, 'ExerciseAngina': 0, 'Oldpeak': 0, 'ChestPainType_ATA': 0,
        'ChestPainType_NAP': 1, 'ChestPainType_TA': 0, 'RestingECG_Normal': 0,
        'RestingECG_ST': 1, 'ST_Slope_Flat': 1, 'ST_Slope_Up': 0}

# Data preparation
df = pd.DataFrame([data])
chol = 240
df['Cholesterol'] = df['Cholesterol'].fillna(chol)

print(str(df))

# Transform data from dataframe
scaler = StandardScaler()
X_test = scaler.fit_transform(df.T)
X_test = X_test.T

print(str(X_test))

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

# Load best model
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = Net()
model.to(DEVICE)
model.load_state_dict(torch.load('./state_dict_final.pt'))


# Prediction
X_valid_batch = torch.from_numpy(X_test).float()
print(X_valid_batch)
output = model(X_valid_batch)
y_pred = torch.round(torch.sigmoid(output))
print("Prediction: "+str(y_pred[0].item()))

