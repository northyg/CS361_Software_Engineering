# Giselle Northy, CS361 Assignment 2
# This program is the main or "UI". It has the user interface and tells the
# os to launch the other two programs in the background, so they run separately.

import os


def get_prng():
    print("Welcome to the cat image service. Press enter to continue...")
    input()
    # 1 UI calls PRNG Service by writing the word "run" to prng-service.txt
    with open("prng-service.txt", "w") as out_file:
        print("run", file=out_file)
    print("starting prng press enter to continue...")
    input()

    # 2 PRNG Service reads prng-service.txt, erases it, and writes a pseudo-random
    # number to it
    os.system("python prng.py > prng-service.txt")
    print("prng finished press enter to continue...")
    input()

    # 3 UI reads prng-service.txt to get the random number
    with open("prng-service.txt", "r") as in_file:
        random_int = int(in_file.read().rstrip())

    # 4 UI writes the pseudo-random number to image-service.txt
    # print("got", some_int)
    with open("image-service.txt", "w") as some_file:
        print(random_int, file=some_file)

    # 5. Image Service reads image-service.txt, erases it, and writes an image path to it
    print("Received", random_int, "Starting image service, press enter to continue...")
    input()
    os.system("python image.py")

    # 6 UI reads image-service.txt then displays the image (or path) to the user
    with open("image-service.txt", "r") as some_file:
        some_path = str(some_file.read().rstrip())
        print("Here's the path to your cat pic!", some_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_prng()
