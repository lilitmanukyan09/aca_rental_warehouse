### Data Engineering Project: Canada Rental Website Warehouse
### Lilit Manukyan

![Data_science](https://www.american.edu/spa/data-science/images/datascience-hero.jpg)

_**Challenges and solutions**_

* **Creating and filling the tables in the database** : The first major issue arose when trying to create and fill the tables in the database. The creation was implemented successfully, but the solutions on the web for filling the values of the table was quite confusing and overcomplicated for me. So based on a solution from google, I simplified the process as follows. I created a dictionary of table names as keys and tables themselves as values. Thereon, a simple but effective snippet of code did the magic :)
```python
        for name, data in sql_script.table_names.items():
            data = data
            copy_data_to_database(cursor=cursor, data=data, table_name=name)
```

* **Overlapping dates** : The problem was that different tenants could not stay in the same apartment at the same time, obviously. First, let's introduce the transactions table, which was created by randomly choosing unique tenant_id's and property_id's and appending a random date to it, created by faker library. Then, the duplicates of property_id was dropeed, as stated in the following code snippet: 

```python
transactions = defaultdict(list)
for l in range (1000):
    # transactions['transaction_id'].append(l)
    transactions['tenant_id'].append(np.random.choice(tenants['tenant_id'].unique()))
    transactions['property_id'].append(np.random.choice(properties['property_id'].unique()))
    transactions['date'].append(fake.date_time_this_month())

transactions = pd.DataFrame(transactions)
transactions = transactions.drop_duplicates(subset=['property_id'], keep = 'last')
```
