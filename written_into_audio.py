import pyttsx3

if __name__ == '__main__':
    print("This is a Robo speaker made by Bharat Sharma .")

    while True:
        X = input("What do you want me to pronounce: ")
        if X.lower() == "q":
         print("thanks to talk with me, this was my first python project")
         break

        engine = pyttsx3.init()
        engine.say(X)
        engine.runAndWait()


