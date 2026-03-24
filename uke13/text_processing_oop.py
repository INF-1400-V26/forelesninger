"""
OOP "over-done" / boilerplate implementation of text processing.

"""

from abc import ABC, abstractmethod


class TextProcessor(ABC):
    @abstractmethod
    def process(self, text: str) -> str:
        pass


class LowerCaseProcessor(TextProcessor):
    def process(self, text: str) -> str:
        return text.lower()


class LetterReplacer(TextProcessor):
    def __init__(self, replacements: dict[str, str] = {"æ": "a", "ø": "o", "å": "a"}):
        self._replacements = replacements

    def process(self, text: str) -> str:
        for old, new in self._replacements.items():
            text = text.replace(old, new)
        return text


class SpaceReplacer(TextProcessor):
    def __init__(self, replacement: str = "-"):
        self._replacement = replacement

    def process(self, text: str) -> str:
        return text.replace(" ", self._replacement)


class NonAlphabeticCharacterRemover(TextProcessor):
    def __init__(self, exceptions: str = "-"):
        self._exceptions = exceptions

    def process(self, text: str) -> str:
        return "".join(char for char in text if char.isalpha() or char in self._exceptions)


class Pipeline(TextProcessor):
    def process(self, text: str) -> str:
        lower_case_processor = LowerCaseProcessor()
        letter_replacer = LetterReplacer()
        space_replacer = SpaceReplacer()
        non_alpha_remover = NonAlphabeticCharacterRemover()

        text = lower_case_processor.process(text)
        text = letter_replacer.process(text)
        text = space_replacer.process(text)
        text = non_alpha_remover.process(text)

        return text


if __name__ == "__main__":
    sample_raw_text = "Årsmøte i Svolvær R'n'B-klubb!"
    expected_output = "arsmote-i-svolvar-rnb-klubb"
    pipeline = Pipeline()
    processed_text = pipeline.process(sample_raw_text)
    print(f"Processed text: {processed_text}")
    assert processed_text == expected_output
