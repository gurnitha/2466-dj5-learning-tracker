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


#### 12. Menjalankan development server untuk kali pertama

        (venv312504) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        June 18, 2024 - 13:10:42
        Django version 5.0.4, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


#### 13. Membuat aplikasi learning_logs di dalam app folder

        (venv312504) λ mkdir app\learning_logs

        E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src(main -> origin)
        (venv312504) λ django-admin startapp learning_logs app\learning_logs

        modified:   README.md
        new file:   app/learning_logs/__init__.py
        new file:   app/learning_logs/admin.py
        new file:   app/learning_logs/apps.py
        new file:   app/learning_logs/migrations/__init__.py
        new file:   app/learning_logs/models.py
        new file:   app/learning_logs/tests.py
        new file:   app/learning_logs/views.py


#### 14. Mendaftarkan aplikasi learning_logs pada config/settings.py

        modified:   README.md
        modified:   app/learning_logs/apps.py
        modified:   config/settings.py


#### 15. Membuat models Topic 

        modified:   README.md
        modified:   app/learning_logs/models.py


#### 16. Menjalankan migrasi

        venv312504) λ python manage.py makemigrations learning_logs
        Migrations for 'learning_logs':
          app\learning_logs\migrations\0001_initial.py
            - Create model Topic

        (venv312504) λ python manage.py migrate learning_logs 0001
        Operations to perform:
          Target specific migration: 0001_initial, from learning_logs
        Running migrations:
          Applying learning_logs.0001_initial... OK


#### 17. Memeriksa hasil migrasi pada database

        mysql> USE 2466_dj5_learning_tracker;
        Database changed
        mysql> SHOW tables;
        +-------------------------------------+
        | Tables_in_2466_dj5_learning_tracker |
        +-------------------------------------+
        | auth_group                          |
        | auth_group_permissions              |
        | auth_permission                     |
        | auth_user                           |
        | auth_user_groups                    |
        | auth_user_user_permissions          |
        | django_admin_log                    |
        | django_content_type                 |
        | django_migrations                   |
        | django_session                      |
        | learning_logs_topic                 |
        +-------------------------------------+
        11 rows in set (0.01 sec)

        mysql> DESC learning_logs_topic;
        +------------+--------------+------+-----+---------+----------------+
        | Field      | Type         | Null | Key | Default | Extra          |
        +------------+--------------+------+-----+---------+----------------+
        | id         | bigint       | NO   | PRI | NULL    | auto_increment |
        | text       | varchar(200) | NO   |     | NULL    |                |
        | date_added | datetime(6)  | NO   |     | NULL    |                |
        +------------+--------------+------+-----+---------+----------------+
        3 rows in set (0.04 sec)


#### 18. Membuat Superuser

        (venv312504) λ python manage.py createsuperuser
        Username (leave blank to use 'ing'): superuser
        Email address: superuser@mail.com
        Password:
        Password (again):
        The password is too similar to the email address.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

        mysql> DESC auth_user;
        +--------------+--------------+------+-----+---------+----------------+
        | Field        | Type         | Null | Key | Default | Extra          |
        +--------------+--------------+------+-----+---------+----------------+
        | id           | int          | NO   | PRI | NULL    | auto_increment |
        | password     | varchar(128) | NO   |     | NULL    |                |
        | last_login   | datetime(6)  | YES  |     | NULL    |                |
        | is_superuser | tinyint(1)   | NO   |     | NULL    |                |
        | username     | varchar(150) | NO   | UNI | NULL    |                |
        | first_name   | varchar(150) | NO   |     | NULL    |                |
        | last_name    | varchar(150) | NO   |     | NULL    |                |
        | email        | varchar(254) | NO   |     | NULL    |                |
        | is_staff     | tinyint(1)   | NO   |     | NULL    |                |
        | is_active    | tinyint(1)   | NO   |     | NULL    |                |
        | date_joined  | datetime(6)  | NO   |     | NULL    |                |
        +--------------+--------------+------+-----+---------+----------------+
        11 rows in set (0.00 sec)

        mysql> SELECT username, is_staff, is_active FROM auth_user;
        +-----------+----------+-----------+
        | username  | is_staff | is_active |
        +-----------+----------+-----------+
        | superuser |        1 |         1 |
        +-----------+----------+-----------+
        1 row in set (0.00 sec)


#### 19. Mendaftarkan models Topic pada admin site

        modified:   README.md
        modified:   app/learning_logs/admin.py
        modified:   app/learning_logs/models.py


#### 20. Membuat topik melalui admin panel

        mysql> SELECT * FROM learning_logs_topic;
        +----+---------+----------------------------+
        | id | text    | date_added                 |
        +----+---------+----------------------------+
        |  1 | Topic 1 | 2024-06-18 06:35:26.576089 |
        |  2 | Topic 2 | 2024-06-18 06:35:37.107576 |
        |  3 | Topic 3 | 2024-06-18 06:35:44.578759 |
        +----+---------+----------------------------+
        3 rows in set (0.00 sec)


#### 21. Membuat models Entry

        modified:   README.md
        modified:   app/learning_logs/models.py


#### 22. Menjalankan migrasi

        (venv312504) λ python manage.py makemigrations learning_logs
        Migrations for 'learning_logs':
          app\learning_logs\migrations\0002_entry.py
            - Create model Entry

        E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src(main -> origin)
        (venv312504) λ python manage.py migrate learning_logs 0002
        Operations to perform:
          Target specific migration: 0002_entry, from learning_logs
        Running migrations:
          Applying learning_logs.0002_entry... OK


#### 23. Mendaftarkan models Topic pada admin site

        modified:   README.md
        modified:   app/learning_logs/admin.py


#### 24. Membuat entry menggunakan admin panel

        modified:   README.md
        modified:   app/learning_logs/models.py

        mysql> SHOW TABLES;
        +-------------------------------------+
        | Tables_in_2466_dj5_learning_tracker |
        +-------------------------------------+
        | auth_group                          |
        | auth_group_permissions              |
        | auth_permission                     |
        | auth_user                           |
        | auth_user_groups                    |
        | auth_user_user_permissions          |
        | django_admin_log                    |
        | django_content_type                 |
        | django_migrations                   |
        | django_session                      |
        | learning_logs_entry                 |
        | learning_logs_topic                 |
        +-------------------------------------+
        12 rows in set (0.00 sec)

        mysql> DESC learning_logs_entry;
        +------------+-------------+------+-----+---------+----------------+
        | Field      | Type        | Null | Key | Default | Extra          |
        +------------+-------------+------+-----+---------+----------------+
        | id         | bigint      | NO   | PRI | NULL    | auto_increment |
        | text       | longtext    | NO   |     | NULL    |                |
        | date_added | datetime(6) | NO   |     | NULL    |                |
        | topic_id   | bigint      | NO   | MUL | NULL    |                |
        +------------+-------------+------+-----+---------+----------------+
        4 rows in set (0.00 sec)

        mysql> SELECT * FROM learning_logs_entry;
        +----+---------------------+----------------------------+----------+
        | id | text                | date_added                 | topic_id |
        +----+---------------------+----------------------------+----------+
        |  1 | Etry 1 dari topic 1 | 2024-06-18 06:56:24.175593 |        1 |
        |  2 | Etry 2 dari topic 1 | 2024-06-18 06:56:34.167726 |        1 |
        |  3 | Etry 1 dari topic 2 | 2024-06-18 06:56:42.683287 |        2 |
        |  4 | Etry 2 dari topic 2 | 2024-06-18 06:56:56.245209 |        2 |
        |  5 | Etry 1 dari topic 3 | 2024-06-18 06:57:06.163563 |        3 |
        |  6 | Etry 2 dari topic 3 | 2024-06-18 06:57:15.654526 |        3 |
        +----+---------------------+----------------------------+----------+
        6 rows in set (0.00 sec)


#### 24. Menggunakan Djano shell

        (venv312504) λ python manage.py shell
        Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)

        >>> from app.learning_logs.models import Topic
        >>> Topic.objects.all()
        <QuerySet [<Topic: Topic 1>, <Topic: Topic 2>, <Topic: Topic 3>]>

        >>> topics = Topic.objects.all()
        >>> for topic in topics:
        ...     print(topic.id, topic)
        ...
        1 Topic 1
        2 Topic 2
        3 Topic 3

        >>> t = Topic.objects.get(id=1)
        >>> t.text
        'Topic 1'
        >>> t.date_added
        datetime.datetime(2024, 6, 18, 6, 35, 26, 576089, tzinfo=datetime.timezone.utc)

        >>> t.entry_set.all()
        <QuerySet [<Entry: Etry 1 dari topic 1...>, <Entry: Etry 2 dari topic 1...>]>


#### 25. Mapping a URL

        modified:   README.md
        new file:   app/learning_logs/urls.py
        modified:   config/urls.py


#### 26. Membuat index View

        modified:   README.md
        modified:   app/learning_logs/urls.py
        modified:   app/learning_logs/views.py


#### 27. Membuat template

        modified:   README.md
        new file:   app/learning_logs/templates/learning_logs/index.html
        modified:   config/settings.py


#### 28. Membuat base template

        modified:   README.md
        new file:   app/learning_logs/templates/learning_logs/base.html
        modified:   app/learning_logs/views.py