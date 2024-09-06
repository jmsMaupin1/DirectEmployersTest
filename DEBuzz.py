def DEBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("Direct Employers")
        elif i % 3 == 0:
            print("Direct")
        elif i % 5 == 0:
            print("Employers")
        else:
            print(i)


if __name__ == "__main__":
    DEBuzz()
