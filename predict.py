import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('pump_prediction_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_pump_status(soil_moisture, temperature, air_humidity):
    """
    Predict whether the water pump should be ON or OFF based on input parameters.
    
    Parameters:
    - soil_moisture: Soil moisture reading
    - temperature: Air temperature in Celsius
    - air_humidity: Air humidity percentage
    
    Returns:
    - prediction: 0 (Pump OFF) or 1 (Pump ON)
    - probability: Confidence level of the prediction
    """
    # Prepare input data
    input_data = np.array([[soil_moisture, temperature, air_humidity]])
    
    # Scale the input
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]
    
    return prediction, probability

def main():
    print("\n" + "="*60)
    print("WATER PUMP PREDICTION SYSTEM")
    print("="*60)
    print("\nThis system predicts whether the water pump should be ON or OFF")
    print("based on soil moisture, temperature, and air humidity readings.")
    
    while True:
        print("\n" + "-"*60)
        try:
            # Get user input
            soil_moisture = float(input("\nEnter Soil Moisture value: "))
            temperature = float(input("Enter Temperature (°C): "))
            air_humidity = float(input("Enter Air Humidity (%): "))
            
            # Make prediction
            prediction, probability = predict_pump_status(soil_moisture, temperature, air_humidity)
            
            # Display results
            print("\n" + "="*60)
            print("PREDICTION RESULTS")
            print("="*60)
            print(f"\nInput Values:")
            print(f"  - Soil Moisture: {soil_moisture}")
            print(f"  - Temperature: {temperature}°C")
            print(f"  - Air Humidity: {air_humidity}%")
            
            print(f"\n{'='*60}")
            if prediction == 1:
                print(f"PREDICTION: Pump should be ON 🟢")
                print(f"Confidence: {probability[1]*100:.2f}%")
            else:
                print(f"PREDICTION: Pump should be OFF 🔴")
                print(f"Confidence: {probability[0]*100:.2f}%")
            print(f"{'='*60}")
            
            print(f"\nProbability Distribution:")
            print(f"  - Pump OFF (0): {probability[0]*100:.2f}%")
            print(f"  - Pump ON (1): {probability[1]*100:.2f}%")
            
        except ValueError:
            print("\n⚠️  Error: Please enter valid numeric values!")
            continue
        except FileNotFoundError:
            print("\n⚠️  Error: Model files not found! Please run 'model_training.py' first.")
            break
        except Exception as e:
            print(f"\n⚠️  Error: {e}")
            break
        
        # Ask if user wants to make another prediction
        print("\n" + "-"*60)
        continue_pred = input("\nWould you like to make another prediction? (yes/no): ").lower()
        if continue_pred not in ['yes', 'y']:
            print("\n" + "="*60)
            print("Thank you for using the Water Pump Prediction System!")
            print("="*60)
            break

if __name__ == "__main__":
    main()
