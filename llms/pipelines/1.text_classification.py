from transformers import pipeline

classifier = pipeline("zero-shot-classification", 
                      model="facebook/bart-large-mnli")
output = classifier("Apple Released a new iPhone - iPhone 18 Pro",
    candidate_labels = ["education", "politics", "business"])
print(output)