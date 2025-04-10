import pandas as pd

# Step 1: Use your actual local paths here
forest_file_path = r"C:\Users\26sin\OneDrive\Desktop\guvi\project_2\Bird_Monitoring_Data_FOREST.XLSX"
grassland_file_path = r"C:\Users\26sin\OneDrive\Desktop\guvi\project_2\Bird_Monitoring_Data_GRASSLAND.XLSX"

# Step 2: Read Excel files
try:
    df_forest = pd.read_excel(forest_file_path)
    print("✅ Forest data loaded successfully")
    print(df_forest.head())

    df_grassland = pd.read_excel(grassland_file_path)
    print("\n✅ Grassland data loaded successfully")
    print(df_grassland.head())

except FileNotFoundError as e:
    print("❌ File not found. Check path or filename.")
    print(e)

except Exception as e:
    print("❌ An error occurred while reading the Excel file.")
    print(e)
# Remove duplicates
df_forest.drop_duplicates(inplace=True)
df_grassland.drop_duplicates(inplace=True)

# Handle missing values (example: filling with mode or mean)
df_forest.fillna(method='ffill', inplace=True)
df_grassland.fillna(method='ffill', inplace=True)

# Standardize column names
df_forest.columns = df_forest.columns.str.strip().str.lower().str.replace(' ', '_')
df_grassland.columns = df_grassland.columns.str.strip().str.lower().str.replace(' ', '_')
# Exploratory Data Analysis (EDA)
import seaborn as sns
import matplotlib.pyplot as plt

# Count per year in forest
forest_year_count = df_forest['year'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
sns.barplot(x=forest_year_count.index, y=forest_year_count.values)
plt.title("Bird Observations Per Year (Forest)")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Show the actual column names in your df_forest dataset
print("📌 Columns in df_forest:")
print(df_forest.columns.tolist())

#top  10 spicies
import matplotlib.pyplot as plt
import seaborn as sns

# Get top 10 species by observation count
top_species_forest = df_forest['scientific_name'].value_counts().head(10)

# Plot
plt.figure(figsize=(10, 5))
sns.barplot(x=top_species_forest.values, y=top_species_forest.index, palette='viridis')
plt.title("Top 10 Bird Species in Forest")
plt.xlabel("Observation Count")
plt.ylabel("Scientific Name")
plt.tight_layout()
plt.show()


print(df_forest.columns.tolist())
#geographic visulization
import pandas as pd
import folium
from sqlalchemy import create_engine
import urllib.parse

# Encode special characters in password
password = urllib.parse.quote("4628@Saru")

# Create MySQL connection engine
engine = create_engine(f'mysql+pymysql://root:{password}@localhost/project_2')

# Create a map centered on India
m = folium.Map(location=[22.5, 78.9], zoom_start=5)

# Plot 5 dummy birds using your actual species names
sample_species = df_forest['scientific_name'].dropna().unique()[:5]
dummy_coords = [[22.5, 78.9], [21.0, 77.5], [23.0, 80.2], [24.2, 75.3], [25.6, 79.1]]

# Add markers to map
for name, coords in zip(sample_species, dummy_coords):
    folium.Marker(location=coords, popup=name).add_to(m)

# Save the map
m.save("dummy_bird_map.html")
print("✅ Map saved as dummy_bird_map.html (with sample bird markers)")

# Save forest and grassland data to MySQL
df_forest.to_sql('bird_monitoring_forest', con=engine, if_exists='replace', index=False)
df_grassland.to_sql('bird_monitoring_grassland', con=engine, if_exists='replace', index=False)
print("✅ Data successfully uploaded to MySQL.")
