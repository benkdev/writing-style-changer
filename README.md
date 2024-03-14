# Writing Style Changer

This program changes the writing style of the text in text.txt within the project directory.
It utilizes the OpenAI API (ChatGPT).

Example:

Original text:
``Call me Ishmael. Some years ago – never mind how long precisely – having little or no money in my purse,
 and nothing particular to interest me on shore, 
 I thought I would sail about a little and see the watery part of the world.``

Changed to Film Noir:
``Darkness enveloped the lonely pier as I stood, the cold mist seeping through my trench coat. 
 Call me Ishmael. Some years back - the specifics elude me - with pockets empty and a heart heavy with nothing to tie me down ashore, 
 I made the decision to set sail and explore the dark depths of the world's waterways.``

## How to Use

1. Clone the repository to your computer.
2. Install Python.
3. Install the dependencies by running ``pip install -r requirements.txt`` as administrator.
4. Add your Open AI API key to environmental variables as OPENAI_API_KEY.
5. Place the text you want to modify in ``text.txt`` within the project directory.
3. Run the program by running ``python style_changer.py``.
5. Enter a writing style.
6. The program will change the writing style of the text in ``text.txt`` to the new style.

## Notes

The program is subject to Open AI rate limiting. See the Open AI website for usage tiers.

## License

This program is licensed under the MIT License.

## Credits

This program was created by benkdev.
