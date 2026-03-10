import sys
import json
import os
from datetime import datetime

FILE = os.path.expanduser("~/.notes.json")

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save(n):
    json.dump(n, open(FILE, "w"), indent=2)

if __name__ == "__main__":
    notes = load()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    
    if cmd == "add":
        notes.append({"id": len(notes)+1, "text": " ".join(sys.argv[2:]), "date": datetime.now().strftime("%Y-%m-%d")})
        save(notes)
        print("saved")
    elif cmd == "del":
        notes.pop(int(sys.argv[2])-1)
        save(notes)
        print("deleted")
    elif cmd == "search":
        q = sys.argv[2].lower()
        for n in notes:
            if q in n["text"].lower():
                print(f"{n['id']}. [{n['date']}] {n['text']}")
    else:
        for n in notes:
            print(f"{n['id']}. [{n['date']}] {n['text']}")
        if not notes:
            print("no notes")
# updated
