# **Documentación del programa***

#### [De que trata el programa](#de-que-trata-el-programa-1)

#### [Entornos virtuales](#entornos-virtuales-1)

#### [Iniciar la app](#iniciarla-app-1)

---

---

---

---

---

## De que trata el programa

La función principal del programa se ordena un poco tu colección de Mangas principalmente y por ahora hay un CRUD sencillo con la opción de descargarte un PDF que contendra el nombre del usuario con la sesión actual y a su interior cuando fue descargado.

### Paquetes y librerías

Algunos del paquetes empleados para hacer este proyecto son:

- OS
- django
- datetime
- pillow


> [!IMPORTANT]  
> No sueño todos los paquetes son algunos de los más importantes


> [!TIP]
> Para instalar cualquier de estas librerías individualmente haremos ```pip install nombre_paquete```

Opcionalmente, pero de manera recomendada podemos hacer un ```pip install -r Requirements.txt``` para instalar todos los paquetes necesarios.


## Entornos virtuales

### Crear en torno y entrar
Para crear un entorno tenemos que ejecutar el de abajo al CMD o alguna de las variantes antes comentadas, es tiene que tener en cuenta el sistema operativo que es tiene instalado para evitarse problemas.

El pedido de bajo de cada uno sirve para entrar y nos tendría que salir cosa así al terminal para verificar que estamos dentro del entorno ```(.nombre_en torno) ruta/actual>``` (puede variar sutilmente dependan del que emplees, CMD,P.S., etc...) de no ser así mirar que estemos a la ruta que toca o que el pedido está bien puesto.

> [!CAUTION]
> Dependiendo de la versión de Windows o Linux quizás pueden variar algunos pedidos

#### WINDOWS

```
pythonpython -m venv .elegir_nombre
.nombre_elegido\Scripts\activate
```

#### LINUX

```
pythonpython3 -m venv .elegir_nombresource .nombre_puesto/bin/activate
```

### Salir en torno
Cuando queremos salir de un entorno simplemente tenemos que ejecutar el pedido de bajo
```
pythondeactivate
```

### Borrar en torno

Para borrar el entorno virtual simplemente borramos la carpeta que es crear al crear el entorno, normalmente solo tenemos uno ```.``` al inicio como el que podemos ver a los ejemplos.

## Iniciar la app

> [!IMPORTANT]  
> Antes de iniciar el app iría bien hacer los siguientes pedidos
>
> ``` python manage.py migrado e  ```
>
> ``` python manage.py loaddata biblioteca/fixtures/initial_fecha.json ```
>
> Si queremos hacer un borrado masivo podemos hacer este pedido:
> ``` rm db.sqlite3 ```
>
> Y después ejecutamos las 2 primeras pedidos para volver a crear la bbdd y poner los datos

Para poner en marcha lo tenemos que accedire acceder dentro de la carpeta ``MangaLibrary``

```
cd .\MangaLibrary
```

Y tenemos que ejecutar este pedido
```
python manage.py runserver
```

# [↑](#documentacio-del-programa)