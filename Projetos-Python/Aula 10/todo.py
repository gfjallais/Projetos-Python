import pandas as pd

def numRows(games):
    return games.index.size


def numColumns(games):
    return games.columns.size


def numGoldTotal(games):
    return games['GoldS'].sum() + games['GoldW'].sum()


def numSummerGoldCountry(games, country):
    found_country = games[games['Country'] == country]
    return found_country['GoldS'].to_string(index = False) 
        

def getCodeMaxSummerGold(games):
    max_gold = games[games['GoldS'] == games['GoldS'].max()]
    return max_gold['Code'].to_string(index = False)


def getNthBestSummerCountry(games, n):
    ordered_table = games.sort_values(["GoldT", "SilverT", "BronzeT"], ascending = False)
    print(ordered_table)
    if n <= numRows(ordered_table):
        return ordered_table.iloc[n]['Country']
    elif n > numRows(ordered_table):
        return "No country"


def numCountriesWithMoreThanNWinterMedals(games, n):
    return len(games[games['TotalW'] > n])

            

def numWinterCountries(games):
    return len(games[games['GoldW'] > games['GoldW'].mean()])
    

def countGoldsWithLetter(games, c):
    filtered_games = games[games['Country'].str.startswith(c)]
    return filtered_games['GoldS'].sum()       
    

def countHybernalCountries(games):
    return len(games[games['TotalW'] >= games['TotalS']])