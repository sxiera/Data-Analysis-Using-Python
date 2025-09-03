# Bike-Sharing Data Analysis & Dashboard  
Dicoding Submission Score: ⭐3/5
## Executive Summary  
This project explores bike-sharing usage patterns using **hourly and daily trip datasets**. Through **exploratory data analysis (EDA)**, statistical modeling, and interactive dashboards, the project uncovers key insights on user demand and its relationship with time and weather. The goal is to help bike-sharing providers make **data-driven decisions** on operations, resource allocation, and customer engagement.  


## Business Problem  
Bike-sharing companies face challenges in:  
- **Predicting demand fluctuations** across different hours, days, and seasons.  
- **Optimizing bike allocation** to reduce shortages and idle bikes.  
- **Understanding external factors** (weather, working days, weekends).  

Without these insights, companies risk inefficiencies, lower customer satisfaction, and missed revenue opportunities.  


## Methodology  
1. **Data Preparation**  
   - Load and clean datasets (`day.csv` & `hour.csv`).  
   - Handle missing values, check formats, ensure consistency.  

2. **Exploratory Data Analysis (EDA)**  
   - Identify peak usage by hour, day, and season.  
   - Analyze weather impact (temperature, humidity, precipitation).  
   - Compare weekday vs. weekend usage.  

3. **Modeling & Statistical Analysis**  
   - Perform correlation analysis.  
   - Build regression/forecasting models to quantify variable importance.  

4. **Dashboard Development** (`aristo_dashboard.py`)  
   - Interactive charts for demand trends.  
   - Time-series plots, weather correlations, hourly/daily breakdowns.  

5. **Insights & Reporting**  
   - Translate findings into business-oriented recommendations.  


## Skills Implemented  
- **Python Programming**  
- **Data Wrangling** (pandas, NumPy)  
- **Data Visualization** (Matplotlib, Seaborn, Plotly)  
- **EDA & Statistical Analysis**  
- **Dashboard Development** (Dash, Streamlit, or Plotly)  
- **Business Communication**  


## Results  
Key findings from the analysis include:  
- **Peak Usage Times**: High demand during **morning (7–9 AM)** and **evening (5–7 PM)**.  
- **Weekly Trends**: Weekday commuter spikes vs. weekend leisure usage.  
- **Weather Effect**: Ridership increases with favorable temperatures, decreases with rain or high humidity.  


## Business Recommendations  
- **Dynamic Bike Allocation**: Deploy more bikes during peak hours and in high-demand locations.  
- **Seasonal Planning**: Adjust inventory and maintenance cycles to match seasonal demand.  
- **Targeted Promotions**: Offer commuter passes for weekdays, leisure packages for weekends.  
- **Station Optimization**: Re-evaluate placement of bike stations to match demand patterns.  
- **Dashboard Integration**: Use interactive dashboards for real-time monitoring and operational adjustments.  
