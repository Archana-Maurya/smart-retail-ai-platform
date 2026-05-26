import joblib

model = joblib.load("../models/random_forest_classifier.pkl")

joblib.dump(model, "../models/superstore_pipeline_model.pkl")

print("Model saved successfully!")