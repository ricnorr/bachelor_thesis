# Introduction
This repository holds data and code for my Bachelor thesis: *"Exploring machine learning models for churn prediction of membership subscriptions"*. The goal is to test different ML models to predict if a member will be renewing their yearly membership.

# Business objective
TBD 

# Data
General facts:
- The available data is inspired by PALMS data found in company named *Business Networking International* (BNI)
- BNI creates local groups of entrepreneurs who form relationships and refer eachother's businesses
- Company business model: yearly membership subscription
- BNI groups meet on a weekly basis
## PALMS
- Data from 2016-03 to 2021-02 in a monthly format
- Each month contains data about near
- Data about each members' performance
- No indicators about cross-member level of relationship

## database_data
General information about all members.

## dropped_members_data
Information about member drop and join dates.

# Thesis plan
1. [ ] 1. Prepare for thesis
   1. [x] Get data
   2. [ ] Business objective
   3. [x] Create a cleaning log
   4. [ ] Decide on metric and threshold of choice
2. [ ] 2. Prepare & clean data (*"cleaning_log.md"*)
   1. [x] Anonymize data
   2. [x] Check control sums to ensure PALMS data hasn't been duplicated
   3. [x] Concatenate PALMS data
   4. [x] Create a master dataset - merge
   5. [ ] Ensure data integrity
   6. [ ] Aggregate 3-, 6-, 9- month datasets
   7. [ ] Label renewal/not renewal
3. [ ] 3. Explore data (each of the 3-, 6-, 9- month aggregated datasets)
   1. [ ] Feature engineering
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
