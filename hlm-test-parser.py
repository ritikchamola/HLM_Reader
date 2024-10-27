#!/usr/bin/env python3
import jieba.posseg as pseg
import re
import os

# Define HTML color codes for different parts of speech
POS_COLORS = {
    'n': "red",       # Nouns
    'v': "green",     # Verbs
    'a': "yellow",    # Adjectives
    'r': "blue",      # Pronouns
    'd': "magenta",   # Adverbs
    # Add more if needed
}

# Dictionary URL for clickable word lookups
DICTIONARY_URL = "https://hanyu.baidu.com/s?wd="

def generate_html(input_filename, output_filename="output.html"):
    # Read the text file
    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Open an HTML file to write the output
    with open(output_filename, "w", encoding="utf-8") as output_file:
        # Start HTML structure with JavaScript for clickable pop-ups
        output_file.write("""
        <html>
        <head>
            <title>红楼梦 Translation</title>
            <style>
              /* Styling for tooltips */
              .tooltip { cursor: pointer; color: inherit; }
              .tooltip:hover { text-decoration: underline; }
            </style>
            <script>
              function openDictionary(word) {
                const url = `""" + DICTIONARY_URL + """${encodeURIComponent(word)}`;
                window.open(url, '_blank');
              }
            </script>
        </head>
        <body>
        """)

        # Main title
        main_title = lines[0].strip()
        output_file.write(f"<h1 style='text-align: center;'>{main_title}</h1>\n")

        # Process each line
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue

            # Check if it's a chapter heading
            if re.match(r"^第[一二三四五六七八九十百千万]+回", line):
                output_file.write(f"<h2 style='text-align: center; color: darkblue;'>{line}</h2>\n")
            else:
                sentences = re.split(r'[。！？]', line)
                for sentence in sentences:
                    if not sentence.strip():
                        continue

                    # Process each word with part-of-speech tagging
                    words = pseg.cut(sentence)
                    sentence_html = ""
                    for word in words:
                        pos = word.flag[0]  # Get the first character of the POS tag
                        color = POS_COLORS.get(pos, "black")  # Default to black if POS not defined
                        # Make the word clickable with JavaScript function
                        sentence_html += f"<span class='tooltip' style='color: {color};' onclick='openDictionary(\"{word.word}\")'>{word.word}</span> "

                    output_file.write(f"<p>{sentence_html.strip()}</p>\n")

        # Close HTML tags
        output_file.write("</body></html>")

    print(f"Output written to: {os.path.abspath(output_filename)}")

# Run the function
input_filename = "./text/红楼梦.txt"
output_filename = "红楼梦_output.html"
generate_html(input_filename, output_filename)
