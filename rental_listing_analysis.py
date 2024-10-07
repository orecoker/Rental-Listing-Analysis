### Rental Listing Analysis ###

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import seaborn as sns

# read in data
airbnb = pd.read_csv("AirbnbSample4.csv")

# Data Analysis Goal:

## Identify if host/listing trustworthiness 
#### defined as: host_identity_verified, number_of_reviews, reviews_per_month, star_rating, host_listings_count
#### impacts the price and service fee of a rental listing.

# Data Cleaning & Missing Values:

## MISSING VALUES ##
## Identify columns with missing values
airbnb.isna().sum()
# IMPORTANT missing values:
# 1. host_identity_verified 
# 2. price
# 3. service_fee
# 4. number_of_reviews
# 5. reviews_per_month
# 6. star_rating
# 7. host_listings_count

# Missing values in price and service fee are errors in data collection. 
# There are total 19 records affected. Therefore, I will drop.
airbnb.dropna(subset=["price", "service_fee"], inplace=True)

# Missing values in star_rating & number_of_reviews makes sense... 
# No reviews/ratings in the listing yet. However, the 24 records should be handled.
airbnb["star_rating"].fillna(0, inplace=True)
airbnb["number_of_reviews"].fillna(0, inplace=True)

# Do missing values in number_of_reviews relate to reviews_per_month?
airbnb["MV_reviews_per_month"] = np.where(airbnb["reviews_per_month"].isna(),
                                      1,
                                      0)

# Look at missing reviews per month against number of reviews
airbnb.boxplot(column=["number_of_reviews"],by=["MV_reviews_per_month"])
plt.show()

# T-test to check if there is significant difference 
print(ttest_ind(airbnb["number_of_reviews"][airbnb["MV_reviews_per_month"]==True], 
                airbnb["number_of_reviews"][airbnb["MV_reviews_per_month"]==False]).pvalue)

# Because the p-value is far less than 0.05, I can deduce that...
# the missing values in reviews_per_month are related to number_of_reviews.
# This makes sense because if there are no reviews, there will be no reviews per month.
# Therefore, I will fill missing values in reviews_per_month with 0.
airbnb["reviews_per_month"].fillna(0, inplace=True)

# Missing values in host_listings_count are errors in the data, impacting further analysis.
# I will drop the 7 records.
airbnb.dropna(subset=["host_listings_count"], inplace=True)

# Look at missing values in host_identity_verified
airbnb[airbnb["host_identity_verified"].isna()]

# Create columns to closer analyze
airbnb["MV_host_identity"] = np.where(airbnb["host_identity_verified"].isna(),
                                      1,
                                      0)
# Look at missing host identity against neighborhood
airbnb.boxplot(column=["host_listings_count"],by=["MV_host_identity"])
plt.show()

# T-test to check if there is significant difference 
print(ttest_ind(airbnb["host_listings_count"][airbnb["MV_host_identity"]==True], 
                airbnb["host_listings_count"][airbnb["MV_host_identity"]==False]).pvalue)

# Because the p-value is far greater than 0.05, I can deduce that...
# the missing values in verified_host_identity are not related to host_listings_count.
# Therefore, I will fill missing values in host_identity_verified with "unverified".
airbnb["host_identity_verified"].fillna("unverified", inplace=True)

## VARIABLE HANDLING ##
# Create dummy variables for verified host identity
airbnb["verified_host"] = np.where(airbnb["host_identity_verified"]=="verified",
                                            True,
                                            False)

# Drop Missing Value columns
airbnb = airbnb.drop(columns=["MV_reviews_per_month", "MV_host_identity"])

# Data Visualization:

# Boxplot of Price against a verified Host Identity.
airbnb.boxplot(column=["price"],by=["verified_host"])
plt.title("Price vs. Host Identity Verified")
plt.suptitle("")
plt.xlabel("Verified Host")
plt.ylabel("Price")
plt.show()
# This shows that there is not much difference in price between verified and unverified hosts.

# Boxplot of Price against Star Rating
airbnb.boxplot(column=["price"], by=["star_rating"])
plt.title("Price vs Star Rating")
plt.suptitle("")  # Removes default subtitle
plt.xlabel("Star Rating")
plt.ylabel("Price")
plt.show()
# There is slight variation between the medians and overall range, especially for 0 rating homes.
# However, the difference is not very significant.

# Compute correlation matrix
corr = airbnb[["verified_host", "price", "number_of_reviews", "reviews_per_month", "service_fee", "host_listings_count", "star_rating"]].corr()
# Create heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
# There is a perfect positive correlation between price and service fee. This makes sense because service fee is a part of the price.
# There is a positive correlation between reviews per month and number of reviews. This makes sense because the more reviews, the more reviews per month.
# I found that a verified host has a very weak but negative correlation with price. This is interesting because I would have expected a positive correlation.
# There is a weak positive correlation between star rating and price. This is also interesting because I would have expected a stronger correlation. Better reviews would typically mean higher price.

airbnb.to_csv("airbnb_cleaned.csv", index=False)

# Text Mining completed in rental_listing_textmining.R

############################################################
