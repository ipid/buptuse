# -*- coding: utf-8 -*-

def diff_last(init_value):
    last_value, new_value = init_value, (yield None)
    while True:
        last_value, new_value = new_value, (yield new_value - last_value)
