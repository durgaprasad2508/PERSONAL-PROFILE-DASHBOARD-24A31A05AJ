import os
import json
import time
from datetime import datetime, timedelta


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def register(users):
    clear()
    print("=" * 50)
    print(" REGISTER NEW USER".center(50))
    print("=" * 50)
    username = input("Enter username: ").strip()
    if username in users:
        print("Username already exists!")
        pause()
        return
    password = input("Enter password: ").strip()
    users[username] = {
        "password": password,
        "profile": {},
        "notes": "",
        "last_updated": "",
    }
    save_users(users)
    print("Registration successful!")
    pause()

def login(users):
    clear()
    print("=" * 50)
    print("USER LOGIN".center(50))
    print("=" * 50)
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username]["password"] == password:
        print("Login successful!")
        time.sleep(1)
        dashboard(users, username)
    else:
        print(" Invalid username or password.")
        pause()

def profile_completeness(profile):
    total = 5
    filled = sum(1 for key in ["name", "age", "email", "hobbies", "skills"] if profile.get(key))
    return int((filled / total) * 100)

def check_profile_reminder(user):
    last_updated = user.get("last_updated")
    if not last_updated:
        print(" You haven't updated your profile yet!")
        return

    last_time = datetime.strptime(last_updated, "%Y-%m-%d %H:%M:%S")
    days_diff = (datetime.now() - last_time).days

    if days_diff >= 7:
        print(f" Reminder: It's been {days_diff} days since your last update. Please review your profile!")
    else:
        print(f" Profile recently updated ({days_diff} days ago).")

def dashboard(users, username):
    while True:
        clear()
        user = users[username]
        completeness = profile_completeness(user["profile"])
        print("=" * 50)
        print(f" Welcome, {username}".center(50))
        print("=" * 50)
        print(f"Profile Completeness: {completeness}%")
        print(f"Last Updated: {user['last_updated'] or 'Not updated yet'}")
        print("=" * 50)
        check_profile_reminder(user)
        print("=" * 50)
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Manage Notes / Journal")
        print("4. Change Password")
        print("5. Export Profile to Text File")
        print("6. Logout")
        print("=" * 50)
        choice = input("Enter choice: ")

        if choice == '1':
            view_profile(user)
        elif choice == '2':
            edit_profile(users, username)
        elif choice == '3':
            manage_notes(users, username)
        elif choice == '4':
            change_password(users, username)
        elif choice == '5':
            export_profile(user, username)
        elif choice == '6':
            print(" Logging out...")
            time.sleep(1)
            break
        else:
            print(" Invalid choice!")
            pause()

def view_profile(user):
    clear()
    print("=" * 50)
    print(" YOUR PROFILE".center(50))
    print("=" * 50)
    profile = user["profile"]
    for key, value in profile.items():
        print(f"{key.capitalize():<15}: {value}")
    print("\nNotes:", user["notes"] or "No notes yet")
    print("=" * 50)
    pause()

def edit_profile(users, username):
    clear()
    profile = users[username]["profile"]
    print("=" * 50)
    print(" EDIT PROFILE".center(50))
    print("=" * 50)
    profile["name"] = input(f"Name [{profile.get('name','')}] : ") or profile.get("name", "")
    profile["age"] = input(f"Age [{profile.get('age','')}] : ") or profile.get("age", "")
    profile["date of birth"] = input(f"Date Of Birth [{profile.get('date of birth','')}] : ") or profile.get("date of birth", "")
    profile["mobile.no"] = input(f"Mobile.No [{profile.get('mobile.no','')}] : ") or profile.get("mobile.no", "")
    profile["gender"] = input(f"Gender [{profile.get('gender','')}] : ") or profile.get("gender", "")
    profile["location"] = input(f"Location [{profile.get('location','')}] : ") or profile.get("location", "")
    profile["email"] = input(f"Email [{profile.get('email','')}] : ") or profile.get("email", "")
    profile["school"] = input(f"School [{profile.get('school','')}] : ") or profile.get("school", "")
    profile["marks"] = input(f"Marks [{profile.get('marks','')}] : ") or profile.get("marks", "")
    profile["interrmediate"] = input(f"Interrmediate [{profile.get('interrmediate','')}] : ") or profile.get("interrmediate", "")
    profile["percentage"] = input(f"Percentage [{profile.get('percentage','')}] : ") or profile.get("percentage", "")
    profile["degree"] = input(f"Degree [{profile.get('degree', '')}]: ") or profile.get("degree", "")
    profile["cgpa"] = input(f"CGPA [{profile.get('cgpa', '')}]: ") or profile.get("cgpa", "")
    profile["skills"] = input(f"Skills (comma-separated) [{profile.get('skills', '')}]: ") or profile.get("skills", "")
    profile["projects"] = input(f"Projects [{profile.get('projects', '')}]: ") or profile.get("projects", "")
    profile["certifications"] = input(f"Certifications [{profile.get('certifications', '')}]: ") or profile.get("certifications", "")
    profile["internships"] = input(f"Internships [{profile.get('internships', '')}]: ") or profile.get("internships", "")
    profile["achievements"] = input(f"Achievements [{profile.get('achievements', '')}]: ") or profile.get("achievements", "")
    profile["linkedin"] = input(f"LinkedIn [{profile.get('linkedin', '')}]: ") or profile.get("linkedin", "")
    profile["github"] = input(f"GitHub [{profile.get('github', '')}]: ") or profile.get("github", "")
    profile["portfolio"] = input(f"Portfolio Link [{profile.get('portfolio', '')}]: ") or profile.get("portfolio", "")
    profile["languages known"] = input(f"Languages Known [{profile.get('languages known', '')}]: ") or profile.get("languages known", "")
    profile["strengths"] = input(f"Strengths [{profile.get('strengths', '')}]: ") or profile.get("strengths", "")
    profile["weaknesses"] = input(f"Weaknesses [{profile.get('weaknesses', '')}]: ") or profile.get("weaknesses", "")
    profile["hobbies"] = input(f"Hobbies [{profile.get('hobbies','')}] : ") or profile.get("hobbies", "")
    profile["goals"] = input(f"Goals [{profile.get('goals','')}] : ") or profile.get("goals", "")


    users[username]["last_updated"] = current_time()
    save_users(users)
    print(" Profile updated successfully!")
    pause()

def manage_notes(users, username):
    clear()
    print("=" * 50)
    print(" NOTES / JOURNAL".center(50))
    print("=" * 50)
    current_notes = users[username]["notes"]
    print("Current Notes:\n", current_notes or "No notes yet")
    print("\nType new notes (leave blank to keep current):")
    new_notes = input("> ").strip()
    if new_notes:
        users[username]["notes"] = new_notes
        users[username]["last_updated"] = current_time()
        save_users(users)
        print("Notes updated!")
    else:
        print(" No changes made.")
    pause()

def change_password(users, username):
    clear()
    print("=" * 50)
    print(" CHANGE PASSWORD".center(50))
    print("=" * 50)
    old = input("Enter current password: ")
    if old != users[username]["password"]:
        print(" Incorrect password!")
    else:
        new = input("Enter new password: ")
        users[username]["password"] = new
        save_users(users)
        print(" Password changed successfully!")
    pause()

def export_profile(user, username):
    filename = f"{username}_profile_report.txt"
    completeness = profile_completeness(user["profile"])
    with open(filename, "w") as f:
        f.write("=========================================\n")
        f.write("      PERSONAL PROFILE DASHBOARD\n")
        f.write("=========================================\n\n")
        for key, value in user["profile"].items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write(f"\nNotes: {user['notes'] or 'No notes yet'}\n")
        f.write(f"Last Updated: {user['last_updated'] or 'Never'}\n")
        f.write(f"Profile Completeness: {completeness}%\n")
        f.write(f"Exported On: {current_time()}\n")
    print(f" Profile exported successfully to '{filename}'")
    pause()

def main():
    users = load_users()
    while True:
        clear()
        print("=" * 50)
        print(" PERSONAL PROFILE DASHBOARD".center(50))
        print("=" * 50)
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("=" * 50)
        choice = input("Enter choice: ")

        if choice == '1':
            login(users)
            users = load_users()
        elif choice == '2':
            register(users)
            users = load_users()
        elif choice == '3':
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice!")
            pause()

if __name__ == "__main__":
    main()

