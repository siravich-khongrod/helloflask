import os
from flask import Flask, jsonify, request
import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
	
	
@app.route('/test1', methods=['GET'])
def get_tasks():		
	docs = ['Glimpse is an indexing and query system that allows for search through a file system or document collection quickly. Glimpse is the default search engine in a larger information retrieval system. It has also been used as part of some web based search engines.'
        ,'The main processes in an retrieval system are document indexing, query processing, query evaluation and relevance feedback. Among these, efficient updating of the index is critical in large scale systems.'
        ,'Clusters are created from short snippets of documents retrieved by web search engines which are as good as clusters created from the full text of web documents.']

	docs_token = docs
	for i in range(0,len(docs)):
		docs_token[i] = docs[i].lower()
	porter = nltk.PorterStemmer()
	for i in range(0,3):
		docs_token[i] = word_tokenize(docs_token[i])
		docs_token[i] = [w for w in docs_token[i] if w not in stopwords.words('english')] # filter English stopwords
		docs_token[i] = [porter.stem(tok) for tok in docs_token[i]] # apply stemmer
		docs_token[i] = [w for w in docs_token[i] if w.isalpha()] # filter tokens that contain non-alphabetic character(s)
	if 'id' in request.args:
		id = int(request.args['id'])
		return jsonify({'docs': docs_token[id]})
		
	return jsonify({'docs': docs_token})
	