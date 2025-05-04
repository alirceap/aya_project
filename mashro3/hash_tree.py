import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkle_tree(records):
    current_level = [hash_data(record) for record in records]
    tree = [current_level]

    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i+1] if i+1 < len(current_level) else left
            combined_hash = hash_data(left + right)
            next_level.append(combined_hash)
        current_level = next_level
        tree.insert(0, current_level)  # بناء الشجرة من الجذر إلى الأوراق

    root = tree[0][0]
    return tree, root
