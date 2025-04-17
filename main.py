from pet import Pet

def main():
    my_pet = Pet("Buddy")
    my_pet.get_status()
    print("\nFeeding pet...")
    my_pet.eat()
    print("\nPlaying with pet...")
    my_pet.play()
    print("\nTraining pet...")
    my_pet.train("Sit")
    my_pet.train("Roll over")
    print("\nLetting pet sleep...")
    my_pet.sleep()
    print("\nFinal Status:")
    my_pet.get_status()

if __name__ == "__main__":
    main()
