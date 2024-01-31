#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
print("=======")

my_cache.print_cache()
print("=======")

my_cache.put("E", "Battery")
print("=======")

my_cache.print_cache()
print("=======")

my_cache.put("C", "Street")
print("=======")

my_cache.print_cache()
print("=======")

my_cache.put("F", "Mission")
print("=======")

my_cache.print_cache()
