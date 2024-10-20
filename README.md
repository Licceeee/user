# user

Django user app

This Django CustomUser app provides a customizable user model for Django projects.
It allows to easily integrate a custom user model as a submodule into an existing Django project.
Features like profile management and authentication can be handled in separate apps.

## Installation

### Step 1: Add the CustomUser App as a Submodule

#### Case 1: Cloning a Project that Contains the Submodule

If you're cloning a repository that already includes this CustomUser app as a submodule, you should use
the `--recurse-submodules` option to ensure that Git fetches the submodule along with the main project:

```
git clone --recurse-submodules <repository-url>
```

This will automatically initialize and update the submodule after cloning. No further steps are required for the submodule setup.

#### Case 2: Adding the CustomUser App as a New Submodule

If you have an existing Django project and want to add this CustomUser app as a submodule manually, follow these steps:

Add the Submodule:

```
git submodule add git@github.com:Licceeee/user.git [path/to/your/django/project/apps/user]
```

Initialize and update the submodule:
After adding the submodule, you need to initialize and update it to fetch the submodule's contents:

```
git submodule init
git submodule update
```

Commit the Submodule Reference:
After adding the submodule, be sure to commit the changes to your main repository:

```
git commit -am "Added user app as a submodule"
```

This ensures that the submodule is linked properly and included in your project.

### Step 2: Add the CustomUser App to `INSTALLED_APPS`

In your Django project's settings.py, add the custom user app to INSTALLED_APPS:

```

INSTALLED_APPS = [
...
"user.apps.UserConfig", # Custom user app
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
