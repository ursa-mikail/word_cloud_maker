#!pip install PyPDF2
from PyPDF2 import PdfReader
import requests

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS , ImageColorGenerator

from itertools import chain
from collections import Counter

def create_word_cloud(data, image_out_name):
    wordcloud = WordCloud(width=1600, height=800,
                          colormap = 'winter',
                          background_color="white"
                          ).generate(str(data))

    plt.figure(figsize=(20,10),facecolor='k')
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

    wordcloud.to_file(image_out_name)
    
def create_word_cloud_from_freq (data, image_out_name):
    wordcloud = WordCloud(width=1600, height=800,
                          colormap = 'winter',
                          background_color="white"
                          ).generate_from_frequencies(data)

    plt.figure(figsize=(20,10),facecolor='k')
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

    wordcloud.to_file(image_out_name)

if __name__ == '__main__':
    file_pdf_url = 'https://github.com/mikail-eliyah-00/trial_00/raw/main/data/The-World-As-I-See-It.pdf'
    response = requests.get(file_pdf_url)
    file_downloaded_and_named_as = 'The-World-As-I-See-It.pdf'

    with open(file_downloaded_and_named_as, 'wb') as f: # set to a file
        f.write(response.content)

    # creating a pdf reader object
    reader = PdfReader(file_downloaded_and_named_as)
    num_pages = len(reader.pages)
    # getting a specific page from the pdf file
    page = 0
    contents_page = reader.pages[0]

    # extracting text from page
    text = contents_page.extract_text()
    print(text)

    # Print the number of pages and extracted text
    print(f"Number of pages: {num_pages}")
    print(f"Extracted text: {text}")


    """
    1THE WORLD AS I SEE IT
    Albert Einstein
        PREFACE TO ORIGINAL EDITION
        Only individuals have a sense of responsibility. --NietzscheThis book does not represent a complete collection of the articles, addresses,
    and pronouncements of Albert Einstein; it is a selection made with a definite
    object-- namely, to give a picture of a man. To-day this man is being drawn,
    contrary to his own intention, into the whirlpool of political passions andcontemporary history. As a result, Einstein is experiencing the fate that somany of the great men of history experienced: his character and opinions arebeing exhibited to the world in an utterly distorted form.
    To forestall this fate is the real object of this book. It meets a wish that has
    constantly been expressed both by Einstein's friends and by the wider public.It contains work belonging to the most various dates-- the article on "TheInternational of Science" dates from the year 1922, the address on "ThePrinciples of Scientific Research" from 1923, the "Letter to an Arab" from1930--and the most various spheres, held together by the unity of thepersonality which stands behind all these utterances. Albert Einstein believes
    in humanity, in a peaceful world of mutual helpfulness, and in the high mission
    of science. This book is intended as a plea for this belief at a time whichcompels every one of us to overhaul his mental attitude and his ideas.
    J. H.
    Number of pages: 76
    Extracted text: 1THE WORLD AS I SEE IT
    Albert Einstein
        PREFACE TO ORIGINAL EDITION
        Only individuals have a sense of responsibility. --NietzscheThis book does not represent a complete collection of the articles, addresses,
    and pronouncements of Albert Einstein; it is a selection made with a definite
    object-- namely, to give a picture of a man. To-day this man is being drawn,
    contrary to his own intention, into the whirlpool of political passions andcontemporary history. As a result, Einstein is experiencing the fate that somany of the great men of history experienced: his character and opinions arebeing exhibited to the world in an utterly distorted form.
    To forestall this fate is the real object of this book. It meets a wish that has
    constantly been expressed both by Einstein's friends and by the wider public.It contains work belonging to the most various dates-- the article on "TheInternational of Science" dates from the year 1922, the address on "ThePrinciples of Scientific Research" from 1923, the "Letter to an Arab" from1930--and the most various spheres, held together by the unity of thepersonality which stands behind all these utterances. Albert Einstein believes
    in humanity, in a peaceful world of mutual helpfulness, and in the high mission
    of science. This book is intended as a plea for this belief at a time whichcompels every one of us to overhaul his mental attitude and his ideas.
    J. H.
    """

    create_word_cloud(text, 'the_world_as_einstein_saw.png')

    #from google.colab import drive
    #drive.mount("/content/drive")

    #path="/content/drive/MyDrive/DataBlog/mass_shooting_events_stanford_msa_release_06142016.csv"
    path='https://raw.githubusercontent.com/mikail-eliyah-00/trial_00/main/data/mass_shooting_events_stanford_msa_release_06142016.csv'
    df=pd.read_csv(path)
    df['History of Mental Illness - Detailed'].head(5)

    stop_w = ['a', 'as', 'NaN', 'of', 'the', 'shooter', 'Name', 'had', 'Possible',
              'by', 'In', 'at', 'n', 'and', 'was', 'si', 'dtype', 'during', 'severa',
              'Detailed', 'Mental', 'entered', 'object', 'History', 'Length']

    data = df['History of Mental Illness - Detailed']

    create_word_cloud(data, "shooter_info_wordcloud.png")


    path2 = "https://raw.githubusercontent.com/mikail-eliyah-00/trial_00/main/data/example.txt"

    response = requests.get(path2)
    data = response.text

    create_word_cloud(data, "shooter_info_wordcloud.png")


    words = {
        "unknown": 114,
        "none": 58,
        "personality disorder": 3,
        "schizotypal personality disorder": 1,
        "narcissistic personality disorder": 1,
        "borderline personality disorder": 3,
        "depression": 31,
        "schizophrenia": 24,
        "psychopathy": 1,
        "paranoia": 27,
        "insanity": 13,
        "compulsivity": 4,
        "anxiety": 6,
        "PTSD": 8,
        "bipolar disorder": 6,
        "OCD": 3,
        "dissociative disorder": 2,
        "delusional disorder": 15,
        "panic disorder": 1,
        "ADHD": 1,
        "sensory processing disorder": 1,
        "dysphoric mania": 1,
        "grandiose": 2,
        "character behavior disorder": 1,
        "psychosis": 13
    }

    word_counts = Counter(words)

    create_word_cloud_from_freq(word_counts, "shooter_mental_illness_wordcloud.png")
