import random

IMAGENES = ['''
        
        +------------
        |           |
                    |
                    |
                    |
                    |
                    |
                    |
        ============|''',

'''
        
        +------------
        |           |
        ☻           |
                    |
                    |
                    |
                    |
                    |
        ============|''',

'''
        
        +------------
        |           |
        ☻           |
        |           |
                    |
                    |
                    |
                    |
        ============|''',

'''
        
        +------------
        |           |
        ☻           |
        |           |
        |           |
                    |
                    |
                    |
        ============|''',

'''
        
        +------------
        |           |
        ☻           |
        |           |
        |           |
        |           |
                    |
                    |
        ============|''',

'''
        
        +------------
        |           |
        ☻           |
        |           |
        |           |
        |           |
       /            |
                    |
        ============|''',

'''
        
        +------------
        |           |
        ☻           |
        |           |
        |           |
        |           |
       / \          |
                    |
        ============|''',

'''
        
        +------------
        |           |
        ☻           |
       /|           |
        |           |
        |           |
       / \          |
                    |
        ============|''',

'''
        
        +------------
        |           |
        ☻           |
       /|\          |
        |           |
        |           |
       / \          |
                    |
        ============|''',



]

WORDS = [
    'sofa',
    'gobierno',
    'computadora',
    'murcielago',
    'comida'
]

def random_word():
    idx = random.randint(0,len(WORDS) -1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGENES[tries])
    print('')
    print(hidden_word)
    print('-----*-----*-----*-----*-----*-----*')
def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        if len(letter_indexes) == 0:
            tries += 1

            if tries == 8:
                display_board(hidden_word, tries)
                print('')
                print('Jajajaja looser, la palabra era {}'.format(word))
                print('')
                break

        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            
            letter_indexes = []


        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades Ganaste, la palabra es {}'.format(word))
            print('')
            break

if __name__ == '__main__':
    print("Bienvenidos al ahorcado")
    run()