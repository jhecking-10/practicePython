def prompt():
    name = input("What is your name?\n")
    while True:
        age = input("What is your age?\n")
        if int(age) <= 0:
            print("Age cannot be zero.")
        else:
            break
    year = input("What year is it?\n")
    return name, int(age), int(year)

name, age, year = prompt()

def calculate_year(): # returns year the user will turn 100
    years_until = 100 - age
    return year + years_until

def main():
    print(f"{name} will turn 100 in the year {calculate_year()}")

main()
