# FraudDetection

## What is fraud detection?
Fraud detection is the process of recognizing and preventing unauthorized or illegal activities or transactions. Fraud detection leverages machine learning, statistical analysis, and behavioral monitoring to identify activities, patterns or other characteristics that signal fraud.

## Learning Goal
The goal of this project is not to find the best model but to show a way to deal with a dataset extremey unbalanced.
Infact as shown in the picture below only the 0.001% are actually fraud transactions.

In this project I will show how to apply resampling to improve the model and how to use cross validation to ensure reliable performance.
Finally I will discuss the metrics to evaluate the performance score.

## Milestone 1: EDA
The dataset is provided by Kaggle.
It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

The picture below shows the proportion between not-fraud and fraud transaction.
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/piechart.png)

As we can see we have just a fews example in comparison with not-fraud transaction.
This is a bit tricky for a model as it needs examples to find patterns.
In Milestone 3 we will the discuss which tecnique to use with this kind of dataframe.

## Milestone 2: Baseline Score

As I said before in this project it doesn't matter the performace of the model itself rather it more important how we can improve it with the right tecniques.

The first model presented is the logistic regression.
It is a relatevely simple model and prone to underfitting so it should struggle with this kind of dataframe.
The following is the baseline score that we get:

![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/summary_logistic.png)

The second one is the GaussianNB and as we can see it performs quite poorly:
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/summary_gaussiannb.png)

## Milestone 3: Apply resampling
Oversampling and Under sampling are techniques used in data analytics to modify the unequal data classes to create balanced data sets as widely known as re-sample as well. The question most frequently thrown is, when do we need to use over-sampling over under -sampling or vice versa?

Under sampling is a bit risky as we are going to remove some examples that could be useful and meaningfull.
This is true especially when the examples are quite spared.
Let's get a general idea about our situation.
The following examples show scatterplots in order to see the distribuition of the two classes:

![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_1.png)
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_2.png)
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_3.png)

As visible it is difficult building clusters around the datapoints.
A good choice could be go for oversampling trying to stick with the original fraud transactions.
A libray that suits very well to our needs is BorderlineSMOTE.
it allows to tune the percentage of resampling.
For example with 0.05 with get the following result:
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_1_res.png)
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_2_res.png)
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_3_res.png)

## Milestone 4: Cross Validation

## Milestone 5: Metrics