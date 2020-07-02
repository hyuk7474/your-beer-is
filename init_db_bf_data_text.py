from pymongo import MongoClient
client = MongoClient('localhost', 27017) # client가 robo와 같은 역할(mongodb에 연결)

db = client["your_beer_is"]
bf_data = db["bf_data"]

document = [{'name': ' Standard American Beer', 'ABV': '2.8 - 4.2%', 'IBU': '8 - 12', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' International Lager', 'ABV': '4.6 - 6%', 'IBU': '18 - 25', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Czech Lager', 'ABV': '3 - 4.1%', 'IBU': '20 - 35', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Pale Malty European Lager', 'ABV': '4.7 - 5.4%', 'IBU': '16 - 22', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Pale Bitter European Beer', 'ABV': '2.4 - 3.6%', 'IBU': '15 - 28', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Amber Malty European Lager', 'ABV': '5.8 - 6.3%', 'IBU': '18 - 24', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Amber Bitter European Lager', 'ABV': '4.7 - 5.5%', 'IBU': '18 - 30', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Dark European Lager', 'ABV': '4.5 - 5.6%', 'IBU': '18 - 28', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Strong European Beer', 'ABV': '7 - 10%', 'IBU': '16 - 26', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' German Wheat Beer', 'ABV': '4.3 - 5.6%', 'IBU': '8 - 15', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' British Bitter', 'ABV': '3.2 - 3.8%', 'IBU': '25 - 35', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Pale Commonwealth Beer', 'ABV': '3.8 - 5%', 'IBU': '20 - 45', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Brown British Beer', 'ABV': '3 - 3.8%', 'IBU': '10 - 25', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Scottish Ale', 'ABV': '2.5 - 3.2%', 'IBU': '10 - 20', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Irish Beer', 'ABV': '3.8 - 5%', 'IBU': '18 - 28', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Dark British Beer', 'ABV': '4 - 6%', 'IBU': '20 - 40', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Strong British Ale', 'ABV': '5.5 - 8%', 'IBU': '30 - 60', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Pale American Ale', 'ABV': '3.8 - 5.5%', 'IBU': '15 - 28', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Amber and Brown American Beer', 'ABV': '4.5 - 6.2%', 'IBU': '25 - 40', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' American Porter and Stout', 'ABV': '4.8 - 6.5%', 'IBU': '25 - 50', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' IPA', 'ABV': '5.5 - 7.5%', 'IBU': '40 - 70', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Strong American Ale', 'ABV': '7.5 - 10%', 'IBU': '60 - 120', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' European Sour Ale', 'ABV': '2.8 - 3.8%', 'IBU': '3 - 8', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Belgian Ale', 'ABV': '4.5 - 5.5%', 'IBU': '8 - 20', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Strong Belgian Ale', 'ABV': '6 - 7.5%', 'IBU': '15 - 30', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Trappist Ale', 'ABV': '4.8 - 6%', 'IBU': '25 - 45', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Historical Beer', 'ABV': '4.2 - 4.8%', 'IBU': '5 - 12', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' American Wild Ale', 'ABV': '0 - 0%', 'IBU': '0 - 0', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Fruit Beer', 'ABV': '3.2 - 22%', 'IBU': '10 - 120', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Spiced Beer', 'ABV': '0 - 0%', 'IBU': '0 - 0', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Alternative Fermentables Beer', 'ABV': '0 - 0%', 'IBU': '0 - 0', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Smoked Beer', 'ABV': '0 - 0%', 'IBU': '0 - 0', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Wood Beer', 'ABV': '0 - 0%', 'IBU': '0 - 0', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Specialty Beer', 'ABV': '0 - 0%', 'IBU': '0 - 0', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' American Ale', 'ABV': '4.5 - 6.2%', 'IBU': '30 - 45', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Belgian and French Ale', 'ABV': '4.5 - 5.5%', 'IBU': '10 - 20', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Belgian Strong Ale', 'ABV': '6 - 7.5%', 'IBU': '15 - 30', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' English Brown Ale', 'ABV': '2.8 - 4.5%', 'IBU': '10 - 25', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' English Pale Ale', 'ABV': '3.2 - 3.8%', 'IBU': '25 - 35', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' India Pale Ale (IPA)', 'ABV': '5 - 7.5%', 'IBU': '40 - 60', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' German Wheat and Rye Beer', 'ABV': '4.3 - 5.6%', 'IBU': '8 - 15', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Light Hybrid Beer', 'ABV': '4.2 - 5.6%', 'IBU': '15 - 20', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Porter', 'ABV': '4 - 5.4%', 'IBU': '18 - 35', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Scottish and Irish Ale', 'ABV': '2.5 - 3.2%', 'IBU': '10 - 20', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Smoke Flavored/Wood-Aged Beer', 'ABV': '4.8 - 6%', 'IBU': '20 - 30', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Sour Ale', 'ABV': '2.8 - 3.8%', 'IBU': '3 - 8', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Stout', 'ABV': '4 - 5%', 'IBU': '30 - 45', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Strong Ale', 'ABV': '6 - 9%', 'IBU': '30 - 60', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Bock', 'ABV': '6.3 - 7.4%', 'IBU': '23 - 35', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Dark Lager', 'ABV': '4.2 - 6%', 'IBU': '8 - 20', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' European Amber Lager', 'ABV': '4.5 - 5.5%', 'IBU': '18 - 30', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Light Lager', 'ABV': '2.8 - 4.2%', 'IBU': '8 - 12', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Pilsner', 'ABV': '4.4 - 5.2%', 'IBU': '25 - 45', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Cider or Perry', 'ABV': '5 - 8%', 'IBU': '0 - 0', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Mead', 'ABV': '3.2 - 35%', 'IBU': '0 - 0', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Spice/Herb/Vegetable Beer', 'ABV': '3.2 - 22%', 'IBU': '10 - 120', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}, {'name': ' Amber Hybrid Beer', 'ABV': '4.5 - 5.2%', 'IBU': '25 - 40', 'info': 'Brett Beer, Mixed-Fermentation Sour Beer, Wild Specialty Beer, Fruit Beer, Fruit and Spice Beer, Specialty Fruit Beer, Spice, Herb, or Vegetable Beer, Alternative Grain Beer, Alternative Sugar Beer, Classic Style Smoked Beer, Specialty Smoked Beer, Wood-Aged Beer, Specialty Wood-Aged Beer, Clone Beer, Mixed-Style Beer, Experimental Beer'}]


bf_data.insert_many(document)