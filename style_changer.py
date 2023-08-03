import os
import openai


def get_text_file_paths(directory):
    """Gets paths for all text files in the specified directory.

    Args:
      directory: The directory where the documents are stored.

    Returns:
      A list of file paths as strings.

    Raises:
      FileNotFoundError: If the directory does not exist.
    """
    paths = []
    if not os.path.exists(directory):
        raise FileNotFoundError("The directory " + directory + " does not exist.")
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            path = os.path.join(directory, filename)
            paths.append(path)
    return paths


def change_style(text, style, api_key):
    """Changes the style of the document using a prompt and Langchain with OpenAI LLM.

    Args:
      text: The text being modified by the LLM.
      style: The style (e.g. Film Noir) to change the text to.
      api_key: Open AI API key loaded from environment variables.

    Returns:
      A list of file paths as strings.
    """
    prompt = ("Pretend you are an expert author and change the style of this document to " + style + ": " + text)
    updated_text = openai.Completion.create(
        prompt=prompt,
        temperature=0.4,
        max_tokens=1000,
        engine="text-davinci-003",
        api_key=api_key)

    return updated_text["choices"][0]["text"]


def transform_documents(paths, style, api_key):
    """ Transforms the style of all documents represented by the paths parameter.

    Args:
      paths: Where the documents are located on disk.
      style: The style (e.g. Film Noir) to change the text to.
      api_key: Open AI API key loaded from environment variables.

    Raises:
    FileNotFoundError: If the directory does not exist.
    """
    for path in paths:
        try:
            f = open(path, errors="ignore")
            text = f.read()
        except PermissionError:
            print("Error: You do not have permission to the file: " + path + ".")
            print("Please try running with administrator privileges.")
            continue
        updated_text = change_style(text, style, api_key)
        (file, extension) = os.path.splitext(path)
        updated_file = os.path.join(file + "_ai.txt")
        try:
            f = open(updated_file, "w")
            f.write(updated_text)
        except PermissionError:
            print("Error: You do not have permission for the file " + updated_file + ".")
            print("Please try running with administrator privileges.")
            continue


def main():
    """This program changes the style of documents and saves them to a new file.

    **Note:** Set the OPENAI_API_KEY environment variable before running this program.
    """
    print("This program takes .txt files in a directory and changes the style they're written in, producing new files "
          "as output")
    print("**Note:** The program is subject to Open AI rate limits.")
    directory = input("Please enter the directory where your documents are stored: ")
    paths = get_text_file_paths(directory)
    style = input("What style do you want to change all documents to? ")
    api_key = os.environ.get("OPENAI_API_KEY")
    transform_documents(paths, style, api_key)
    print("Your documents have been updated.")


if __name__ == "__main__":
    main()
