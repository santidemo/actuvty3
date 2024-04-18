import random
import json
import csv

# Generar datos de prueba
users = []
for i in range(10):
    user = {
        'id': i + 1,
        'name': f'User{i + 1}',
        'age': random.randint(18, 60),
        'email': f'user{i + 1}@gmail.com'
    }
    users.append(user)

# Guardar datos en formato JSON
with open('users.json', 'w') as f:
    json.dump(users, f, indent=4)

# Guardar datos en formato CSV
with open('users.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=users[0].keys())
    writer.writeheader()
    writer.writerows(users)