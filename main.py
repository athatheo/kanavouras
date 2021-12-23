import itertools
def create_all_possibilities(kanavouras_sifona, kanavouras_fonieda, kanavouras_possibilities):
    perms = [''.join(p) for p in itertools.permutations('kanavour')]

    for element in perms:
        for i, letter in enumerate(element):
            if letter == 'o' and (i == 7 or element[i+1] != 'u'):
                break
            elif i == 0 and letter in kanavouras_fonieda:
                break
            elif i > 0 and letter in kanavouras_fonieda and element[i-1] in kanavouras_fonieda:
                break
            elif i > 0 and letter == 'a' and element[i-1] == 'a':
                break
            elif i > 0 and letter == 'o' and element[i-1] == 'a':
                break
            elif i > 0  and letter == 'a' and element[i-1] == 'u':
                break
            elif i == len(element)-1 and letter == 'u':
                break
            elif i == len(element)-1 and letter == 'a':
                break
            elif i > 0 and letter in kanavouras_sifona and element[i-1] in kanavouras_sifona:
                break
            elif i == len(element)-1:
                kanavouras_possibilities.append(element)

    return kanavouras_possibilities


def print_kanavouras():
    kanavouras_sifona = ['k','n','v','r']
    kanavouras_fonieda = ['a','a','ou']
    kanavouras_kataliksi = ['as']
    kanavouras_possibilities = []
    kanavouras_possibilities = create_all_possibilities(kanavouras_sifona, kanavouras_fonieda, kanavouras_possibilities)
    for i, _ in enumerate(kanavouras_possibilities):
        kanavouras_possibilities[i] += kanavouras_kataliksi[0]

    print("Number of possible permutations: ", len(kanavouras_possibilities))

    for i in range(len(kanavouras_possibilities)):
        print(kanavouras_possibilities[i])



if __name__ == '__main__':
    print_kanavouras()
