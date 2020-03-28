# 0x0F. Python - Object-relational mapping
---
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
---
| File | Description |
| --- | --- |
| [0-select_states.py]() | script that lists all states from the database hbtn_0e_0_usa.|
| [0-select_states.sql]() | Database.|
| [1-filter_states.py]() | Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa. |
| [2-my_filter_states.py]() | Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.|
| [3-my_safe_filter_states.py]() | Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections! |
| [4-cities_by_state.py]() |Script that lists all cities from the database hbtn_0e_4_usa. |
| [4-cities_by_state.sql]() | Cities database. |
| [5-filter_cities.py]() | Script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa. |
| [6-model_state.py]() | Script that starts link class to table in database|
| [6-model_state.sql]() | Database |
| [7-model_state_fetch_all.py]() | Script that lists all State objects from the database hbtn_0e_6_usa.|
| [7-model_state_fetch_all.sql]() | Inserts values to the Database 6.|
| [8-model_state_fetch_first.py]() | Script that prints the first State object from the database hbtn_0e_6_usa. |
| [9-model_state_filter_a.py]() | Script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa. |
| [10-model_state_my_get.py]() | Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa. |
| [11-model_state_insert.py]() | Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa. |
| [12-model_state_update_id_2.py]() | Script that changes the name of a State object from the database hbtn_0e_6_usa. |
| [13-model_state_delete_a.py]() | Script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa. |
| [14-model_city_fetch_by_state.py]() | Script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa. |
| [14-model_city_fetch_by_state.sql]() | Databse. |
| [model_state.py]() | Class definition of a State and an instance Base = declarative_base().|
| [model_city.py]() | Class definition of a City that inherits from  model_base().|
