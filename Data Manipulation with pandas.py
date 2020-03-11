## Inspecting a DataFrame
print(homelessness.head())
print(homelessness.info())
print(homelessness.shape)
print(homelessness.describe())
##Parts of a DataFrame
print(homelessness.values)
print(homelessness.columns)
print(homelessness.index)
homelessness_ind = homelessness.sort_values("individuals")
print(homelessness_ind.head())
