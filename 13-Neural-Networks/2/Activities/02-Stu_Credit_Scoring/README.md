# Credit Scoring

In this activity, you will use a deep learning model to predict the credit scores of borrowers using alternative data.

## Instructions

Fintech opportunities in emerging economies are extremely large. There are billions of new consumers, with access to a digital wallet, who have a desire to get a lower interest rate loan. The trouble is, most of them don't have a credit score.

An alternative data firm is therefore collecting data on emerging market consumers, from utility bills, to industry worked, to even responses to online surveys about good money habits. They've provided you this data, in order to build a model which can be use all of this information to provide a usable credit score for anyone interested in applying for a loan.

The dataset contains `68` encoded features (columns from `0` to `67`), with all personal identifying information removed. The last two columns of the dataset (columns `68` and `69`) are preliminary credit score quality indicators that have been manually assigned by staff at the firm. (The firm thinks that if a model can be built for this labeled data, it can then be used to automatically make credit predictions about customers it hasn't gone through this labelling process with).

1. Create a shallow (`1` hidden layer) and deep neural network (with two layers) to predict the credit scores represented in the data. Decide on your own how many neurons you will use on each hidden layer.

2. Fit each model with at least `800` epochs, and setting `validation_split=0.3`.

3. Compare the loss metrics for the two models.

4. Compare train (loss) and test (val_loss) metrics for both models, and look for signs of overfitting.

## Hint

* Note that that there needs to be two regression outputs. Your model structure should reflect this.

* When fitting the model, you can set the parameter `verbose=0` in the `fit()` method to mute the printing of each epoch's results.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
