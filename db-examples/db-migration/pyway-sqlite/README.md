 **Using pyway **
- Library: https://pypi.org/project/pyway/
- Database: SQLite3 https://www.sqlite.org/ Version 3.43.2 
   - check version `sqlite3 --version`

 **Reference books and resource**:
   - https://sqlite.org/cli.html
   - https://www.sqlite.org/docs.html
   - https://github.com/jasondcamp/pyway

# Step 1: using pyway 
- Install pyway module   
  `pip install pyway`

# Step 2 :create configuration file for _SQLite:_
- Note: For this example  configuration is created in file with name .pyway-sqllite.conf
        ```
        database_type: sqlite
        database_name: phyway-sqlite-db
        database_migration_dir: db.sqlite
        database_table: pyway
        database_username: phyway-sqlite
        database_host: localhost
        ```
# Step 3: Test phyway setup 
        ```
        cd pyway-sqlite/
        pyway info -c .pyway-sqllite.conf
      O/P : When there are no sql files  in database_migration_dir configured in .conf file 
          pyway info -c .pyway-sqllite.conf
          PyWay 0.3.32
          Gathering info...
          No migrations found.

     O/P  When there are  sql files  in database_migration_dir configured in .conf file 
        PyWay 0.3.32
        Gathering info...
        +-----------+-------------+--------------------------------+------------+-------------------+
        |   version | extension   | name                           | checksum   | apply_timestamp   |
        |-----------+-------------+--------------------------------+------------+-------------------|
        |      1.01 | SQL         | V01_01__base-schema-tables.sql | new        | new               |
        +-----------+-------------+--------------------------------+------------+-------------------+


        ```
  - Note:  
    - pyway info command creates _SQLite:_  database file based on the configuration
    - pyway, sqlite_master are tables created in  _SQLite:_ database file
    - sqlite_master: is created when any table is table in database 
    - pyway: This table is created based on the name provided in configuration .conf file 
    - _migration_ is not executed 

# Step 4: Run validation  

        ```
        cd pyway-sqlite/
        pyway validate -c .pyway-sqllite.conf

     O/P  
        PyWay 0.3.32
        Starting validation process
        
        Validation completed.

        ```
# Step 5: Run migration   

        ```
        cd pyway-sqlite/
        pyway migrate -c .pyway-sqllite.conf

     O/P  
        PyWay 0.3.32
        Starting validation process
        
        Validation completed.
        Starting migration process...
        Migrating --> V01_01__base-schema-tables.sql
        V01_01__base-schema-tables.sql SUCCESS
        
        Migration completed.

        ```
# Step 6: Run Validation again  to verify migration is applied
        ```
        cd pyway-sqlite/
        pyway validate -c .pyway-sqllite.conf

     O/P  
        PyWay 0.3.32
        Starting validation process
        Validating --> V01_01__base-schema-tables.sql
        V01_01__base-schema-tables.sql VALID
        
        Validation completed.

        ```
# Step 7: Additional Validation to make sure tables and table structure  are created in SQLLite database file 


    # Step 1: connect to database
        ```
        cd pyway-sqlite/
        sqlite3 phyway-sqlite-db
        ```
    # Step 2: list tables 
        ```
        sqlite> .tables
        events    pyway     swimmers  times 

        ```
    # Step 3: list table structure
        ```
        sqlite> SELECT * FROM sqlite_master;
        
        # Make sure the O/P matches structure as defined in sql file

        ```