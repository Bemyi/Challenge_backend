# Como correr la aplicación

- Clonar el repositorio: `git clone https://github.com/Bemyi/Challenge_backend.git`
- Accedemos a la carpeta raíz de la aplicación: `cd challenge_backend/`
- Instalar dependencias: `pip install -r requirements.txt`
- Como base de datos se utiliza postgres, por lo tanto deberá seguir los siguientes pasos para configurarla
  y que se pueda crear correctamente:
  1. Crear un usuario con las siguientes credenciales:
     - Usuario = userrafam
     - Contraseña: userrafam
  2. Creación de la base de datos:
     - Nombre de la base de datos: friends_lessons
     - Host: localhost
     - Puerto: 5432
- Una vez configurada la base correctamente, corremos las migraciones: `python manage.py migrate`
- Luego para cargar información sobre los modelos creados, corremos: `python manage.py loaddata api/fixtures/*.json`
- Correr la aplicación: `python manage.py runserver`

# Acceder a los endpoints

Se puede probar directamente colocando la URL en el navegador o utilizando un API Client como "Postman".

- Listar todos los usuarios del sistema: `http://localhost:8000/api/users/`
- Listar todas las amitades registradas en el sistema: `http://localhost:8000/api/friendships/`
- **Nota:** Reemplazar <user_id> por el número de un usuario del 1 al 5.
- Listar todos los amigos de un usuario en específico: `http://localhost:8000/api/user/<user_id>/friends/`
- Listar todas las lecciones que tomó un usuario en específico: `http://localhost:8000/api/user/<user_id>/lessons/`
- Ver API integrada del tiempo (muestra temperatura mínima y máxima del día en Buenos Aires): `http://localhost:8000/api/weather/`

# Unit Tests

Los unit test se encuentran en el archivo `api\tests.py`, se pueden correr los tests con
el comando: `python manage.py test`

# UML

En el directorio raíz del proyecto se encuentra el archivo `UML.png` con el diagrama UML de la solución.
