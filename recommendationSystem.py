from graph import Graph
from hashTable import HashTable
from priorityQueue import PriorityQueue
from collections import defaultdict
from math import sqrt

class RecommendationSystem:
    def __init__(self):
        self.user_preferences = HashTable()
        self.product_graph = Graph()
        self.recommendations = PriorityQueue()

    def add_user_preference(self, user_id, product_id, rating):
        user_prefs = self.user_preferences.get(user_id)
        if user_prefs is None:
            user_prefs = {}
        self.user_preferences.insert(user_id, user_prefs)
        user_prefs[product_id] = rating

    def add_product_relation(self, product1, product2, strength):
        self.product_graph.add_edge(product1, product2, strength)

    def cosine_similarity(self, vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        
        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = sqrt(sum1) * sqrt(sum2)
        
        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    def generate_recommendations(self, user_id, top_n=5):
        user_prefs = self.user_preferences.get(user_id)
        if user_prefs is None:
            return []

        candidate_products = set()
        for product in user_prefs:
            candidate_products.update(self.product_graph.get_neighbors(product).keys())
        candidate_products -= set(user_prefs.keys())

        recommendations = []
        for product in candidate_products:
            product_relations = self.product_graph.get_neighbors(product)
            similarity = self.cosine_similarity(user_prefs, product_relations)
            recommendations.append((product, similarity))

        return sorted(recommendations, key=lambda x: x[1], reverse=True)[:top_n]

    def batch_update_preferences(self, preferences):
        for user_id, product_id, rating in preferences:
            self.add_user_preference(user_id, product_id, rating)

    def batch_update_relations(self, relations):
        for product1, product2, strength in relations:
            self.add_product_relation(product1, product2, strength)

    def clear_data(self):
        self.user_preferences = HashTable()
        self.product_graph = Graph()
        self.recommendations = PriorityQueue()