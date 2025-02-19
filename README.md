# **Documentation of the program**

#### [Of which treats the program](#of-which-treats-the-program-1)

#### [Virtual surroundings](#virtual-surroundings-1)

#### [Create .env a key](#create-env-a-key-1)

#### [Initiate the app](#initiate-the-app-1)

---

---

---

---

---

## Of which treats the program

The main function of the program orders  one little your collection of Mangas mainly and so far there is one simple CRUD with the option to download you a PDF that contendra the name of the user with the current session and to his inner when was downloaded.

### Packages and bookshops

Some of the packages employed to do this project are:

- BONE
- django
- datetime
- pillow


> [!IMPORTANT]  
> No sleep all the packages are some of the most important


> [!TIP]
> To install any one of these bookshops individually will do ```pip install name_package```

Optionally, but of way recommended can do a ```pip install -r Requirements.txt``` To install all the necessary packages.


## Virtual surroundings

### Create surroundings and go in
To create some surroundings have to execute the one of down below to the CMD or any of the before commented variants, is has that take into account the operating system that is has installed to avoid  problems.

The comanda of low of each one serves to go in and would have to go out us thing like this to the terminal to verify that we are in the surroundings ```(.Name_surroundings) current/route>``` (can vary subtly depend of what employ, CMD,PS, etc...) Of not being like this look that we are to the route that touches or that the comanda is well put.

> [!CAUTION]
> Depending of the version of Windows or Linux perhaps can vary some comandes

#### WINDOWS

```python
python -m venv .Choose_name
.Name_chosen\Scripts\activate
```

#### LINUX

```python
python3 -m venv .Choose_namesource .Name_put/bin/activate
```

### Go out surroundings
When want to go out of some surroundings simply have to execute the comanda of
bass 
```python
deactivate
```

### Erase surroundings

To erase the virtual surroundings simply erase the folder that is to create in creating the surroundings, usually only have one ```.``` To the start how what can see to the examples.

## Create a .env Key

Before initializing the app, you need to generate two things:

1. **.env File**: Create it manually or use the command `touch .env`.
2. **Django Secret Key**: Visit [this website](https://miniwebtool.com/django-secret-key-generator/) to generate a key.

After that, add this to your `.env` file:
```
SECRET_KEY='your_generated_secret_key'
```

## Initiate the app

> [!IMPORTANT]  
> Before initiating the app would go well do the following comandes
>
> ``` python manage.py migrate  ```
>
> ``` python manage.py loaddata biblioteca/fixtures/initial_data.json ```
>
> If we want to do an erased massive can do this comanda:
> ``` rm db.sqlite3 ```
>
> And next execute the 2 first comandes to go back to create the bbdd and put the data

For engegar have to it accedire access in the folder ``MangaLibrary``

```
cd .\MangaLibrary
```

And we have to execute this comanda
```
python manage.py runserver
```

# [↑](#of-which-treats-the-program)