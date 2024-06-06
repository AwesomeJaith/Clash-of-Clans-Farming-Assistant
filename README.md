# Clash of Clans Farming Assistant

The Clash of Clans farming assistant is a command line program that looks for a base with your desired amount of gold, elixir, and dark elixir.

# Demo

https://github.com/AwesomeJaith/Clash-of-Clans-Farming-Assistant/assets/70965009/76b04e69-e446-4eef-8a00-3148abe5c29d

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites
* pip
* 1080p screen
* Clash of Clans installed through Google Play Games for Windows

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AwesomeJaith/Clash-of-Clans-Farming-Assistant
   ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Modify file paths to match your computer's path
   * Line 80 in utils.py
     ```py
     clouds = screenshot(dimensions, "C:\\Your Path to Clash of Clans Farming Assistant\\clouds.png")
     ```
   * Line 86 and 88 in utils.py
     ```py
     screenshot(dimensions, "C:\\Your Path to Clash of Clans Farming Assistant\\village.png")
     ```
   * Line 90 in utils.py
     ```py
     images = preprocess_image("C:\\Your Path to Clash of Clans Farming Assistant\\resources.png")
     ```
4. Modify pyautogui.click x and y values in coc_base_finder.py to match your computer
   * Run click.py to find your x and y values
     ```sh
     python click.py
     ```
   * Line 20 in coc_base_finder.py should have the x and y coordinates for the attack button
     ```py
     pyautogui.click(x=200, y=1000)
     ```
   * Line 22 in coc_base_finder.py should have the x and y coordinates for the next button
     ```py
     pyautogui.click(x=1350, y=700)
     ```
   
## Usage

```py
python coc_base_finder.py (gold) (elixir) (dark elixir)
```

Replace the resource names in the line above with your desired minimum values to search for in a base.

## Motivation

As a Clash of Clans farmer, it gets boring to press next over and over to find that glorious dead base with 1 million+ loot. So I created this script to automate finding a loaded base for me and save myself some brain power to spam goblins around the resource collectors.

## Notes

I would be interested in expanding upon this application and improving the code in the future. Some things I would add are:
* The capability to adjust to different window sizes
* More filtering options such as a farming/trophy toggle
* An autoattack feature utilizing Barch (A simple army to use)

## Contributing

Clash-of-Clans-Farming-Assistant is an open-source project and we welcome contributions from the community.

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are welcome.

## License

MIT License

Copyright (c) 2024 Jaith Darrah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
