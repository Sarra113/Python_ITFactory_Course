# Sesiunea 18: SQL, NOSQL
## 📝 OBIECTIVE
- Sa invatam cum sa interactionam cu bazele de date
- SQL
- NoSQL
- SQL vs NoSQL

## 📌 Baze de date
- Ramura a programarii care se ocupa cu stocarea datelor
- Dezvolatorii de aplicatii pot alege intre doua mari categori
de baze de date (Relational DB vs Non-relational DB):
  - SQL (Structured Query Language)
  - NoSQL (Not Only SQL)
- Baze de date SQL
  - baze de date RELATIONALE
  - date structurate, stocate in format tabelar, existand relatii intre entitati (tabele)
  - folosite de peste 40 de ani, dar in ciuda varstei pe care o au inca raman extrem de populare
  - exemple: SQLite, MariaDB, MySQL, PostgreSQL, Oracle etc
  - sqlite, fata de restul db-urilor, salveaza datele intr-un
singur fisier, in timp ce celalate db-uri sunt deployate pe un server.
  - avantaj: avem o schema predefinita a datelor, acces rapid si ocupa relativ putin spatiu de stocare
- Baze de date NoSQL
  - sunt baze de date non-relationale
  - date nestructurate, nu sunt stocate sub format tabelar, 
ci pot fi salvate sub forma de documente, grafuri, json etc
  - permit salvarea de imagini, videouri, articole etc
  - avantaj: creste viteza de dezvoltare a aplicatiilor, nefiind nevoie de a respecta o schema predefinita
  - au prins popularitate mare in ultimii ani
  - o misconceptie des intalnita in legatura cu bazele de date NoSQL
este ca "No" nu inseamna NU SQL, ci de fapt inseamna Not Only SQL.
  - putem intalni SQL in baze de date NoSQL
  - 4 categorii de baze de date NoSQL:
    - Document stores (MongoDB, DynamoDB, CosmosDB etc)
    - Graph databases (Neo4j, AragonDB etc)
    - Key-value stores (Redis, Memcached etc)
    - Wide-column data stores (Cassandra, Hbase, Bigtable etc)

## 📌 Ce este un ORM
- ORM (Object-Relational Mapping) reprezinta o tehnica care iti
permite sa manipulezi date dintr-o baza de date folosind
o paradigma object-oriented.
- Cand povestim despre ORM-uri, majoritatea oamenilor se refera
la o librarie care implementeaza tehnici Object-Relational Mapping
- O librarie ORM incapsuleaza codul necesar pentru manipularea
de date, iar facand aceasta nu mai trebuie sa folosim in mod direct
limbaj de tip SQL, practic interactionam direct cu un obiect
scris in limbajul pe care il folosim.

## 📌 SQL
- SQL este limbajul standard pentru tratarea bazelor de date
relationale.
- Poate fi utilizat pentru a insera, cauta si sterge inregistrarile
in baza de date.
- SQL poate face multe alte operatiuni, inclusiv optimizarea si
intretinerea bazelor de date.
- BAZA DE DATE
  - colectie sistemica de date
  - accepta stocarea si manipularea datelor
  - faciliteaza gestionarea datelor
  - formate din unul sau mai multe tabele
- TABELA
  - colectie de inregistrari, structurate pe una sau mai multe coloane
  - orice baza de date proaspat creata este vida - nu contine nici un tabel.
- O baza de date arata ca un fisier Excel (avem coloane, iar fiecare
rand reprezinta o intrare in tabela)
- Comenzi in baza de date: create/drop DB, create/drop table
  - SELECT (WHERE, ORDER BY, COUNT, GROUP BY)
  - INSERT
  - UPDATE
  - DELETE
  - FOREIGN KEY, PRIMARY KEY
  - PRIMARY KEY (PK) = e un field (o coloana) care identifica in mod unic
fiecare rand dintr-o tabela; o astfel de coloana nu poate avea valori duplicate sau valori nule
  - FOREIGN KEY (FK) = un field (o coloana) al unui tabel care face legatura (relatia) cu
o alta tabela, identificand astfel o relatie parinte-copil, unde tabela care tine FK
este copilul; in general in aceasta coloana FK referentiaza id-ul (PK) din tabela parinte
- Comenzile SQL sunt organizate in 5 categorii
  - **DDL** - Data Defined Language
    - Lucreaza cu structura bazei de date, adica cu forma ei 
    - Create, Drop, Alter, Truncate
  - DQL - Data Query Language
    - Select
  - **DML** - Data Manipulation Language
    - Lucreaza cu datele stocate in baza de date
    - Insert, Update, Delete
  - DCL - Data Control Language
    - Grant, Revoke
  - TCL - Transaction Control Language
    - Commit, Savepoint, Rollback, Set Transaction, Set Constraint

```python
"""
Vom crea o baza de date de tip SQLite in care sa salvam si sa 
interactionam cu datele necesare pentru o aplicatie marketplace.

Pentru interactiunea cu baza de date din Python, se va folosi
libraria sqlite3.
"""
```

```python
"""
Creaza tabelele conform indicatiilor de mai jos:

========== tabelul users ==========
- COLOANE:
1. id (primary key)
- identificator unic al utilizatorului
- tip: numar intreg
- valoarea se va auto incrementa
(primul user adaugat in tabel va avea id-ul 1)
(al doilea user adaugat in tabel va avea id-ul 2)
2. username
- usernume-ul utilizatorului 
- tip: text
- ne asiguram ca acest camp nu va fi niciodata gol
3. email
- email-ul utilizatorului
- tip: text
- ne asiguram ca acest camp nu va fi niciodata gol
4. password
- parola utilizatorului
- tip: text
- ne asiguram ca acest camp nu va fi niciodata gol
5. first_name
- prenume utilizator
- tip: text
- not null
6. last_name
- nume de familie utilizator
- tip: text
- not null
7. address
- adresa utilizator
- tip: text
8. city
- oras
- tip: text
9. postal_code
- codul postal
- tip: text
10. country
- tara
- tip: text

========== tabelul products ==========
- COLOANE:
1. id
- identificator unic al produsului
- tip: numar intreg
- valoarea se va auto incrementa
2. name
- numele produsului
- tip: text
- not null
3. category
- categorie produs
- tip: text
- not null
4. price
- pretul produsului
- tip: numar float
- not null
5. stock_count
- cantitatea in stoc a produsului
- tip: numar intreg
- default 0
6. description
- scurta descriere a produsului
- tip: text

========== tabelul orders ==========
- COLOANE:
1. id
- identificator unic comanda
- tip: numar intreg
- valoarea se va auto-incrementa
2. customer_id
- id-ul clientului/user-ului care a facut comanda
- foreign key cu referinta la users.id
- tip: numar intreg
3. order_date
- data plasarii comenzii
- tip: text
- not null

========== tabelul order_items ==========
- COLOANE:
1. id
- identificator unic al order line-ului
- tip: numar intreg
- se auto incrementeaza
2. order_id
- tip: numar intreg
- foreign key cu referire la id-ul comenzii de care apartine din tabelul orders.id
- not null
3. product_id
- tip: numar intreg
- foreign key cu referire la id-ul produsului pe care il contine
4. quantity
- tip: numar intreg
- cantitatea produsului adaugat in comanda
- default 1
5. total_price
- tip: float
- pretul calculat in functie de cantitatea de produs 
- not null
"""
```

```python
"""
Executa toate operatiile CRUD (prin query-uri SQL) pe tabelul products.
"""
```
