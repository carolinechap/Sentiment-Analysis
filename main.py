import pandas as pd
import time

print("Loading data file now")
start = time.time()

df = pd.read_csv('data/Hotel_Reviews.csv')
end = time.time()

print("Loading took " + str(round(end - start, 2)) + "seconds")


# print(df["Reviewer_Nationality"])

# Number of each nationality : 227
frequency_nationality  = df["Reviewer_Nationality"].value_counts()
# print(str(frequency_nationality.size))

# List of each nationality :
# print(frequency_nationality.to_string())

# The first nationality reviewer :
# print(frequency_nationality.index[0])

# 10 most reviewer (nationality) + nb review :
first_ten_nationality_reviewers = frequency_nationality[0:10]
# print(first_ten_nationality_reviewers)

# The first nationality reviewer
# print(frequency_nationality.index[0].strip())


# The most frequency review hotel of each 10 most reviewer nationalities :
for nationality in first_ten_nationality_reviewers.index:
    nat_df = df[df['Reviewer_Nationality'] == nationality]
    frequencies = nat_df["Hotel_Name"].value_counts()
    # print(nationality, "/ hotel : ", frequencies.index[0])



# Reviews per hotel
## Copy the dataset in order to only have the wanted column.
hotel_reviews_df = df[["Hotel_Name", "Total_Number_of_Reviews"]].copy()
## Group by hotel's name.
hotel_reviews_df["Total_of_our_reviews"] = hotel_reviews_df.groupby('Hotel_Name').transform('count')
hotel_reviews_df = hotel_reviews_df.drop_duplicates(subset = ["Hotel_Name"])
