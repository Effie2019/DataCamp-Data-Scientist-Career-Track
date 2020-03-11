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
store_depts =sales.drop_duplicates(subset=["store","department"])
holiday_dates = sales[sales["is_holiday"]==True].drop_duplicates("date")
##Count
sales_all = sales["weekly_sales"].sum()
sales_A = sales[sales["type"]=="A"]["weekly_sales"].sum()
##Group by
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
##Pivot table
mean_sales_by_type = sales.pivot_table(values="weekly_sales",index="type")
###Slicing and indexing
##index
#Set index
temperatures_ind = temperatures.set_index("city")
#Reset index 
temperatures_ind.reset_index()
temperatures_ind.reset_index(drop=True)
##Subsetting 
#with .loc[]
temperatures_ind.loc[["Moscow","Saint Petersburg"]]
temperatures_ind.loc[[("Brazil","Rio De Janeiro"),("Pakistan","Lahore")]]
##Sort
#Sorting by index values
temperatures_ind.sort_index(level=["country","city"],ascending=[True,False])
##Slice
#Rows
temperatures_srt.loc[("Pakistan","Lahore"):("Russia","Moscow")]
#Columns
temperatures_srt.loc[:,"date":"avg_temp_c"]
#Both directions 
temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad"),"date":"avg_temp_c"]
#.loc
temperatures.iloc[22,1]
##Pivot table
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c",index=["country","city"],columns="year")

###Creating and Visualizing DataFrames
##Missing Value
#check
print(avocados_2016.isna())
print(avocados_2016.isna().any().sum())
#drop
avocados_complete = avocados_2016.dropna()
#replace
avocados_filled =avocados_2016.fillna(0)
##DataFrame
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, 	"large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17"	,"2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}



