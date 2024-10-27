
# HLM Reader with Pop-Up Dictionary

## Project Overview
This project displays excerpts from *红楼梦* (*Dream of the Red Chamber*) with a pop-up dictionary feature. Hovering over specific words reveals a tooltip with a brief description, and clicking the word opens an online dictionary link for a more detailed definition.

## Features
1. **Hover Tooltip**: Hover over selected words to see a quick definition or hint in a tooltip.
2. **Dictionary Links**: Click on a word to open its full definition in an online dictionary in a new tab.

## Usage
1. Clone this repository and navigate to the project folder.
2. Open `index.html` in your web browser to start the reader.
3. Hover over words to view tooltips.
4. Click on a word to open the dictionary link.

## Project Structure
- **`index.html`**: The main HTML file displaying text with clickable dictionary links and tooltips for specific words.
- **`style.css`**: CSS for styling tooltips, text layout, and color-coded parts of speech.
- **`script.js`**: JavaScript for handling dictionary pop-up links and tooltip interactivity.
- **`text/红楼梦.txt`**: Source text file containing selected passages from *Dream of the Red Chamber*.

## Setup and Installation

1. **Install Dependencies**:
   - Make sure you have Python 3 installed.
   - Install `jieba` for Chinese word segmentation:
     ```bash
     pip3 install jieba
     ```

2. **Generate HTML with Python**:
   Run the provided Python script to process `红楼梦.txt` and generate `index.html` with tooltips and dictionary links:
   ```bash
   python3 hlm-test-parser.py
   ```

3. **Open `index.html`**:
   After running the script, open `index.html` in any web browser to view the interactive text with dictionary pop-ups.

## Notes
- **Modifications**: To add or modify words and definitions, edit `hlm-test-parser.py` or the tooltips in `index.html` directly.
- **Dictionary Links**: This project uses Baidu Dictionary for online lookups; modify the URL in `script.js` if you'd like to use a different dictionary.
