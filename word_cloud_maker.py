from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Path to your text file
text_file = 'extracted_text.txt'

# Read the text file
with open(text_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis', 
                      max_words=200, contour_width=1, contour_color='steelblue').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Disable axis
plt.show()

# Optionally, save the word cloud image to a file
wordcloud.to_file("wordcloud_output.png")
