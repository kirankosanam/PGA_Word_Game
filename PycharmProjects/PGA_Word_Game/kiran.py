import random

spaces = 3


def generate_random_locations(n, n_stars):
    lis = list()
    while len(lis) < n_stars + 1:
        x = random.randint(0, n - 1)
        if x not in lis:
            lis.append(x)
    return lis


def generate_miss_word(word):
    max_length = len(word)
    max_spaces = max_length // 2
    locations = generate_random_locations(max_length, max_spaces)
    # print(locations, "locations")
    word_list = list(word)
    for i in locations:
        word_list[i] = '*'
    missed_word = ''.join(word_list)
    # print(missed_word)
    return [missed_word, len(locations)]


def select_difficulty(simplicity):
    rw = ''
    if simplicity == 1:
        rw = random.choice(words)
        while True:
            rw = random.choice(words)
            if len(rw) <= 7:
                break
        return rw

    elif simplicity == 2:
        rw = random.choice(words)
        while True:
            rw = random.choice(words)
            if 5 < len(rw) <= 9:
                break
        return rw

    elif simplicity == 3:
        rw = random.choice(words)
        while True:
            rw = random.choice(words)
            if 9 < len(rw):
                break
        return rw
    else:
        raise IndexError


def select_trails(simplicity, loc):
    if simplicity == 1:
        return loc * 2

    elif simplicity == 2:
        return loc + (loc // 2)

    elif simplicity == 3:
        return loc

    else:
        raise IndexError


def play(original_word, modified_word, no_of_trails):
    original_word = original_word
    modified_word = modified_word
    no_of_trails = no_of_trails
    missing_numbers = list()
    missing_numbersindex = list()

    for i in range(0, len(original_word)):
        if (original_word[i] != modified_word[i]):
            missing_numbers.append(original_word[i])
            missing_numbersindex.append(i)

    for j in range(0, no_of_trails):
        if len(missing_numbers) != 0:
            enter_character = input(f"Enter Character {modified_word}:")
            if enter_character in missing_numbers:
                k = missing_numbers.index(enter_character)
                m = int(missing_numbersindex[k])
                missing_numbers.remove(enter_character)
                modifiedtest = list(modified_word)
                modifiedtest[m] = enter_character
                modified_word1 = "".join(modifiedtest)
                modified_word = modified_word1
                print("Correct And Word is: " + modified_word)
                print(f'The Remaining Trails Are {no_of_trails - j - 1}.')
                missing_numbersindex.remove(m)

            else:
                if j < no_of_trails - 1:
                    print("Wrong Try Again")
                    print(f'The Remaining Trails Are {no_of_trails - j - 1}.')
                else:
                    print("Nah! Try again\nYou Loose")
        else:
            if len(missing_numbers) == 0:
                print("You WIN And The Word Is: " + modified_word)
                break
    print("The Original Word is:" + original_word)


random_word = []
n = input("What is your name? ")
print("Good Luck ! ", n)
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'alcohol', 'copy', 'paste', 'milk', 'empty', 'floor', 'come', 'hundred',
         'coding', 'getup', 'vegetables', 'spacebar', 'control', 'oldman', 'talking', 'eating', 'wnated', 'lie',
         'equal', 'separate', 'wordgame', 'monk', 'india', 'indian', 'america', 'american', 'put', 'hut', 'exam',
         'blue', 'green', 'laptop', 'lockdown', 'college', 'mistake', 'learn', 'friend', 'relative', 'spoon', 'school',
         'telegram', 'drahon', 'army', 'thermodynamics', 'mechanical', 'work', 'wrong', 'language', 'write', 'read',
         'help', 'running', 'brother', 'parents', 'hotter', 'sunlight', 'cement', 'record', 'operating', 'singing',
         'humming', 'swimming', 'complex', 'clean', 'hair', 'game', 'bell', 'temple', 'church', 'religion', 'contact',
         'message', 'coconut', 'ringing', 'vibrate', 'project', 'screte', 'palace', 'estivation', 'regnant', 'candy',
         'unknown', 'playground', 'pitch', 'mother', 'father', 'canyon', 'evidence', 'imposter', 'lift', 'function',
         'birthday', 'marraige', 'cake', 'snail', 'lighting', 'typing', 'river', 'strawberry', 'table', 'package',
         'startup', 'myrmidon', 'terpsichorean', 'oneiromancy', 'mate', 'siblings', 'old', 'gold', 'silver', 'paltinum',
         'oneiromancy', 'party', 'fry', 'compiler', 'processor', 'submit', 'oneiromancy', 'area', 'clinic', 'weight',
         'pass', 'result', 'universe', 'slim', 'diet', 'corona', 'immunity', 'village', 'town', 'mindset', 'attractive',
         'shoppingmall', 'theater', 'hsopital', 'curd', 'interview', 'bread', 'animal', 'feather', 'where', 'who',
         'what', 'cream', 'breakfast', 'butter', 'countdown', 'transparent', 'shoes', 'local', 'attitude', 'mission',
         'critical', 'overtime', 'remember', 'forget', 'database', 'qualification', 'multinational', 'shipment',
         'callcentre', 'knowledge', 'skills', 'labour', 'factory', 'impossible', 'fairytale', 'choclate', 'weak',
         'sunday', 'dozon', 'dumb', 'instrument', 'store', 'leave', 'tomorrowm', 'yesterday', 'white', 'balck',
         'rainbow', 'stereo', 'audio', 'audioplayer', 'quality', 'algorithm', 'motorcycle', 'indicator', 'forum',
         'multiplex', 'plantation', 'migrate', 'desert', 'solar', 'invertor', 'time', 'inversion', 'cinematography',
         'million', 'moonlight', 'grammar', 'gravity', 'mailbox', 'map', 'offline', 'micro', 'operation', 'labs',
         'development', 'date', 'bronze', 'oxygen', 'carbon', 'dioxide', 'helium', 'octacore', 'quadcore', 'tomato',
         'track', 'delivery', 'farmer', 'minister', 'orange', 'apple', 'banana', 'guava', 'tool', 'kit', 'repair',
         'triple', 'percentage', 'century', 'streak', 'mango', 'double', 'power', 'camp', 'fire', 'primary',
         'secondary', 'internet', 'stomach', 'physical', 'mental', 'heart', 'pair', 'parachute', 'believe', 'painful',
         'compose', 'studio', 'partner', 'crime', 'gateway', 'hexacore', 'management', 'chairman', 'president',
         'skating', 'shaking', 'melody', 'ocean', 'blood', 'antidust', 'lucky', 'businessman', 'international',
         'national', 'elections', 'ballotbox', 'integrated', 'alert', 'punch', 'popup', 'shirt', 'imigration', 'turbo',
         'military', 'attend', 'absent', 'clear', 'wireless', 'screenshot', 'newsreporter', 'multimedia', 'statement',
         'dairy', 'farm', 'prime', 'parliament', 'flag', 'gas', 'vaccine', 'booking', 'bank', 'deposit', 'credit',
         'mask', 'statement', 'phone', 'telephone', 'speed', 'petroleum', 'card', 'organnisation', 'voting', 'counters',
         'counting', 'stadium', 'commisoner', 'incharge', 'inside', 'outside', 'boundary', 'deputy', 'division', 'pool',
         'pole', 'polling', 'repolling', 'institution', 'statue', 'action', 'nine', 'twelve', 'swimmingpool',
         'publicity', 'municipality', 'information', 'isolation', 'litre', 'profit', 'collection', 'collector',
         'toothpaste', 'handwash', 'hearing', 'jeep', 'press', 'backside', 'caught', 'bowling', 'socail', 'chemistry',
         'subject', 'belief', 'cattle', 'thousand', 'sufficient', 'glasses', 'shampoo', 'soap', 'hosting', 'paltform',
         'metro', 'domain', 'free', 'service', 'cart', 'install', 'installment', 'journey', 'ox', 'cost', 'canvas',
         'advertisement', 'cyber', 'wheel', 'bullockcart', 'building', 'education', 'environment', 'notes',
         'individual', 'new', 'refresh', 'website', 'lightup', 'laugh', 'lighthouse', 'beach', 'continent', 'pacific',
         'noun', 'verb', 'nature', 'herbal', 'lifetime', 'understanding', 'sucess', 'successful']
diff = int(input("Enter\n1 -> Simple \n2 -> Medium \n3 -> Hard \n"))
try:
    random_word.append(select_difficulty(diff))
except IndexError:
    print("Invalid selection range")
random_word.append(generate_miss_word(random_word[0]))

# print(random_word)

r_word = random_word[0]
r_trails = select_trails(diff, random_word[1][1])
rm_word = random_word[1][0]
# print(r_word)
print(f'You only have {r_trails} trails')
# print(random_word[1][0])
play(r_word, rm_word, r_trails)
