[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> Overall the relationship between birth weight and mother's age is **pretty weak**. As evidence see:

>>**Scatter Plot:**

>>![Mother's Age vs. Birth Weight Scatter Plot]
(https://github.com/sosier/dsp/blob/master/img/ageWghtScatter.png?raw=true)

>>**Code:**
```python
live = live.dropna(subset=["agepreg", "totalwgt_lb"])
ages = live.agepreg
weights = live.totalwgt_lb

>>thinkplot.Scatter(ages, weights)
thinkplot.Show(xlabel="Mother's Age", ylabel="Birth Weight (lbs)", axis=[10, 45, 0, 16])
```

>>**Birth Weight Percentiles by Mother's Age:**

>>![Birth Weight Percentiles by Mother's Age Chart]
(https://github.com/sosier/dsp/blob/master/img/ageWeightPercentiles.png?raw=true)

>>**Code:**
```python
bins = np.arange(15, 40, 1)  # Ages <15 and >40 excluded due to low sample size
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)

>>ages = [group.agepreg.mean() for i, group in groups][1:-1]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

>>thinkplot.PrePlot(3)
for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weights, label=label)

>>thinkplot.Show(xlabel="Mother's Age", ylabel="Birth Weight (lbs)", axis=[10, 45, 0, 16])
```

>>**Correlations:**
- _**Pearson's:**_ ~0.07
- _**Spearman's:**_ ~0.09

>>**Code:**
```python
# Reset data back to normal first
ages = live.agepreg
weights = live.totalwgt_lb

>>print("Pearson's Correlation: %s" % str(thinkstats2.Corr(ages, weights)))
print("Spearman's Correlation: %s" % str(thinkstats2.SpearmanCorr(ages, weights)))
```
