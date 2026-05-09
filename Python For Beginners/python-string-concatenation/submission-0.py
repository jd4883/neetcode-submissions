def concatenate(s1: str, s2: str) -> str:
    conc = s1 + s2
    if len(conc) > 10:
        return "Too long!"
    return conc




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
