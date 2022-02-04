# Segmenting with PCA

In this activity, you will use your knowledge of PCA in order to reduce the dimensionality of the the customers DataFrame that you used previously. Then, you'll compare that result to the segmentation of the data using all of the factors.

## Instructions

The PCA technique for dimensional reduction has just come to your attention. At this point, you have already segmented the data based on all of the factors, but are wondering if PCA would alter the segmentation results.

Using the [starter code](Unsolved/segmenting_with_pca.ipynb) and the customer data provided, reduce the factors to only two dimensions by using PCA and determine the optimal value for k by using the PCA DataFrame. Then, segment the data using the K-means algorithm and the optimal value for k. Once these steps are complete, segment the preprocessed customers DataFrame using the K-means algorithm and that same value for k, and then compare the segmentation results.

This task will involve five steps. Follow the instructions below to accomplish each step.

1. Use PCA to reduce the dimensionality of the `customers_transformed_df` DataFrame to two principal components.

    * Import the PCA module from scikit-learn.

    * Instantiate the instance of the PCA model declaring the number of principal components as two.

    * Using the `fit_transform` function from PCA, fit the PCA model to the `customers_transformed_df` DataFrame. Review the first five rows of list data.

    * Using the `explained_variance_ratio_` function from PCA, calculate the percentage of the total variance that is captured by the two PCA variables. What is the explained variance ratio captured by the two PCA variables?

    * Using the `customer_pca` data, create a Pandas DataFrame called `customers_pca_df`. The columns of the DataFrame should be called "PCA1" and "PCA2".

2. Using the `customers_pca_df` DataFrame, use the elbow method to determine the optimal value of k.

3. Segment the `customers_pca_df` DataFrame using the K-means algorithm and the optimal value for k defined in Step 2.

4. Segment the `customers_transformed_df` DataFrame with all factors by using the K-means algorithm.

5. Compare the segmentation results between the PCA DataFrame and the full-factored DataFrame.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
