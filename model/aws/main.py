import pandas as pd
from model.adaptive_model import AdaptiveThresholdModel
from aws.upload_to_s3 import upload_to_s3

# Load Data
df = pd.read_csv("data/emg_signals.csv")
X = df[['signal1', 'signal2', 'signal3']]
y = df['label']

# Train Model
model = AdaptiveThresholdModel()
model.train(X, y)

# Predict and simulate feedback
preds = model.predict(X)
feedback_accuracy = sum(preds == y) / len(y)
print("Initial Accuracy:", feedback_accuracy)

# Update threshold based on feedback
model.update_threshold(feedback_accuracy)
print("Updated threshold:", model.threshold)

# Save result
output_file = "output_results.txt"
with open(output_file, "w") as f:
    f.write(f"Accuracy: {feedback_accuracy}\nThreshold: {model.threshold}")

# Upload to S3
upload_to_s3(output_file, "your-s3-bucket-name")
