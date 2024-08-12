# ECG Anomaly Detection using Darts Temporal Convolutional Network (TCN)
This project focuses on anomaly detection in ECG 5000 time series dataset using Temporal Convolutional Networks (TCNs) with the Darts library. The project includes data preprocessing, exploratory data analysis (EDA), forecasting, and anomaly detection and visualization.

### Data Preprocessing and EDA
Data was split into training, validation, and test sets, and then normalized and scaled. Different Classes in the dataset were identified and their samples were visualized and the number of counts of each class were identified. 

### Model Training
Model was trained on test and validation data and then dropout technique and early stopping till 10 epochs was used to ensure model doesnt overfit and the best model weights are restored after training. The model then generated predictions on the test set using the trained TCN model to assess its performance.

### Anomaly Detection
Calculated key metrics, including Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE), to quantify the model’s accuracy in forecasting ECG signals. Comparison plot was created between actual and predicted ECG values, with a clear visual representation highlighting the model's forecasting ability. Used the plotted results to visually assess the alignment between the model’s predictions and actual data, providing an intuitive understanding of model performance.

![image](https://github.com/user-attachments/assets/dc4e5445-189d-4993-856b-83b885956d6f)
