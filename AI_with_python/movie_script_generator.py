def create_movie_script():

    print("=== Movie Script Generator ===")

    title = input("Movie title: ")
    hero = input("Hero name: ")
    villain = input("Villain name: ")
    location = input("Location: ")

    script = f"""
========================================
             {title}
========================================

Scene 1
Location: {location}

{hero}: We have to stop {villain}!

{villain}: You cannot stop me!

{hero}: We will see about that.

The adventure begins...

========================================
                THE END
========================================
"""

    with open("movie_script.txt", "w") as file:
        file.write(script)

    print("\nMovie script created successfully!")
    print(script)


create_movie_script()