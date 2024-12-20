
import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Define the number of rows
n_rows = 2000

# Define the columns
columns = [
    'Project ID',
    'Project Name',
    'Location',
    'Project Type',
    'Total Cost',
    'Labor Cost',
    'Material Cost',
    'Equipment Cost',
    'Start Date',
    'End Date',
    'Duration',
    'Contractor',
    'Architect',
    'Number of Stories',
    'Building Type',
    'Site Conditions',
    'Permitting and Inspection Costs'
]

# Generate the data
data = {
    'Project ID': range(1, n_rows + 1),
    'Project Name': [f'Construction Project {i} in Bihar' for i in range(1, n_rows + 1)],
    'Location': np.random.choice(['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Darbhanga'], size=n_rows),
    'Project Type': np.random.choice(['Residential', 'Commercial', 'Industrial', 'Infrastructure'], size=n_rows),
    'Total Cost': np.random.randint(500000, 5000000, size=n_rows),
    'Labor Cost': np.random.randint(150000, 1500000, size=n_rows),
    'Material Cost': np.random.randint(200000, 2000000, size=n_rows),
    'Equipment Cost': np.random.randint(50000, 500000, size=n_rows),
    'Start Date': pd.date_range(start='2022-01-01', periods=n_rows, freq='D'),
    'End Date': pd.date_range(start='2023-12-31', periods=n_rows, freq='D'),
    'Duration': np.random.randint(100, 365, size=n_rows),
    'Contractor': np.random.choice(['S K Singh Construction', 'Bhawana Infrabuild Private Limited', 'Balaji Construction', 'Ala Construction','Bevarc Construction Pvt. Ltd'], size=n_rows),
    'Architect': np.random.choice(['Bihar Architects', 'Patna Designers', 'Gaya Planners', 'Bhagalpur Engineers'], size=n_rows),
    'Number of Stories': np.random.randint(1, 10, size=n_rows),
    'Building Type': np.random.choice(['Residential', 'Commercial', 'Industrial', 'Infrastructure'], size=n_rows),
    'Site Conditions': np.random.choice(['Flat', 'Sloping', 'Rocky', 'Hilly'], size=n_rows),
    'Permitting and Inspection Costs': np.random.randint(5000, 50000, size=n_rows)
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('bihar_construction_project_costs.csv', index=False)
