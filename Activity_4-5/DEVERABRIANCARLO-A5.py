import pandas as pd
import spacy

# Load the SpaCy language model (ensure this is installed with: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Step 1: Load the anomalies_detected_evidence.csv file
input_file = "anomalies_detected_evidence.csv"
df = pd.read_csv(input_file)

# Ensure the message column exists
if 'message' not in df.columns:
    raise ValueError(f"'message' column not found in {input_file}")

# Step 2: Extract entities
extracted_data = []

for index, row in df.iterrows():
    message_text = str(row['message'])  # Ensure text is string
    doc = nlp(message_text)
    for ent in doc.ents:
        extracted_data.append({
            "index": index,               # Row index from original file
            "entity_text": ent.text,      # The actual entity found
            "entity_label": ent.label_    # The type of entity (e.g., PERSON, ORG, GPE)
        })

# Step 3: Convert extracted entities into a DataFrame
entities_df = pd.DataFrame(extracted_data)

# Step 4: Save the extracted entities to a new CSV file
output_file = "extracted_entities.csv"
entities_df.to_csv(output_file, index=False)

print(f"Extraction complete! Found {len(entities_df)} entities. Saved to {output_file}.")
