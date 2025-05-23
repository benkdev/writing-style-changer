import os
from openai import OpenAI
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


def change_style(text, style):
    """
    Changes the style of text using OpenAI ChatCompletion API.

    Args:
      text: The text being modified by the LLM.
      style: The style (e.g. Film Noir) to change the text to.

    Returns:
      The changed text.
    """

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Pretend you are an expert author."},
            {"role": "user", "content": "Change the style of this document to " + style + ": " + text}
        ]
    )

    return completion.choices[0].message.content


def transform_documents(path, style):
    """
    Transforms the style of the document represented by the path parameter.

    Args:
      path: Path to text.txt within this project.
      style: The style (e.g. Film Noir) to change the text to.

    Raises:
        PermissionError: If you don't have permissions to open or write.

    Returns:
        The updated text.
    """
    text = ""
    try:
        f = open(path, errors="ignore")
        text = f.read()
    except PermissionError:
        print("Error: You do not have permission to open the file: " + path + ".")
        print("Please try running this program with administrator privileges.")
    updated_text = change_style(text, style)
    (file, extension) = os.path.splitext(path)
    updated_file = os.path.join(file + "_ai.txt")
    try:
        f = open(updated_file, "w")
        f.write(updated_text)
    except PermissionError:
        print("Error: You do not have permission to write the file " + updated_file + ".")
        print("Please try running this program with administrator privileges.")
    return updated_text


def main():
    """
    This program changes the style of the text in text.txt within this project and saves them to a new file.

    **Note:** Set the OPENAI_API_KEY environment variable before running this program.
    """
    print("This program changes the style of text in text.txt, producing a new file.")
    print("**Note:** The program is subject to Open AI rate limits.")
    directory = os.path.curdir
    path = os.path.join(directory, "text.txt")
    style = input("What style do you want to change the text to? ")

    updated_text = transform_documents(path, style)
    print("Your text has been updated and is in text_ai.txt")
    print("New text: \n" + updated_text)


if __name__ == "__main__":
    main()
