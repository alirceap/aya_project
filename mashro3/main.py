import csv
from hash_tree import build_merkle_tree

def load_dataset_from_csv(file_path):
    records = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # تعديل بناء السجل حسب الأعمدة الفعلية
            record_str = f"{row['class']},{row['image_count']},{row['avg_width']},{row['avg_height']}"
            records.append(record_str)
    return records

if __name__ == "__main__":
    dataset = load_dataset_from_csv(r"C:\Users\josaL\Downloads\new\mashro3\dataset_stats.csv")
    tree, root = build_merkle_tree(dataset)

    print("🔐 Merkle Root:", root)
    print("\n🌳 Merkle Tree (from root to leaves):")
    for level in tree:
        print(level)
