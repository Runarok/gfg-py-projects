# FLAMES Compatibility Tool — Clean, Case-Insensitive, and Batch-Friendly

def remove_common_letters(name1, name2):
    n1 = list(name1.lower().replace(" ", ""))
    n2 = list(name2.lower().replace(" ", ""))
    for char in name1.lower():
        if char in n2:
            n1.remove(char)
            n2.remove(char)
    return len(n1) + len(n2)

def flames_letter(count):
    flames = list("FLAMES")
    idx = 0
    while len(flames) > 1:
        idx = (idx + count - 1) % len(flames)
        flames.pop(idx)
    return flames[0]

def meaning(letter):
    return {
        "F": "Friendship",
        "L": "Love",
        "A": "Affinity",
        "M": "Marriage",
        "E": "Distance",
        "S": "Sibling-like"
    }[letter]

def score_value(letter):
    return {
        "L": 6,
        "M": 5,
        "A": 4,
        "F": 3,
        "S": 2,
        "E": 1
    }[letter]

def compare(name1, name2):
    count = remove_common_letters(name1, name2)
    letter = flames_letter(count)
    return meaning(letter), score_value(letter)

def run_single_vs_single():
    n1 = input("Enter first name: ").strip()
    n2 = input("Enter second name: ").strip()
    relation, val = compare(n1, n2)
    print(f"\n📌 {n1} & {n2} → {relation} (Score: {val})")

def run_single_vs_batch():
    base = input("Enter main name: ").strip()
    group = input("Enter other names (comma-separated): ").strip().split(",")
    results = []
    for name in group:
        name = name.strip()
        rel, val = compare(base, name)
        results.append((name, rel, val))
    results.sort(key=lambda x: -x[2])
    print(f"\n📊 Compatibility of '{base}' with others:\n")
    print(f"{'Name':<20} | {'Relation':<15} | Score")
    print("-" * 45)
    for name, rel, val in results:
        print(f"{name:<20} | {rel:<15} | {val}")

def run_batch_vs_batch():
    g1 = [x.strip() for x in input("Enter Group 1 names (comma-separated): ").split(",")]
    g2 = [x.strip() for x in input("Enter Group 2 names (comma-separated): ").split(",")]
    all_results = []

    print("\n📊 Top Matches for Each Person:\n")
    for name1 in g1:
        person_results = []
        for name2 in g2:
            rel, val = compare(name1, name2)
            person_results.append((name2, rel, val))
        person_results.sort(key=lambda x: -x[2])
        best = person_results[0]
        print(f"{name1} 💫 Best match → {best[0]} ({best[1]}, Score: {best[2]})")
        all_results.append((name1, best[0], best[1], best[2]))

    print("\n📋 Full Comparison Table:\n")
    print(f"{'Name 1':<15} <-> {'Name 2':<15} | {'Relation':<12} | Score")
    print("-" * 60)
    for name1 in g1:
        for name2 in g2:
            rel, val = compare(name1, name2)
            print(f"{name1:<15} <-> {name2:<15} | {rel:<12} | {val}")

def menu():
    print("\n🧩 FLAMES Compatibility Tool")
    print("1. Compare two names")
    print("2. One name vs a group")
    print("3. Group vs Group")
    print("4. Exit")
    return input("Choose an option: ").strip()

# Main loop
while True:
    choice = menu()
    if choice == "1":
        run_single_vs_single()
    elif choice == "2":
        run_single_vs_batch()
    elif choice == "3":
        run_batch_vs_batch()
    elif choice == "4":
        print("Done. Thanks for using.")
        break
    else:
        print("Invalid option. Try again.")
