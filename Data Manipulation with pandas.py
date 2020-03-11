###Transforming Data
## Inspecting a DataFrame
print(homelessness.head())
print(homelessness.info())
print(homelessness.shape)
print(homelessness.describe())
##Parts of a DataFrame
print(homelessness.values)
print(homelessness.columns)
print(homelessness.index)
##Sort
homelessness_ind = homelessness.sort_values("individuals") #One column
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False]) #multiple columns
##Subset
#Subsetting columns
individuals =homelessness["individuals"]  #One column
state_fam = homelessness[["state","family_members"]]  #multiple columns
#Subsetting rows
ind_gt_10k = homelessness[homelessness["individuals"]>10000]
mountain_reg = homelessness[homelessness["region"]=="Mountain"]
fam_lt_1k_pac = homelessness[(homelessness["family_members"]<1000) & (homelessness["region"]=="Pacific")] #multiple conditions
regions = ["South Atlantic","Mid-Atlantic"] #Subsetting rows by categorical variables
condition = homelessness["region"].isin(regions)
south_mid_atlantic=homelessness[condition] 
##Add new columns
homelessness["total"]=homelessness["individuals"]+homelessness["family_members"]

###Aggregating Data
sales[["weekly_sales"]].mean()
sales[["weekly_sales"]].median()
sales[["date"]].max()
sales[["date"]].min()
##.agg()
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(sales["temperature_c"].agg(iqr))
print(sales[["temperature_c","fuel_price_usd_per_l","unemployment"]].agg(iqr))
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))
##Cumulative statistics
sales_1_1 =sales_1_1.sort_values("date") 
sales_1_1["cum_weekly_sales"]= sales_1_1["weekly_sales"].cumsum()
sales_1_1["cum_max_sales"]=sales_1_1["weekly_sales"].cummax()
##Dropping duplicates

###Slicing and indexing
###Creating and Visualizing DataFrames



