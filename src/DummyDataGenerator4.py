import pandas as pd
from faker import Faker
import random

fake = Faker('en_IN')

# Helper functions
def generate_btech_age():
    return random.randint(18, 23)

def generate_mtech_age():
    return random.randint(22, 27)

def generate_id(course, index):
    return f"{course}{index:03d}"

def generate_phone_number():
    return f"+91{random.randint(7000000000, 9999999999)}"

# Lists of Indian cities and states
indian_cities = ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Pune", "Jaipur", "Kolkata", "Hyderabad", "Ahmedabad", "Lucknow"]
indian_states = ["Maharashtra", "Delhi", "Karnataka", "Tamil Nadu", "Maharashtra", "Rajasthan", "West Bengal", "Telangana", "Gujarat", "Uttar Pradesh"]

# Columns
columns = ["Student Name", "Course ID", "Student ID", "Enrollment Number", "Year", "Course Name", "Duration (Years)", "Branch", "Specialization",
           "Total Fees (Per Annum)", "Yearly Fees", "Exam Fees", "Extra Fees", "Hostel Accommodation", "Occupancy", "City", "State", "Country",
           "Email", "Phone", "Payment Mode", "12th Percentage", "10th Percentage", "Hostel Room Type", "Annual Income", "Date of Birth"]

# Data generation
data = []

for i in range(1, 1200):
    year = random.choice([2018, 2019,2020,2021,2022,2023])
    course_name = "B.Tech in Computer Science and Engineering"
    duration = 4
    branch = "Computer Science and Engineering"
    specializations = [
        "Data Science", "Artificial Intelligence and Machine Learning", "Cloud Computing and Virtualization",
        "Internet of Things and Cyber Security Including Blockchain Technology", "Gaming Technology", "Full Stack Development",
        "Geographical Information Systems and Remote Sensing", "Data Analytics", "Business Analytics and Optimization",
        "Cyber Security and Digital Forensic"
    ]
    specialization = random.choice(specializations)
    total_fees = 169000
    yearly_fees = 154000
    exam_fees = 15000
    extra_fees = 0
    hostel_accommodation = "Yes"
    occupancy_types = ["Single Occupancy", "Double Occupancy", "Triple Occupancy"]
    occupancy = random.choice(occupancy_types)
    city = random.choice(indian_cities)
    state = indian_states[indian_cities.index(city)]
    country = "India"
    email = fake.email()
    phone = generate_phone_number()
    payment_modes = ["UPI", "Cash", "Cheque", "RTGS", "DD"]
    payment_mode = random.choice(payment_modes)
    twelfth_percentage = random.randint(60, 90)
    tenth_percentage = random.randint(60, 92)
    hostel_room_type = random.choice(["AC", "Non-AC"])
    annual_income = random.randint(100000, 800000)
    dob = fake.date_of_birth(minimum_age=18, maximum_age=23)
    student_name = fake.name()
    course_id = generate_id("BTechCSE", i)
    student_id = generate_id("STU", i)
    enrollment_number = generate_id("ENR", i)

    data.append([student_name, course_id, student_id, enrollment_number, year, course_name, duration, branch, specialization,
                 total_fees, yearly_fees, exam_fees, extra_fees, hostel_accommodation, occupancy, city, state, country, email,
                 phone, payment_mode, twelfth_percentage, tenth_percentage, hostel_room_type, annual_income, dob])

for i in range(1, 400):
    year = random.choice([2018, 2019,2020,2021,2022,2023])
    course_name = "M.Tech in Computer Science Engineering"
    duration = 2
    branch = "Computer Science Engineering"
    specializations = [
        "Data Science", "Artificial Intelligence & Machine Learning", "Cloud Computing & Virtualization", 
        "Internet of Things & Cyber Security Including Blockchain Technology", "Data Analytics", "Business Analytics & Optimization"
    ]
    specialization = random.choice(specializations)
    total_fees = 92000
    yearly_fees = 77000
    exam_fees = 15000
    extra_fees = 0
    hostel_accommodation = "Yes"
    occupancy_types = ["Single Occupancy", "Double Occupancy", "Triple Occupancy"]
    occupancy = random.choice(occupancy_types)
    city = random.choice(indian_cities)
    state = indian_states[indian_cities.index(city)]
    country = "India"
    email = fake.email()
    phone = generate_phone_number()
    payment_modes = ["UPI", "Cash", "Cheque", "RTGS", "DD"]
    payment_mode = random.choice(payment_modes)
    twelfth_percentage = random.randint(60, 90)
    tenth_percentage = random.randint(60, 92)
    hostel_room_type = random.choice(["AC", "Non-AC"])
    annual_income = random.randint(100000, 800000)
    dob = fake.date_of_birth(minimum_age=22, maximum_age=27)
    student_name = fake.name()
    course_id = generate_id("MTechCSE", i)
    student_id = generate_id("STU", 125 + i)
    enrollment_number = generate_id("ENR", 125 + i)

    data.append([student_name, course_id, student_id, enrollment_number, year, course_name, duration, branch, specialization,
                 total_fees, yearly_fees, exam_fees, extra_fees, hostel_accommodation, occupancy, city, state, country, email,
                 phone, payment_mode, twelfth_percentage, tenth_percentage, hostel_room_type, annual_income, dob])

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('engineering_college_enrollment.csv', index=False)
