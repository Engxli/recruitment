def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["Python", "Sleeping", "Eating"]


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    for count,skill in enumerate(skills,1):
        print (count,skill)


def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    show_skills(skills)
    userSelection = []
    userSelection.append(skills[int(input("Choose a skill from above by entering its number: "))-1])
    userSelection.append(skills[int(input("Choose a skill from above by entering its number: "))-1])
    return userSelection

def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    cv = {}
    cv["name"] = input("What's your name? ")
    cv["age"] = int(input("How old are you? "))
    cv["experience"] = int(input("How many years of experience do you have? "))
    cv["skills"] = get_user_skills(skills)
    return cv

def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    if(cv["age"] >= 25 and int(cv["age"]) <= 40 ) and (cv["experience"] > 3) and (desired_skill in cv["skills"]):
        return True


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:\n ")
    skills = get_skills()
    cv = get_user_cv(skills)
    if(check_acceptance(cv, skills[2])):
        print("You have been accepted,", cv["name"])
    else:   
        print("Sorry!, you have been rejected")

if __name__ == "__main__":
    main()
