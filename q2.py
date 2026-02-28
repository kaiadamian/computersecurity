import string

'''Define Global Variables'''
p = [
    0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015,
    0.060, 0.065, 0.005, 0.005, 0.035, 0.030,
    0.070, 0.080, 0.020, 0.002, 0.065, 0.060,
    0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002
]
PHI_values = {}

'''Define Functions'''
def PHI(i, f):
    # compute PHI(i)
    total = 0
    for c_index, c in enumerate(string.ascii_lowercase):
        new_index = (c_index - i) % 26
        total += f[c] * p[new_index]
    return total

def main(ciphertext):
    # compute f(c)
    f = {letter:0 for letter in string.ascii_lowercase}
    for c in ciphertext.lower():
        f[c] += 1
    for letter in f:
        f[letter] /= len(ciphertext)

    # calculate PHI(i) for i = 0 to i = 25 and print the values
    for i in range(26):
        PHI_values[i] = PHI(i,f)
        print(f'PHI({i}) = {PHI_values[i]:.3f}')

    # find maximum i value
    max_i = max(PHI_values, key=PHI_values.get)
    return max_i

if __name__ == '__main__':
    ciphertext = "MVLESRXPIIYEIRSEGVILXJAXSSTPIYXR"
    max_i = main(ciphertext)
    for i in range(26):
        print(f'PHI({i}) = {PHI_values[i]:.3f}')
    print(f'\nKey with highest PHI value: {max_i}')