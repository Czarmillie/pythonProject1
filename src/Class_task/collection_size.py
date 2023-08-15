def get_collection_size(collection):
    counter = 0
    for _ in collection:
        counter += 1

    return counter

collections = [30, 78, 96, 100, 85, 46, 89]
print(get_collection_size(collections))
