# Python-basic

Esto es una serie de ejemplos que abarcan conocimientos basicos del lenguaje python.

## Instalación

Trabajaremos con Python 3.8. Lo instalamos de la siguiente forma.

```sh
	brew install python
```

Cuando instalamos python en nuestro equipo este se ubicará en una ruta como esta:

```sh
	/usr/local/bin/python3
```

Tambien se crea una carpeta respectiva a la version que se ha instalado en el equipo.

```sh
	/Users/rapser/Library/Python/3.8
```
Existe una version previa instalada python 2 en el equipo en la siguiente ubicación.

```sh
	/usr/bin/python
```
## Como usar

Si usamos python directamente estaremos usando la version 2.7. Si queremos utilizar la version recientemente instalada tenemos que agregar un 3 al final.

```sh
	$ python3 example.py
	$ pip3 --version
```

## Alias

Si queremos cambiar la forma como llamamos a python en nuestro terminal. Tenemos que agregar un alias para que se pueda abrir la version 3.8 sin necesidad de agregar el numero 3 a python.

```sh
	alias python=python3.8
```
Finalmente, esto 

```sh
	$ python example.py
	$ pip --version
```