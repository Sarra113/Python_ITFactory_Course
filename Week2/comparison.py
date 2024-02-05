"""
Compararea colecțiilor de date Listă vs. Tuplu vs. Set

+----------------------+---------+--------+------+
| Structură            |  Listă  | Tuplu  | Set  |
+----------------------+---------+--------+------+
| Sintaxă              |  []     |   ()   |  {}  |
| Ordonat              |  Da     |   Da   |  Nu  |
| Mutabil              |  Da     |   Nu   |Da, p.|
| Duplicatele permise  |  Da     |   Da   |  Nu  |
| Indexare             |  Da     |   Da   |  Nu  |
| Extensibilitate      |  Da     |   Nu   |  Da  |
| Căutare rapidă       |  Nu     |   Nu   |  Da  |
| Element unic         |  Nu     |   Nu   |  Da  |
| Utilizare în dict.   |  Nu     |   Da   |  Nu  |
+----------------------+---------+--------+------+

Legendă:
- Ordonat: Dacă menține ordinea elementelor
- Mutabil (p=parțial): Dacă elementele pot fi modificate după creare
- Duplicatelor permise: Dacă permite elemente duplicate
- Indexare: Dacă elementele pot fi accesate prin index
- Extensibilitate: Dacă pot fi adăugate sau eliminate elemente
- Căutare rapidă: Dacă structura este optimizată pentru căutări rapide
- Element unic: Dacă fiecare element există o singură dată
- Utilizare în dict.: Dacă poate fi utilizat ca cheie în dicționare
"""
