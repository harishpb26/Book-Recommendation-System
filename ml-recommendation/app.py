from flask import Flask, render_template, url_for, request, jsonify
import json
import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
from urllib.parse import unquote


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)
db.create_all()

# Load the data from the db
# books df
books_db = db.session.execute('select * from Books LIMIT 1000')
books = DataFrame(books_db.fetchall())
books.columns = books_db.keys()
#print(books.head())
#print(books.shape)

# ratings df
ratings_db = db.session.execute('select * from ratings LIMIT 1000')
ratings = DataFrame(ratings_db.fetchall())
ratings.columns = ratings_db.keys()
#print(ratings.head())
#print(ratings.shape)

# book_tags df
book_tags_db = db.session.execute('select * from book_tags LIMIT 1000')
book_tags = DataFrame(book_tags_db.fetchall())
book_tags.columns = book_tags_db.keys()
#print(book_tags.head())
#print(book_tags.shape)

# tags_db df
tags_db = db.session.execute('select * from tags LIMIT 1000')
tags = DataFrame(tags_db.fetchall())
tags.columns = tags_db.keys()
#print(tags.head())
#print(tags.shape)

# Function that get book recommendations based on the cosine similarity score
def authors_recommendations(title, indices, titles, ratings, cosine_sim, ids, images):
    print("inside the function", title)
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    book_indices = [i[0] for i in sim_scores]
    print(titles.iloc[book_indices])
    t = titles.iloc[book_indices].tolist()
    #print(t)
    r = ratings.iloc[book_indices].tolist()
    i = ids.iloc[book_indices].tolist()
    img = images.iloc[book_indices].tolist()
    l = list()
    for k in range(len(t)):
        d = dict()
        d["title"] = t[k]
        d["average_rating"] = r[k]
        d["book_id"] = i[k]
        d["image_url"] = img[k]
        l.append(d)
    print(l[0])
    return l

@app.route('/recommend/<toRecommendTitle>')
def recommendation(toRecommendTitle):
    print("Inside recommendation function title to recommend is", toRecommendTitle)

    # Build a 1-D arr
    titles = books['title']
    ratings = books['average_rating']
    ids = books['book_id']
    images = books['image_url']
    indices = pd.Series(books.index, index=books['title'])

    # TfidfVectorizer function that transforms text to feature vectors then used input to estimator
    # used Cosine similarity to calculate numeric value that denotes the similarity bet 2 books
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(books['authors'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    #print(cosine_sim)

    recommendations = authors_recommendations(unquote(toRecommendTitle), indices, titles, ratings, cosine_sim, ids, images)
    return jsonify({'books' : recommendations})

b = list()
@app.route('/books', methods=["POST"])
def listallbooks():
    global b
    d = request.get_json()
    index = d["index"]
    size = d["size"]
    print(index, size)
    if(index == 0):
        b = []
    if(index > 999):
        print("done")
        b = []
        return jsonify({"books": ""})
    bookdf = books.iloc[index:index+size]
    #print("inside /books")
    t = bookdf.to_dict()['title']
    i = bookdf.to_dict()['book_id']
    img = bookdf.to_dict()['image_url']
    r = bookdf.to_dict()['average_rating']
    right = index + size
    if(index + size > 1000):
        right = 1000
    for k in range(index, right):
        d = dict()
        d['title'] = t[k]
        d['book_id'] = i[k]
        d['average_rating'] = r[k]
        d['image_url'] = img[k]
        b.append(d)
    time.sleep(0.5)
    return jsonify({'books': b})

@app.route('/add_book', methods=["POST"])
def add_book():
    data = request.get_json()
    print()
    print(type(data["title"]))
    print()
    if(not data["title"] or not data["authors"]):
        return jsonify({"books": ""})
    data["image_url"]='https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png'
    m_id=db.session.execute('select max(id) from books')
    l=[]
    for i in m_id:
    	l.append(i[0])
    m_id=l[0]
    #print(l[0])
    #print(type(l[0]))
    data['id']=m_id+1

    # to find available id
    m_id=db.session.execute('select max(book_id) from books')
    l=[]
    for i in m_id:
    	l.append(i[0])
    m_id=l[0]
    data['book_id']=m_id+1
    # to find available books_id

    # execute insert statement below
    query='INSERT INTO books('
    i=0
    key_l=list(data.keys())
    for key in key_l:
    	if(i==0):
    		query=query+key
    		i=i+1
    	else:
    		query=query+','+key
    query=query+') VALUES('
    i=0
    for key in key_l:
    	if(i==0):
    		if(key=='book_id' or key=='id' or key=='average_rating'):
    			query=query+str(data[key])
    		else:
    			query=query+"\'"+str(data[key])+"\'"
    		i=i+1
    	else:
    		if(key=='book_id' or key=='id' or key=='average_rating'):
    			query=query+','+str(data[key])
    		else:
    			query=query+','+"\'"+str(data[key])+"\'"
    query=query+')'
    print()
    print(query)
    print()
    db.session.execute(query)
    db.session.commit()
    print(data)
    l = []
    l.append(data)
    return jsonify({"books":l})

if __name__ == '__main__':
    app.run(debug=True)
