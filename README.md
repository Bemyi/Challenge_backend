# Como correr la aplicación

- Clonar el repositorio: `git clone https://github.com/Bemyi/Challenge_backend.git`
- Accedemos a la carpeta raíz de la aplicación: `cd challenge_backend/`
- Instalar dependencias: `pip install -r requirements.txt`
- Como base de datos se utiliza postgres, por lo tanto deberá seguir los siguientes pasos para configurarla
  y que se pueda crear correctamente:
  1. Crear un usuario con las siguientes credenciales:
     Usuario = userrafam
     Contraseña: userrafam
  2. Creación de la base de datos:
     Nombre de la base de datos: friends_lessons
     Host: localhost
     Puerto: 5432
- Una vez configurada la base correctamente, corremos las migraciones: `python manage.py migrate`
- Luego para cargar información sobre los modelos creados, corremos: `python manage.py loaddata api/fixtures/*.json`
- Correr la aplicación: `python manage.py runserver`

# Acceder a los endpoints

- Listar todos los usuarios del sistema: `http://localhost:8000/api/users/`
- Listar todas las amitades registradas en el sistema: `http://localhost:8000/api/friendships/`
  **Nota:** Reemplazar <user_id> por el número de un usuario del 1 al 5.
- Listar todos los amigos de un usuario en específico: `http://localhost:8000/api/user/<user_id>/lessons/`
- Listar todas las lecciones que tomó un usuario en específico: `http://localhost:8000/api/user/<user_id>/lessons/`
