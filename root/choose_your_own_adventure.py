user_choice = None

story = """Rabani, seated in her computer class, is startled by the school fire alarm.

The principal, over the intercom:

“Attention students. This is a drill. Rabani, please come to the office.”

Students in Rabani’s class turn to look at her.

Rabani, the principal’s favorite, obedient student, gets up to go.

The principal, upon Rabani’s arrival, gives her a laptop.

"Rabani, someone locked the school's online grade system. Can you help us fix it?"

A : Use the school Wi-Fi to track down the hacker.
OR
B : Open the secret computer repair toolkit on the desk.
"""

print(story)
user_choice = input().lower()

if user_choice == "a":
    story = """Rabani connects her laptop to the Wi-Fi and starts scanning the network.

She finds a suspicious file hiding in the school's art club folder. 

A message pops up on her screen: "You found me! But what will you do next?"

A : Delete the suspicious art file right away.
OR
B : Open the file to read what it says.
"""
    print(story)
    user_choice = input().lower()

    if user_choice == "a":
        story = """Rabani decides to delete the file instantly. 

A box pops up asking if she is really sure.

A : Click 'Yes' to confirm and delete it.
OR
B : Click 'No' and try to save a copy first.
"""
        print(story)
        user_choice = input().lower()

        if user_choice == "a":
            story = """Rabani confirms the delete. The lock on the grade system disappears, and all the grades come back safely!

THE END 
"""
            print(story)
        else:
            story = """She tries to save a copy, but the file turns out to be a harmless joke program that instantly turns all the text on her screen upside down.

THE END 
"""
            print(story)

    else:
        story = """Rabani opens the file. It plays a silly song through the laptop speakers.

A new text box asks her a question: 'Who is the coolest coder in school?'

A : Type 'Rabani' into the box.
OR
B : Type 'The Principal' into the box.
"""
        print(story)
        user_choice = input().lower()

        if user_choice == "a":
            story = """She types her own name. The computer rewards her by instantly unlocking the whole school system and printing out a digital gold star.

THE END 
"""
            print(story)
        else:
            story = """She types the principal's name. The computer laughs and rewards the principal with a free online coupon, while Rabani has to guess one more password.

THE END 
"""
            print(story)

else:
    story = """Rabani opens the repair toolkit. Inside, she finds a special master key card and a small handheld scanner.

She needs to check the school servers in the basement.

A : Take the elevator down to the basement server room.
OR
B : Take the stairs to check the hallway security cameras first.
"""
    print(story)
    user_choice = input().lower()

    if user_choice == "a":
        story = """Rabani takes the elevator down to the dark server room. 

She uses the master key card to unlock the main computer. Two big buttons glow on the screen.

A : Press the big green reset button.
OR
B : Press the flashing red emergency button.
"""
        print(story)
        user_choice = input().lower()

        if user_choice == "a":
            story = """She presses the green button. The computers beep happily, and everything goes back to normal. Rabani is named the official tech helper!

THE END 
"""
            print(story)
        else:
            story = """She presses the red button. Instead of fixing the grades, it accidentally turns on the school's indoor sprinklers, giving everyone an unexpected indoor rain shower!

THE END 
"""
            print(story)

    else:
        story = """Rabani runs up the stairs to check the hallway cameras. 

On the screen, she sees the school mascot (someone in a giant animal suit) running away from the office laptop!

A : Chase after the mascot down the hallway.
OR
B : Use the intercom microphone to call out the mascot.
"""
        print(story)
        user_choice = input().lower()

        if user_choice == "a":
            story = """Rabani chases the mascot all the way to the gym and catches them. It turns out to be her computer teacher, who gives her an automatic A+!

THE END 
"""
            print(story)
        else:
            story = """Rabani speaks into the microphone: "I see you by the gym doors, mascot!" The person stops, walks back, and unlocks the computer themselves.

THE END 
"""
            print(story)