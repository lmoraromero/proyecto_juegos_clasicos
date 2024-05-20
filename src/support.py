import random
from random import choices


def juego1():
    game = ['Piedra', 'Papel', 'Tijera']

    mark = 1
    victories_user = 0
    victories_comp = 0

    print('¡BIENVENIDO PIEDRA, PAPEL O TIJERA!', flush=True)
    print(' ')
    print('''¡Las normas del juego son simples!
        1. Elige tu arma: Cada jugador elige entre piedra, papel o tijera. Es una decisión rápida, ¡así que elige tu favorita!
        2. ¡Un, dos, tres! ¡Piedra, Papel o Tijera!: Tendrás que elegir una de las tres opciones. La máquina hace una elección aleatoria y se muestran a la vez. 
        3. La lucha: Piedra aplasta tijera, tijera corta papel y papel envuelve piedra. Así de simple.
        4. ¡Gana el más astuto!: Si tu elección vence a la de tu oponente, ¡eres el ganador! Si no, ¡inténtalo de nuevo!
        5. Hay tres rondas en total, ¡gana el mejor de tres!'''
        )

    while mark <= 3:
        print('----')
        print('¡Un, dos, tres! ¡Piedra, Papel o Tijera!')
        question = input('¡Piedra, Papel o Tijera!')
        choice = random.choice(game)
        if choice.lower() == question.lower():
            print(f'{choice.upper()} es igual a {question.upper()}')
        elif question.lower() == 'piedra' and choice.lower() == 'tijera':
            print(f'{question.upper()} gana a {choice.upper()}')
            print('¡Has ganado!')
            mark += 1
            victories_user += 1
        elif question.lower() == 'papel' and choice.lower() == 'piedra':
            print(f'{question.upper()} gana a {choice.upper()}')
            print('¡Has ganado!')
            mark += 1
            victories_user += 1
        elif question.lower() == 'tijera' and choice.lower() == 'papel':
            print(f'{question.upper()} gana a {choice.upper()}')
            print('¡Has ganado!')
            mark += 1
            victories_user += 1
        else:
            print(f'{choice.upper()} gana a {question.upper()}')
            print('¡Has perdido!')
            mark += 1
            victories_comp += 1
    if victories_user > victories_comp:
        print('----')
        print('¡Genial!¡Has ganado el juego! :D')
    else:
        print('----')
        print('¡Oh no!¡Has perdido! Inténtalo de nuevo ;)')
def juego2():
    def arte():
        art = {
            "1. ¿Quién pintó 'Los girasoles'?": "van Gogh",
            "2. ¿Qué movimiento artístico surgió en Italia en el siglo XVI y se caracteriza por el uso de la perspectiva y el realismo?": "Barroco",
            "3. ¿Quién es el autor del famoso cuadro 'El nacimiento de Venus'?": "Botticelli",
            "4. ¿Quién es el autor de la escultura 'David'?": "Miguel Ángel",
            "5. ¿Qué artista es conocido por su serie de cuadros de latas de sopa Campbell's?": "Warhol",
            "6. ¿Cuál es el movimiento artístico que se caracteriza por el uso de colores vivos y formas geométricas?": "Arte abstracto",
            "7. ¿Quién es el autor de 'El Grito'?": "Munch",
            "8. ¿Qué estilo artístico precedió al Renacimiento?": "Gótico",
            "9. ¿Cuál es la escultura más famosa de Rodin?": "El Pensador",
            "10. ¿Quién es conocido como el padre del cubismo?": "Picasso",
            "11. ¿Cuál es la obra más famosa de Vermeer?": "La joven de la perla",
            "12. ¿Cuál es el nombre del movimiento artístico que se caracteriza por el uso de líneas curvas y formas orgánicas inspiradas en la naturaleza?": "Art Nouveau",
            "13. ¿Quién es el autor de 'La persistencia de la memoria'?": "Dalí",
            "14. ¿Quién es conocido como el padre del impresionismo?": "Monet",
            "15. ¿Quién es el autor de 'El Jardín de las Delicias'?": "El Bosco",
            "16. ¿Qué movimiento artístico se desarrolló en Francia a finales del siglo XIX y se caracteriza por el uso de colores vivos y pinceladas visibles?": "Impresionismo",
            "17. ¿Cuál es la pintura más famosa de Leonardo da Vinci?": "La Mona Lisa",
            "18. ¿Quién es el pintor de 'Saturno devorando a su hijo'?": "Goya",
            "19. ¿Qué pintor es conocido por su estilo surrealista y sus relojes derretidos?": "Dalí",
            "20. ¿Quién es el pintor español asociado con el movimiento surrealista y conocido por su técnica de 'Automatismo psíquico'?": "Miró",
            "21. ¿Cuál es el museo en Madrid que alberga una extensa colección de arte contemporáneo español, incluidas obras de Picasso y Dalí?": "Museo Reina Sofía",
            "22. ¿Quién es el pintor español famoso por sus representaciones de escenas religiosas y su uso magistral de la luz y el color?": "El Greco",
            "23. ¿Cuál es el nombre del movimiento artístico que surgió en Francia a principios del siglo XX y se caracteriza por la representación de la realidad de manera distorsionada?": "Cubismo",
            "24. ¿Cuál es la obra maestra de Diego Velázquez que muestra a la familia real española en un retrato informal?": "Las Meninas",
            "25. ¿Cuál es el movimiento artístico que se caracteriza por la representación de objetos de manera realista y detallada?": "Hiperrealismo"
        }
        return art

    def historia():
        history = {
            "1. ¿Quién fue el líder de la expedición que llevó al descubrimiento de América en 1492?": "Colón",
            "2. ¿Cuándo comenzó la Reconquista en la península ibérica?": "711",
            "3. ¿Qué reyes españoles financiaron el viaje de Cristóbal Colón en 1492?": "Los Reyes Católicos",
            "4. ¿Qué evento histórico ocurrió en 1492 que llevó a la expulsión de los judíos de España?": "La Reconquista de Granada",
            "5. ¿Cuándo se estableció el primer régimen parlamentario en España?": "1812,",
            "6. ¿Qué líder militar español conquistó el Imperio Inca en el siglo XVI?": "Pizarro",
            "7. ¿Cuándo terminó la Guerra Civil Española?": "1939",
            "8. ¿Qué dictador español gobernó España desde 1939 hasta su muerte en 1975?": "Franco",
            "9. ¿Cuál fue la última colonia española en América en obtener su independencia?": "Cuba",
            "10. ¿Quién fue el primer rey de España después de la caída del régimen franquista?": "Juan Carlos I",
            "11. ¿Cuándo se proclamó la Segunda República Española?": "En 1931",
            "12. ¿Quién fue el líder de los carlistas durante el siglo XIX en España?": "Carlos María Isidro de Borbón",
            "13. ¿Cuándo se celebraron los Juegos Olímpicos en Barcelona?": "1992",
            "14. ¿Cuándo se firmó el Tratado de Tordesillas, que dividió el mundo entre España y Portugal?": "1494",
            "15. ¿Quién fue el líder del gobierno republicano durante la Guerra Civil Española?": "Azaña",
            "16. ¿Cuál fue el nombre del tratado que puso fin a la Guerra de Sucesión Española y reconoció a Felipe V como rey de España en 1713?": "Tratado de Utrecht",
            "17. ¿Cuál fue el nombre de la expedición liderada por Fernando de Magallanes que llevó a la primera circunnavegación del globo?": "La expedición de Magallanes-Elcano",
            "18. ¿Cuándo comenzó la colonización española de América?": "1492",
            "19. ¿Quién fue el rey español que construyó el Escorial como un monumento a la batalla de San Quintín?": "Felipe II",
            "20. ¿Cuándo se llevó a cabo la invasión de España por parte de Napoleón Bonaparte?": "1808",
            "21. ¿Quién fue el primer presidente del gobierno de la Segunda República Española en 1931?": "Alcalá-Zamora",
            "22. ¿Cuándo se celebró la Exposición Universal de Sevilla?": "1992",
            "23. ¿Qué acontecimiento histórico marcó el fin de la dominación musulmana en la península ibérica?": "La conquista de Granada",
            "24. ¿Cuál fue la ciudad que se convirtió en la capital de Al-Andalus durante el periodo del Califato de Córdoba?": "Córdoba",
            "25. ¿Cuándo se proclamó la Constitución Española que estableció la democracia parlamentaria en España?": "1978"
    }
        return history

    def literatura():
        literature = {
            "1. ¿Quién escribió 'Cien años de soledad'?": "García Márquez",
            "2. ¿Quién es el autor de 'Don Quijote de la Mancha'?": "Cervantes",
            "3. ¿Qué autor escribió '1984' y 'Rebelión en la granja'?": "Orwell",
            "4. ¿Quién escribió 'Orgullo y prejuicio'?": "Austen",
            "5. ¿Cuál es el autor de 'La metamorfosis'?": "Kafka",
            "6. ¿Qué autor español escribió 'Fortunata y Jacinta'?": "Pérez Galdós",
            "7. ¿Quién escribió 'La casa de Bernarda Alba'?": "García Lorca",
            "8. ¿Quién es el autor de 'San Manuel Bueno, mártir'?": "Unamuno",
            "9. ¿Qué autor argentino escribió 'Ficciones'?": "Borges",
            "10. ¿Quién es el autor de 'El Lazarillo de Tormes'?": "Anónimo",
            "11. ¿Cuál es el autor de 'La Odisea'?": "Homero",
            "12. ¿Quién es el autor de 'Ulises'?": "Joyce",
            "13. ¿Qué escritor inglés es conocido por sus obras de teatro y sonetos?": "Shakespeare",
            "14. ¿Quién escribió 'El retrato de Dorian Gray'?": "Wilde",
            "15. ¿Qué autor escribió 'Cumbres Borrascosas'?": "Brontë",
            "16. ¿Quién es el autor de 'Crimen y castigo'?": "Dostoyevski",
            "17. ¿Qué autor escribió 'Las aventuras de Huckleberry Finn'?": "Twain",
            "18. ¿Quién es el autor de 'Alicia en el país de las maravillas'?": "Carroll",
            "19. ¿Qué autor escribió 'El señor de los anillos'?": "Tolkien",
            "20. ¿Quién es el autor de 'Jane Eyre'?": "Brontë",
            "21. ¿Qué autor japonés escribió 'Kafka en la orilla'?": "Murakami",
            "22. ¿Quién es la autora de 'La casa de los espíritus'?": "Allende",
            "23. ¿Qué autor escribió 'El viejo y el mar'?": "Hemingway",
            "24. ¿Qué autor español escribió 'Don Juan Tenorio'?": "Zorrilla",
            "25. ¿Qué autora canadiense escribió 'El cuento de la criada'?": "Atwood",
        }
        return literature

    def ingles():
        english = {
            "1. ¿Cómo se dice 'libro' en inglés?": "book",
            "2. ¿Cómo se dice 'casa' en inglés?": "house",
            "3. ¿Cómo se dice 'escuela' en inglés?": "school",
            "4. ¿Cómo se dice 'perro' en inglés?": "dog",
            "5. ¿Cómo se dice 'gato' en inglés?": "cat",
            "6. ¿Cómo se dice 'familia' en inglés?": "family",
            "7. ¿Cómo se dice 'amigo' en inglés?": "friend",
            "8. ¿Cómo se dice 'ciudad' en inglés?": "city",
            "9. ¿Cómo se dice 'comida' en inglés?": "food",
            "10. ¿Cómo se dice 'agua' en inglés?": "water",
            "11. ¿Cómo se dice 'amor' en inglés?": "love",
            "12. ¿Cómo se dice 'trabajo' en inglés?": "work",
            "13. ¿Cómo se dice 'felicidad' en inglés?": "happiness",
            "14. ¿Cómo se dice 'música' en inglés?": "music",
            "15. ¿Cómo se dice 'película' en inglés?": "movie",
            "16. ¿Cómo se dice 'playa' en inglés?": "beach",
            "17. ¿Cómo se dice 'montaña' en inglés?": "mountain",
            "18. ¿Cómo se dice 'sol' en inglés?": "sun",
            "19. ¿Cómo se dice 'luna' en inglés?": "moon",
            "20. ¿Cómo se dice 'estrella' en inglés?": "star",
            "21. ¿Cómo se dice 'noche' en inglés?": "night",
            "22. ¿Cómo se dice 'día' en inglés?": "day",
            "23. ¿Cómo se dice 'verano' en inglés?": "summer",
            "24. ¿Cómo se dice 'invierno' en inglés?": "winter",
            "25. ¿Cómo se dice 'primavera' en inglés?": "spring"
        }
        return english

    def geografia():
        geo = {
            "1. ¿Cuál es el río más largo del mundo?": "Amazonas",
            "2. ¿Cuál es la montaña más alta del mundo?": "Monte Everest",
            "3. ¿Cuál es el desierto más grande del mundo?": "Sahara",
            "4. ¿Cuál es el país más grande del mundo?": "Rusia",
            "5. ¿Cuál es el océano más grande del mundo?": "Océano Pacífico",
            "6. ¿Cuál es el lago más grande del mundo?": "Mar Caspio",
            "7. ¿Cuál es el país más pequeño del mundo?": "Ciudad del Vaticano",
            "8. ¿Cuál es la capital de Australia?": "Canberra",
            "9. ¿En qué continente se encuentra Egipto?": "África",
            "10. ¿Cuál es la capital de Canadá?": "Ottawa",
            "11. ¿En qué continente se encuentra Brasil?": "América del Sur",
            "12. ¿Cuál es la capital de Japón?": "Tokio",
            "13. ¿En qué país se encuentra la Torre Eiffel?": "Francia",
            "14. ¿Cuál es la capital de Argentina?": "Buenos Aires",
            "15. ¿Cuál es el país con la mayor población del mundo?": "China",
            "16. ¿En qué continente se encuentra España?": "Europa",
            "17. ¿Cuál es la capital de Italia?": "Roma",
            "18. ¿En qué país se encuentra el río Nilo?": "Egipto",
            "19. ¿Cuál es la capital de México?": "Ciudad de México",
            "20. ¿En qué continente se encuentra la Antártida?": "Antártida",
            "21. ¿Cuál es la capital de Rusia?": "Moscú",
            "22. ¿En qué país se encuentra el Monte Kilimanjaro?": "Tanzania",
            "23. ¿Cuál es el país más grande de América del Sur?": "Brasil",
            "24. ¿Cuál es la capital de India?": "Nueva Delhi",
            "25. ¿En qué continente se encuentra Alemania?": "Europa"
        }
        return geo

    def cultura():
        culture = {
            "1. ¿Quién fue el primer presidente de los Estados Unidos?": "Washington",
            "2. ¿Cuál es el idioma más hablado en el mundo?": "Chino mandarín",
            "3. ¿En qué año llegó el hombre a la Luna?": "1969",
            "4. ¿Cuál es la capital de Francia?": "París",
            "5. ¿Quién escribió 'Hamlet'?": "Shakespeare",
            "6. ¿Cuál es la moneda oficial de Japón?": "Yen",
            "7. ¿En qué país se encuentra Machu Picchu?": "Perú",
            "8. ¿Cuál es el elemento químico con el símbolo O?": "Oxígeno",
            "9. ¿Qué artista pintó la Mona Lisa?": "Leonardo da Vinci",
            "10. ¿Cuál es el océano más pequeño del mundo?": "Océano Ártico",
            "11. ¿En qué año comenzó la Primera Guerra Mundial?": "1914",
            "12. ¿Cuál es el país más poblado de África?": "Nigeria",
            "13. ¿Quién es el autor de 'Cien años de soledad'?": "García Márquez",
            "14. ¿Cuál es el planeta más grande del sistema solar?": "Júpiter",
            "15. ¿Quién fue la primera mujer en ganar un Premio Nobel?": "Curie",
            "16. ¿Qué ciudad es conocida como la Gran Manzana?": "Nueva York",
            "17. ¿Cuál es el animal terrestre más rápido del mundo?": "Guepardo",
            "18. ¿En qué país se encuentra la torre de Pisa?": "Italia",
            "19. ¿Cuál es el himno nacional de Francia?": "La Marsellesa",
            "20. ¿Qué país es conocido como la tierra del sol naciente?": "Japón",
            "21. ¿Quién escribió '1984'?": "Orwell",
            "22. ¿Cuál es el libro sagrado del Islam?": "Corán",
            "23. ¿En qué año se disolvió la Unión Soviética?": "1991",
            "24. ¿Qué pintor es conocido por cortar una parte de su oreja?": "van Gogh",
            "25. ¿Cuál es el metal más ligero?": "Litio"
        }
        return culture
    
    mark = 1
    points = 0

    print('¡BIENVENIDO PREGUNTAS Y RESPUESTAS!', flush=True)
    print(' ')
    print('''¡Las normas del juego son simples!
        Tendrás que elegir entre diferentes temáticas:
        1. HISTORIA
        2. ARTE
        3. LITERATURA
        4. INGLÉS
        5. GEOGRAFÍA
        6. CULTURA GENERAL
        ¡Responde a las preguntas!
        En las preguntas:
        - Si se pide un nombre, sólo se pide el apellido. Por ejemplo: ¿Quién escribió el Quijote? Cervantes
        - Los años deben escribirse directamente y numéricamente: ¿Cuándo se celebró la Exposición Universal de Sevilla? 1992
        Al final recibirás un ranking para ver tu nivel sobre el tema.
        
        ¡Mucha suerte!''')
    print('----')

    theme = input('¿Sobre qué quieres que te preguntemos? Escribe el número correspondiente. Por ejemplo: 1')

    while mark <= 10:
        if int(theme) == 1:
            theme_choice = historia()
            question, answer = choices(list(theme_choice.items()), k=1)[0]
            user = (input(question))
            theme_choice.pop(question)
        elif int(theme) == 2:
            theme_choice = arte()
            question, answer = choices(list(theme_choice.items()), k=1)[0]
            user = (input(question))
            theme_choice.pop(question)
        elif int(theme) == 3:
            theme_choice = literatura()
            question, answer = choices(list(theme_choice.items()), k=1)[0]
            user = (input(question))
            theme_choice.pop(question)
        elif int(theme) == 4:
            theme_choice = ingles()
            question, answer = choices(list(theme_choice.items()), k=1)[0]
            user = (input(question))
            theme_choice.pop(question)
        elif int(theme) == 5:
            theme_choice = geografia()
            question, answer = choices(list(theme_choice.items()), k=1)[0]
            user = (input(question))
            theme_choice.pop(question)
        elif int(theme) == 6:
            theme_choice = cultura()
            question, answer = choices(list(theme_choice.items()), k=1)[0]
            user = (input(question))
            theme_choice.pop(question)
        else:
            print("Tema no válido")
            break

        if user.lower() == answer.lower():
            print(f'¡Genial! Efectivamente la respuesta era {answer}')
            mark += 1
            points += 1
        else:
            print(f'¡Has fallado! La respuesta era {answer}')
            mark += 1

    if points == 10:
        print(f'Has conseguido {points} puntos. ¡Eres un máquina!')
    elif points == 0:
        print(f'Has conseguido {points} puntos. ¡Vuelve a intentarlo!')
    elif points > 0 and points < 4:
        print(f'Has conseguido {points} puntos. ¡Vuelve a intentarlo!')
    elif points >= 4 and points <= 6:
        print(f'Has conseguido {points} puntos. No está mal, aún puedes mejorar ;)')
    elif points >= 7 and points <= 9:
        print(f'Has conseguido {points} puntos. ¡Está muy bien!')