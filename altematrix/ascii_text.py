ascii_0 = r'          _______  ______   _______  ______   _______  _______  _______          __________________ _        _        _______  _        _______  _______  _______  _______  _______ _________                                              _______ '
ascii_1 = r'         (  ___  )(  ___ \ (  ____ \(  __  \ (  ____ \(  ____ \(  ____ \|\     /|\__   __/\__    _/| \    /\( \      (       )( (    /|(  ___  )(  ____ )(  ___  )(  ____ )(  ____ \\__   __/|\     /||\     /||\     /||\     /||\     /|/ ___   )'
ascii_2 = r'         | (   ) || (   ) )| (    \/| (  \  )| (    \/| (    \/| (    \/| )   ( |   ) (      )  (  |  \  / /| (      | () () ||  \  ( || (   ) || (    )|| (   ) || (    )|| (    \/   ) (   | )   ( || )   ( || )   ( |( \   / )( \   / )\/   )  | _______'
ascii_3 = r'         | (___) || (__/ / | |      | |   ) || (__    | (__    | |      | (___) |   | |      |  |  |  (_/ / | |      | || || ||   \ | || |   | || (____)|| |   | || (____)|| (_____    | |   | |   | || |   | || | _ | | \ (_) /  \ (_) /     /   )(       )'
ascii_4 = r'         |  ___  ||  __ (  | |      | |   | ||  __)   |  __)   | | ____ |  ___  |   | |      |  |  |   _ (  | |      | |(_)| || (\ \) || |   | ||  _____)| |   | ||     __)(_____  )   | |   | |   | |( (   ) )| |( )| |  ) _ (    \   /     /   / (       |'
ascii_5 = r'         | (   ) || (  \ \ | |      | |   ) || (      | (      | | \_  )| (   ) |   | |      |  |  |  ( \ \ | |      | |   | || | \   || |   | || (      | | /\| || (\ (         ) |   | |   | |   | | \ \_/ / | || || | / ( ) \    ) (     /   /  '
ascii_6 = r'         | )   ( || )___) )| (____/\| (__/  )| (____/\| )      | (___) || )   ( |___) (___|\_)  )  |  /  \ \| (____/\| )   ( || )  \  || (___) || )      | (_\ \ || ) \ \__/\____) |   | |   | (___) |  \   /  | () () |( /   \ )   | |    /   (_/\\'
ascii_7 = r'         |/     \||/ \___/ (_______/(______/ (_______/|/       (_______)|/     \|\_______/(____/   |_/    \/(_______/|/     \||/    )_)(_______)|/       (____\/_)|/   \__/\_______)   )_(   (_______)   \_/   (_______)|/     \|   \_/   (_______/'

ascii = [ ascii_0, ascii_1, ascii_2, ascii_3, ascii_4, ascii_5, ascii_6, ascii_7 ]

letters = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
width = 9

def write(word):
  timer = 8
  for ascii_line in ascii:
    whole_line = ''
    for letter in word:
      index = letters.index(letter.upper())
      position = index * width
      letter_line = ascii_line[position : position + width]
      whole_line += letter_line
    timer -= 1
    if timer == 0:
      whole_line += "\n Powered by: CodingPeps (Brown Bear) \nAuthor: Ir0n-c0d3X"
    print(whole_line)