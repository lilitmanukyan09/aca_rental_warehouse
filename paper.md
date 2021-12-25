### Data Engineering Project: Canada Rental Website Warehouse
### Lilit Manukyan

![Data_science](https://www.american.edu/spa/data-science/images/datascience-hero.jpg)

_**Challenges and solutions**_

* **Creating and filling the tables in the database** : The first major issue arose when trying to create and fill the tables in the database. The creation was implemented successfully, but the solutions on the web for filling the values of the table was quite confusing and overcomplicated for me. So based on a solution from google, I simplified the process as follows. I created a dictionary of table names as keys and tables themselves as values. Thereon, a simple but effective snippet of code did the magic :)
```
        for name, data in sql_script.table_names.items():
            data = data
            copy_data_to_database(cursor=cursor, data=data, table_name=name)
```
