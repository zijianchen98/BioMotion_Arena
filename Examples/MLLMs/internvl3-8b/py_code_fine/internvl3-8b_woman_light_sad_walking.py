
def sad_woman_walking_animation():
    import time
    for i in range(10):
        print("\n" * 15)
        for j in range(7):
            print("O " * (7 - i) + "O" * (2*i))
        time.sleep(0.25)
    for i in range(10):
        print("\n" * 15)
        for j in range(7):
            print("O " * (i) + "O" * (7 - i))
        time.sleep(0.25)

sad_woman_walking_animation()
