from flask import Flask, jsonify , request
import csv


all_movies = []


with open("movies.csv") as f:
    a = csv.reader(f)
    data = list(a)
    all_movies = data[1:]


liked_movies = []
not_liked_movies = []
did_not_watched_movies = []

app = Flask(__name__)


@app.route("/get-movie")

def get_movie():
    return jsonify({
        "data" : all_movies[0],
        "status" : "success"
    })


@app.route("/liked-movie" , methods = ["POST"])

def liked_movie():

    movie = all_movies[0]

    all_movies = all_movies[1:]

    liked_movie.append(movie)

    return jsonify({
        "status" : "success"
    })


# http://127.0.0.1:5000/get-movie

@app.route("/unliked-movie" , methods = ["POST"])

def disliked_movie():

    movie = all_movies[0]

    all_movies = all_movies[1:]

    not_liked_movies.append(movie)

    return jsonify({
        "status" : "success"
    })



@app.route("/did-not-watched-movie" , methods = ["POST"])

def did_not_watched_movies():

    movie = all_movies[0]

    all_movies = all_movies[1:]

    did_not_watched_movies.append(movie)

    return jsonify({
        "status" : "success"
    })

if __name__ == "__main__":
    app.run()


