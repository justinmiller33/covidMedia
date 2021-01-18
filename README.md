# covidMedia
Some Random Projects on Media Coverage of Covid-19

## Improving Expected COVID Distributions by Race with Geographic Weighting
### Intuition
We know that COVID-19 disproportionately affects marginalized racial groups. 
However, comparing case and death rates by race to overall population fails to account for the geographical distribution of the pandemic. 
For example, since cases are highly concentrated in the American South one could expect the overall racial distribution to more closely resemble that of the South.
<br>

To create a benchmark for comparison that accounts for geographical variation, we can reweight distributions by each state's demographic makeup. 
In other words, we create an expected value as if COVID was randomly distributed in each state vs. randomly distributed in the entire nation.
This strategy accounts for geographical differences without whitewashing disparities faced on a more local basis, such as town-by-town.

### Results
The first chart compares US population proportions with the geographical-adjusted expected case and death counts. <br>
The second chart shows the percent difference between the actual cases/deaths and the US population. <br>
(These disparities are what is commonly used in news articles) <br>
The third chart shows the percent difference between the actual cases/deaths and the geographical adjusted expected counts. <br>
(These are more representative of the true disparities and should be communicated)

![](https://github.com/justinmiller33/covidMedia/blob/master/geographicAdjustedRace/january/januaryResults.png)

### Takeaways
The charts show how significant of an impact that geographical distribution has on our idea of COVID's racial impact. <br>
In specific, the media's traditional view overstate's COVID's impact on hispanics, while understating it's impact on Native American groups. 
These results can be confirmed by intuition: Hispanic populations are much larger in hard-hit Southern/Western states while Native Groups are more common in the Plains Region. <br>

Misrepresentations like these are why media accountability and diligence is crucial to proper representation of complex data.
