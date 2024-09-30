import time
import random
from recommendationSystem import RecommendationSystem
import sys

def generate_data(num_users, num_products, num_preferences, num_relations):
    users = [f"user{i}" for i in range(num_users)]
    products = [f"product{i}" for i in range(num_products)]
    
    preferences = [(random.choice(users), random.choice(products), random.uniform(1, 5))
                   for _ in range(num_preferences)]
    
    relations = [(random.choice(products), random.choice(products), random.uniform(0, 1))
                 for _ in range(num_relations)]
    
    return preferences, relations

def run_scalability_test(sizes, output_file):
    results = []
    for size in sizes:
        rec_system = RecommendationSystem()
        
        num_users = size
        num_products = size * 10
        num_preferences = size * 100
        num_relations = size * 50
        
        preferences, relations = generate_data(num_users, num_products, num_preferences, num_relations)
        
        start_time = time.time()
        rec_system.batch_update_preferences(preferences)
        rec_system.batch_update_relations(relations)
        update_time = time.time() - start_time
        
        start_time = time.time()
        for _ in range(100):
            user = f"user{random.randint(0, num_users-1)}"
            rec_system.generate_recommendations(user)
        recommend_time = (time.time() - start_time) / 100
        
        results.append((size, update_time, recommend_time))
        
        output_file.write(f"Size: {size}, Update Time: {update_time:.2f}s, Recommend Time: {recommend_time:.4f}s\n")
    
    return results

# Redirect output to file
with open("output.txt", "w") as output_file:
    # Redirect stdout to the file
    sys.stdout = output_file

    # Run scalability test
    sizes = [1000, 5000, 10000, 50000, 100000]
    results = run_scalability_test(sizes, output_file)

    # Analyze results
    for size, update_time, recommend_time in results:
        output_file.write(f"Size: {size}\n")
        output_file.write(f"  Update Time: {update_time:.2f}s\n")
        output_file.write(f"  Recommend Time: {recommend_time:.4f}s\n")
        output_file.write(f"  Update Time Ratio: {update_time / sizes[0]:.2f}\n")
        output_file.write(f"  Recommend Time Ratio: {recommend_time / results[0][2]:.2f}\n")
        output_file.write("\n")

# Reset stdout
sys.stdout = sys.__stdout__

print("Results have been written to output.txt")