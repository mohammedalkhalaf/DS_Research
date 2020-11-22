# Mohammed Alkhalaf
# Misk class excrsice 

#Recearch quations: 
#  
# installing packeges 
import math # Functions beyond the basic maths
# Import an entire library and give it an alias
import pandas as pd # For DataFrame and handling
import numpy as np # Array and numerical processing
import matplotlib.pyplot as plt # Low level plotting
import seaborn as sns # High level Plotting
import statsmodels.api as sm # Modeling, e.g. ANOVA

# Reading the data 
indian_food = pd.read_csv("indian_food.csv")
indian_food
indian_food_tidy = pd.read_csv("indian_food_tidy.csv")
indian_food_tidy

#how many dishes per region?
indian_food.groupby(['region']).size()
#Ploting the results 
indian_food.groupby('region').region.value_counts().unstack().plot.barh()

#how many dishes per state?
indian_food.groupby(['state']).size()
#Ploting the results 
indian_food.groupby('state').state.value_counts().unstack().plot.barh()

#how many dishes per diet?
indian_food.groupby(['diet']).size()
#Ploting the results 
indian_food.groupby('diet').diet.value_counts().unstack().plot.barh()

#how many dishes in each course?
indian_food.groupby("course").size()
#how many dishes in each course based on the reigon?
indian_food.groupby(["region", "course"])["course"].count()
#how many dishes in each course based on the state?
indian_food.groupby(["region", "course"])["course"].count()

# The most comman 10 ingredients overall 
indian_food_tidy[('ingredients')].value_counts()[:10].index.tolist()
# The most comman ingredients based on the region
indian_food_tidy.groupby('region')['ingredients'].apply(lambda x: x.value_counts().head(3))
# the most comman ingrediatens in a falvor type?
indian_food_tidy.groupby('flavor_profile')['ingredients'].apply(lambda x: x.value_counts().head(1))
# the most comman ingrediatens in a course type?
indian_food_tidy.groupby('course')['ingredients'].apply(lambda x: x.value_counts().head(1))

# what is the avrage preparing time?
np.mean(indian_food['prep_time'])
# what is the avrage cooking time?
np.mean(indian_food['cook_time'])

# what is the avrage preparing time based on the reigon?
indian_food.groupby('region')['prep_time'].mean()
# what is the avrage cooking time based on the reigon?
indian_food.groupby('region')['cook_time'].mean()

# sum of total time for a meal
sum_time = indian_food["prep_time"] + indian_food["cook_time"]
indian_food["sum_time"] = sum_time

#total avreage time for a meal 
np.mean(indian_food['sum_time'])
# what is the avrage total time based on the reigon?
indian_food.groupby('region')['sum_time'].mean()


# shortest meals in total time by reigon
indian_food.loc[indian_food.groupby('region').sum_time.idxmin()]
# longest meals in total time by reigon
indian_food.loc[indian_food.groupby('region').sum_time.idxmax()]

# shortest meals in total time by course
indian_food.loc[indian_food.groupby('course').sum_time.idxmin()]
# longest meals in total time by course
indian_food.loc[indian_food.groupby('course').sum_time.idxmax()]

# shortest meals in total time by diet
indian_food.loc[indian_food.groupby('diet').sum_time.idxmin()]
# longest meals in total time by diet
indian_food.loc[indian_food.groupby('diet').sum_time.idxmax()]


