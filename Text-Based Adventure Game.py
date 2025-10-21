
print("Mystery at the Library")
print("It's late, the library is eerily quiet. You're the last one left, surrounded by towering stacks of forgotten tales.")
print("Just as you're about to pack up, you hear a faint, quiet, metallic clink from the restricted 'Ancient Manuscripts' section.")
print("Do you want to investigate the sound or leave the library?")

choice1 = input("Type '1' to investigate' or '2' to leave: ").lower()

if choice1 == "1":
    print("\nYou tiptoe toward the Ancient Manuscripts section. The air grows colder.")
    print("You see a dusty tome lying open on a pedestal, glowing faintly. Do you read it or look around?")
    choice2 = input("Type '1' to read or '2' look around: ").lower()

    if choice2 == "1":
        print("\nAs you read the cryptic text, the room begins to shift. You're walked into a hidden chamber beneath the library!")
        print("In the chamber, there's a locked chest and a strange puzzle on the wall. Do you solve the puzzle or try to break the chest?")
        choice3 = input("Type '1' to solve' or '2' to break: ").lower()

        if choice3 == "1":
            print("\nYou solve the puzzle, and the chest opens magically. Inside is a map to a forgotten archive of lost knowledge. You've uncovered a secret society of scholars!")
        elif choice3 == "2":
            print("\nYou try to break the chest, but a trap is triggered! You're teleported back to the library entrance, dazed and confused. The mystery remains unsolved.")
        else:
            print("Invalid choice. The mystery fades as the tome closes itself.")

    elif choice2 == "2":
        print("\nYou notice a shadow moving behind the shelves. It's a librarian ghost guarding the secrets!")
        print("Do you speak to the ghost or hide?")
        choice3 = input("Type '1' to speak' or '2' hide: ").lower()

        if choice3 == "1":
            print("\nThe ghost reveals the library's hidden history and grants you access to the secret archives. You're now part of the legacy.")
        elif choice3 == "2":
            print("\nYou hide, but the ghost vanishes. You missed your chance to uncover the truth.")
        else:
            print("Invalid choice. The ghost disappears into the mist.")

    else:
        print("Invalid choice. The tome closes, and the sound fades away.")

elif choice1 == "2":
    print("\nYou decide it's best not to meddle with mysterious sounds. As you exit, you notice a strange symbol etched into the doorframe.")
    print("Do you take a photo or ignore it?")
    choice2 = input("Type '1' to photo or '2' to ignore: ").lower()

    if choice2 == "1":
        print("\nLater, you research the symbol and discover it's linked to a secret society. You return to the library the next day, determined to learn more.")
    elif choice2 == "2":
        print("\nYou walk away, never knowing what secrets the library held. Sometimes, mystery is best left untouched.")
    else:
        print("Invalid choice. The symbol fades from memory.")

else:
    print("Invalid choice. The sound fades, and the night returns to silence.")
