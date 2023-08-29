# FraudDetection

## What is fraud detection?
Fraud detection is the process of recognizing and preventing unauthorized or illegal activities or transactions. Fraud detection leverages machine learning, statistical analysis, and behavioral monitoring to identify activities, patterns or other characteristics that signal fraud.

## Learning Goal
The goal of this project is not to find the best model but to show a way to deal with a dataset extremey unbalanced.<br/>
In fact, as shown in the picture in Milestone 1 only 0.001% is actually fraud transactions.<br/>

In this project, I will show how to apply resampling to improve the model and how to use cross-validation to ensure reliable performance.<br/>
Finally, I will discuss the metrics to evaluate the performance score.<br/>

## Milestone 1: EDA
The dataset is provided by Kaggle.<br/>
It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features that have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependent cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.<br/>

The picture below shows the proportion between not-fraud and fraud transactions.<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/piechart.png)<br/>

As we can see we have just a few examples in comparison with not-fraud transactions.<br/>
This is a bit tricky for a model as it needs examples to find patterns.<br/>
In Milestone 3 we will discuss which techniques to use with this kind of data frame.<br/>

## Milestone 2: Baseline Score

As I said before in this project it doesn't matter the performance of the model itself rather it is more important how we can improve it with the right techniques.<br/>

The first model presented is the logistic regression.<br/>
It is a relatively simple model and prone to underfitting so it should struggle with this kind of data frame.<br/>
The following is the baseline score that we get:<br/>

![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/summary_logistic.png)<br/>

The second one is the GaussianNB and as we can see it performs quite poorly:<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/summary_gaussiannb.png)<br/>

## Milestone 3: Apply resampling
Oversampling and Under sampling are techniques used in data analytics to modify the unequal data classes to create balanced data sets widely known as re-sample. <br/>
The question most frequently thrown is, when do we need to use over-sampling over under-sampling or vice versa?<br/>

Under sampling is a bit risky as we are going to remove some examples that could be useful and meaningful.<br/>
This is true especially when the examples are quite spared.<br/>
Let's get a general idea about our situation.<br/>
The following examples show scatterplots in order to see the distribution of the two classes:<br/>

![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_1.png)<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_2.png)<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_3.png)<br/>

As visible it is difficult to build clusters around the data points.<br/>
A good choice could be to go for oversampling trying to stick with the original fraud transactions.<br/>
A library that suits very well to our needs is BorderlineSMOTE.<br/>
It allows tuning the percentage of resampling.<br/>
For example, with 0.05 we get the following result:<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_1_res.png)<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_2_res.png)<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/scatter_3_res.png)<br/>

## Milestone 4: Cross Validation
Another complex problem to solve is how to make sure we get reliable results as we have just a few examples for fraud detection.<br/>
As visible in resampling_helper.py I use StratifiedKFold.<br/>
What is that?<br/>
According to the documentation of sklearn<br/>
(https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) <br/>
This cross-validation is a variation of KFold that returns stratified folds. The folds are made by preserving the percentage of samples for each class.<br/>

In this way, we can assume that the result will be more similar to what we will get in testing.<br/>

## Milestone 5: Metrics
Let's imagine we build a model that says always "it is not a fraud".<br/>
What will it be its accuracy?<br/>
Well,0.99 accuracy.It is easy to predict as we have in our dataframe 0.99 not fraud transactions.<br/>
It goes without saying that we need another metric.<br/>
A good solution could be the f1-score.<br/>
What is that?<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/f1.png)<br/>
Basically it is the harmonic mean between precision and recall.<br/>
It is useful because this kind of mean will be closer to the lowest number.<br/>

So let's say our model says "It is a fraud,run to check!"<br/>
With precision we can see how believable it is this warning.<br/>

Recall is essential as it shows how many fraud transactions we are able to catch.<br/>

### Precision-Recall Trade-Off

Ideally, we would want both: a model that identifies all of our positive cases and that is at the same time identifies only positive cases.<br/>

In real life, we, unfortunately, have to deal with the so-called Precision-Recall Trade-Off.<br/>
The Precision-Recall Trade-Off represents the fact that in many cases, you can tweak a model to increase precision at a cost of a lower recall, or on the other hand increase recall at the cost of lower precision.<br/>

## Milestone 6: Performance after resampling
First of all, we need to find the best rate of resampling(check out the code in project.py).<br/>
For example for logistic regression we get this result:<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/resamling_rate.png)<br/>

On X-axis we have the rate of resampling and on Y-Axis we have to f1 score.<br/>
So we are going to pick the greatest one.<br/>

Let's now compare the performance in testing with the no resampled one:<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/resampled_log.png)<br/>

As we can see we get better results and the same is for the GaussianNB model.<br/>
Another good way to compare the two models in this case is the precision-recall curve as it shows the trade-off(it works very similar to ROC-Curve)<br/>
Below the results for logistic regression:<br/>
Before resampling:<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/PreCallLog.png)<br/>

After resampling:<br/>
![alt text](https://github.com/alessandroNarcisi96/FraudDetection/blob/master/images/PreCallLogRes.png)<br/>
