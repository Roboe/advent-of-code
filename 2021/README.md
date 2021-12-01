Advent of Code 2021
===

Veamos si aguanto las ganas algo más que el año pasado.

Dos ficheros por problema:
- el _input_, `dayN.input.txt`
- el _test_ que resuelve el problema: `dayN_test.py` en el caso de Python

Resolverlos en un lenguaje o paradigma que controlo no me incentiva mucho, así que utilizaré lenguajes que no piloto demasiado.


Python
---

Para correr los _tests_:

    $ pytest -v # o dayN_test.py

Para formatear el código según la PEP8:

    $ black . # o dayN_test.py


SQL (SQLite)
---

SQL **es** un lenguaje de programación. Específico de dominio (DSL), no de uso general (GPL), claro. En realidad solo voy a resolver un puzzle con SQL, me han retado (_How dare you, @juanPorti!_). Y resulta que con la CLI de SQLite3 [se pueden importar CSV](https://www.sqlite.org/cli.html#importing_csv_files).

Para ejecutar las consultas:

    $ cat day01.sqlite3_cli | sqlite3
