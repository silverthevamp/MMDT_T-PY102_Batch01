"""
Lab 03 — Hash Tables (4 Questions)

Rules:
- Do NOT use print() or input().
- Implement the functions exactly as named.
- You may use basic Python lists and dictionaries.
- Do NOT use any built-in hash table libraries except dict for Q1.

Questions:
Q1) Hash map usage
Q2) Hash table with chaining (conceptual simulation)
Q3) Linear probing simulation
Q4) Quadratic probing simulation
"""


# -------------------------
# Q1 — Hash Map
# -------------------------

def char_frequency(s: str) -> dict[str, int]:
    dict = {} 
    for char in s:
        if char in dict: 
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1  
    return dict 
    raise NotImplementedError


# -------------------------
# Q2 — Chaining (Collision Handling)
# -------------------------

def insert_chaining(table: list[list[int]], key: int, size: int) -> list[list[int]]:
    table = [[], [], []] 
    index = key % size 
    if table[index] == None:
        table[index] = key
    else : 
        table[index].append(key) 
    print (table)
    return table
    raise NotImplementedError
# -------------------------
# Q3 — Linear Probing
# -------------------------

def insert_linear_probing(table: list[int | None], key: int) -> list[int | None]:
    size = len(table)
    index = key % size 
    while table[index] != None: 
        index = (index + 1) % size 
    table[index] = key 
    return table
    raise NotImplementedError


# -------------------------
# Q4 — Quadratic Probing
# -------------------------

def insert_quadratic_probing(table: list[int | None], key: int) -> list[int | None]:
    size = len(table)
    hash = key % size
    i = 0
    while True:
        index = (hash + i * i) % size
        if table[index] is None:
            table[index] = key
            return table
        i += 1
    raise NotImplementedError