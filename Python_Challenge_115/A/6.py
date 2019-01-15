'''
Statement
Given a list of countries and cities of each country, then given the names of the cities. For each city print the country in which it is located.

Example input
2
USA Boston Pittsburgh Washington Seattle
UK London Edinburgh Cardiff Belfast
3
Cardiff
Seattle
London

Example output
UK
USA
UK
'''
country_dic = {}

for _ in range(int(input())):
    arr = input().split()
    country = arr.pop(0)

    for city in arr:
        country_dic[city] = country

for _ in range(int(input())):
    city = input()

    print(country_dic[city])
