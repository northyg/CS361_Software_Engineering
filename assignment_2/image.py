# Giselle Northy, CS361 Assignment 2
# This program has the cat image array and reads and writes the image path

images = ['\\cats\\cat1.jpg', '\\cats\\cat2.jpg', '\\cats\\cat3.jpg',
          '\\cats\\cat4.jpg', '\\cats\\cat5.jpg', '\\cats\\cat6.jpg',
          '\\cats\\cat7.jpg', '\\cats\\cat8.jpg', '\\cats\\cat9.jpg', '\\cats\\cat10.jpg']

# 5 Image Service reads image-service.txt, erases it, and writes an image path to it
with open("image-service.txt", "r") as some_file:
    some_int = int(some_file.read().rstrip())

with open("image-service.txt", "w") as some_file:
    print(images[some_int], file=some_file)
