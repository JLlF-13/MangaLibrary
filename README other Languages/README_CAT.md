# ***Documentació del programa***

#### [De què tracta el programa](#de-què-tracta-el-programa-1)

#### [Entorns virtuals](#entorns-virtuals-1)

#### [Iniciar la app](#iniciar-la-app-1)

---

---

---

---

---

## De què tracta el programa

La funció principal del programa es ordena un poc la teva col·lecció de Mangas principalment i per ara hi ha un CRUD senzill amb la opció de descarregar-te un PDF que contendra el nom de l'usuari amb la sessió actual i al seu interior quan va ser descarregat.

### Paquets i llibreries

Alguns del paquets emprats per a fer aquest projecte són:

- OS
- django
- datetime
- pillow


> [!IMPORTANT]  
> No son tots els paquets són alguns dels més importants


> [!TIP]
> Per a instal·lar qualsevol d'aquestes llibreries individualment farem ```pip install nom_paquet```

Opcionalment, però de manera recomanada podem fer un ```pip install -r Requirements.txt``` per a instal·lar tots els paquets necessaris.


## Entorns virtuals

### Crear entorn i entrar
Per a crear un entorn hem d'executar el de a baix al CMD o alguna de les variants abans comentades, és té que tenir en compte el sistema operatiu que és té instal·lat per a evitar-se problemes.

La comanda de baix de cada un serveix per entrar i ens hauria de sortir cosa així al terminal per a verificar que estem dins l'entorn ```(.nom_entorn) ruta/actual>``` (pot variar subtilment depenguen del que empris, CMD,PS, etc...) de no ser així mirar que estiguem a la ruta que toca o que la comanda està ben posada.

> [!CAUTION]
> Depenent de la versió de Windows o Linux potser poden variar algunes comandes

#### WINDOWS

```python
python -m venv .triar_nom
.nom_triat\Scripts\activate
```

#### LINUX

```python
python3 -m venv .triar_nom
source .nom_posat/bin/activate
```

### Sortir entorn
Quan volem sortir d'un entorn simplement hem d'executar la comanda de baix
```python
deactivate
```

### Esborrar entorn

Per a esborrar l'entorn virtual simplement esborrem la carpeta que és crear en crear l'entorn, normalment sol tenim un ```.``` a l'inici com el que podem veure als exemples.

## Iniciar la app

> [!IMPORTANT]  
> Abans de iniciar l'app aniria bé fer les següents comandes
>
> ``` python manage.py migrate  ```
>
> ``` python manage.py loaddata biblioteca/fixtures/initial_data.json ```
>
> Si volem fer un esborrat massiu podem fer aquesta comanda:
> ``` rm db.sqlite3 ```
>
> I després executem les 2 primeres comandes per a tornar a crear la bbdd i posar les dades

Per a engegar el hem d'accedire accedir dins la carpeta ``MangaLibrary``

```
cd .\MangaLibrary
```

I hem de executar aquesta comanda
```
python manage.py runserver
```

# [↑](#documentació-del-programa)