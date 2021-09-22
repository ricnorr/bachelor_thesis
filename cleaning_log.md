# Purpose
The goal of this file is to document the cleaning process of the data in order to maintain it's integrity and to enable double-checking for external people.

# Log

| # | Date       | Contributor | Description                                                                                                        |
|---|------------|-------------|--------------------------------------------------------------------------------------------------------------------|
| 1 | 2021-09-01 | DM          | Created 'main_script.ipynb' for data cleaning and preparation                                                      |
| 2 | 2021-09-01 | DM          | Imported all PALMS datasets and concatenated them as ```df_palms```                                                |
| 3 | 2021-09-01 | DM          | Imported 'database_data.csv' as ```df_database``` and 'dropped_members_data.csv' as ```df_dropped_members```       |
|   | 2021-09-01 | DM          | Dropped ```chapter_ID``` column from ```df_database``` as I assume it won't be needed later.                       |
|   | 2021-09-01 | DM          | Dropped ```Date/Time``` column from ```df_dropped_members```. This column contains time of the drop action         |
|   | 2021-09-01 | DM          | Dropped records with invalid ```user_ID``` from ```df_dropped_members```                                           |
|   | 2021-09-01 | DM          | Converted column types in all datasets                                                                             |
|   | 2021-09-01 | DM          | Merged three datasets to create ```df_master``` : ```df_palms```, ```df_database``` and ```df_dropped_members```   |
|   | 2021-09-02 | DM          | Calculated relative time-distance to the nearest renewal date per member                                           |
|   | 2021-09-02 | DM          | Started aggregation for 3-months data                                                                              |
|   | 2021-09-17 | DM          | Added control sums for PALMS data to ensure that no datasets have been duplicated                                  |
|   | 2021-09-17 | DM          | Re-added the ```chapter_ID``` column to ```df_database```. It is needed for the master dataset                     |
|   | 2021-09-17 | DM          | Copied ```df_master``` to ```df_master_cleaned``` for cleaning process                                             |
|   | 2021-09-17 | DM          | Substituted 0 with 12 in the ```months_to_renewal``` column in ```df_master_cleaned``` for ease of aggregation.    |
|   | 2021-09-17 | DM          | Find records in ```df_master_cleaned``` which have a negative ```year_of_membership```                             |
|   | 2021-09-17 | DM          | Checked members with two or less months of negative membership in ```df_master_cleaned```                          |
|   | 2021-09-17 | DM          | Started member-by-member cleaning who have more than two months of negative membership in ```df_master_cleaned```  |
|   |            |             |                                                                                                                    |