from flask import Flask, jsonify, request
import itertools
import random
import datetime

app = Flask(__name__)

def generate_distance_matrix(num_cities):
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            distance = random.randint(1, 100)
            distances[i][j] = distance
            distances[j][i] = distance
    return distances

def tsp_brute_force(distances):
    num_cities = len(distances)
    cities = range(num_cities)
    shortest_path = None
    shortest_distance = float('inf')

    for path in itertools.permutations(cities):
        current_distance = 0
        for i in range(num_cities - 1):
            current_distance += distances[path[i]][path[i+1]]
        current_distance += distances[path[-1]][path[0]]

        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = path

    return shortest_path, shortest_distance

@app.route('/api')
def api():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = {
        'message': 'Hello, world!',
        'current_time': current_time
    }
    return jsonify(response)

@app.route('/api/tsp/<int:num_cities>', methods=['GET'])
def tsp(num_cities):
    distances = generate_distance_matrix(num_cities)

    shortest_path, shortest_distance = tsp_brute_force(distances)

    response = {
        'distances': distances,
        'shortest_path': shortest_path,
        'shortest_distance': shortest_distance
    }

    return jsonify(response)