def check_range(num: int) -> str:
    result = None
    if num < 0:
        result = "negative"
    if num == 0:
        result = "zero"
    if num > 0 < 10:
        result = "positive single digit"
    if num >= 10:
        result = "positive multi digit"
    return result








  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))
