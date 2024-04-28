from generator import Generator
from prompt import Prompt


if __name__ == "__main__":
    prompt = Prompt()
    generator = Generator()

    generator.generate(prompt.get_path(), prompt.get_supported_properties())
