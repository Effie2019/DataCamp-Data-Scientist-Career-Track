##Matplotlib Intro
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
plt.show()
# Customizing data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b',marker='o',linestyle='--')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r',marker='v',linestyle='--')
# Customizing axis labels and adding titles
ax.set_xlabel("Time (months)")
ax.set_ylabel("Precipitation (inches)")
ax.set_title("Weather patterns in Austin and Seattle")
# Small multiples with plt.subplots
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(seattle_weather['MONTH'], seattle_weather["MLY-PRCP-NORMAL"])
ax[1,0].plot(seattle_weather['MONTH'],seattle_weather["MLY-TAVG-NORMAL"] )
ax[0, 1].plot(austin_weather['MONTH'], austin_weather["MLY-PRCP-NORMAL"] )
ax[1,1].plot(austin_weather['MONTH'],austin_weather["MLY-TAVG-NORMAL"] 
plt.show()
# Small multiples with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color = 'b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color = 'b',linestyle ='--')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color = 'b',linestyle ='--')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color = 'r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color = 'r',linestyle ='--')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color = 'r',linestyle ='--')
plt.show()
             
##time-series
# Defining a function that plots time-series data
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
axes.plot(x, y, color=color)
axes.set_xlabel(xlabel)
axes.set_ylabel(ylabel,color=color)
axes.tick_params('y', colors=color)
fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")
ax2 = ax.twinx() # Create a twin Axes object that shares the x-axis
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative temperature (Celsius)")
plt.show()
#Annotating a plot
fig, ax = plt.subplots()
ax.plot(climate_change.index,climate_change["relative_temp"])
ax.annotate('>1 degree', (pd.Timestamp('2015-10-06'), 1)) # Annotate the date at which temperatures exceeded 1 degree
plt.show()
#Statistical Visualizations
##Bar
fig, ax = plt.subplots()
ax.bar(medals.index,medals["Gold"])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
ax.bar(medals.index, medals["Silver"],bottom=medals["Gold"], label="Silver") #Stacked bar chart 1
ax.bar(medals.index, medals["Bronze"],bottom=medals["Gold"]+medals["Silver"], label="Bronze") #Stacked bar chart 2
ax.legend()# Display the legend
plt.show()
##Hist
ax.hist(mens_rowing["Weight"],histtype='step',label="Rowing",bins=5)
ax.hist(mens_gymnastics["Weight"],histtype='step',label="Gymnastics",bins=5)
ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")
ax.legend()
plt.show()
## Error Bar
#Adding error-bars to a bar chart           
ax.bar("Rowing", mens_rowing["Height"].mean(),yerr=mens_rowing["Height"].std())
#Adding error-bars to a chart  
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])
## Box
ax.boxplot([mens_rowing["Height"],mens_gymnastics["Height"]])
## Scatter plot 
ax.scatter(climate_change["co2"],climate_change["relative_temp"])
ax.scatter(climate_change["co2"],climate_change["relative_temp"],c=climate_change.index)      
   
##Sharing visualizations with others
#select style
plt.style.use("ggplot")
plt.style.use("Solarize_Light2")
#save
fig.set_size_inches([3,5]) #set size
fig.savefig("my_figure.png",dpi=300)   
# Automate the visualization             
fig, ax = plt.subplots()
for sport in sports:# Loop over the different sports branches
  sport_df = summer_2016_medals[summer_2016_medals["Sport"]==sport]
  ax.bar(sport,sport_df["Weight"].mean(),yerr=sport_df["Weight"].std())
ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)
fig.savefig("sports_weights.png")
