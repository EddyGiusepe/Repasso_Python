def nemo(text):
    find_nemo = text.title().split()

    if 'Nemo' in find_nemo:
        local = find_nemo.index("Nemo") + 1
        return 'I found Nemo at {}!'.format(local)
    return 'I can t find Nemo :('


if(__name__ == "__main__"):
    nemo()