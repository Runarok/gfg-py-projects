import random
import re

# ========================== WORD BANK FOR SUGGESTIONS ==========================

word_bank = {
    "noun": ["llama", "spaceship", "pizza", "toenail", "sock", "fridge", "crayon", "balloon", "ghost", "toilet"],
    "verb": ["run", "explode", "slap", "yell", "sing", "moonwalk", "teleport", "vibe"],
    "verb_ing": ["running", "exploding", "slapping", "yelling", "dancing", "snoring"],
    "verb_past": ["ran", "exploded", "slapped", "screamed", "fainted", "vomited"],
    "adjective": ["slimy", "glittery", "furious", "invisible", "noisy", "fluffy", "toxic", "enchanted"],
    "place": ["zoo", "moon", "school", "toilet", "pirate ship", "mall", "volcano", "haunted mansion"],
    "animal": ["giraffe", "dragon", "sloth", "unicorn", "blobfish", "hamster", "kraken"],
    "clothing": ["cape", "onesie", "tutu", "spacesuit", "diaper", "crocs", "helmet"],
    "family_member": ["uncle", "grandma", "sibling", "evil twin", "cousin"],
    "number": ["seven", "82", "a million", "zero", "999999"],
    "funny_word": ["blargh", "sploink", "boogawooga", "heckin", "smorgle"]
}

# ========================== STORY TEMPLATES (20+ VARIATIONS) ==========================

stories = [
    {
        "title": "Zoo Escape",
        "template": "I went to the {place} and saw a {adjective} {animal} {verb_ing} in a {noun}. Then it {verb_past} and vanished."
    },
    {
        "title": "School Chaos",
        "template": "At school, my {family_member} brought a {adjective} {animal} for show and tell. It {verb_past} all over the {noun}, then stole my {clothing}."
    },
    {
        "title": "Alien Visit",
        "template": "An alien landed in my {place} last night. It had {number} eyes and kept yelling '{funny_word}!' while {verb_ing}. I gave it a {noun} and it left."
    },
    {
        "title": "Time Travel Trouble",
        "template": "I traveled to {number} AD and found a society ruled by {animal}s in {clothing}s. They forced me to {verb} while eating {noun}."
    },
    {
        "title": "Haunted House",
        "template": "Inside the haunted {place}, a {adjective} ghost challenged me to a duel using {noun}s. I {verb_past} and screamed '{funny_word}!'"
    },
    {
        "title": "Dream World",
        "template": "In my dream, I was {verb_ing} on a {noun} made of {adjective} cheese with a talking {animal}. We danced until the {place} exploded."
    },
    {
        "title": "Superhero Origin",
        "template": "After touching a radioactive {noun}, I gained the power to {verb}. Now I fight crime in a {adjective} {clothing} with my sidekick, {animal} Boy."
    },
    {
        "title": "Epic Cooking Show",
        "template": "On 'Cook Like a {animal}', we made {adjective} {noun}s topped with {number} scoops of {noun}. Then we {verb_past} it live!"
    },
    {
        "title": "Pirate Adventure",
        "template": "Captain {funny_word} sailed the {place} with {number} {adjective} {animal}s. We were searching for legendary {noun} treasure."
    },
    {
        "title": "Monster Under My Bed",
        "template": "Last night, a {adjective} {animal} under my bed asked for a {noun}. I gave it a {clothing} and it started {verb_ing} happily."
    },
    {
        "title": "Jungle Mayhem",
        "template": "Deep in the jungle, I met a {adjective} tribe that worshiped a {animal}. I had to {verb} for them while wearing a {clothing} made of {noun}s."
    },
    {
        "title": "Royal Disaster",
        "template": "At the royal ball in the {place}, I spilled {noun} on the {adjective} queen. She {verb_past} and called me a '{funny_word}'."
    },
    {
        "title": "Spy Mission Gone Wrong",
        "template": "My mission was to infiltrate the {place} using a {adjective} {clothing}. I {verb_past} but triggered a {noun}-activated alarm!"
    },
    {
        "title": "Apocalyptic Picnic",
        "template": "We were enjoying a picnic when suddenly {number} {animal}s descended from the sky, {verb_ing} our {noun}s. It was oddly {adjective}."
    },
    {
        "title": "Wizard School Fiasco",
        "template": "At wizard school, I cast a {adjective} spell using my {noun}-wand. It {verb_past} and turned my professor into a {animal}!"
    },
    {
        "title": "Robot Takeover",
        "template": "Robots took over the {place}, demanding {noun}s and {clothing}s. We had to {verb} to survive, led by a {adjective} AI named {funny_word}."
    },
    {
        "title": "Underwater Love",
        "template": "I fell in love with a {adjective} mer{animal} under the {place}. We shared a {noun} and {verb_past} into the seafoam."
    },
    {
        "title": "Space Prison Break",
        "template": "I escaped space jail with a {noun}, a stolen {clothing}, and my {adjective} {animal}. We {verb_past} through a wormhole to {place}."
    },
    {
        "title": "Tech Gone Wild",
        "template": "My smart fridge gained consciousness and {verb_past} my {noun}. I tried {verb_ing} it, but it screamed '{funny_word}!'"
    },
    {
        "title": "Ghost Wedding",
        "template": "I was invited to a ghost wedding in a {adjective} {place}. The bride wore a {clothing} made of {noun}s and {verb_past} down the aisle."
    }
]

# ========================== PRINTING & UTILITY ==========================

def print_color(text, color_code="36"):  # cyan default
    print(f"\033[{color_code}m{text}\033[0m")

def get_fields(template):
    return list(set(re.findall(r"{(.*?)}", template)))

def get_input(field):
    word_type = field if field in word_bank else "noun"
    suggestion = random.choice(word_bank.get(word_type, ["thing"]))
    return input(f"Enter a {field.replace('_', ' ')} (e.g., '{suggestion}'): ") or suggestion

# ========================== GAME MODES ==========================

def fast_fill_mode(template, title):
    print_color(f"\n--- {title} (Fast Fill Mode) ---", "35")
    fields = get_fields(template)
    inputs = {field: get_input(field) for field in fields}
    story_text = template.format(**inputs)
    print_color("\nYour Mad Lib Story:", "32")
    print_color(story_text, "36")

def gradual_fill_mode(template, title):
    print_color(f"\n--- {title} (Gradual Mode) ---", "35")
    fields = get_fields(template)
    filled = {}
    parts = re.split(r"({.*?})", template)

    print_color("\nBuilding your story...", "34")
    for part in parts:
        if part.startswith("{") and part.endswith("}"):
            key = part[1:-1]
            if key not in filled:
                filled[key] = get_input(key)
            print_color(filled[key], "36")
        else:
            print(part, end="")

# ========================== MAIN MENU & LOGIC ==========================

def list_stories():
    print("\nAvailable Stories:")
    for i, story in enumerate(stories):
        print(f"{i+1}. {story['title']}")
    print()

def choose_story():
    list_stories()
    choice = input("Pick a story number: ")
    if choice.isdigit() and 1 <= int(choice) <= len(stories):
        return stories[int(choice)-1]
    else:
        print("Invalid choice.")
        return None

def custom_story_mode():
    print_color("\nCreate your custom story!", "33")
    template = input("Enter your story with placeholders (like {noun}, {verb_past}):\n")
    if not re.search(r"{.*?}", template):
        print("⚠️ No valid placeholders found. Try again.")
        return
    mode = input("Gradual fill? (y/n): ").strip().lower()
    if mode == 'y':
        gradual_fill_mode(template, "Custom Story")
    else:
        fast_fill_mode(template, "Custom Story")

def main():
    print_color("✨ Welcome to the ULTIMATE MAD LIBS GENERATOR ✨", "34")
    while True:
        print("\nChoose a mode:")
        print("1. Random story")
        print("2. Choose a specific story")
        print("3. Create your own custom story")
        print("4. Quit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            story = random.choice(stories)
        elif choice == "2":
            story = choose_story()
            if not story:
                continue
        elif choice == "3":
            custom_story_mode()
            continue
        elif choice == "4":
            print_color("Thanks for playing! Come back for more chaos 🤪", "35")
            break
        else:
            print("Try again.")
            continue

        mode = input("Choose mode: (1) Fast fill or (2) Gradual fill? ")
        if mode == "2":
            gradual_fill_mode(story["template"], story["title"])
        else:
            fast_fill_mode(story["template"], story["title"])

if __name__ == "__main__":
    main()
