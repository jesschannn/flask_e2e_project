from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from azure import BehavioralHealthService, Patient
import random
from datetime import timedelta
import os
import random 
from dotenv import load_dotenv

load_dotenv()

#Database credentials
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

#Connection string and creating the engine
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")

engine = create_engine(
        connection_string,
        connect_args=connect_args)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker instance
fake = Faker()

# Function to generate fake patient data
def create_patient():
    return Patient(
        name=fake.name(),
        date_of_birth=fake.date_of_birth(),
        diagnosis=fake.sentence(nb_words=5)
    )

# Function to generate fake behavioral health service data
def create_behavioralhealthservice(patient):
    return BehavioralHealthService(
        state=fake.state(),
        month=fake.month_name(),
        service_type=random.choice(['Emergency Department', 'Telehealth', 'Inpatient', 'Outpatient']),
        count=random.randint(1, 10000),
        rate_per_1000=random.uniform(1, 150)
    )

# Generate and insert fake data
for _ in range(100):  # Adjust the number of records you want to generate
    fake_patient = create_patient()
    session.add(fake_patient)
    session.commit()
    
    fake_behavioral_health_service = create_behavioralhealthservice(fake_patient)
    session.add(fake_behavioral_health_service)
    session.commit()

# Close the session
session.close()

print("Done")