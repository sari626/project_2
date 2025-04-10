import mysql.connector

# Step 1: Connect to MySQL (without database to create it first)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='4628@Saru',
    auth_plugin='mysql_native_password' 
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS project_2")
cursor.close()
conn.close()

# Step 2: Connect again, this time to the new database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='4628@Saru',
    auth_plugin='mysql_native_password', 
    database='project_2'
)
cursor = conn.cursor()

# Step 3: Create tables

# 1. bird_monitoring
cursor.execute("""
CREATE TABLE IF NOT EXISTS bird_monitoring (
    id INT AUTO_INCREMENT PRIMARY KEY,
    site_name VARCHAR(255),
    sci_name VARCHAR(100),
    com_name VARCHAR(255),
    observer VARCHAR(100),
    temperature FLOAT,
    humidity FLOAT,
    date DATE,
    location_type VARCHAR(255)
)
""")

# 2. bird_monitoring_grassland
cursor.execute("""
CREATE TABLE IF NOT EXISTS bird_monitoring_grassland (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plot_name VARCHAR(255),
    observer VARCHAR(100),
    id_method VARCHAR(100),
    wind VARCHAR(100),
    sci_name VARCHAR(100),
    com_name VARCHAR(255)
)
""")

# 3. grassland_year (fixing missing comma issue)
cursor.execute("""
CREATE TABLE IF NOT EXISTS grassland_year (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plot_name VARCHAR(255),
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    sci_name VARCHAR(100),
    com_name VARCHAR(255)
)
""")

# 4. forest_year
cursor.execute("""
CREATE TABLE IF NOT EXISTS forest_year (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plot_name VARCHAR(255),
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    sci_name VARCHAR(100),
    com_name VARCHAR(255)
)
""")

conn.commit()
cursor.close()
conn.close()

print("✅ All tables created successfully in database 'project_2'.")
