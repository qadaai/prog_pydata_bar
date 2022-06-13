def crimes(population, police, wealth):
    wealth_per_person = wealth/population
    police_per_person = police/population
    baseline_crime = 100_000/population
    
    prediction = baseline_crime - wealth_per_person - police_per_person
    
    return prediction