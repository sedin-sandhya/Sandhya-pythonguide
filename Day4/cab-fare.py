# Build a fare caching system for a cab app. 
# Fares are stored in a HashMap keyed by route (e.g. "Pune->Mumbai"). On a new request: 
# If route exists in cache → return instantly (cache HIT) 
# If not → calculate fare, store it, return it (cache MISS) 
# Also track search frequency and show top 3 most-searched routes. 

class FareCache:
    RATE_PER_KM = 12

    def __init__(self):

        self.cache = {}
        self.frequency = {}
        self.distances = {
            "Pune->Mumbai": 148,
            "Pune->Nashik": 210,
            "Mumbai->Pune": 148,
            "Pune->Nagpur": 720
        }

    def search(self, route):

        if route not in self.frequency:
            self.frequency[route] = 0
        self.frequency[route] += 1

        if route in self.cache:
            fare = self.cache[route]
            print(f"HIT - Rs.{fare:,} (instant)")
            return fare

        if route not in self.distances:
            print("Route not found")
            return None
        
        distance = self.distances[route]
        fare = distance * self.RATE_PER_KM

        self.cache[route] = fare
        print(f"MISS - Rs.{fare:,} [saved to cache]")
        return fare
    
    def top_routes(self, n):

        sorted_routes = sorted(
            self.frequency.items(),
            key = lambda x: x[1],
            reverse = True
        )

        print()
        print("Top Routes:")

        for i, (route, count) in enumerate(
            sorted_routes[:n], start = 1
            ):

            print(f"{i}. {route} (searched {count}x)")

    def clear_cache(self):
        self.cache.clear()
        print("Cache cleared")

def main():
    fc = FareCache()

    fc.search("Pune->Mumbai")
    fc.search("Pune->Mumbai")
    fc.search("Pune->Nashik")
    fc.search("Pune->Mumbai")

    fc.top_routes(3)

    fc.clear_cache()

    fc.top_routes(3)

if __name__ == "__main__":
    main()