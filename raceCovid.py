# Racial distributions adjusted by states
import numpy as np
import pandas as pd

# Load covid data
data = pd.read_csv('covidDeaths.csv')
# Name Columns
data.columns =  ['abbr','fips','jurisdiction','TotalCases','TotalDeath','Death100k','CasesInLast7Days','DeathsInLast7Days','RatePer100000']
# Save states as index
data.index = data.jurisdiction
# Dropping jurisdiction
data = data.drop(columns = ["jurisdiction",'abbr'])
# Clipping csv junk
data = data[2:]
# Clipping every teritory that isn't a state
data = data.drop(index = ['American Samoa','Federated States of Micronesia','District of Columbia','Guam','Northern Mariana Islands','Puerto Rico','Palau','Republic of Marshall Islands','Virgin Islands','United States of America'])
# Add NYC and NY together
data.loc['New York'] = data.loc['New York'].astype(int)+data.loc['New York City'].astype(int)
# Drop NYC
data = data.drop(index = ['New York City'])

# Load state demographic data
dems = pd.read_csv('stateDemographics.csv')
# Name Columns
dems.columns = ['Location','White','Black','Hispanic','American Indian/Alaska Native','Asian','Native Hawaiian/Other Pacific Islander','Two Or More Races','Total']
# Saving states as index
dems.index = dems.Location
# Dropping location and total (for linear combinations later)
dems = dems.drop(columns = ["Location","Total"])
# Clipping csv junk
dems = dems.iloc[2:]

# Initializing running total
tDeathRace = []
# Looping through each state
for state in data.index:
    
    # Get races for that state
    races = dems.loc[state]
    # Filling any nans with 0
    races = races.fillna(0)
    
    # Multiply by total number of deaths in that state
    deathRace = races.astype(int) * int(data.TotalDeath[state])

    if len(tDeathRace):
        tDeathRace = tDeathRace + deathRace
        
    else:
        tDeathRace = deathRace

# Calculating expected percent
expectedPercent = tDeathRace/sum(tDeathRace)
print("Expected Death Distribution:")
print(expectedPercent)
