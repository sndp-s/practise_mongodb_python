# Setup
1. Install the `requirements.txt` in your virtual env
2. Start the mongodb server
3. Create the `practise_restaurants_db` DB, `restaurants` collection and import `restaurants.json` data into the `restaurants` collection using the following command:
```bash
mongoimport --db practise_restaurants_db --collection restaurants --file restaurants.json --jsonArray
```
4. Start your practise
