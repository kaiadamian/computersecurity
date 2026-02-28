import string
from collections import Counter, defaultdict
import q2

'''Define Functions'''
def calculate_IC(ciphertext, n):
    # obtain the letter frequencies
    F = Counter(ciphertext)
    # calculate IC using the given formula
    return (sum(Fi * (Fi - 1) for Fi in F.values())) / (n * (n - 1))
def kasiski(ciphertext):
    # create a dictionary to hold the starting positions of each substring
    substring_starting_positions = defaultdict(list)
    # accumulate all substrings of lengths 2 to n that occur within ciphertext, keeping note of their starting positions
    for substring_length in range (2, n):
        for i in range((n - substring_length) + 1):
            letters = ciphertext[i:i+substring_length]
            substring_starting_positions[letters].append(i)
    
    kasiski_table = []
    for letters, starting_positions in substring_starting_positions.items():
        if len(starting_positions) <= 1:
            continue
        else:
            for i in range(len(starting_positions) - 1):
                start = starting_positions[i]
                end = starting_positions[i+1]
                gap_length = end - start
                factors_of_gaplength = [i for i in range(2, gap_length + 1) if gap_length % i == 0]
                kasiski_table.append((letters, start, end, gap_length, factors_of_gaplength))
    return kasiski_table
def print_kasiski(kasiski_table):
    # print the kasiski table
    factors = []
    print('\nKasiski Table:')
    print(f'{'Letters':<12}{'Start':<8}{'End':<8}{'Gap Length':<12}{'Factors of Gap Length'}')
    for substring in kasiski_table:
        print(f'{substring[0]:<12}{substring[1]:<8}{substring[2]:<8}{substring[3]:<12}{substring[4]}')
        # obtain all the factors of each substring
        for f in substring[4]:
            factors.append(f)
    factor_counts = Counter(factors)
    print(f'Most Common Factors: {factor_counts.most_common(2)}')
def div_into_cols(ciphertext, key_len):
    columns = ["" for n in range(key_len)]
    for i, char in enumerate(ciphertext):
        columns[i % key_len] += char
    return columns

'''Main Function'''
if __name__ == '__main__':
    # ciphertext
    ciphertext = "TTEUMGQNDVEOIOLEDIREMQTGSDAFDRCDYOXIZGZPPTAAITUCSIXFBXYSUNFESQRHISAFHRTQRVSVQNBEEEAQGIBHDVSNARIDANSLEXESXEDSNJAWEXAODDHXEYPKSYEAESRYOETOXYZPPTAAITUCRYBETHXUFINR"
    n = len(ciphertext)
    print(f'Ciphertext = {ciphertext}')
    # index of coincidence
    IC = calculate_IC(ciphertext, n)
    print(f'\nIC = {IC}')
    # apply the kasiski method and print the generated table
    kasiski_table = kasiski(ciphertext)
    print_kasiski(kasiski_table)
    # arrange the message into key_len columns and calculate IC for each
    key_len = 5
    columns = div_into_cols(ciphertext, key_len)
    print(f'\nCiphertext Divided Into {key_len} Columns/Alphabets:')
    for i, c in enumerate(columns, start=1):
        # compute IC for each column
        print(f'Alphabet #{i}')
        print(c)
        print(f'IC = {calculate_IC(c, len(c))}')
        
    # treat each column as its own caesar cipher to find each letter of the key
    print(f'\nTreat each column as its own Caesar Cipher:')
    keys = [None] * key_len
    for i, c in enumerate(columns):
        print(f'\nAlphabet #{i+1}')
        keys[i] = q2.main(c)
        print(f'Maximum i Value: {keys[i]}')