def is_dangerous(text: str) -> bool:
    keywords = {
        "electric", "electricity", "high voltage",
        "gas", "flammable", "fire",
        "sharp", "blade", "cut"
    }
    return any(word in text.lower() for word in keywords)
