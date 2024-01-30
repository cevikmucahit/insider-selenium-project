import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
WAIT_TIMEOUT = os.getenv("WAIT_TIMEOUT")

RESULT_OUR_LOCATIONS_LIST = [
    'Amsterdam', 'Ankara', 'Bangkok', 'Barcelona', 'Bogota', 'Buenos Aires', 'Dubai', 'Helsinki', 'Ho Chi Minh City',
    'Istanbul', 'Jakarta', 'Kiev', 'Kuala Lumpur', 'Lima', 'London', 'Manila', 'Mexico City', 'Moscow', 'New York',
    'Paris', 'Santiago', 'Sao Paulo', 'Seoul', 'Singapore', 'Sydney', 'Taipei', 'Tokyo', 'Warsaw'
]

RESULT_DEPARTMENTS_LIST = [
    'Business Intelligence', 'CEO’s Executive Office', 'Customer Success', 'Finance & Business Support', 'Marketing',
    'Mobile Business Unit', 'Partner Support Development', 'Partnership', 'People and Culture', 'Product & Engineering',
    'Product Design', 'Purchasing & Operations', 'Quality Assurance', 'Sales', 'Security Engineering'
]
