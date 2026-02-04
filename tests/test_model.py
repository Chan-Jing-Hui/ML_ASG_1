import sys
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
import numpy as np
model = joblib.load("model.pkl")

# Load the dataset used for evaluation
test_data = pd.read_csv("test_data.csv")

# Split into inputs and target
X_test = test_data.drop(columns=["cnt"])
y_test = test_data["cnt"]

# Make predictions and calculate RMSE
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Test RMSE: {rmse:.4f}")

# Define the baseline RMSE
rmse_baseline = 674

# Quality Gate: assert that RMSE is below 95% of baseline
assert rmse <= 0.95 * rmse_baseline, (
    f"Quality Gate failed: RMSE {rmse:.4f} exceeds 95% of baseline ({0.95 * rmse_baseline:.4f})"
)

print("Quality Gate passed")
