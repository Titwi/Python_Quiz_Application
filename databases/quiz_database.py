### quiz_data is a dictionary, which contains four keys. Each theme contains a list of question dictionaries
### In addition, each question dictionary contains:a string (question), a list of strings (options), and a string (correct_answer)

quiz_questions = {
    "General Knowledge": [
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Blue whale", "African elephant", "Hippopotamus", "Giraffe"],
            "correct_answer": "Blue whale"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["Avocado", "Tomato", "Cucumber", "Lettuce"],
            "correct_answer": "Avocado"
        },
        {
            "question": "Who is known as the 'Father of the United States' and the first President of the country?",
            "options": ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"],
            "correct_answer": "George Washington",
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Vincent van Gogh"],
            "correct_answer": "Leonardo da Vinci",
        },
        {
            "question": "What is the name of the largest ocean on Earth?",
            "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
            "correct_answer": "Pacific Ocean",
        },
        {
            "question": "What famous music group was John Lennon a part of before pursuing a solo career?",
            "options": ["The Beatles", "The Rolling Stones", "Pink Floyd", "The Who"],
            "correct_answer": "The Beatles",
        },
        {
            "question": "In the story of Snow White, how many dwarfs are there?",
            "options": ["Seven", "Five", "Six", "Eight"],
            "correct_answer": "Seven",
        },
        {
            "question": "Who is the king of the gods in Greek mythology?",
            "options": ["Zeus", "Poseidon", "Hades", "Apollo"],
            "correct_answer": "Zeus",
        },
        {
            "question": "What do bees collect to make honey?",
            "options": ["Nectar", "Pollen", "Sap", "Water"],
            "correct_answer": "Nectar",
        },
        {
            "question": "In what galaxy is our solar system located?",
            "options": ["Milky Way", "Andromeda", "Triangulum", "Whirlpool Galaxy"],
            "correct_answer": "Milky Way",
        },
        {
            "question": "Which planet is known as the 'Blue Planet'?",
            "options": ["Earth", "Neptune", "Uranus", "Venus"],
            "correct_answer": "Earth",
        },
        {
            "question": "Which geometric shape has four equal sides and four right angles?",
            "options": ["Square", "Rectangle", "Rhombus", "Parallelogram"],
            "correct_answer": "Square",
        },
        {
            "question": "What is the main ingredient in the dish sushi?",
            "options": ["Rice", "Salmon", "Seaweed", "Tuna"],
            "correct_answer": "Rice",
        },
        {
            "question": "What is the rarest blood type among humans?",
            "options": ["AB-negative", "O-negative", "AB-positive", "A-negative"],
            "correct_answer": "AB-negative",
        },
        {
            "question": "How many wives did King Henry VIII have?",
            "options": ["Six", "Four", "Five", "Seven"],
            "correct_answer": "Six",
        },
        {
            "question": "In what year and in which city were the first modern Olympic Games held?",
            "options": ["1896 in Athens, Greece", "1900 in Paris, France", "1888 in London, England",
                        "1892 in Rome, Italy"],
            "correct_answer": "1896 in Athens, Greece",
        },
        {
            "question": "Who is the Greek god of war and son of Zeus and Hera?",
            "options": ["Ares", "Hermes", "Hephaestus", "Dionysus"],
            "correct_answer": "Ares",
        },
        {
            "question": "What is the chemical symbol for the element mercury?",
            "options": ["Hg", "Mr", "Mc", "Me"],
            "correct_answer": "Hg",
        },
        {
            "question": "What is the name of the largest moon of Jupiter?",
            "options": ["Ganymede", "Io", "Europa", "Callisto"],
            "correct_answer": "Ganymede",
        },
        {
            "question": "In what year did the Berlin Wall fall?",
            "options": ["1989", "1987", "1990", "1991"],
            "correct_answer": "1989",
        },
        {
            "question": "What is the capital city of Brazil?",
            "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
            "correct_answer": "Brasília",
        },
        {
            "question": "Who wrote 'Pride and Prejudice'?",
            "options": ["Jane Austen", "Charlotte Brontë", "Emily Brontë", "Mary Shelley"],
            "correct_answer": "Jane Austen",
        },
        {
            "question": "Who is known as the 'Father of Modern Physics'?",
            "options": ["Albert Einstein", "Isaac Newton", "Niels Bohr", "Galileo Galilei"],
            "correct_answer": "Albert Einstein",
        },
        {
            "question": "Which mountain range is the longest in the world?",
            "options": ["The Andes", "The Rockies", "The Himalayas", "The Alps"],
            "correct_answer": "The Andes",
        },
        {
            "question": "What is the largest island in the world?",
            "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"],
            "correct_answer": "Greenland",
        },
        {
            "question": "What is the chemical symbol for silver?",
            "options": ["Ag", "Si", "Au", "Sr"],
            "correct_answer": "Ag",
        },
        {
            "question": "Who painted 'The Persistence of Memory'?",
            "options": ["Salvador Dali", "Pablo Picasso", "Henri Matisse", "Claude Monet"],
            "correct_answer": "Salvador Dali",
        },
        {
            "question": "What is the largest bone in the human body?",
            "options": ["Femur", "Tibia", "Humerus", "Pelvis"],
            "correct_answer": "Femur",
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1912", "1905", "1914", "1920"],
            "correct_answer": "1912",
        },
        {
            "question": "What is the capital city of Argentina?",
            "options": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza"],
            "correct_answer": "Buenos Aires",
        },
        {
            "question": "Who painted the famous artwork 'The Last Supper'?",
            "options": ["Leonardo da Vinci", "Raphael", "Michelangelo", "Sandro Botticelli"],
            "correct_answer": "Leonardo da Vinci",
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1945", "1944", "1939", "1950"],
            "correct_answer": "1945",
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["Japanese Yen", "Japanese Dollar", "Japanese Won", "Japanese Peso"],
            "correct_answer": "Japanese Yen",
        },

    ],

    "History & Geography": [
        {
            "question": "What is the name of the thin and long country that spans more than half of the western coast of South America?",
            "options": ["Chile", "Peru", "Argentina", "Colombia"],
            "correct_answer": "Chile",
        },
        {
            "question": "Which American state is the largest by area?",
            "options": ["Alaska", "Texas", "California", "Montana"],
            "correct_answer": "Alaska",
        },
        {
            "question": "Which two countries share the longest international border?",
            "options": ["Canada and the USA", "Russia and China", "Argentina and Chile", "USA and Mexico"],
            "correct_answer": "Canada and the USA",
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"],
            "correct_answer": "Vatican City",
        },
        {
            "question": "Which continent is the largest?",
            "options": ["Asia", "Africa", "North America", "Europe"],
            "correct_answer": "Asia",
        },
        {
            "question": "Which of the Seven Wonders is located in Egypt?",
            "options": ["The Pyramids of Giza", "The Hanging Gardens of Babylon", "The Statue of Zeus at Olympia",
                        "The Colossus of Rhodes"],
            "correct_answer": "The Pyramids of Giza",
        },
        {
            "question": "What is the capital of New Zealand?",
            "options": ["Wellington", "Auckland", "Christchurch", "Hamilton"],
            "correct_answer": "Wellington",
        },
        {
            "question": "Which desert is the largest in the world?",
            "options": ["The Sahara Desert", "The Gobi Desert", "The Arabian Desert", "The Kalahari Desert"],
            "correct_answer": "The Sahara Desert",
        },
        {
            "question": "What is the name of the world’s longest river?",
            "options": ["The Nile", "The Amazon", "The Yangtze", "The Mississippi"],
            "correct_answer": "The Nile",
        },
        {
            "question": "Which city in India would you find the Taj Mahal in?",
            "options": ["Agra", "Delhi", "Jaipur", "Mumbai"],
            "correct_answer": "Agra",
        },
        {
            "question": "What is the largest island in the Mediterranean Sea?",
            "options": ["Sicily", "Sardinia", "Cyprus", "Crete"],
            "correct_answer": "Sicily",
        },
        {
            "question": "Which river runs through the Grand Canyon?",
            "options": ["Colorado River", "Missouri River", "Rio Grande", "Columbia River"],
            "correct_answer": "Colorado River",
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["Japan", "China", "South Korea", "Thailand"],
            "correct_answer": "Japan",
        },
        {
            "question": "Which African country is known as the 'Pearl of Africa'?",
            "options": ["Uganda", "Kenya", "Tanzania", "Ghana"],
            "correct_answer": "Uganda",
        },
        {
            "question": "Which Asian river is considered the longest?",
            "options": ["Yangtze River", "Mekong River", "Ganges River", "Yellow River"],
            "correct_answer": "Yangtze River",
        },
        {
            "question": "By what name were the Egyptian kings and rulers known?",
            "options": ["Pharaohs", "Sultans", "Emirs", "Caesars"],
            "correct_answer": "Pharaohs",
        },
        {
            "question": "How many Pyramids of Giza were made?",
            "options": ["Three", "Four", "Five", "Two"],
            "correct_answer": "Three",
        },
        {
            "question": "Which queen was Julius Caesar involved with?",
            "options": ["Cleopatra", "Nefertiti", "Elizabeth I", "Catherine the Great"],
            "correct_answer": "Cleopatra",
        },
        {
            "question": "Where did the Franks settle after defeating the Romans?",
            "options": ["Gaul", "Iberia", "Britannia", "Italia"],
            "correct_answer": "Gaul",
        },
        {
            "question": "How long did the Middle Ages last?",
            "options": ["About 1000 years", "About 500 years", "About 1500 years", "About 700 years"],
            "correct_answer": "About 1000 years",
        },
        {
            "question": "Which religion dominated the Middle Ages in Europe?",
            "options": ["Catholicism", "Islam", "Orthodox Christianity", "Protestantism"],
            "correct_answer": "Catholicism",
        },
        {
            "question": "In which year did World War I begin?",
            "options": ["1914", "1912", "1918", "1905"],
            "correct_answer": "1914",
        },
        {
            "question": "In which country was Adolf Hitler born?",
            "options": ["Austria", "Germany", "Switzerland", "Poland"],
            "correct_answer": "Austria",
        },
        {
            "question": "John F. Kennedy was assassinated in which city?",
            "options": ["Dallas", "Washington, D.C.", "Los Angeles", "New York City"],
            "correct_answer": "Dallas",
        },
        {
            "question": "On Sunday 18th June 1815, which famous battle took place?",
            "options": ["The Battle of Waterloo", "The Battle of Trafalgar", "The Battle of Leipzig",
                        "The Battle of Austerlitz"],
            "correct_answer": "The Battle of Waterloo",
        },
        {
            "question": "What event marked the beginning of World War I?",
            "options": ["The assassination of Archduke Franz Ferdinand", "The invasion of Belgium",
                        "The sinking of the Lusitania", "The Zimmerman Telegram"],
            "correct_answer": "The assassination of Archduke Franz Ferdinand",
        },
        {
            "question": "Who was the leader of the Soviet Union during World War II?",
            "options": ["Joseph Stalin", "Vladimir Lenin", "Nikita Khrushchev", "Leon Trotsky"],
            "correct_answer": "Joseph Stalin",
        },
        {
            "question": "What ancient wonder was located in the city of Alexandria in Egypt?",
            "options": ["The Lighthouse of Alexandria", "The Pyramids of Giza", "The Hanging Gardens of Babylon",
                        "The Temple of Artemis"],
            "correct_answer": "The Lighthouse of Alexandria",
        },
        {
            "question": "Who was the famous nurse known for her work during the Crimean War and considered the founder of modern nursing?",
            "options": ["Florence Nightingale", "Clara Barton", "Mary Seacole", "Elizabeth Blackwell"],
            "correct_answer": "Florence Nightingale",
        },
        {
            "question": "What was the name of the ship that brought the Pilgrims to America in 1620?",
            "options": ["The Mayflower", "The Santa Maria", "The Discovery", "The Endeavour"],
            "correct_answer": "The Mayflower",
        },

    ],
    "Modern Music & Literature": [
        {
            "question": "What was the name of the group Justin Timberlake used to be part of?",
            "options": ["*NSYNC", "Backstreet Boys", "New Kids on the Block", "Westlife"],
            "correct_answer": "*NSYNC",
        },
        {
            "question": "What was the name of the rock band formed by Jimmy Page?",
            "options": ["Led Zeppelin", "Deep Purple", "The Who", "Cream"],
            "correct_answer": "Led Zeppelin",
        },
        {
            "question": "Which country did AC/DC originate in?",
            "options": ["Australia", "United Kingdom", "United States", "Canada"],
            "correct_answer": "Australia",
        },
        {
            "question": "What genre of music did Taylor Swift start in?",
            "options": ["Country", "Pop", "Rock", "R&B"],
            "correct_answer": "Country",
        },
        {
            "question": "Who was the lead singer of the iconic '80s band Culture Club?",
            "options": ["Boy George", "George Michael", "Simon Le Bon", "Morrissey"],
            "correct_answer": "Boy George",
        },
        {
            "question": "Which name is rapper Sean Combs better known by?",
            "options": ["P. Diddy", "Lil Wayne", "Dr. Dre", "Ice Cube"],
            "correct_answer": "P. Diddy",
        },
        {
            "question": "Which musical legend is Jay-Z married to?",
            "options": ["Beyoncé", "Rihanna", "Alicia Keys", "Janet Jackson"],
            "correct_answer": "Beyoncé",
        },
        {
            "question": "How many Grammys does John Legend have?",
            "options": ["Ten", "Five", "Seven", "Twelve"],
            "correct_answer": "Ten",
        },
        {
            "question": "Which British girl group had a member by the name of Mel B?",
            "options": ["Spice Girls", "Little Mix", "All Saints", "Girls Aloud"],
            "correct_answer": "Spice Girls",
        },
        {
            "question": "Who is often referred to as the 'King of Pop' and is known for iconic hits like 'Thriller' and 'Billie Jean'?",
            "options": ["Michael Jackson", "Elvis Presley", "Prince", "Stevie Wonder"],
            "correct_answer": "Michael Jackson",
        },

        {
            "question": "What author became famous for his six-volume biography of Abraham Lincoln?",
            "options": ["Carl Sandburg", "Doris Kearns Goodwin", "David McCullough", "Shelby Foote"],
            "correct_answer": "Carl Sandburg",
        },
        {
            "question": "Who wrote 'The Old Man and the Sea' and is considered one of the greatest writers of the 20th century?",
            "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner"],
            "correct_answer": "Ernest Hemingway",
        },
        {
            "question": "What Danish author is considered by many to be the most prolific fairy tale writer?",
            "options": ["Hans Christian Andersen", "J.R.R. Tolkien", "C.S. Lewis", "The Brothers Grimm"],
            "correct_answer": "Hans Christian Andersen",
        },
        {
            "question": "Who is the writer of 'The Merchant of Venice'?",
            "options": ["William Shakespeare", "Christopher Marlowe", "Ben Jonson", "Thomas Kyd"],
            "correct_answer": "William Shakespeare",
        },
        {
            "question": "'The Adventures of Sherlock Holmes' was written by which writer?",
            "options": ["Arthur Conan Doyle", "Agatha Christie", "G.K. Chesterton", "Edgar Allan Poe"],
            "correct_answer": "Arthur Conan Doyle",
        },
        {
            "question": "What is the name of the fourth book in the Harry Potter series?",
            "options": ["Harry Potter and the Goblet of Fire", "Harry Potter and the Prisoner of Azkaban",
                        "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince"],
            "correct_answer": "Harry Potter and the Goblet of Fire",
        },
        {
            "question": "The Hunger Games series was written by which author?",
            "options": ["Suzanne Collins", "Veronica Roth", "J.K. Rowling", "Stephenie Meyer"],
            "correct_answer": "Suzanne Collins",
        },
        {
            "question": "Which country is Aesop's Fables believed to originate in?",
            "options": ["Greece", "Italy", "Egypt", "India"],
            "correct_answer": "Greece",
        },
        {
            "question": "In Herman Melville’s novel 'Moby-Dick', who was the loyal, reasonable first mate?",
            "options": ["Starbuck", "Queequeg", "Ishmael", "Stubb"],
            "correct_answer": "Starbuck",
        },
        {
            "question": "The book 'The Da Vinci Code' was written by whom?",
            "options": ["Dan Brown", "James Patterson", "John Grisham", "Tom Clancy"],
            "correct_answer": "Dan Brown",
        },
        {
            "question": "Who wrote the novel 'One Hundred Years of Solitude'?",
            "options": ["Gabriel García Márquez", "Mario Vargas Llosa", "Jorge Luis Borges", "Isabel Allende"],
            "correct_answer": "Gabriel García Márquez",
        },
        {
            "question": "Who wrote the classic children’s book 'Charlotte’s Web'?",
            "options": ["E.B. White", "Roald Dahl", "Beatrix Potter", "A.A. Milne"],
            "correct_answer": "E.B. White",
        },
        {
            "question": "What is the title of the classic Greek epic attributed to Homer, telling the story of the Trojan War?",
            "options": ["The Iliad", "The Odyssey", "The Aeneid", "Argonautica"],
            "correct_answer": "The Iliad",
        },
        {
            "question": "What is the name of the protagonist in Jules Verne’s 'Twenty Thousand Leagues Under the Sea'?",
            "options": ["Captain Nemo", "Phileas Fogg", "Professor Aronnax", "Captain Ahab"],
            "correct_answer": "Captain Nemo",
        },
        {
            "question": "Who wrote the gothic novel 'Frankenstein; or, The Modern Prometheus'?",
            "options": ["Mary Shelley", "Bram Stoker", "Edgar Allan Poe", "Ann Radcliffe"],
            "correct_answer": "Mary Shelley",
        },
    ],
    "Games & Riddles": [
        {
            "question": "Where did backgammon originate?",
            "options": ["Persia", "Egypt", "Greece", "China"],
            "correct_answer": "Persia",
        },
        {
            "question": "How many cards are there in a deck of Uno?",
            "options": ["108", "52", "100", "96"],
            "correct_answer": "108",
        },
        {
            "question": "In which board game do you try to solve a murder?",
            "options": ["Clue", "Monopoly", "Scrabble", "Risk"],
            "correct_answer": "Clue",
        },
        {
            "question": "In chess, the queen has the combined movement of which two pieces?",
            "options": ["Bishop and rook", "Knight and rook", "Bishop and knight", "King and rook"],
            "correct_answer": "Bishop and rook",
        },
        {
            "question": "Which of these games includes the phrase 'Do not pass go, do not collect $200'?",
            "options": ["Monopoly", "Clue", "The Game of Life", "Risk"],
            "correct_answer": "Monopoly",
        },
        {
            "question": "The video game 'Happy Feet' features what animals?",
            "options": ["Penguins", "Dolphins", "Polar bears", "Seals"],
            "correct_answer": "Penguins",
        },
        {
            "question": "What classic video game requires you to eat all the dots throughout a maze?",
            "options": ["Pac-Man", "Space Invaders", "Tetris", "Donkey Kong"],
            "correct_answer": "Pac-Man",
        },
        {
            "question": "Which Street Fighter character wears a white outfit and a red headband?",
            "options": ["Ryu", "Ken", "Guile", "Chun-Li"],
            "correct_answer": "Ryu",
        },
        {
            "question": "'Astro Boy' is what genre of video game?",
            "options": ["Action", "Puzzle", "Racing", "Sports"],
            "correct_answer": "Action",
        },
        {
            "question": "What sport is featured in the video game 'FIFA'?",
            "options": ["Football", "Basketball", "Rugby", "Baseball"],
            "correct_answer": "Football",
        },
        {
            "question": "What type of game is Axie Infinity?",
            "options": ["Blockchain game", "Racing game", "First-person shooter", "Puzzle game"],
            "correct_answer": "Blockchain game",
        },
        {
            "question": "In 'The Farmer in the Dell', what did the cat take?",
            "options": ["The rat", "The cheese", "The dog", "The cow"],
            "correct_answer": "The rat",
        },
        {
            "question": "What did the 'Itsy Bitsy Spider' climb up?",
            "options": ["The waterspout", "The tree", "The wall", "The fence"],
            "correct_answer": "The waterspout",
        },
        {
            "question": "What did the 'Three Little Kittens' lose?",
            "options": ["Their mittens", "Their hats", "Their shoes", "Their toys"],
            "correct_answer": "Their mittens",
        },
        {
            "question": "How many bags of wool did 'Baa Baa Black Sheep' have?",
            "options": ["Three", "Two", "Four", "One"],
            "correct_answer": "Three",
        },
        {
            "question": "Why did Jack and Jill go up the hill?",
            "options": ["To fetch a pail of water", "To fly a kite", "To pick some flowers", "To see the view"],
            "correct_answer": "To fetch a pail of water",
        },
        {
            "question": "How can a man go eight days without sleep?",
            "options": ["By sleeping during the night", "By drinking lots of coffee", "By taking naps at work",
                        "By never closing his eyes"],
            "correct_answer": "By sleeping during the night",
        },
        {
            "question": "How can you drop a raw egg on the concrete floor without cracking it?",
            "options": ["The egg won’t crack the concrete floor", "Drop it from a very low height",
                        "Wrap it in cloth first", "Place a cushion underneath"],
            "correct_answer": "The egg won’t crack the concrete floor",
        },
        {
            "question": "If there are six apples and you take away four, how many do you have?",
            "options": ["Four", "Two", "Six", "None"],
            "correct_answer": "Four",
        },
        {
            "question": "What goes up and down, but still remains in the same place?",
            "options": ["Stairs", "A balloon", "A yo-yo", "A seesaw"],
            "correct_answer": "Stairs",
        },
        {
            "question": "What gets wetter and wetter the more it dries?",
            "options": ["A towel", "A sponge", "A river", "A cloud"],
            "correct_answer": "A towel"
        },

    ],

}




