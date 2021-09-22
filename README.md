# Introduction
This repository holds data and code for my Bachelor thesis: *"Exploring machine learning models for churn prediction of membership subscriptions"*. The goal is to test different ML models to predict if a member will be renewing their yearly membership.

The metric of choice for this classification task of predicting non-renewals will be **precision** with the acceptable threshold of 75%. That being said the performance metric and threshold might be re-evaluated after performing some EDA on the data and determining class balance.

# Business objective
Devise a ML model for for predicting who won't be renewing their membership and to determine if the non-renewing member can be converted 3 months prior to their renewal date.

**Extra:** If a probability model has good performance then determine users who are within 30% - 50% chance of renewing. Those users have the biggest potential to be converted from non-renewals to renewals.

# Data
General facts:
- The available data is inspired by PALMS data found in company named *Business Networking International* (BNI)
- BNI creates local groups of entrepreneurs who form relationships and refer eachother's businesses
- Company business model: yearly membership subscription
- BNI groups meet on a weekly basis
## Datasets: PALMS
- Data from 2016-03 to 2021-02 in a monthly format
- Each months' PALMS data contains information members and chapters performance

Here are a couple of links with a legend/explanation of the PALMS data: [Link 1](https://support.bniconnect.com/hc/en-us/articles/219067027-Summary-PALMS-Report) and [Link 2](https://bniblog.co.nz/bni-core-values/accountability/palms-for-beginners/).


## Dataset: database_data
General information about all members.

## Dataset: dropped_members_data
Information about member drop and join dates.

# Thesis plan
1. [x] 1. Prepare for thesis
   1. [x] Get data
   2. [x] Business objective
   3. [x] Create a cleaning log
   4. [x] Decide on metric and threshold of choice
2. [ ] 2. Prepare & clean data (*"cleaning_log.md"*)
   1. [x] Anonymize data
   2. [x] Check control sums to ensure PALMS data hasn't been duplicated
   3. [x] Concatenate PALMS data
   4. [x] Create a master dataset - merge
   5. [ ] Ensure data integrity:
      1. [x] Fix member records with two or less months with negative year of membership
      2. [ ] Fix member records with more than two months with negative year of membership
      3. [ ] Remove duplicate records
   6. [ ] Aggregate 3-, 6-, 9- month datasets
   7. [ ] Re-merge datasets
   8.  [ ] Label: renewing/not renewing
3. [ ] 3. Explore data (each of the 3-, 6-, 9- month aggregated datasets)
   1. [ ] Feature engineering:
      1. [ ] Seat popularity rate
      2. [ ] Chapter retention rate
      3. [ ] Chapter size
   2. [ ] Feature selection
   3. [ ] Exploratory Data Analysis:
      1. [ ] Summary Statistics
      2. [ ] Outliers
      3. [ ] Normality
      4. [ ] Visual representations
   4. [ ] Scale
   5. [ ] [Extra] Data Analysis:
      1. [ ] Which features are the most indicative if the member will or won't renew?
      2. [ ] Which seats are the most profitable?
4. [ ] 4. Create ML models
   1. [ ] Split data: train, validate, test
   2. [ ] Hyperparameter tuning (cross-validate & plot)
   3. [ ] Learning curve
   4. [ ] Power analysis
   5. [ ] Test results
5. [ ] 5. Meet with promotor to discuss results and get feedback
6. [ ] 6. Write LaTeX thesis 
