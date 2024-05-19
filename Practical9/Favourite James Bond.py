 # Define the function
def favourite_James_Bond(year_of_birth):
    # Calculate the year when the person start watching Bond movies
    year_watching_Bond=18+year_of_birth
    # Define a dictionary including different actors of James Bond in different periods of time 
    bond_actors = {(1973, 1986): "Roger Moore",(1987, 1994): "Timothy Dalton", (1995, 2005): "Pierce Brosnan", (2006, 2021): "Daniel Craig" }
    # Loop through each time period and associated actor in the dictionary
    for (start_year, end_year), actor in bond_actors.items():
        # Check if the year the person started watching falls within the current time period
        if start_year <= year_watching_Bond <= end_year:
            return actor
    return "No Bond actor found."
# example
print(favourite_James_Bond(1999))
