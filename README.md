# Sparkify Pipeline

This is a project demonstrating how to create a data mart for a music streaming app and persists data to it via an ETL data pipeline extracting information from JSON logs and loading it into a Postgres database.

It processes the JSON record with the Panda library.

## TD;LR

To test the project locally

1. Install Jupyter Lab
2. Install PostgreSQL
3. Install Python3
4. Install Python Panda library
5. Checkout the code
6. Navigate to the root of the project
7. Run the command `bash run_create_etl.sh` which will create the database and populate it
7. Start the notebook by running the command `jupyter notebook` which will launch it in the browser
9. Open `test.ipynb` to run queries and view the data

## What You're Getting

```bash
├── README.md - This file.
├── create_tables.py # Python script with all methods necessary to recreate the data mart.
├── etl.ipynb # Python based Jupyter Notebook describing and executing all tasks related to the extraction, tranformation and loading of the data.
├── run_create_etl.sh # Bash shell script executing the creation of the schema and the persistence of the data into it.
├── sql_queries.py # Python script defining the data mart schema and prepared/reusable queries.
└── test.ipynb # Python based Jupyter Notebook for veryfying if the database contains any data.
```

## Contributing

Do not hesitate to submit a pull request.