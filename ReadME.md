# PostgreSQL Database CLI Interface

This Python program provides a Command Line Interface (CLI) for interacting with a PostgreSQL database. It supports various database operations such as insert, delete, update, search, and more.

## Getting Started

### Prerequisites
You will first need a postgre SQL database to interact with as well as the connection details to manage it.

Ensure you have Python installed on your system. You will also need `psycopg2`, a PostgreSQL database adapter for Python. Install it using pip if you haven't already:

pip install psycopg2

#### Setting Up Database Connection
Before running the program, you need to configure the database connection details. Open the Python script and locate the db_params dictionary near the top of the file:


db_params = {
    "dbname": "RLCS_Game_Data",
    "user": "postgres",
    "password": "password",
    "host": "localhost"
}

Change the values of dbname, user, password, and host to match your PostgreSQL database credentials.

### Running the Program
Execute the script from your command line by navigating to the directory containing the script and running:

python CLI.py

### Usage
After starting the program, you will see a menu with options to perform different database operations:

Insert Data: Insert records into a specific table.
Delete Data: Delete records from a specific table based on a condition.
Update Data: Update records in a specific table.
Search Data: Search for records in a specific table.
Aggregate Functions: Perform aggregate functions like SUM, COUNT, etc., on a table.
Sorting: Sort data in a specific table by a column.
Joins: Perform inner joins between two tables.
Grouping: Group data in a specific table and perform operations.
Subqueries: Execute operations that involve subqueries.
Exit: Close the program.
Select an option by entering the corresponding number. Follow the prompts to specify details for each operation, such as table name, column names, and conditions.

### Error Handling
The program handles errors by rolling back the transaction if an operation fails, ensuring data integrity. Detailed error messages are printed to help diagnose issues.

### Closing the Connection
The program automatically closes the database connection and cursor when you choose to exit.



### Notes Regarding RLCS_Game_Database
The database for this project can be created by first creating a blank database running the following commands in pgAdmin using the Query Tool:
##### DDL Commands
Regions Table

CREATE TABLE Regions (
 region_id VARCHAR(255) PRIMARY KEY
);

Teams Table

CREATE TABLE Teams (
 team_id VARCHAR(255) PRIMARY KEY,
 region_id VARCHAR(255) NOT NULL,
 FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

Cars Table

CREATE TABLE Cars (
 car_id SERIAL PRIMARY KEY,
 car_name VARCHAR(255) NOT NULL
);

Players Table

CREATE TABLE Players (
 player_id VARCHAR(255) PRIMARY KEY,
 player_tag VARCHAR(255) NOT NULL,
 team_id VARCHAR(255) NOT NULL,
 region_id VARCHAR(255) NOT NULL,
 car_id INT NOT NULL,
 ranking_id FLOAT NOT NULL,
 FOREIGN KEY (team_id) REFERENCES Teams(team_id),
 FOREIGN KEY (region_id) REFERENCES Regions(region_id),
 FOREIGN KEY (car_id) REFERENCES Cars(car_id)
);

Rankings Table

CREATE TABLE Rankings (
 ranking_id FLOAT PRIMARY KEY,
 player_id VARCHAR(255) UNIQUE NOT NULL,
 FOREIGN KEY (player_id) REFERENCES Players(player_id)
);

Camera Settings Table

CREATE TABLE Camera_Settings (
 camera_settings_id VARCHAR(255) PRIMARY KEY,
 player_id VARCHAR(255) UNIQUE NOT NULL,
 camera_fov INT,
 camera_height INT,
 camera_pitch INT,
 camera_distance INT,
 camera_stiffness FLOAT,
 camera_swivel_speed FLOAT,
 camera_transition_speed FLOAT,
 FOREIGN KEY (player_id) REFERENCES Players(player_id)
);

Games Table

CREATE TABLE Games (
 game_id VARCHAR(255) PRIMARY KEY
);

Performance Metrics Table

CREATE TABLE Performance_Metrics (
 game_id VARCHAR(255) NOT NULL,
 player_id VARCHAR(255) NOT NULL,
 core_shots INT,
 core_goals INT,
 core_saves INT,
 core_assists INT,
 core_score INT,
 demo_inflicted INT,
 demo_taken INT,
 advanced_rating FLOAT,
 PRIMARY KEY (game_id, player_id),
 FOREIGN KEY (game_id) REFERENCES Games(game_id),
 FOREIGN KEY (player_id) REFERENCES Players(player_id)
);

Car Usage Table

CREATE TABLE Car_Usage (
 game_id VARCHAR(255) NOT NULL,
 player_id VARCHAR(255) NOT NULL,
 car_id INT NOT NULL,
 PRIMARY KEY (game_id, player_id, car_id),
 FOREIGN KEY (game_id) REFERENCES Games(game_id),
 FOREIGN KEY (player_id) REFERENCES Players(player_id),
 FOREIGN KEY (car_id) REFERENCES Cars(car_id)
);

After this you can either insert synthetic data to test the database, or upload a CSV file (one I have provided) that contains the proper information with proper headers for import. To test the CLI I used synthetic data similar to the inputs below. Once again run these using the Query tool:

-- Insert into Regions

INSERT INTO Regions VALUES ('NorthAmerica');

-- Insert into Teams

INSERT INTO Teams VALUES ('TeamAlpha', 'NorthAmerica');

-- Insert into Cars

INSERT INTO Cars (car_name) VALUES ('Octane');

-- Insert into Players

INSERT INTO Players VALUES ('Player1', 'AlphaTag', 'TeamAlpha', 'NorthAmerica', 1, 100.0);

-- Insert into Rankings

INSERT INTO Rankings VALUES (100.0, 'Player1');

-- Insert into Camera Settings

INSERT INTO Camera_Settings VALUES ('CS1', 'Player1', 110, 100, 10, 270, 0.9, 4.5, 1.2);

-- Insert into Games

INSERT INTO Games VALUES ('Game1');

-- Insert into Performance Metrics

INSERT INTO Performance_Metrics VALUES ('Game1', 'Player1', 5, 2, 1, 3, 800, 2, 1, 97.5);

-- Insert into Car Usage
INSERT INTO Car_Usage VALUES ('Game1', 'Player1', 1);


