INDICATIVO = "indicativo"
IMPERATIVO = "imperativo"
SUBJUNTIVO = "subjuntivo"


tiempos = (
    (INDICATIVO, "presente", "presente"),
    (
        INDICATIVO,
        "imperfecto",
        "imperfectoⓘTambién llamado:pretérito imperfecto o copretérito",
    ),
    (
        INDICATIVO,
        "pretérito",
        "pretéritoⓘTambién llamado:pretérito perfecto simple o pretérito indefinido",
    ),
    (INDICATIVO, "futuro", "futuroⓘTambién llamado:futuro simple o futuro imperfecto"),
    (
        INDICATIVO,
        "condicional",
        "condicionalⓘTambién llamado:condicional simple o pospretérito",
    ),
    (INDICATIVO, "pretérito perfecto", "pretérito perfecto"),
    (
        INDICATIVO,
        "pluscuamperfecto",
        "pluscuamperfectoⓘTambién llamado:pretérito pluscuamperfecto",
    ),
    (INDICATIVO, "futuro perfecto", "futuro perfecto"),
    (INDICATIVO, "condicional perfecto", "condicional perfecto"),
    (SUBJUNTIVO, "presente", "presente"),
    (
        SUBJUNTIVO,
        "imperfecto",
        "imperfectoⓘTambién llamado:pretérito o pretérito imperfecto",
    ),
    (SUBJUNTIVO, "futuro", "futuroⓘTambién llamado:futuro simple o futuro imperfecto"),
    (SUBJUNTIVO, "pretérito perfecto", "pretérito perfecto"),
    (SUBJUNTIVO, "pluscuamperfecto", "pluscuamperfecto"),
    (SUBJUNTIVO, "futuro perfecto", "futuro perfecto"),
    (IMPERATIVO, "afirmativo", "afirmativo\n–"),
    (IMPERATIVO, "negativo", "negativo\n–"),
    (INDICATIVO, "pretérito anterior", "pretérito anterior"),
)

pronouns = (
    "yo",
    "tú",
    "él, ella, usted",
    "nosotros, nosotras",
    "vosotros, vosotras",
    "ellos, ellas, ustedes",
    "vos",
)

pronouns_short = (
    "yo",
    "tú",
    "él, ella, Vd",
    "nosotros/as",
    "vosotros/as",
    "ellos/as, Vds",
    "vos",
)

pronouns_imperativo = (
    "(tú)",
    "(usted)",
    "(nosotros, nosotras)",
    "(vosotros, vosotras)",
    "(ustedes)",
    "(vos)",
)

pronouns_imperativo_short = (
    "(tú)",
    "(usted)",
    "(nosotros/as)",
    "(vosotros/as)",
    "(ustedes)",
    "(vos)",
)


def tiempos_list():
    """Builds a list of commands of tenses"""
    commands = [f"{ele[1].replace(' ', '_')}_{ele[0]}" for ele in tiempos]
    commands.append("start")

    return commands
