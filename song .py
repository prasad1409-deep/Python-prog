import time

def play_samjhawan():
    lyrics = [
        ("Nahi jeena tere baaju...",1.0),
        ("Nahi jeena, nahi jeena.", 5.5),
        ("Main tenu samjhawan ki,", 4.0),
        ("Na tere bina lagda jee...", 6.5),
        ("", 6.0),
        ("Tu ki jaane pyaar mera,", 5.0),
        ("Main karoon intezar tera,", 10.0),
        ("Tu dil, tui-yon jaan meri!", 2.0),
        ("", 0.5),
        ("Mere dil ne chun laiyaa ne,", 2.0),
        ("Tere dil diyaan raahan...", 1.0),
        ("Tu jo mere naal tu rehnda,", 2.0),
        ("Turpe meriyaan saaha.", 1.0),
        ("", 0.5),
        ("JEENA MERA... HAYE,", 2.0), 
        ("HUN HAI TERA, KI MAIN KARAAN.", 2.0),
        ("", 1.0),
        ("Tu kar aitbaar mera,", 1.0),
        ("Main karoon intezar tera,", 2.0),
        ("Tu dil, tui-yon jaan meri.", 1.0),
    ]

    print("---  NOW PLAYING: SAMJHAWAN  ---\n")
    
    for line, delay in lyrics:
        print(line)
        time.sleep(delay)

    print("\n---  TERMINAL FADES TO BLACK  ---")

if __name__ == "__main__":
    play_samjhawan()