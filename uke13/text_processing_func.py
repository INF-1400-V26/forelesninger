def lower_case(text: str) -> str:
    return text.lower()


def replace_norwegian_letters(text: str) -> str:
    text = text.replace("æ", "a")
    text = text.replace("ø", "o")
    text = text.replace("å", "a")
    return text


def replace_spaces_with_hyphens(text: str) -> str:
    return text.replace(" ", "-")


def remove_non_alphabetic_characters(text: str) -> str:
    return "".join(char for char in text if char.isalpha() or char == "-")


def pipeline(text: str) -> str:
    text = lower_case(text)
    text = replace_norwegian_letters(text)
    text = replace_spaces_with_hyphens(text)
    text = remove_non_alphabetic_characters(text)
    return text


if __name__ == "__main__":
    sample_raw_text = "Årsmøte i Svolvær R'n'B-klubb!"
    expected_output = "arsmote-i-svolvar-rnb-klubb"
    processed_text = pipeline(sample_raw_text)
    print(f"Processed text: {processed_text}")
    assert processed_text == expected_output
