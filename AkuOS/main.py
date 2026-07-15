from speaker import speak
from brain import ask
import esp32

print("AkuOS Started!")

speak("whats good boss")

esp32.happy()

while True:

    question = input("\nYou: ")

    if question.lower() == "quit":
        break

    if "light" in question.lower():

        esp32.light_on()

    answer = ask(question)

    print()

    speak(answer)

    esp32.normal()