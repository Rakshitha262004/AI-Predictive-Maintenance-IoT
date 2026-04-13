from src.preprocess import load_data, preprocess_data
from src.train import train_model
from src.predict import make_predictions
from src.visualize import plot_results, plot_feature_importance

# Load dataset
data = load_data("data/sensor_data.csv")

print("✅ Data Loaded Successfully")
print(data.head())

# Preprocess
X_train, X_test, y_train, y_test = preprocess_data(data)

# Train model
model = train_model(X_train, y_train)

# Predict
y_pred = make_predictions(model, X_test)

# Evaluate
plot_results(y_test, y_pred)

# Feature importance
plot_feature_importance()