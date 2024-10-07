# Rental-Listing-Analysis
### October 2024

## As the individual developer of this analysis in R and Python, I gained insights to further understand how host/listing trustworthiness impacts the price and service fee of a rental listing.
## Using a sample dataset with 5,000 records and 19 distinct variables, I cleaned and pre-processed the data as my first step. 

## Using Python, I created a dummy variable for the qualitative variable (verified host identity). I also dealed with the missing values in the columns of interest, looking at the relationship between missing values in one variable and another variable. I filled in the missing values as necessary.

## Also in Python, I created visualizations to compare the price between unverified host and verified host, price among all 5 star ratings, and a correlation matrix between all variables of interest.

## In R, I completed some text mining processes to create a word cloud and visualize commonly used words in the house rules for a rental listing, as well as, sentiment analysis to identify the overall sentiment of the house rules.

## At the end of the analysis, I produced many insights:
### 1. Because the p-value between number of reviews and reviews per month is far less than 0.05, I can deduce that the missing values in reviews_per_month are related to number_of_reviews. This makes sense because if there are no reviews, there will be no reviews per month. Additionally, there is a positive correlation between reviews per month and number of reviews. This makes sense because the more number of reviews, the more reviews per month.
### 2. Because the p-value between verified_host_identity and host_listings_count is far greater than 0.05, I can deduce that the missing values in verified_host_identity are not related to host_listings_count.
### 3. The boxplot showing price distribution between verified and unverified host identity shows that there is not much difference in price between verified and unverified hosts.
### 4. The boxplot showing price against star rating shows that there is slight variation between the medians and overall range, especially for 0 rating homes. However, the difference is not very significant.
### 5. The correlation showed many insights including... There is a perfect positive correlation between price and service fee. This makes sense because service fee is a part of the price. Verified host identity has a very weak but negative correlation with price. This is interesting because I would have expected a positive correlation, that a verified identity would increase the price. There is a weak positive correlation between star rating and price. This is also interesting because I would have expected a stronger correlation. Better reviews would typically mean higher price.
### 6. The overall sentiment of the house rules was mostly neutral with a few more being a little bit negative. From the word cloud, the most frequent words were "please", "smoke", "respect", and "pet". Overall, I can understand that the hosts are concerned about respect for their property, while being polite in their requests!
