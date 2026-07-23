import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class ModelTraining:

    def train(self):

        # df = pd.read_json("output/student_performance_cleaned.json")
        df = pd.read_json("output/energy_efficiency_cleaned.json")

        # Features
        X = df.drop(["heating_load", "cooling_load"], axis=1)
        y = df[["heating_load", "cooling_load"]]

        # Train Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        # Model
        model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)

        model.fit(X_train, y_train)
        print("Model Trained Successfully!")

        importance = pd.DataFrame(
            {"Feature": X.columns, "Importance": model.feature_importances_}
        )

        print("\nFeature Importance:")
        print(importance.sort_values(by="Importance", ascending=False))

        prediction = model.predict(X_test)

        print("Prediction:")
        print(prediction)

        plt.figure(figsize=(10, 4))

        # Heating Load
        plt.subplot(1, 2, 1)
        plt.scatter(y_test["heating_load"], prediction[:, 0])
        plt.title("Heating Load")
        plt.xlabel("Actual")
        plt.ylabel("Predicted")

        # Cooling Load
        plt.subplot(1, 2, 2)
        plt.scatter(y_test["cooling_load"], prediction[:, 1])
        plt.title("Cooling Load")
        plt.xlabel("Actual")
        plt.ylabel("Predicted")

        plt.tight_layout()
        plt.show()

        # Evaluation
        mae = mean_absolute_error(y_test, prediction)

        mse = mean_squared_error(y_test, prediction)

        r2 = r2_score(y_test, prediction)

        print("\n===== Model Evaluation =====")

        print("Mean Absolute Error (MAE):", mae)

        print("Mean Squared Error (MSE):", mse)

        print("R2 Score:", r2)
