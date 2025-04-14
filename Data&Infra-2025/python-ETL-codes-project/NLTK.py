#natural language processing
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
import re
import pandas as pd
nltk.download('punkt')


#user defined variables
input_text = 'input_files/service.csv'
text_column = 'response'
output_file = 'output_files/service_clean.csv'


#load the csv file into a pandas dataframe
df = pd.read_csv(input_text)
df = df[[text_column]]

#function to clean the text data
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text
    #loop through the dataframe and clean the text data
for index, row in df.iterrows():
    df.at[index, text_column] = clean_text(row[text_column])

#apply the clean_text function to the text column
df[text_column] = df[text_column].apply(clean_text)

#create dataframe
df['tokenized'] = df[text_column].apply(word_tokenize)
df['stemmed'] = df[text_column].apply(lambda x: [PorterStemmer().stem(word) for word in word_tokenize(x)])
# Save the cleaned data to a new CSV file   
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")
#nltk.download('stopwords') 
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')
