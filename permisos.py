# -*- coding: utf-8 -*-
"""
===============================================================================
MATEMÁTICAS DISCRETAS - UNIDAD 2
Modelo de usuarios, recursos, roles y permisos
Caso: plataforma educativa institucional (10 usuarios, 3 roles, 7 recursos)
-------------------------------------------------------------------------------
Este programa reproduce paso a paso, en Python, el modelo matemático del
reporte: conjuntos, subconjuntos, operaciones, producto cartesiano, relación
de acceso, matriz, propiedades y funciones.
===============================================================================
"""

# =============================================================================
# 0. DATOS DEL SISTEMA
# =============================================================================

# Conjunto universal U: los 10 usuarios de la plataforma.
USUARIOS = ["Valeria", "Diego", "Mariana", "Emiliano", "Lucía",
            "Sebastián", "Regina", "Rodrigo", "Ximena", "Bruno"]
U = set(USUARIOS)

# Conjunto R: los 7 recursos digitales.
RECURSOS = ["BD_ACADEMICA", "SERVIDOR", "REPOSITORIO", "LMS",
            "CALIFICACIONES", "BIBLIOTECA", "RESPALDOS"]
R = set(RECURSOS)

# Subconjuntos por rol (cada rol es un subconjunto de U).
ROLES = {
    "Administrador": {"Valeria", "Diego"},
    "Docente":       {"Diego", "Mariana", "Emiliano", "Lucía"},
    "Estudiante":    {"Sebastián", "Regina", "Rodrigo", "Ximena", "Bruno"},
}

# Nivel de permiso de cada usuario en cada recurso:
#   1 = lectura, 2 = escritura, 3 = administración.
# La jerarquía 3 > 2 > 1 significa: quien administra también escribe y lee.
# Si un usuario no aparece con un recurso, no tiene ningún acceso a él.
NIVELES = {
    "Valeria": {"BD_ACADEMICA": 3,"SERVIDOR": 3,"REPOSITORIO": 3,"LMS": 2,"CALIFICACIONES": 2,"BIBLIOTECA": 1,"RESPALDOS": 3},
    "Diego": {"BD_ACADEMICA": 2,"SERVIDOR": 2,"REPOSITORIO": 3,"LMS": 3,"CALIFICACIONES": 3,"BIBLIOTECA": 1},
    "Mariana": {"REPOSITORIO": 2,"LMS": 3,"CALIFICACIONES": 3,"BIBLIOTECA": 1},
    "Emiliano": {"BD_ACADEMICA": 1, "REPOSITORIO": 2,"LMS": 2,"CALIFICACIONES": 2,"BIBLIOTECA": 1},
    "Lucía": {"REPOSITORIO": 2,"LMS": 3,"CALIFICACIONES": 2,"BIBLIOTECA": 1},
    "Sebastián": {"REPOSITORIO": 1, "LMS": 1,"BIBLIOTECA": 1},
    "Regina": {"REPOSITORIO": 1,"LMS": 1,"BIBLIOTECA": 1},
    "Rodrigo": {"LMS": 1,"BIBLIOTECA": 1},
    "Ximena": {"REPOSITORIO": 1,"LMS": 1,"BIBLIOTECA": 1},
    "Bruno": {},          # cuenta creada pero todavía sin activar
}

# Nombres cortos para imprimir la matriz en una sola pantalla.
ABREV = {"BD_ACADEMICA": "BD", "SERVIDOR": "SRV", "REPOSITORIO": "REP",
         "LMS": "LMS", "CALIFICACIONES": "CAL", "BIBLIOTECA": "BIB",
         "RESPALDOS": "BKP"}


def titulo(texto):
    """Imprime un encabezado para separar las secciones de la salida."""
    print("\n" + "=" * 78)
    print(texto)
    print("=" * 78)


# Convertimos la tabla de niveles en un diccionario plano (usuario, recurso).
NIVEL = {(u, r): n for u, filas in NIVELES.items() for r, n in filas.items()}

# =============================================================================
# 1. CONJUNTO UNIVERSAL Y CARDINALIDADES
# =============================================================================
titulo("1. CONJUNTO UNIVERSAL Y CARDINALIDADES")

print("U =", sorted(U))
print("R =", sorted(R))
print("|U| =", len(U), " usuarios")
print("|R| =", len(R), " recursos")
print("U contiene a todos los usuarios dados de alta en la plataforma.")
print("R contiene todos los recursos digitales que la plataforma protege.")

# =============================================================================
# 2. SUBCONJUNTOS POR ROL
# =============================================================================
titulo("2. SUBCONJUNTOS POR ROL (A, D, E)")

ADMIN = ROLES["Administrador"]
DOCENTES = ROLES["Docente"]
ESTUDIANTES = ROLES["Estudiante"]

print("A (Administradores) =", sorted(ADMIN), " ->", len(ADMIN))
print("D (Docentes)        =", sorted(DOCENTES), " ->", len(DOCENTES))
print("E (Estudiantes)     =", sorted(ESTUDIANTES), " ->", len(ESTUDIANTES))
print("\nIntersección A n D =", sorted(ADMIN & DOCENTES))
print("¿Son disjuntos A y D?", ADMIN & DOCENTES == set(),
      "(Diego tiene los dos roles)")
print("¿La unión A u D u E cubre todo U?", (ADMIN | DOCENTES | ESTUDIANTES) == U)

# Conjuntos de usuarios según el tipo de permiso que tienen en algún recurso.
USUARIOS_LECTURA = {u for (u, r), n in NIVEL.items() if n >= 1}
USUARIOS_ESCRITURA = {u for (u, r), n in NIVEL.items() if n >= 2}
USUARIOS_ADMIN = {u for (u, r), n in NIVEL.items() if n >= 3}

print("\nL (usuarios con lectura en algún recurso)        =",
      sorted(USUARIOS_LECTURA))
print("W (usuarios con escritura en algún recurso)      =",
      sorted(USUARIOS_ESCRITURA))
print("M (usuarios con administración en algún recurso) =",
      sorted(USUARIOS_ADMIN))

# =============================================================================
# 3. OPERACIONES CON CONJUNTOS
# =============================================================================
titulo("3. OPERACIONES CON CONJUNTOS Y SU INTERPRETACIÓN")

print("3.1 Unión   A u D =", sorted(ADMIN | DOCENTES))
print("    -> usuarios con privilegios de administración o de docencia.")

print("\n3.2 Intersección   D n W =", sorted(DOCENTES & USUARIOS_ESCRITURA))
print("    -> docentes que además pueden modificar información.")

print("\n3.3 Diferencia   D - M =", sorted(DOCENTES - USUARIOS_ADMIN))
print("    -> docentes que no tienen permiso de administración.")

print("\n3.4 Complemento   A' = U - A =", sorted(U - ADMIN))
print("    -> usuarios que no son administradores del sistema.")

COMBINADA = (DOCENTES | ESTUDIANTES) & USUARIOS_ADMIN - ADMIN
print("\n3.5 Combinada   (D u E) n M - A =", sorted(COMBINADA))
print("    -> docentes o estudiantes con permiso de administración que no")
print("       pertenecen al área de sistemas (jefes de academia).")

print("\n3.6 Diferencia adicional   U - W =", sorted(U - USUARIOS_ESCRITURA))
print("    -> usuarios sin permiso de escritura (solo lectura o sin acceso).")

# =============================================================================
# 4. PRODUCTO CARTESIANO U x R
# =============================================================================
titulo("4. PRODUCTO CARTESIANO U x R")

PRODUCTO = {(u, r) for u in USUARIOS for r in RECURSOS}
print("|U x R| = |U| * |R| =", len(U), "*", len(R), "=", len(PRODUCTO))
print("Muestra representativa (primeros 10 pares):")
for par in sorted(PRODUCTO)[:10]:
    print("   ", par)
print("Cada par (u, r) es una combinación posible de un usuario con un")
print("recurso; la relación de acceso dirá cuáles de esas combinaciones")
print("están efectivamente autorizadas.")

# =============================================================================
# 5. RELACIÓN DE ACCESO A (subconjunto de U x R)
# =============================================================================
titulo("5. RELACIÓN DE ACCESO A")

# Un par (u, r) está en A si el usuario tiene al menos un permiso en r.
ACCESO = set(NIVEL.keys())
ACCESO_LECTURA = {p for p, n in NIVEL.items() if n >= 1}
ACCESO_ESCRITURA = {p for p, n in NIVEL.items() if n >= 2}
ACCESO_ADMIN = {p for p, n in NIVEL.items() if n >= 3}

print("A = A_lectura u A_escritura u A_admin  ->",
      ACCESO == (ACCESO_LECTURA | ACCESO_ESCRITURA | ACCESO_ADMIN))
print("Pares en A:", len(ACCESO), "de", len(PRODUCTO), "posibles")
for u in USUARIOS:
    fila = sorted(r for r in RECURSOS if (u, r) in ACCESO)
    print("   ", u.ljust(9), len(fila), "recursos ->", fila)

DOMINIO = {u for u, r in ACCESO}
IMAGEN = {r for u, r in ACCESO}

print("\nDominio de A (usuarios con al menos un acceso):", sorted(DOMINIO))
print("Imagen de A (recursos con al menos un usuario):", sorted(IMAGEN))
print("Usuarios sin acceso: U - Dominio =", sorted(U - DOMINIO))
print("Recursos sin usuarios autorizados: R - Imagen =", sorted(R - IMAGEN))

CON_VARIOS = {u for u in DOMINIO
              if len([r for r in RECURSOS if (u, r) in ACCESO]) > 1}
print("Usuarios con acceso a más de un recurso:", sorted(CON_VARIOS))
print("Total de usuarios con acceso a más de un recurso:", len(CON_VARIOS))

# =============================================================================
# 6. MATRIZ DE LA RELACIÓN
# =============================================================================
titulo("6. MATRIZ DE LA RELACIÓN  M_A = [a_ij]")

encabezado = "".ljust(9) + "".join(ABREV[r].rjust(5) for r in RECURSOS)
print(encabezado)
print("-" * len(encabezado))

for u in USUARIOS:
    fila = ""
    for r in RECURSOS:
        fila += ("1" if (u, r) in ACCESO else "0").rjust(5)
    print(u.ljust(9) + fila + "|" )

print("-" * len(encabezado))

# =============================================================================
# 7. PROPIEDADES DE LAS RELACIONES
# =============================================================================
titulo("7. PROPIEDADES DE LA RELACIÓN DE ACCESO Y DE LA RELACIÓN AUXILIAR")


def revisar_propiedades(nombre, relacion, conjunto):
    """Calcula si una relación sobre 'conjunto' es reflexiva, simétrica,
    antisimétrica y transitiva, e imprime un ejemplo de cada caso."""
    reflexiva = all((x, x) in relacion for x in conjunto)
    simetrica = all((b, a) in relacion for (a, b) in relacion)
    antisimetrica = all(a == b for (a, b) in relacion if (b, a) in relacion)

    transitiva = True
    fallo = None
    for (a, b) in relacion:
        for c in conjunto:
            if (b, c) in relacion and (a, c) not in relacion:
                transitiva = False
                fallo = (a, b, c)
                break
        if not transitiva:
            break

    print("\nRelación " + nombre)
    print("  reflexiva:      ", "SÍ" if reflexiva else "NO")
    print("  simétrica:      ", "SÍ" if simetrica else "NO")
    print("  antisimétrica:  ", "SÍ" if antisimetrica else "NO")
    print("  transitiva:     ", "SÍ" if transitiva else "NO")
    if not transitiva:
        a, b, c = fallo
        print("  contraejemplo: ({}, {}) y ({}, {}) existen,".format(a, b, b, c))
        print("  pero ({}, {}) no existe.".format(a, c))


# 7.1 Propiedades de A como relación entre conjuntos distintos
INVERSA = {(r, u) for (u, r) in ACCESO}
print("Relación inversa A^-1 (recurso, usuario), pares:", len(INVERSA))
print("Ejemplo:", sorted(INVERSA)[:5])

imagenes_por_usuario = {u: len([r for r in RECURSOS if (u, r) in ACCESO])
                        for u in USUARIOS}
maximo = max(imagenes_por_usuario.values())
print("\n¿Cada usuario tiene al menos un recurso?", DOMINIO == U)
print("¿Algún recurso está asociado con todos los usuarios?",
      any(len([u for u in USUARIOS if (u, r) in ACCESO]) == len(U) for r in RECURSOS))
print("¿A es función de U en R?", maximo <= 1,
      "(hay usuarios con hasta", maximo, "recursos, por lo tanto NO lo es)")


# 7.2 Relación auxiliar S: "comparte al menos un rol con"
def roles_de(usuario):
    """Devuelve el conjunto de roles que tiene un usuario."""
    return {rol for rol, miembros in ROLES.items() if usuario in miembros}


S = {(u, v) for u in USUARIOS for v in USUARIOS if roles_de(u) & roles_de(v)}
print("\nRelación S = 'comparte al menos un rol con'  |S| =", len(S))
revisar_propiedades("S (comparte al menos un rol con)", S, U)

# 7.3 Segunda relación: T = "tiene el mismo rol principal que"
ROL_PRINCIPAL = {
    "Valeria": "Administrador", "Diego": "Administrador", "Mariana": "Docente",
    "Emiliano": "Docente", "Lucía": "Docente", "Sebastián": "Estudiante",
    "Regina": "Estudiante", "Rodrigo": "Estudiante", "Ximena": "Estudiante",
    "Bruno": "Estudiante"
}
T = {(u, v) for u in USUARIOS for v in USUARIOS
     if ROL_PRINCIPAL[u] == ROL_PRINCIPAL[v]}
revisar_propiedades("T (tiene el mismo rol principal que)", T, U)

print("\nClases de equivalencia de T (perfiles de acceso):")
for rol in ROLES:
    clase = sorted(u for u in USUARIOS if ROL_PRINCIPAL[u] == rol)
    print("   ", rol.ljust(14), clase)

# =============================================================================
# 8. FUNCIONES ASOCIADAS
# =============================================================================
titulo("8. FUNCIONES ASOCIADAS AL SISTEMA")

# 8.1 f: U -> M   (identificador institucional)
IDS = {"Valeria": "20260001", "Diego": "20260002", "Mariana": "20260003",
       "Emiliano": "20260004", "Lucía": "20260005", "Sebastián": "20260006",
       "Regina": "20260007", "Rodrigo": "20260008", "Ximena": "20260009",
       "Bruno": "20260010"}
M = {"2026%04d" % i for i in range(1, 13)}          # 12 identificadores válidos

print("f: U -> M ,  f(usuario) = identificador institucional")
for u in USUARIOS:
    print("   f({}) = {}".format(u.ljust(9), IDS[u]))
print("Dominio:", len(set(IDS)), "usuarios | Codominio |M| =", len(M))
print("Imagen:", len(set(IDS.values())), "identificadores")
print("Inyectiva:", len(set(IDS.values())) == len(IDS))
print("Sobreyectiva:", set(IDS.values()) == M)
print("Biyectiva:", len(set(IDS.values())) == len(IDS) and set(IDS.values()) == M)

# 8.2 g: U -> Roles  (rol principal)
print("\ng: U -> Roles ,  g(usuario) = rol principal")
print("Codominio:", sorted(ROLES.keys()))
print("Imagen:", sorted(set(ROL_PRINCIPAL.values())))
print("Inyectiva:", len(set(ROL_PRINCIPAL.values())) == len(ROL_PRINCIPAL))
print("Sobreyectiva:", set(ROL_PRINCIPAL.values()) == set(ROLES.keys()))

# 8.3 h: U -> N  (número de recursos accesibles)
print("\nh: U -> N ,  h(usuario) = número de recursos a los que accede")
for u in USUARIOS:
    print("   h({}) = {}".format(u.ljust(9), imagenes_por_usuario[u]))

print("\n" + "=" * 78)
print("FIN DEL ANÁLISIS")
print("=" * 78)