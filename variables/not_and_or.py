# Операторы NOT , AND , OR
# Приоритетность Выполнения NOT -> AND -> OR
# a > b or (a > 1 and b > 1)

# ---   NOT   ---------------------------------------------------------------------------------------
# оператор not переворачивает значение

# not True  -> False
# not False -> True

not 4 == 4  # -> False
not 4 != 4  # -> True

# ---   AND   ---------------------------------------------------------------------------------------
# оператор and возвращает True только если оба значения True
# в других случаях возвращает False

# True  and True  -> True
# False and False -> False
# True  and False -> False
# False and True  -> False

1 > 0 and 2 > 0  # -> True
1 < 0 and 2 < 0  # -> False
1 > 0 and 2 < 0  # -> False
1 < 0 and 2 > 0  # -> False


# ---   OR   ----------------------------------------------------------------------------------------
# or возвращает True, если хотябы одно условие возвращает True

# True  or True  -> True
# False or False -> False
# True  or False -> True
# False or True  -> True

1 > 0 or 2 > 0  # -> True
1 < 0 or 2 < 0  # -> False
1 > 0 or 2 < 0  # -> True
1 < 0 or 2 > 0  # -> True
