import csv
import matplotlib.pyplot as plt

# Read data from CSV file
csv_file_path = "student_data.csv"
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Extract height and weight data
heights = [float(row['Height (cm)']) for row in data]
weights = [float(row['Weight (kg)']) for row in data]

# Create a scatter plot
plt.scatter(heights, weights, alpha=0.5)
plt.title('Height vs. Weight for Students')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()
