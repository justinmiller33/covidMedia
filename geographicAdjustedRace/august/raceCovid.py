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
tCaseRace = []
# Looping through each state
for state in data.index:
    
    # Get races for that state
    races = dems.loc[state]
    # Filling any nans with 0
    races = races.fillna(0)
    
    # Multiply by total number of deaths in that state
    deathRace = races.astype(int) * int(data.TotalDeath[state])
    caseRace = races.astype(int) * int(data.TotalCases[state])
    
    if len(tDeathRace):
        tDeathRace = tDeathRace + deathRace
        tCaseRace = tCaseRace + caseRace
        
    else:
        tDeathRace = deathRace
        tCaseRace = caseRace

# Calculating expected percent
expDeath = tDeathRace/sum(tDeathRace)
expCase = tCaseRace/sum(tCaseRace)
"""
print("Expected Death Distribution:")
print(expDeath)
print("Expected Case Distribution:")
print(expCase)
"""

# Comparing with actual
# Data from https://covid.cdc.gov/covid-data-tracker/#demographics
# Accessed 08/22/20
actIndex = ["Hispanic","American Indian/Alaska Native","Asian","Black","Native Hawaiian/Other Pacific Islander","White","Two Or More Races"]
actDeath = pd.Series(data = [18147,827,5445,23882,158,54423,4847], index = actIndex)
actCase = pd.Series(data = [633987, 25580, 73247, 400756, 6735, 815265, 88307], index = actIndex)


# Naive expectation assuming random geographical distribution
naiveExp = dems.loc['United States'].astype(int)/sum(dems.loc['United States'].astype(int))


print("\nUS Population vs. Expected COVID-19 Distribution:\n")

df = pd.DataFrame(index = actIndex)
df['Population'] = naiveExp
df['ExpCases'] = expCase/sum(expCase)
df['ExpDeaths'] = expDeath/sum(expDeath)

print(100 * df.round(4))
#print(100 * df.loc[["Hispanic","Asian","Black","White"]].round(4))

print("\nPercent Difference between Actual Cases and Deaths from US Population:\n")
df = pd.DataFrame(index = actIndex)
df['Cases'] = actCase/sum(actCase) / naiveExp -1
df['Deaths'] = actDeath/sum(actDeath) / naiveExp -1

print(100 * df.round(4))
#print(100 * df.loc[["Hispanic","Asian","Black","White"]].round(4))

print("\nPercent Difference between Actual Cases and Deaths from Improved Proportions:\n")

df = pd.DataFrame(index = actIndex)
df['Cases'] = actCase/sum(actCase) / expCase -1
df['Deaths'] = actDeath/sum(actDeath) / expDeath -1

print(100 * df.round(4))
#print(100 * df.loc[["Hispanic","Asian","Black","White"]].round(4))
