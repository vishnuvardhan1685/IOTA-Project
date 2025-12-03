# Water Pump Prediction System

This project uses **Logistic Regression** machine learning to predict whether a water pump should be ON or OFF based on environmental sensor data.

## 📊 Dataset

- **File**: `Soil Moisture, Air Temperature and humidity, and Water Motor onoff Monitor data.AmritpalKaur.csv`
- **Total Records**: 3,000
- **Features**:
  - Soil Moisture (numeric)
  - Temperature (°C)
  - Air Humidity (%)
- **Target**: Pump Data (0 = OFF, 1 = ON)

## 🎯 Model Performance

- **Algorithm**: Logistic Regression
- **Accuracy**: **99.83%**
- **Training Set**: 2,400 samples (80%)
- **Testing Set**: 600 samples (20%)

### Classification Report:
```
              precision    recall  f1-score   support
Pump OFF (0)       1.00      1.00      1.00       286
Pump ON (1)        1.00      1.00      1.00       314
    accuracy                           1.00       600
```

### Key Insights:
- **Soil Moisture** is the strongest predictor (coefficient: -9.91)
  - Lower soil moisture → Pump ON
  - Higher soil moisture → Pump OFF
- Temperature and humidity have minimal impact

## 📁 Project Files

1. **`model_training.py`**: Trains the logistic regression model
2. **`predict.py`**: Interactive prediction system for user input
3. **`test_predictions.py`**: Tests model with sample data
4. **`pump_prediction_model.pkl`**: Saved trained model
5. **`scaler.pkl`**: Feature scaler for data normalization

## 🚀 Quick Start

### 1. Train the Model
```bash
python model_training.py
```

This will:
- Load and analyze the CSV data
- Train the logistic regression model
- Display model performance metrics
- Save the model and scaler

### 2. Make Predictions (Interactive)
```bash
python predict.py
```

This will prompt you to enter:
- Soil Moisture value
- Temperature (°C)
- Air Humidity (%)

Then it will predict whether the pump should be ON or OFF with confidence levels.

### 3. Test with Sample Data
```bash
python test_predictions.py
```

## 💡 Example Predictions

### Example 1: Low Soil Moisture
```
Input:
  - Soil Moisture: 400
  - Temperature: 33°C
  - Air Humidity: 77%

PREDICTION: Pump should be ON 🟢
Confidence: 100.00%
```

### Example 2: High Soil Moisture
```
Input:
  - Soil Moisture: 800
  - Temperature: 32°C
  - Air Humidity: 50%

PREDICTION: Pump should be OFF 🔴
Confidence: 99.81%
```

## 📦 Dependencies

```
pandas
numpy
scikit-learn
joblib
```

Install with:
```bash
pip install pandas numpy scikit-learn joblib
```

## 🔧 How It Works

1. **Data Preprocessing**: Features are standardized using StandardScaler
2. **Model Training**: Logistic Regression with max_iter=1000
3. **Prediction**: New inputs are scaled and fed to the model
4. **Output**: Binary classification (0/1) with probability scores

## 🎓 Understanding the Model

The model predicts pump status based on the logistic function:

**Key Pattern Learned**:
- **Soil Moisture < ~650**: Pump ON (soil needs water)
- **Soil Moisture > ~650**: Pump OFF (soil has enough water)

Temperature and humidity play minor roles in fine-tuning the decision.

## 📈 Model Coefficients

| Feature | Coefficient | Impact |
|---------|------------|--------|
| Soil Moisture | -9.91 | Strong negative (lower → ON) |
| Temperature | 0.004 | Minimal positive |
| Air Humidity | -0.014 | Minimal negative |

## 🤝 Usage Tips

- Ensure input values are within reasonable ranges:
  - Soil Moisture: 300-1000
  - Temperature: 18-40°C
  - Air Humidity: 35-85%
- The model provides probability scores for transparency
- Higher confidence (>95%) indicates more certain predictions

## 📝 Notes

- The model uses feature scaling for better performance
- Always use the same scaler that was used during training
- Model files (`.pkl`) must be in the same directory as the prediction scripts

---

**Created**: December 2025
**Model**: Logistic Regression (scikit-learn)
**Accuracy**: 99.83%
