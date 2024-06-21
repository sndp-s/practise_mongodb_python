"""
Learn MongoDB by practise - Python edition

[Problem set source - W3resource](https://www.w3resource.com/mongodb-exercises/#MongoDB_restaurants)

Document schema:
```
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
```
"""

from pymongo import MongoClient
from bson.json_util import dumps


def pp(results):
    """
    Pretty prints docs
    """
    for doc in results:
        print(dumps(doc, indent=4))


# setup db, access collection
client = MongoClient('localhost', 27017)
db = client["practise_restaurants_db"]
restaurants = db['restaurants']


# 1. Write a MongoDB query to display all the documents in the collection restaurants.
# Uncomment the following two lines and run this file with the python interpretter to see things in action
# results = restaurants.find({})
# pp(results)

# 2. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.


# 3. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant.


# 4. Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.


# 5. Write a MongoDB query to display all the restaurant which is in the borough Bronx.


# 6. Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.


# 7.Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.


# 8. Write a MongoDB query to find the restaurants who achieved a score more than 90.


# # 9. Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.


# 10. Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168.


# 11. Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168.


# 12. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.
# Note : Do this query without using $and operator.


# 13. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.


# 14. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name.


# 15. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'ces' as last three letters for its name.


# 16. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Reg' as three letters somewhere in its name.


# 17. Write a MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish.


# 18. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronxor Brooklyn.


# 19. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn.


# 20. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which achieved a score which is not more than 10.


# 21. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinees' or restaurant's name begins with letter 'Wil'.


# 22. Write a MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of "A" and scored 11 on an ISODate "2014-08-11T00:00:00Z" among many of survey dates..


# 23. Write a MongoDB query to find the restaurant Id, name and grades for those restaurants where the 2nd element of grades array contains a grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z".


# 24. Write a MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52..


# 25. Write a MongoDB query to arrange the name of the restaurants in ascending order along with all the columns.


# 26. Write a MongoDB query to arrange the name of the restaurants in descending along with all the columns.


# 27. Write a MongoDB query to arranged the name of the cuisine in ascending order and for that same cuisine borough should be in descending order.


# 28. Write a MongoDB query to know whether all the addresses contains the street or not.


# 29. Write a MongoDB query which will select all documents in the restaurants collection where the coord field value is Double.


# 30. Write a MongoDB query which will select the restaurant Id, name and grades for those restaurants which returns 0 as a remainder after dividing the score by 7.


# 31. Write a MongoDB query to find the restaurant name, borough, longitude and attitude and cuisine for those restaurants which contains 'mon' as three letters somewhere in its name.


# 32. Write a MongoDB query to find the restaurant name, borough, longitude and latitude and cuisine for those restaurants which contain 'Mad' as first three letters of its name.


# 33. Write a MongoDB query to find the restaurants that have at least one grade with a score of less than 5.


# 34. Write a MongoDB query to find the restaurants that have at least one grade with a score of less than 5 and that are located in the borough of Manhattan.


# 35. Write a MongoDB query to find the restaurants that have at least one grade with a score of less than 5 and that are located in the borough of Manhattan or Brooklyn.


# 36. Write a MongoDB query to find the restaurants that have at least one grade with a score of less than 5 and that are located in the borough of Manhattan or Brooklyn, and their cuisine is not American.


# 37. Write a MongoDB query to find the restaurants that have at least one grade with a score of less than 5 and that are located in the borough of Manhattan or Brooklyn, and their cuisine is not American or Chinese.


# 38. Write a MongoDB query to find the restaurants that have a grade with a score of 2 and a grade with a score of 6.


# 39. Write a MongoDB query to find the restaurants that have a grade with a score of 2 and a grade with a score of 6 and are located in the borough of Manhattan.


# 40. Write a MongoDB query to find the restaurants that have a grade with a score of 2 and a grade with a score of 6 and are located in the borough of Manhattan or Brooklyn.


# 41. Write a MongoDB query to find the restaurants that have a grade with a score of 2 and a grade with a score of 6 and are located in the borough of Manhattan or Brooklyn, and their cuisine is not American.


# 42. Write a MongoDB query to find the restaurants that have a grade with a score of 2 and a grade with a score of 6 and are located in the borough of Manhattan or Brooklyn, and their cuisine is not American or Chinese.


# 43. Write a MongoDB query to find the restaurants that have a grade with a score of 2 or a grade with a score of 6.


# 44. Write a MongoDB query to find the restaurants that have a grade with a score of 2 or a grade with a score of 6 and are located in the borough of Manhattan.


# 45. Write a MongoDB query to find the restaurants that have a grade with a score of 2 or a grade with a score of 6 and are located in the borough of Manhattan or Brooklyn.


# 46. Write a MongoDB query to find the restaurants that have a grade with a score of 2 or a grade with a score of 6 and are located in the borough of Manhattan or Brooklyn, and their cuisine is not American.


# 47. Write a MongoDB query to find the restaurants that have a grade with a score of 2 or a grade with a score of 6 and are located in the borough of Manhattan or Brooklyn, and their cuisine is not American or Chinese.


# 48. Write a MongoDB query to find the restaurants that have all grades with a score greater than 5.


# 49. Write a MongoDB query to find the restaurants that have all grades with a score greater than 5 and are located in the borough of Manhattan.


# 50. Write a MongoDB query to find the restaurants that have all grades with a score greater than 5 and are located in the borough of Manhattan or Brooklyn.


# 51. Write a MongoDB query to find the average score for each restaurant.


# 52. Write a MongoDB query to find the highest score for each restaurant.


# 53. Write a MongoDB query to find the lowest score for each restaurant.


# 54. Write a MongoDB query to find the count of restaurants in each borough.


# 55. Write a MongoDB query to find the count of restaurants for each cuisine.


# 56. Write a MongoDB query to find the count of restaurants for each cuisine and borough.


# 57. Write a MongoDB query to find the count of restaurants that received a grade of 'A' for each cuisine.


# 58. Write a MongoDB query to find the count of restaurants that received a grade of 'A' for each borough.


# 59. Write a MongoDB query to find the count of restaurants that received a grade of 'A' for each cuisine and borough.


# 60. Write a MongoDB query to find the number of restaurants that have been graded in each month of the year.


# 61. Write a MongoDB query to find the average score for each cuisine.


# 62. Write a MongoDB query to find the highest score for each cuisine.


# 63. Write a MongoDB query to find the lowest score for each cuisine.


# 64. Write a MongoDB query to find the average score for each borough.


# 65. Write a MongoDB query to find the highest score for each borough.


# 66. Write a MongoDB query to find the lowest score for each borough.


# 67. Write a MongoDB query to find the name and address of the restaurants that received a grade of 'A' on a specific date.


# 68. Write a MongoDB query to find the name and address of the restaurants that received a grade of 'B' or 'C' on a specific date.


# 69. Write a MongoDB query to find the name and address of the restaurants that have at least one 'A' grade and one 'B' grade.


# 70. Write a MongoDB query to find the name and address of the restaurants that have at least one 'A' grade and no 'B' grades.


# 71. Write a MongoDB query to find the name ,address and grades of the restaurants that have at least one 'A' grade and no 'C' grades.


# 72. Write a MongoDB query to find the name, address, and grades of the restaurants that have at least one 'A' grade, no 'B' grades, and no 'C' grades.


# 73. Write a MongoDB query to find the name and address of the restaurants that have the word 'coffee' in their name.


# 74. Write a MongoDB query to find the name and address of the restaurants that have a zipcode that starts with '10'.


# 75. Write a MongoDB query to find the name and address of the restaurants that have a cuisine that starts with the letter 'B'.


# 76. Write a MongoDB query to find the name, address, and cuisine of the restaurants that have a cuisine that ends with the letter 'y'.


# 77. Write a MongoDB query to find the name, address, and cuisine of the restaurants that have a cuisine that contains the word 'Pizza'.


# 78. Write a MongoDB query to find the restaurants achieved highest average score.


# 79. Write a MongoDB query to find all the restaurants with the highest number of "A" grades.


# 80. Write a MongoDB query to find the cuisine type that is most likely to receive a "C" grade.


# 81. Write a MongoDB query to find the restaurant that has the highest average score for thecuisine "Turkish".


# 82. Write a MongoDB query to find the restaurants that achieved the highest total score.


# 83. Write a MongoDB query to find all the Chinese restaurants in Brooklyn.


# 84. Write a MongoDB query to find the restaurant with the most recent grade date.


# 85. Write a MongoDB query to find the top 5 restaurants with the highest average score for each cuisine type, along with their average scores.


# 86. Write a MongoDB query to find the top 5 restaurants in each borough with the highest number of "A" grades.


# 87. Write a MongoDB query to find the borough with the highest number of restaurants that have a grade of "A" and a score greater than or equal to 90.
