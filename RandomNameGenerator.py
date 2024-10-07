import random

first_names = [
    "Ram", "Shyam", "Hari", "Sita", "Gita", "Kumar",
    "Anita", "Suman", "Sunita", "Raju", "Bina", "Raj",
    "Nabin", "Nirmala", "Bikash", "Sarita", "Prakash", "Mina"
]

last_names = [
    "Sharma", "Thapa", "Rai", "Tamang", "Magar", "Gurung",
    "Khadka", "Karki", "Singh", "Bista", "Joshi", "Chaudhary",
    "Koirala", "Basnet", "Bhattarai", "Lama", "Rana", "Mahato"
]

def generate_random_nepali_names(n):
    return [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(n)]

for name in generate_random_nepali_names(20):
    print(name)
