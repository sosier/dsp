[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The NSFG data suggests that _first born babies are **~0.1 lbs lighter** than later born babies_. 

>>However, the _Cohen's d for this difference is quite small at just **~0.09 standard deviations**_, though this effect is greater than the ~0.03 standard deviations for the difference in pregnancy length for first babies vs. others. 

>>**Code:**
>>```python
print("Mean diference in Birth Weight - First Born vs. Others:")
print(firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean())


>>def cohensD(group1, group2):
    """
                     (Group 1 Mean  - Group 2 Mean)
    Cohen's d = ------------------------------------------
                Standard Deviation of Group 1 & 2 Combined
    """
    combinedGroup = group1.append(group2)

>>     return (group1.mean() - group2.mean()) / combinedGroup.std()

>>print("Cohen's d for Birth Weight - First Born vs. Others:")
print(cohensD(firsts.totalwgt_lb, others.totalwgt_lb))
print("Cohen's d for Pregnancy Length - First Pregnancy vs. Others:")
print(cohensD(firsts.prglngth, others.prglngth))
```
