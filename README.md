# 2466-dj5-learning-tracker
Membuat aplikasi Learning Tracker menggunakan Django versi 5.0.4
Github: https://github.com/gurnitha/2466-dj5-learning-tracker
Local: E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker


#### 1. Mengklon repositori dari Github

        modified:   README.md


#### 2. Membuat lingkungan virtual dengan nama 'venv312504'

        modified:   .gitignore
        modified:   README.md


#### 3. Menginstal Django versi 5.0.4

        λ venv312504\Scripts\activate.bat
        (venv312504) λ pip install django==5.0.4
        Collecting django==5.0.4


#### 4. Membuat proyek Django dengan nama config

        modified:   README.md
        new file:   config/config/__init__.py
        new file:   config/config/asgi.py
        new file:   config/config/settings.py
        new file:   config/config/urls.py
        new file:   config/config/wsgi.py
        new file:   config/manage.py


#### 5. Mengganti nama root direktori (config-terluar) menjadi src

        modified:   README.md
        renamed:    config/config/__init__.py -> src/config/__init__.py
        renamed:    config/config/asgi.py -> src/config/asgi.py
        renamed:    config/config/settings.py -> src/config/settings.py
        renamed:    config/config/urls.py -> src/config/urls.py
        renamed:    config/config/wsgi.py -> src/config/wsgi.py
        renamed:    config/manage.py -> src/manage.py


#### 6. Meng-upgrade pip

        (venv312504) λ python.exe -m pip install --upgrade pip


#### 7. Membuat MySQL database

        λ mysql -u root
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 403
        Server version: 8.0.30 MySQL Community Server - GPL

        Copyright (c) 2000, 2022, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql> CREATE DATABASE 2466_dj5_learning_tracker;
        Query OK, 1 row affected (0.13 sec)


#### 8. Menginstal MySQL driver

        (venv312504) λ pip install mysqlclient
        Collecting mysqlclient
          Using cached mysqlclient-2.2.4-cp312-cp312-win_amd64.whl.metadata (4.6 kB)
        Using cached mysqlclient-2.2.4-cp312-cp312-win_amd64.whl (203 kB)
        Installing collected packages: mysqlclient
        Successfully installed mysqlclient-2.2.4


#### 9. Menghubungkan db dengan proyek

        modified:   README.md
        modified:   src/config/settings.py


#### 10. House keeping - memindahkan .git dan file .gitignore dan README.md ke dalam folder src

        modified:   README.md
        renamed:    src/config/__init__.py -> config/__init__.py
        renamed:    src/config/asgi.py -> config/asgi.py
        renamed:    src/config/settings.py -> config/settings.py
        renamed:    src/config/urls.py -> config/urls.py
        renamed:    src/config/wsgi.py -> config/wsgi.py
        renamed:    src/manage.py -> manage.py


#### 11. Menjalankan migrasi

        (venv312504) λ python manage.py makemigrations
        No changes detected

        E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src(main -> origin)
        (venv312504) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK