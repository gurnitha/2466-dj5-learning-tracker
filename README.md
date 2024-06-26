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


#### 29. Template inheritance

        modified:   README.md
        modified:   app/learning_logs/templates/learning_logs/base.html
        modified:   app/learning_logs/templates/learning_logs/index.html
        modified:   app/learning_logs/views.py


#### 30. Membuat laman topics: View dan Url

        modified:   README.md
        modified:   app/learning_logs/urls.py
        modified:   app/learning_logs/views.py


#### 31. Membuat laman topics: template

        modified:   README.md
        new file:   app/learning_logs/templates/learning_logs/topics.html


#### 32. Mentautkan laman home dan laman topics

        modified:   README.md
        modified:   app/learning_logs/templates/learning_logs/base.html


#### 33. Membuat laman detail topic: View dan Url

        modified:   README.md
        modified:   app/learning_logs/urls.py
        modified:   app/learning_logs/views.py


#### 34. Membuat laman detail topic: template

        modified:   README.md
        new file:   app/learning_logs/templates/learning_logs/topic.html
        modified:   app/learning_logs/templates/learning_logs/topics.html



## USER ACCOUNTS


### Add New Topic


#### 35. Adding New Topics part 1: The Topic ModelForm

        modified:   README.md
        new file:   app/learning_logs/forms.py


#### 36. Adding New Topics part 2: Url

        modified:   README.md
        modified:   app/learning_logs/urls.py

        Note: Ada peringatan, belum ada view

        File "E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src\app\learning_logs\urls.py", line 21, in <module>
            path('new_topic/', views.new_topic, name='new_topic'),
                               ^^^^^^^^^^^^^^^
        AttributeError: module 'app.learning_logs.views' has no attribute 'new_topic'

        Next: Membuat view


#### 37. Adding New Topics part 3: Membuat View dan logiknya

        modified:   README.md
        modified:   app/learning_logs/views.py


#### 38. Adding New Topics part 4: Membuat form template

        modified:   README.md
        new file:   app/learning_logs/templates/learning_logs/new_topic.html
        modified:   app/learning_logs/templates/learning_logs/topics.html
        modified:   app/learning_logs/views.py


### Add New Entry


#### 39. Adding New Entry part 1: Membuat EntryForm template

        modified:   README.md
        modified:   app/learning_logs/forms.py


#### 40. Adding New Entry part 2: Membuat Url

        modified:   README.md
        modified:   app/learning_logs/urls.py

        Note: Ada peringatan karena belum ada new_entry view 

          File "E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src\app\learning_logs\urls.py", line 24, in <module>
            path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
                                              ^^^^^^^^^^^^^^^
        AttributeError: module 'app.learning_logs.views' has no attribute 'new_entry'

        Next: Membuat new_entry view


#### 41. Adding New Entry part 3: Membuat new_entry view

        modified:   README.md
        modified:   app/learning_logs/views.py


#### 42. Adding New Entry part 4: Membuat new_entry template

        modified:   README.md
        new file:   app/learning_logs/templates/learning_logs/new_entry.html
        modified:   app/learning_logs/templates/learning_logs/topic.html


#### 43. Edit Entry part 1: Membuat edit_entry URL

        modified:   README.md
        modified:   app/learning_logs/urls.py

        Note: Ada peringatan karena belum ada edit_entry view 

          File "E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src\app\learning_logs\urls.py", line 25, in <module>
            path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
                                               ^^^^^^^^^^^^^^^^
        AttributeError: module 'app.learning_logs.views' has no attribute 'edit_entry'


#### 44. Edit Entry part 2: Membuat  edit_entry() View Function

        modified:   README.md
        modified:   app/learning_logs/views.py


#### 45. Edit Entry part 3: Membuat edit_entry Template

        modified:   README.md
        new file:   app/learning_logs/templates/learning_logs/edit_entry.html
        modified:   app/learning_logs/templates/learning_logs/topic.html
        modified:   app/learning_logs/views.py



### Setting Up User Accounts


#### 46. Membuat aplikasi accounts di dalam folder app

        modified:   README.md
        new file:   app/accounts/__init__.py
        new file:   app/accounts/admin.py
        new file:   app/accounts/apps.py
        new file:   app/accounts/migrations/__init__.py
        new file:   app/accounts/models.py
        new file:   app/accounts/tests.py
        new file:   app/accounts/views.py


#### 47. Mendaftarkan aplikasi accounts pada config/settings.py

        modified:   README.md
        modified:   app/accounts/apps.py
        modified:   config/settings.py


### Login


#### 48. Membuat accounts/urls.py dan menyertakannya pada config/urls.py

        modified:   README.md
        new file:   app/accounts/urls.py
        modified:   config/urls.py


#### 49. Membuat login template

        modified:   README.md
        new file:   app/accounts/templates/registration/login.html


#### 50. Membuat  LOGIN_REDIRECT_URL Settting

        modified:   README.md
        modified:   app/accounts/urls.py
        modified:   app/learning_logs/templates/learning_logs/base.html
        modified:   config/settings.py


### Logging Out


#### 51. Adding a Logout Form to base.html

        modified:   README.md
        modified:   app/learning_logs/templates/learning_logs/base.html
        modified:   config/settings.py


### Registration


#### 52. Membuat url register

        modified:   README.md
        modified:   app/accounts/urls.py

        Note: Ada peringatan karena belum ada register view

          File "E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src\app\accounts\urls.py", line 17, in <module>
            path('register/', views.register, name='register'),
                              ^^^^^^^^^^^^^^
        AttributeError: module 'app.accounts.views' has no attribute 'register'


#### 53. Membuat register() View Function

        modified:   README.md
        modified:   app/accounts/views.py


#### 54. Membuat  register template

        modified:   README.md
        new file:   app/accounts/templates/registration/register.html
        modified:   app/learning_logs/templates/learning_logs/base.html

        Note:

        Sistem pendaftaran yang kami siapkan memungkinkan siapa saja untuk melakukannya
        sejumlah akun untuk Log Pembelajaran. Beberapa sistem
        mengharuskan pengguna untuk mengkonfirmasi identitas mereka dengan mengirimkan a
        email konfirmasi yang harus dibalas pengguna. Dengan melakukan hal tersebut,
        sistem menghasilkan lebih sedikit akun spam daripada sistem yang sederhana
        yang kami gunakan di sini. Namun, saat Anda sedang belajar
        membangun aplikasi, sangat tepat untuk berlatih dengan sebuah
        sistem registrasi pengguna sederhana seperti yang kami gunakan.


### Melindungi sistem dari un-registered users


#### 55. Membatasi akses ke laman topics

        modified:   README.md
        modified:   app/learning_logs/views.py
        modified:   config/settings.py


#### 56. Membatasi akses ke seluruh Learning Log

        modified:   README.md
        modified:   app/learning_logs/views.py


#### 57. Menghubungkan data dengan user tertentu

        modified:   README.md
        new file:   app/learning_logs/migrations/0003_topic_owner.py
        modified:   app/learning_logs/models.py

        E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src(main -> origin)
        (venv312504) λ  python manage.py shell
        Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>> from django.contrib.auth.models import User
        >>> User.objects.all()
        <QuerySet [<User: superuser>, <User: newuser1>]>
        >>> for user in User.objects.all():
        ...     print(user.username, user.id)
        ...
        superuser 1
        newuser1 2
        >>> exit()

        E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src(main -> origin)
        (venv312504) λ  python manage.py makemigrations learning_logs
        It is impossible to add a non-nullable field 'owner' to topic without specifying a default. This is because the database needs something to populate existing rows.
        Please select a fix:
         1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
         2) Quit and manually define a default value in models.py.
        Select an option: 1
        Please enter the default value as valid Python.
        The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value. Type 'exit' to exit this prompt
        >>> 1
        Migrations for 'learning_logs':
          app\learning_logs\migrations\0003_topic_owner.py
            - Add field owner to topic

        E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src(main -> origin)
        (venv312504) λ  python manage.py migrate learning_logs 0003
        Operations to perform:
          Target specific migration: 0003_topic_owner, from learning_logs
        Running migrations:
          Applying learning_logs.0003_topic_owner... OK

        E:\_WORKSPACE\2024\django\2466\2466-dj5-learning-tracker\src(main -> origin)
        (venv312504) λ  python manage.py shell
        Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>> from app.learning_logs.models import Topic
        >>> for topic in Topic.objects.all():
        ...     print(topic, topic.owner)
        ...
        Topic 1 superuser
        Topic 2 superuser
        Topic 3 superuser
        test-new-topic-1 superuser
        test-new-topic-2 superuser
        test-new-topic-3 superuser
        test-new-topic-4 superuser
        >>> exit()

        Note

        Anda cukup mereset database daripada menjalankan migrasi, tapi
        yang Anda akan kehilangan semua data yang ada. 

        Ini adalah praktik yang baik untuk mempelajari caranya
        untuk memigrasi database dengan tetap menjaga integritas
        data pengguna. Jika Anda ingin memulai dengan database baru,
        keluarkan perintah python manage.py flush untuk membangun kembali database
        struktur. Anda harus membuat pengguna super baru, dan semuanya
        data Anda akan hilang.


#### 58. Membatasi Akses Topik kepada Pengguna yang Sesuai

        modified:   README.md
        modified:   app/learning_logs/views.py

        Note: error

        IntegrityError at /new_topic/
        (1048, "Column 'owner_id' cannot be null")

        Solution: Create a new user

        :)


#### 59. Melindungi a User’s Topics

        modified:   README.md
        modified:   app/learning_logs/views.py


#### 60. Melindungi  edit_entry Page

        modified:   README.md
        modified:   app/learning_logs/views.py


#### 61. Mengaitkan Topik Baru dengan Pengguna Saat Ini

        modified:   README.md
        modified:   app/learning_logs/views.py


### STYLING


#### 62. Install Bootstrap5

        (venv312504) λ pip install django-bootstrap5
        Collecting django-bootstrap5

        modified:   README.md
        modified:   config/settings.py


#### 63. Styling base.html dan index.html

        modified:   README.md
        modified:   app/learning_logs/templates/learning_logs/base.html
        modified:   app/learning_logs/templates/learning_logs/index.html


#### 64. Styling the Login Page

        modified:   README.md
        modified:   app/accounts/templates/registration/login.html


#### 65. Styling the laman Topics

        modified:   README.md
        modified:   app/learning_logs/templates/learning_logs/topics.html


#### 66. Styling Entries pada laman Topic

        modified:   README.md
        modified:   app/learning_logs/templates/learning_logs/topic.html


#### 67. Membuat requirements.txt file

        (venv312504) λ pip freeze > requirements.txt

        modified:   README.md
        new file:   requirements.txt