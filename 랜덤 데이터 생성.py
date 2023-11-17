import csv
import random

# Function to generate a random resident registration number (for illustration purposes)
def generate_resident_number():
    birth_year = random.randint(80, 99)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    gender = random.choice(["1", "2"])  # 1 for male, 2 for female
    random_nums = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return f"{birth_year:02d}{birth_month:02d}{birth_day:02d}-{gender}{random_nums}"

# Generating random data for 1,000 students
data = []
for _ in range(1000):
    name = f"Student_{_ + 1}"
    height = random.uniform(150, 190)  # Random height between 150 and 190 cm
    grade = random.randint(1, 12)
    gender = random.choice(["Male", "Female"])
    resident_number = generate_resident_number()
    weight = random.uniform(45, 90)  # Random weight between 45 and 90 kg

    data.append([name, height, grade, gender, resident_number, weight])

# Writing data to CSV file
csv_file_path = "student_data.csv"
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Writing header
    csv_writer.writerow(["Name", "Height (cm)", "Grade", "Gender", "Resident Number", "Weight (kg)"])
    # Writing data rows
    csv_writer.writerows(data)

print(f"Student data has been written to {csv_file_path}.")
