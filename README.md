This section describes a stock prediction task, the goal is to use data science methods to predict the rise and fall of future trading days based on historical stock data.

The target stock can be freely selected, this example uses ZIONL.

1. Task goal: Based on past stock data, it is necessary to identify patterns and label each trading day ("+" represents rise, "-" represents fall), and then predict the trend of future trading days based on these labels.

2. Data processing: First, read the daily return data of stocks and S&P-500, and label each day with "True Label" according to the daily return rate. For the data of the first 3 years, calculate the ratio of rising days to falling days respectively.

3. Question 1: Based on the data of the first 3 years, calculate the probability of rising or falling on the k+1th day after k consecutive "falling" or "rising" days.

4. Question 2: For each day of the 4th and 5th year, predict whether it will rise or fall based on the pattern of the previous 3 years, and test the prediction accuracy based on different W values ​​(pattern window length, W=2,3,4).

5. Question 3: Use the ensemble learning method to further improve the prediction accuracy through majority voting of the results of W=2,3,4.

6. Question 4: Calculate the statistics of the predicted labels, such as TP, FP, TN, FN, and analyze the performance of the prediction model, including TPR and TNR.

7. Question 5: Simulate the predicted trading strategy, starting from the 4th year, with an initial capital of $100, calculate the capital growth under the best W value and ensemble learning method, and compare it with the buy and hold strategy.

The final task is to analyze the performance of the model through experimental results and compare the capital growth under different strategies.
