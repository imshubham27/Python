#  A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
# Pandas DataFrame consists of three principal components, the data, rows, and columns.

# Because Pandas is an open source software library which is built on top of NumPy
# Pandas is used for data manipulation, analysis and cleaning.
import pandas as pd

XYZ_web = {'Day': [1, 2, 3, 4, 5, 6], "Visitors": [
    1000, 700, 6000, 1000, 400, 350], "Bounce_Rate": [20, 20, 23, 15, 10, 34]}
df = pd.DataFrame(XYZ_web)
print(df)
print(df.head(2))
print(df.tail(2))

# Merging & Joining
df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate1": [
                   2, 1, 2, 3], "IND_GDP1": [50, 45, 45, 67]}, )
df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate2": [
                   24, 14, 24, 34], "IND_GDP2": [505, 455, 455, 675]},)
merged = pd.merge(df1, df2,)
print(merged)

# join quite similar to the “merge” operation, except the joining operation will be on the “index” instead of  the “columns”.
df1 = pd.DataFrame({"Int_Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"Low_Tier_HPI": [50, 45, 67, 34], "Unemployment": [
                   1, 3, 5, 6]}, index=[2001, 2003, 2004, 2004])
joined = df1.join(df2)
print(joined)

# As you can notice in the above output, in year 2002(index), there is no value attached to columns “low_tier_HPI” and “unemployment”, therefore it has printed NaN (Not a Number).
# Later in 2004, both the values are available, therefore it has printed the respective values.

# Concatenation basically glues the dataframes together.
df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])
concat = pd.concat([df1, df2], axis=0)
print(concat)
concat = pd.concat([df1, df2], axis=1)
print(concat)


df = pd.DataFrame({"Day": [1, 2, 3, 4], "Visitors": [
                  200, 100, 230, 300], "Bounce_Rate": [20, 45, 60, 10]})
df.set_index("Day", inplace=True)
print(df)
# As you can notice in the output above, the index value has been changed with respect to the “Day” column.
df = df.rename(columns={"Visitors": "Users"})
print(df)
# As you see above, column header “Visitors” has been changed to “Users”.

# Data Munging
# In Data munging, you can convert a particular data into a different format.
# country= pd.read_csv("D:UsersAayushiDownloadsworld-bank-youth-unemploymentAPI_ILO_country_YU.csv",index_col=0)
# country.to_html('edu.html')

# Python Pandas Tutorial: Use Case to Analyze Youth Unemployment Data
# Problem Statement: You are given a dataset which comprises of the percentage of unemployed youth globally from 2010 to 2014. You have to use this dataset and find the change in the percentage of youth for every country from 2010-2011.
# see on edureka
