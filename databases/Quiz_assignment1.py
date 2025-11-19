### quiz_data is a dictionary, which contains four keys. Each theme contains a list of question dictionaries
### In addition, each question dictionary contains:a string (question), a list of strings (options), and a string (answer)

quiz_questions = {
    "General Knowledge": [
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Blue whale", "African elephant", "Hippopotamus", "Giraffe"],
            "answer": "options"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["Avocado", "Tomato", "Cucumber", "Lettuce"],
            "answer": "options"
        },
        {
            "question": "Who is known as the 'Father of the United States' and the first President of the country?",
            "options": ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"],
            "answer": "options",
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Vincent van Gogh"],
            "answer": "options",
        },
        {
            "question": "What is the name of the largest ocean on Earth?",
            "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
            "answer": "options",
        },
        {
            "question": "What famous music group was John Lennon a part of before pursuing a solo career?",
            "options": ["The Beatles", "The Rolling Stones", "Pink Floyd", "The Who"],
            "answer": "options",
        },
        {
            "question": "In the story of Snow White, how many dwarfs are there?",
            "options": ["Seven", "Five", "Six", "Eight"],
            "answer": "options",
        },
        {
            "question": "Who is the king of the gods in Greek mythology?",
            "options": ["Zeus", "Poseidon", "Hades", "Apollo"],
            "answer": "options",
        },
        {
            "question": "What do bees collect to make honey?",
            "options": ["Nectar", "Pollen", "Sap", "Water"],
            "answer": "options",
        },
        {
            "question": "In what galaxy is our solar system located?",
            "options": ["Milky Way", "Andromeda", "Triangulum", "Whirlpool Galaxy"],
            "answer": "options",
        },
        {
            "question": "Which planet is known as the 'Blue Planet'?",
            "options": ["Earth", "Neptune", "Uranus", "Venus"],
            "answer": "options",
        },
        {
            "question": "Which geometric shape has four equal sides and four right angles?",
            "options": ["Square", "Rectangle", "Rhombus", "Parallelogram"],
            "answer": "options",
        },
        {
            "question": "What is the main ingredient in the dish sushi?",
            "options": ["Rice", "Salmon", "Seaweed", "Tuna"],
            "answer": "options",
        },
        {
            "question": "What is the rarest blood type among humans?",
            "options": ["AB-negative", "O-negative", "AB-positive", "A-negative"],
            "answer": "options",
        },
        {
            "question": "How many wives did King Henry VIII have?",
            "options": ["Six", "Four", "Five", "Seven"],
            "answer": "options",
        },
        {
            "question": "In what year and in which city were the first modern Olympic Games held?",
            "options": ["1896 in Athens, Greece", "1900 in Paris, France", "1888 in London, England",
                        "1892 in Rome, Italy"],
            "answer": "options",
        },
        {
            "question": "Who is the Greek god of war and son of Zeus and Hera?",
            "options": ["Ares", "Hermes", "Hephaestus", "Dionysus"],
            "answer": "options",
        },
        {
            "question": "What is the chemical symbol for the element mercury?",
            "options": ["Hg", "Mr", "Mc", "Me"],
            "answer": "options",
        },
        {
            "question": "What is the name of the largest moon of Jupiter?",
            "options": ["Ganymede", "Io", "Europa", "Callisto"],
            "answer": "options",
        },
        {
            "question": "In what year did the Berlin Wall fall?",
            "options": ["1989", "1987", "1990", "1991"],
            "answer": "options",
        },
        {
            "question": "What is the capital city of Brazil?",
            "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
            "answer": "options",
        },
        {
            "question": "Who wrote 'Pride and Prejudice'?",
            "options": ["Jane Austen", "Charlotte Brontë", "Emily Brontë", "Mary Shelley"],
            "answer": "options",
        },
        {
            "question": "Who is known as the 'Father of Modern Physics'?",
            "options": ["Albert Einstein", "Isaac Newton", "Niels Bohr", "Galileo Galilei"],
            "answer": "options",
        },
        {
            "question": "Which mountain range is the longest in the world?",
            "options": ["The Andes", "The Rockies", "The Himalayas", "The Alps"],
            "answer": "options",
        },
        {
            "question": "What is the largest island in the world?",
            "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"],
            "answer": "options",
        },
        {
            "question": "What is the chemical symbol for silver?",
            "options": ["Ag", "Si", "Au", "Sr"],
            "answer": "options",
        },
        {
            "question": "Who painted 'The Persistence of Memory'?",
            "options": ["Salvador Dali", "Pablo Picasso", "Henri Matisse", "Claude Monet"],
            "answer": "options",
        },
        {
            "question": "What is the largest bone in the human body?",
            "options": ["Femur", "Tibia", "Humerus", "Pelvis"],
            "answer": "options",
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1912", "1905", "1914", "1920"],
            "answer": "options",
        },
        {
            "question": "What is the capital city of Argentina?",
            "options": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza"],
            "answer": "options",
        },
        {
            "question": "Who painted the famous artwork 'The Last Supper'?",
            "options": ["Leonardo da Vinci", "Raphael", "Michelangelo", "Sandro Botticelli"],
            "answer": "options",
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1945", "1944", "1939", "1950"],
            "answer": "options",
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["Japanese Yen", "Japanese Dollar", "Japanese Won", "Japanese Peso"],
            "answer": "options",
        },

    ],

    "History and Geography": [
        {
            "question": "What is the name of the thin and long country that spans more than half of the western coast of South America?",
            "options": ["Chile", "Peru", "Argentina", "Colombia"],
            "answer": "options",
        },
        {
            "question": "Which American state is the largest by area?",
            "options": ["Alaska", "Texas", "California", "Montana"],
            "answer": "options",
        },
        {
            "question": "Which two countries share the longest international border?",
            "options": ["Canada and the USA", "Russia and China", "Argentina and Chile", "USA and Mexico"],
            "answer": "options",
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"],
            "answer": "options",
        },
        {
            "question": "Which continent is the largest?",
            "options": ["Asia", "Africa", "North America", "Europe"],
            "answer": "options",
        },
        {
            "question": "Which of the Seven Wonders is located in Egypt?",
            "options": ["The Pyramids of Giza", "The Hanging Gardens of Babylon", "The Statue of Zeus at Olympia",
                        "The Colossus of Rhodes"],
            "answer": "options",
        },
        {
            "question": "What is the capital of New Zealand?",
            "options": ["Wellington", "Auckland", "Christchurch", "Hamilton"],
            "answer": "options",
        },
        {
            "question": "Which desert is the largest in the world?",
            "options": ["The Sahara Desert", "The Gobi Desert", "The Arabian Desert", "The Kalahari Desert"],
            "answer": "options",
        },
        {
            "question": "What is the name of the world’s longest river?",
            "options": ["The Nile", "The Amazon", "The Yangtze", "The Mississippi"],
            "answer": "options",
        },
        {
            "question": "Which city in India would you find the Taj Mahal in?",
            "options": ["Agra", "Delhi", "Jaipur", "Mumbai"],
            "answer": "options",
        },
        {
            "question": "What is the largest island in the Mediterranean Sea?",
            "options": ["Sicily", "Sardinia", "Cyprus", "Crete"],
            "answer": "options",
        },
        {
            "question": "Which river runs through the Grand Canyon?",
            "options": ["Colorado River", "Missouri River", "Rio Grande", "Columbia River"],
            "answer": "options",
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["Japan", "China", "South Korea", "Thailand"],
            "answer": "options",
        },
        {
            "question": "Which African country is known as the 'Pearl of Africa'?",
            "options": ["Uganda", "Kenya", "Tanzania", "Ghana"],
            "answer": "options",
        },
        {
            "question": "Which Asian river is considered the longest?",
            "options": ["Yangtze River", "Mekong River", "Ganges River", "Yellow River"],
            "answer": "options",
        },
        {
            "question": "By what name were the Egyptian kings and rulers known?",
            "options": ["Pharaohs", "Sultans", "Emirs", "Caesars"],
            "answer": "options",
        },
        {
            "question": "How many Pyramids of Giza were made?",
            "options": ["Three", "Four", "Five", "Two"],
            "answer": "options",
        },
        {
            "question": "Which queen was Julius Caesar involved with?",
            "options": ["Cleopatra", "Nefertiti", "Elizabeth I", "Catherine the Great"],
            "answer": "options",
        },
        {
            "question": "Where did the Franks settle after defeating the Romans?",
            "options": ["Gaul", "Iberia", "Britannia", "Italia"],
            "answer": "options",
        },
        {
            "question": "How long did the Middle Ages last?",
            "options": ["About 1000 years", "About 500 years", "About 1500 years", "About 700 years"],
            "answer": "options",
        },
        {
            "question": "Which religion dominated the Middle Ages in Europe?",
            "options": ["Catholicism", "Islam", "Orthodox Christianity", "Protestantism"],
            "answer": "options",
        },
        {
            "question": "In which year did World War I begin?",
            "options": ["1914", "1912", "1918", "1905"],
            "answer": "options",
        },
        {
            "question": "In which country was Adolf Hitler born?",
            "options": ["Austria", "Germany", "Switzerland", "Poland"],
            "answer": "options",
        },
        {
            "question": "John F. Kennedy was assassinated in which city?",
            "options": ["Dallas", "Washington, D.C.", "Los Angeles", "New York City"],
            "answer": "options",
        },
        {
            "question": "On Sunday 18th June 1815, which famous battle took place?",
            "options": ["The Battle of Waterloo", "The Battle of Trafalgar", "The Battle of Leipzig",
                        "The Battle of Austerlitz"],
            "answer": "options",
        },
        {
            "question": "What event marked the beginning of World War I?",
            "options": ["The assassination of Archduke Franz Ferdinand", "The invasion of Belgium",
                        "The sinking of the Lusitania", "The Zimmerman Telegram"],
            "answer": "options",
        },
        {
            "question": "Who was the leader of the Soviet Union during World War II?",
            "options": ["Joseph Stalin", "Vladimir Lenin", "Nikita Khrushchev", "Leon Trotsky"],
            "answer": "options",
        },
        {
            "question": "What ancient wonder was located in the city of Alexandria in Egypt?",
            "options": ["The Lighthouse of Alexandria", "The Pyramids of Giza", "The Hanging Gardens of Babylon",
                        "The Temple of Artemis"],
            "answer": "options",
        },
        {
            "question": "Who was the famous nurse known for her work during the Crimean War and considered the founder of modern nursing?",
            "options": ["Florence Nightingale", "Clara Barton", "Mary Seacole", "Elizabeth Blackwell"],
            "answer": "options",
        },
        {
            "question": "What was the name of the ship that brought the Pilgrims to America in 1620?",
            "options": ["The Mayflower", "The Santa Maria", "The Discovery", "The Endeavour"],
            "answer": "options",
        },

    ],
    "Modern Music and Literature": [
        {
            "question": "What was the name of the group Justin Timberlake used to be part of?",
            "options": ["*NSYNC", "Backstreet Boys", "New Kids on the Block", "Westlife"],
            "answer": "options",
        },
        {
            "question": "What was the name of the rock band formed by Jimmy Page?",
            "options": ["Led Zeppelin", "Deep Purple", "The Who", "Cream"],
            "answer": "options",
        },
        {
            "question": "Which country did AC/DC originate in?",
            "options": ["Australia", "United Kingdom", "United States", "Canada"],
            "answer": "options",
        },
        {
            "question": "What genre of music did Taylor Swift start in?",
            "options": ["Country", "Pop", "Rock", "R&B"],
            "answer": "options",
        },
        {
            "question": "Who was the lead singer of the iconic '80s band Culture Club?",
            "options": ["Boy George", "George Michael", "Simon Le Bon", "Morrissey"],
            "answer": "options",
        },
        {
            "question": "Which name is rapper Sean Combs better known by?",
            "options": ["P. Diddy", "Lil Wayne", "Dr. Dre", "Ice Cube"],
            "answer": "options",
        },
        {
            "question": "Which musical legend is Jay-Z married to?",
            "options": ["Beyoncé", "Rihanna", "Alicia Keys", "Janet Jackson"],
            "answer": "options",
        },
        {
            "question": "How many Grammys does John Legend have?",
            "options": ["Ten", "Five", "Seven", "Twelve"],
            "answer": "options",
        },
        {
            "question": "Which British girl group had a member by the name of Mel B?",
            "options": ["Spice Girls", "Little Mix", "All Saints", "Girls Aloud"],
            "answer": "options",
        },
        {
            "question": "Who is often referred to as the 'King of Pop' and is known for iconic hits like 'Thriller' and 'Billie Jean'?",
            "options": ["Michael Jackson", "Elvis Presley", "Prince", "Stevie Wonder"],
            "answer": "options",
        },

        {
            "question": "What author became famous for his six-volume biography of Abraham Lincoln?",
            "options": ["Carl Sandburg", "Doris Kearns Goodwin", "David McCullough", "Shelby Foote"],
            "answer": "options",
        },
        {
            "question": "Who wrote 'The Old Man and the Sea' and is considered one of the greatest writers of the 20th century?",
            "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner"],
            "answer": "options",
        },
        {
            "question": "What Danish author is considered by many to be the most prolific fairy tale writer?",
            "options": ["Hans Christian Andersen", "J.R.R. Tolkien", "C.S. Lewis", "The Brothers Grimm"],
            "answer": "options",
        },
        {
            "question": "Who is the writer of 'The Merchant of Venice'?",
            "options": ["William Shakespeare", "Christopher Marlowe", "Ben Jonson", "Thomas Kyd"],
            "answer": "options",
        },
        {
            "question": "'The Adventures of Sherlock Holmes' was written by which writer?",
            "options": ["Arthur Conan Doyle", "Agatha Christie", "G.K. Chesterton", "Edgar Allan Poe"],
            "answer": "options",
        },
        {
            "question": "What is the name of the fourth book in the Harry Potter series?",
            "options": ["Harry Potter and the Goblet of Fire", "Harry Potter and the Prisoner of Azkaban",
                        "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince"],
            "answer": "options",
        },
        {
            "question": "The Hunger Games series was written by which author?",
            "options": ["Suzanne Collins", "Veronica Roth", "J.K. Rowling", "Stephenie Meyer"],
            "answer": "options",
        },
        {
            "question": "Which country is Aesop's Fables believed to originate in?",
            "options": ["Greece", "Italy", "Egypt", "India"],
            "answer": "options",
        },
        {
            "question": "In Herman Melville’s novel 'Moby-Dick', who was the loyal, reasonable first mate?",
            "options": ["Starbuck", "Queequeg", "Ishmael", "Stubb"],
            "answer": "options",
        },
        {
            "question": "The book 'The Da Vinci Code' was written by whom?",
            "options": ["Dan Brown", "James Patterson", "John Grisham", "Tom Clancy"],
            "answer": "options",
        },
        {
            "question": "Who wrote the novel 'One Hundred Years of Solitude'?",
            "options": ["Gabriel García Márquez", "Mario Vargas Llosa", "Jorge Luis Borges", "Isabel Allende"],
            "answer": "options",
        },
        {
            "question": "Who wrote the classic children’s book 'Charlotte’s Web'?",
            "options": ["E.B. White", "Roald Dahl", "Beatrix Potter", "A.A. Milne"],
            "answer": "options",
        },
        {
            "question": "What is the title of the classic Greek epic attributed to Homer, telling the story of the Trojan War?",
            "options": ["The Iliad", "The Odyssey", "The Aeneid", "Argonautica"],
            "answer": "options",
        },
        {
            "question": "What is the name of the protagonist in Jules Verne’s 'Twenty Thousand Leagues Under the Sea'?",
            "options": ["Captain Nemo", "Phileas Fogg", "Professor Aronnax", "Captain Ahab"],
            "answer": "options",
        },
        {
            "question": "Who wrote the gothic novel 'Frankenstein; or, The Modern Prometheus'?",
            "options": ["Mary Shelley", "Bram Stoker", "Edgar Allan Poe", "Ann Radcliffe"],
            "answer": "options",
        },
    ],
    "Games & Riddles": [
        {
            "question": "Where did backgammon originate?",
            "options": ["Persia", "Egypt", "Greece", "China"],
            "answer": "options",
        },
        {
            "question": "How many cards are there in a deck of Uno?",
            "options": ["108", "52", "100", "96"],
            "answer": "options",
        },
        {
            "question": "In which board game do you try to solve a murder?",
            "options": ["Clue", "Monopoly", "Scrabble", "Risk"],
            "answer": "options",
        },
        {
            "question": "In chess, the queen has the combined movement of which two pieces?",
            "options": ["Bishop and rook", "Knight and rook", "Bishop and knight", "King and rook"],
            "answer": "options",
        },
        {
            "question": "Which of these games includes the phrase 'Do not pass go, do not collect $200'?",
            "options": ["Monopoly", "Clue", "The Game of Life", "Risk"],
            "answer": "options",
        },
        {
            "question": "The video game 'Happy Feet' features what animals?",
            "options": ["Penguins", "Dolphins", "Polar bears", "Seals"],
            "answer": "options",
        },
        {
            "question": "What classic video game requires you to eat all the dots throughout a maze?",
            "options": ["Pac-Man", "Space Invaders", "Tetris", "Donkey Kong"],
            "answer": "options",
        },
        {
            "question": "Which Street Fighter character wears a white outfit and a red headband?",
            "options": ["Ryu", "Ken", "Guile", "Chun-Li"],
            "answer": "options",
        },
        {
            "question": "'Astro Boy' is what genre of video game?",
            "options": ["Action", "Puzzle", "Racing", "Sports"],
            "answer": "options",
        },
        {
            "question": "What sport is featured in the video game 'FIFA'?",
            "options": ["Football", "Basketball", "Rugby", "Baseball"],
            "answer": "options",
        },
        {
            "question": "What type of game is Axie Infinity?",
            "options": ["Blockchain game", "Racing game", "First-person shooter", "Puzzle game"],
            "answer": "options",
        },
        {
            "question": "In 'The Farmer in the Dell', what did the cat take?",
            "options": ["The rat", "The cheese", "The dog", "The cow"],
            "answer": "options",
        },
        {
            "question": "What did the 'Itsy Bitsy Spider' climb up?",
            "options": ["The waterspout", "The tree", "The wall", "The fence"],
            "answer": "options",
        },
        {
            "question": "What did the 'Three Little Kittens' lose?",
            "options": ["Their mittens", "Their hats", "Their shoes", "Their toys"],
            "answer": "options",
        },
        {
            "question": "How many bags of wool did 'Baa Baa Black Sheep' have?",
            "options": ["Three", "Two", "Four", "One"],
            "answer": "options",
        },
        {
            "question": "Why did Jack and Jill go up the hill?",
            "options": ["To fetch a pail of water", "To fly a kite", "To pick some flowers", "To see the view"],
            "answer": "options",
        },
        {
            "question": "How can a man go eight days without sleep?",
            "options": ["By sleeping during the night", "By drinking lots of coffee", "By taking naps at work",
                        "By never closing his eyes"],
            "answer": "options",
        },
        {
            "question": "How can you drop a raw egg on the concrete floor without cracking it?",
            "options": ["The egg won’t crack the concrete floor", "Drop it from a very low height",
                        "Wrap it in cloth first", "Place a cushion underneath"],
            "answer": "options",
        },
        {
            "question": "If there are six apples and you take away four, how many do you have?",
            "options": ["Four", "Two", "Six", "None"],
            "answer": "options",
        },
        {
            "question": "What goes up and down, but still remains in the same place?",
            "options": ["Stairs", "A balloon", "A yo-yo", "A seesaw"],
            "answer": "options",
        },
        {
            "question": "What gets wetter and wetter the more it dries?",
            "options": ["A towel", "A sponge", "A river", "A cloud"],
            "answer": "options",
        },

    ],

}


# Post-processing: replace numeric answer_index with string correct_answer across all questions
for _category, _questions in quiz_questions.items():
    for _q in _questions:
        if 'answer_index' in _q and 'correct_answer' not in _q:
            _idx = _q['answer_index']
            _opts = _q.get('options', [])
            if isinstance(_idx, int) and 0 <= _idx < len(_opts):
                _q['correct_answer'] = _opts[_idx]
                del _q['answer_index']
            else:
                pass
