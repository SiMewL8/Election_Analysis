counties = ['Arapahoe', 'Denver', 'Jefferson']


# if counties[1] == 'Denver':
#      print(counties[1])

# print("-"*35)

# if counties[3] != 'Jefferson':
#         print(counties[1])

# print("-"*35)

# if 'El Paso' in counties:
#         print("El Paso is in the list of counties.")
# else:
#         print("El Paso is not in the list of counties.")

# if 'Arapahoe' and 'El Paso' in counties:
#         print("Arapahoe and El Paso are in the county list.")
# else:
#         print("Either Arapahoe or El Paso are not in the county list.")

# if 'Arapahoe' or 'El Paso' in counties:
#         print("Either Arapahoe or El Paso are in the county list.")
# else: 
#         print("Neither Arapahoe nor El Pase are in county list. ")

# for Q in counties:
#         print(Q)


numbshi = [0, 1, 2 , 3, 4, 5]
# for num in numbshi:
#         print(num)

# for numbah in range(6):
#         print(numbah)

# for k in range(len(counties)):
#         print(counties[k])

ddict_counties = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for listcounty in ddict_counties:
#         print(listcounty)

# for listcounty in ddict_counties.keys():
#         print(listcounty)

# for listcounty in counties.keys():
#         print(listcounty)
# check in speedrun vid 'Print each county from the counties dictionary using the keys() method.

# for voters in ddict_counties:
#         print(ddict_counties[voters])


# for voters in ddict_counties:
#         print(ddict_counties.get(voters))


# for listcounty, voters in ddict_counties.items():
#         print(listcounty, voters)

# for listcounty, voters in ddict_counties.items():
#         print(f'{listcounty} county has {voters} registered voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for v in range(len(voting_data)):
#         print(voting_data[v])

# for ddict_counties in voting_data:
#         for value in ddict_counties.values():
#                 print(value)


for listcounty, voters in ddict_counties.items():
        print(f'{listcounty} county has {voters:,} registered voters.')