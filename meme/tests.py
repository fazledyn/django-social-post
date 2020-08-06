import difflib

# Create your tests here.
string_array = [
    "doge cheems bonk hit stick dogelore",
    "always has been astronaut",
    "was i a good boy told you're the best",
    "chude chatni bekar khatni thakurmar jhuli",
    "rick ashley never gonna let you down",
    "gordon ramsey dissapointed look disgusted face"
]

user_string = input("Enter your string: ")

user_string_slice = user_string.split(" ")
meme_array = []

for string in string_array:
    ratio = difflib.SequenceMatcher(None, user_string, string).ratio()
    print("Current Ratio: ", ratio)
    if ratio > 0.3:
        meme_array.append(string)

print()
print(meme_array)