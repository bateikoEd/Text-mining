# Text-mining

1. Parsing website
2. Classifying news articles
3. Analysing data


# Team Members
- Eduard Bateiko(KA-72) 
- Pavlo Boyko (KA-72)
- Svitlana Zinchenko (KA-72) 
- Eugen Orel (KA-72) 

 
# Description



We want to explore how the number of news about coronavirus has changed from January 1st to the end of quarantine (we may choose shorter period), and plot dependencies (chart or bar chart from January 1st to *) between these news articles and articles on another topics such as economics , politics etc. We will create a spreadsheet contains topics and appropriate words or combinations(selected words does not dependent on the case or plural form, like virus, viruses etc). Every theme will have probability of word found in text(for instance, there is probability about 0.8 to found word “pandemia” in article about coronavirus). Then we will calculate a frequency of words from every topic we are looking for(for example, 0.2 coronavirus, 0.5 economics, 0.2 politics, 0.1 science). And comparing this indicators with probabilities we will make conclusions.


# Target

To develop a classifier of news articles in order to determine what articles concern coronavirus.

# Available sites to use

| Website               | Description                       |
| --------------------- | --------------------------    |
| https://www.bbc.com/ukrainian             | List of different available news articles. This site is the main one to parse data from.          | 
| https://zn.ua/             | Ukrainian news portal, which is easy to parse.                         | 


# Suggested approaches for analysis:
- Parsing news articles on different themes
- Find special phrases(words) that determine articles concern coronavirus
- Build an taxonomy tree as a classification model with a help of Content Categorization studio, also we used a IPTC model as a “ground” model for our project.
- Define rules for every category
- Make some analytics on results of test reports 


# Example chart 

![chart](/Create_charts/Img_carts/2.jpeg)