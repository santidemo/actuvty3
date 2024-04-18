import json

def crear_user(data, user):
    data.append(user)

def leer_data(data):
    for user in data:
        print(user)

def actualizar(data, user_id, new_data):
    for user in data:
        if user['id'] == user_id:
            user.update(new_data)
            break

def eliminar(data, user_id):
    for user in data:
        if user['id'] == user_id:
            data.remove(user)
            break

# Uso de las operaciones CRUD
with open('users.json', 'r') as f:
    data = json.load(f)

# Crear un nuevo usuario
new_user = {
    'id': 3,
    'name': 'Paola',
    'age': 25,
    'email': 'Paola@gmail.com'
}
crear_user(data, new_user)

# Leer todos los usuarios (antes de las operaciones CRUD)
print("Usuarios antes de las operaciones CRUD:")
leer_data(data)
print()

# Actualizar un usuario existente
# update_user(data, 1, {'name': 'Usuario actualizado'})

# Eliminar un usuario existente
# eliminar(data, 3)

# Leer todos los usuarios (después de las operaciones CRUD)
print("Usuarios despues de las operaciones CRUD:")
leer_data(data)