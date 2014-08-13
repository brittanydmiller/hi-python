
def convert(num):
    numbers = [1000,500,100,50,10,5,1]
    numerals = ["M", "D", "C", "L", "X", "V", "I"]
    if num in numbers:
        match_index = numbers.index(num)
        return numerals[match_index]
    else:
        return "Too hard"
