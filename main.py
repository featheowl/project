def strcounter(s):
    sym_counter = {}
    for sym in s:
        sym_counter[sym] = sym_counter.get(sym, 0) + 1
    print(sym_counter)

strcounter('aabbsscc')
