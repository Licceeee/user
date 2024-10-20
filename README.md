# user

Django user app

This Django CustomUser app provides a customizable user model for Django projects.
It allows to easily integrate a custom user model as a submodule into an existing Django project.
Features like profile management and authentication can be handled in separate apps.

## Installation

### Step 1: Add the CustomUser App as a Submodule

```
git submodule add git@github.com:Licceeee/user.git [path/to/your/django/project/apps/user]
```

Initialize and update the submodule:

```
git submodule init
git submodule update
```

### Step 2: Add the CustomUser App to `INSTALLED_APPS`

In your Django project's settings.py, add the custom user app to INSTALLED_APPS:

```
INSTALLED_APPS = [
    ...
    'user',  # or path to the submodule (e.g., 'path.to.submodule.user')
]
```

### Step 3: Set the Custom User Model

You need to tell Django to use the custom user model provided by this app. In settings.py, set the AUTH_USER_MODEL:

```
AUTH_USER_MODEL = 'user.CustomUser'
```

### Step 4: Migrate the Database

Run migrations to create the necessary database tables for the custom user model:

```
python manage.py migrate
```

This will ensure that the custom user model is applied to your database.

### Step 5: Optional Settings

If you want to extend or modify the `CustomUser` model, ensure you have the correct fields defined in your `CustomUser` class
and update any related forms or admin configurations as needed.
