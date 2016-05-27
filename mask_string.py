import sys


def mask_string(string, start=None, stop=None, mask='****', match_length=True):
    length = len(string)
    if start is None:
        start = 0
    if stop is None:
        stop = max(0, length - 1)
    start %= length
    stop %= length

    if match_length and (not mask or len(mask) != length):
        mask = mask[0] * length

    return string[:start] + mask + string[stop+1:]

sys.modules[__name__] = mask_string
