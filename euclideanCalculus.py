import math

points: list[dict[str, tuple[int, int]]] = [
    {"values1": (4, 2)}, 
    {"values2": (3, 6)}, 
    {"values3": (8, 7)}, 
    {"values4": (1, 9)}, 
    {"values5": (8, 1)}, 
    {"values6": (2, 4)}, 
    {"values7": (3, 1)}, 
    {"values8": (7, 2)}
    ]

distances: list[dict[str, object]] = []

def euclideanDistance(x2: float, x1: float, y2: float, y1: float) -> float:
    d = ( (x2 - x1) ** 2 ) + ( (y2 - y1) ** 2 )
    return math.sqrt(d)

for i, point1 in enumerate(points):
    for value1, (x1, y1) in point1.items():
        for j, point2 in enumerate(points):
            for value2, (x2, y2) in point2.items():
                if i != j:
                    distance = euclideanDistance(x2, x1, y2, y1)
                    distances.append({
                        "value1": f"{value1} : x: {x1} y: {y1}",
                        "value2": f"{value2} : x: {x2} y: {y2} ",
                        "distance": distance 
                    })

minDistance: float = float('inf')
for distance_entry in distances:
    distance = distance_entry["distance"]
    if(minDistance > distance):
        minDistance = distance
  
    
print(minDistance)
    

