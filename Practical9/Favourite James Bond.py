def favourite_James_Bond(year_of_birth):
    year_watching_Bond=18+year_of_birth
    bond_actors = {(1973, 1986): "Roger Moore",(1987, 1994): "Timothy Dalton", (1995, 2005): "Pierce Brosnan", (2006, 2021): "Daniel Craig" }
    for (start_year, end_year), actor in bond_actors.items():
        if start_year <= year_watching_Bond <= end_year:
            return actor
    return "No Bond actor found."
print(favourite_James_Bond(1999))