# After Training

In this activity, you will create a deep learning model from the credit score data, save it, and load it to evaluate its performance on unseen data.

## Instructions

1. Split the data into training and test sets using the `train_test_split` method from `sklearn`. Then scale the features data using an instance of the `StandardScaler`.

2. Using the training set, construct a shallow neural net model to predict the credit score features (you can use the same model that you constructed in the _Credit Scoring_ Activity).

> **Note** When fitting the model, you will not need a `validation-split` parameter because the data was seperated into training and testing datasets.

3. Using relative file paths, save the model and its weights.

4. Load the model and its weights.

5.  Use this loaded model to predict points for the test data and print the mean squared error metric for the predicted points vs. the actual points.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
