def greet(language):
    db = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }
    
    return db[language] if language in db else db["english"]

if __name__ == '__main__':
    languages = [
        "lithuanian",
        "finnish",
        "IP_ADDRESS_NOT_FOUND",
        "dutch",
        "irish",
        "czech",
        "IP_ADDRESS_REQUIRED"
        ]
    
    for language in languages:
        print(f"The greetings for {language} is {greet(language)}")