import os
import mimetypes

def get_extension(path: str) -> str:
    root, ext = os.path.splitext(path)

    return root, ext



def main():
    example_file = "example.txt"
    root, ext = get_extension(example_file)
    mimetype, _ = mimetypes.guess_type(example_file)
    print("Part 1: Get Extension")
    print(example_file)
    print(f"Root: {root}")
    print(f"Extension: {ext}")
    print(f"Mime type: {mimetype}")

if __name__ == "__main__":
    main()