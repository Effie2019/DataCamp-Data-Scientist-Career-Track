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

             ax.bar(medals.index, medals["Silver"],bottom=medals["Gold"], label="Silver")


# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals["Bronze"],bottom=medals["Gold"]+medals["Silver"], label="Bronze")

# Display the legend
ax.legend()
plt.show()
