import pandas as pd 

#Read csv file, use shape and head

row_data = DataFrame = pd.read_csv("../../data/databank_education_2018.csv")

spending: str = "SE.XPD.TOTL.GB.ZS"
enrollmt: str = "SE.ENR.TERT.FM.ZS"

print(f"The shape of row_data is: {row_data.shape}")
print(row_data.head(10))


#Selecting Column subsets
select: DataFrame = row_data[["Country", spending, enrollmt]]
print(f"The shape of select is: {select.shape}")
print(select.head(10))


#selecting rows with complete data
notna: DataFrame = select[select[enrollmt].notna() & select[spending].notna()]
print(f"The shape of notna is: {notna.shape}")
print(notna.head(10))

#10 largest values
sort: DataFrame = notna.sort_values(by = [spending], ascending = False)
print("The countries who spend the greatest percentage of government expenditure on education are:")
sort.head(10)

#scatter plot and correlation
x = sort.plot.scatter(spending, enrollmt, title = "Gov't Spending on Education vs. Enrollment in Tertiary Education", xlabel = "Government Spending", ylabel = "Tertiary Enrollment")
correlation: float = sort[spending].corr(sort[enrollmt])
print(f"The correlation between government spending and tertiary school enrollment is {correlation}")
