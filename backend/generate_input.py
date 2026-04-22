import numpy as np
import json

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
X = np.load(os.path.join(BASE_DIR, "data/processed/X.npy"))

# Take one sample (already correct format)
sample = X[0].tolist()

data = {"sequence": sample}

# Save to file instead of printing
with open("sample_input.json", "w") as f:
    json.dump(data, f)

print("File saved: sample_input.json")