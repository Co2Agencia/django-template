# Django configuración y migraciones básicas

## Para usar repositorio:

1) **Clonamos el repositorio (A)** o creamos un **repositorio remoto (B)**:
    * Clonamos(A):
        - ``` git clone https://github.com/Co2Agencia/django-template.git ```
    
    * Creamos repositorio remote(B):
        - Iniciamos repositorio local: ``` git init ```
        - Conectamos con repostiorio en GITHUB: ``` git remote add origin https://github.com/Co2Agencia/django-template.git ```
        - Traemos los cambios de GITHUB a local: ``` git pull origin master ```
        - Si tenemos cambios para pasar a GITHUB: ``` git push -f origin NOMBRE_BRANCH ```
        
2) **Creamos variable de entorno en local**
    - ``` python -m venv NOMBRE_ENV ```

3) **Activamos el ENV**
    - ```env\scripts\activate```

4) **Descargamos requirements.txt**
    - ``` pip install -r requirements.txt ```

5) **Migramos para crear base de datos**
    - ```python manage.py migrate```

6) **Creamos superuser**
    - ```python manage.py createsuperuser```

7) **Runserver**
    - ```python manage.py runserver```