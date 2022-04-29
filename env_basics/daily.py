toDo = {
    "monday": "play football",
    "tuesday": "code",
    "wednesday": "go to the gym",
    "thursday": "bake a cake",
    "friday": "attend a dance class",
    "saturday": "go to church",
    "sunday": "watch movie"
}


def get_all_to_do():
    return f"<ul>{to_do()}</ul>"


def to_do():
    li = ""
    # for key in toDo:
    #     li = li+f"<li><h1>On:<b>{key}</b>We {toDo[key]}</h1></li>"

    for key in toDo:
        href = f"http://127.0.0.1:5000/day/{key}"
        li = li + \
            f"<li><a href={href}><h1>On:<b>{key}</b>We {toDo[key]}</h1><a/></li>"
    return li


def get_the_to_do(key):
    return f"<h1>On this day {key}</h1><h2>{toDo[key]}</h2>"


# print(get_all_to_do())
