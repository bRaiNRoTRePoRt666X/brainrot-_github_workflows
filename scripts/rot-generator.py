#!/usr/bin/env python3
"""
🧠🔥 ROT GENERATOR 666 🔥🧠
Turns sane text into pure brainrot energy
"""

import random
import sys

BRAINROT_WORDS = [
    "Skibidi", "Ohio", "Rizz", "Fanum", "Grimace", "Gyatt",
    "Sigma", "Alpha", "Beta", "NPC", "Mogging", "Looksmaxxing",
    "Baby Gronk", "Livvy Dunne", "Kai Cenat", "IShowSpeed",
    "Amongus", "Imposter", "Sus", "Baka", "UwU", "Smol",
    "Dop Dop", "Yes Yes", "Skibidi Toilet", "Cameraman",
    "Titan", "Speakerman", "TV Woman", "G-Man", "Astro"
]

REPLACEMENTS = {
    "very": "extremely sigma",
    "good": "bussin",
    "bad": "negative rizz",
    "cool": "666 energy",
    "crazy": "pure Ohio",
    "weird": "fanum taxed",
    "funny": "skibidi approved",
    "smart": "giga chad coded"
}

def rotify(text: str) -> str:
    """Convert normal text into brainrot"""
    words = text.split()
    result = []
    
    for word in words:
        # Random brainrot injection
        if random.random() < 0.3:
            result.append(random.choice(BRAINROT_WORDS))
        
        # Apply replacements
        lower = word.lower()
        if lower in REPLACEMENTS:
            result.append(REPLACEMENTS[lower])
        else:
            result.append(word)
    
    # Add emoji chaos
    emojis = ["🧠", "🔥", "💀", "🃏", "💜", "⚡", "🎵", "📱"]
    output = ""
    for word in result:
        output += word + " "
        if random.random() < 0.4:
            output += random.choice(emojis) + " "
    
    return output.strip()

def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = sys.stdin.read().strip()
    
    if not text:
        text = "Your code is so mid right now"
    
    print("🧠🔥 === BRAINROT GENERATOR 666 === 🔥🧠")
    print()
    print(f"Original: {text}")
    print()
    print(f"Rotified: {rotify(text)}")
    print()
    print("🃏 HA HA HA HA HA!")

if __name__ == "__main__":
    main()
