# make mini translate dict with values
translate = {
    "kursi" : "chair",
    "madad" : "help",
    "kutta" : "dog",
    "bili" :  "cat"
}
# for a user's words
users_word = input("Enter your words for translate: ")

# from translate dict we want user's word
print(translate[users_word])