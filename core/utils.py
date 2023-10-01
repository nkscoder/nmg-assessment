def prime(number):
    p=[]
    for num in range(2,number):
        status = True
        for i in range(2,num):
            if num % i == 0:
                status = False
        if status:
            p.append(num)
    return p

print(prime(101))
# ...............................prime number end..................................................................
import sys

INF = sys.maxsize

def floyd_warshall(graph):
    num_vertices = len(graph)
    
    dist = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = INF
    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist



graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

result = floyd_warshall(graph)

for row in result:
    print(row)
    
#  .................................................................................   
from scipy.optimize import minimize

def objective(x):
    a, b = x
    return -0.5 * a * b  

def constraint(x):
    a, b = x
    return 2 * (a + b) - P  

# Given perimeter
P = 20
initial_guess = [1, 1]
bounds = [(0, None), (0, None)]
constraints = {'type': 'eq', 'fun': constraint}
result = minimize(objective, initial_guess, bounds=bounds, constraints=constraints)
optimal_dimensions = result.x
max_area = -result.fun
print(f"Optimal Dimensions (a, b): {optimal_dimensions}")
print(f"Maximum Area: {max_area}")    

