import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# De Vera, Brian Carlo A.
# Step 1: Load the data
# ======================
anomalies_file = "anomalies_detected_evidence.csv"
entities_file = "extracted_entities.csv"

df_anomalies = pd.read_csv(anomalies_file)
df_entities = pd.read_csv(entities_file)

# De Vera, Brian Carlo A.
# Step 2: Summarize findings
# ======================
# Total anomalies
num_anomalies = df_anomalies[df_anomalies["is_anomaly"] == 1].shape[0]

# Count by event type (only anomalies)
anomaly_event_counts = (
    df_anomalies[df_anomalies["is_anomaly"] == 1]["event_type"].value_counts()
)

# Top entities (by label and text)
top_entity_labels = df_entities["entity_label"].value_counts().head(5)
top_entity_texts = df_entities["entity_text"].value_counts().head(5)

# De Vera, Brian Carlo A.
# Step 3: Visualizations
# ======================
plt.style.use("dark_background")  # Dark cosmic background

# --- Timeline of anomalous events ---
if "timestamp" in df_anomalies.columns:
    # Parse timestamp column
    df_anomalies["timestamp"] = pd.to_datetime(df_anomalies["timestamp"], errors="coerce")

    # Filter anomalies only
    anomaly_timeline = df_anomalies[df_anomalies["is_anomaly"] == 1]

    # Group anomalies by date
    anomaly_time_counts = anomaly_timeline.groupby(
        anomaly_timeline["timestamp"].dt.date
    )["event_type"].count()

    # Plot timeline
    plt.figure(figsize=(8, 4), facecolor="white")
    ax = anomaly_time_counts.plot(
        kind="line",
        marker="o",
        color="#D200FF",   # Neon purple line
        linewidth=2
    )

    # White background
    ax.set_facecolor("white")

    # Black outline
    for spine in ax.spines.values():
        spine.set_edgecolor("black")

    plt.title("Anomalous Events Over Time", color="black")
    plt.xlabel("Date", color="black")
    plt.ylabel("Number of Anomalous Events", color="black")
    plt.xticks(rotation=30, ha="right", color="black")
    plt.yticks(color="black")

    plt.tight_layout()
    plt.savefig("anomalous_events_timeline.png", dpi=300, facecolor="white")
    plt.close()

# --- Bar chart for entity labels ---
plt.figure(figsize=(6, 4), facecolor="white")
ax = top_entity_labels.plot(
    kind="bar",
    color="#D200FF",   # Neon purple
    edgecolor="black"
)

# Make plot background white
ax.set_facecolor("white")

# Make box outline (spines) black
for spine in ax.spines.values():
    spine.set_edgecolor("black")

plt.title("Top 5 Extracted Entity Labels", color="black")
plt.xlabel("Entity Label", color="black")
plt.ylabel("Count", color="black")
plt.xticks(rotation=30, ha="right", color="black")
plt.yticks(color="black")

plt.tight_layout()
plt.savefig("entity_distribution.png", dpi=300, facecolor="white")
plt.close()

# De Vera, Brian Carlo A.
# Step 4: Generate Markdown Report
# ======================
with open("forensic_report.md", "w", encoding="utf-8") as f:
    # Title & Date
    f.write("# Forensic Investigation Report\n\n")
    f.write(f"**Date Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    # Executive Summary
    f.write("## Executive Summary\n")
    f.write(
        f"This forensic investigation identified **{num_anomalies} anomalous events** "
        "and extracted multiple key entities from the available evidence. "
        "The analysis highlights suspicious network connections, unauthorized login attempts, "
        "and communications involving sensitive projects.\n\n"
    )

    # Methodology
    f.write("## Methodology\n")
    f.write("The following steps were carried out in this forensic investigation:\n")
    f.write("1. Acquired raw dataset (`raw_evidence.csv`).\n")
    f.write("2. Preprocessed and cleaned data (`cleaned_evidence.csv`).\n")
    f.write("3. Engineered features (`feature_engineered_evidence.csv`).\n")
    f.write("4. Detected anomalies (`anomalies_detected_evidence.csv`).\n")
    f.write("5. Extracted entities (`extracted_entities.csv`).\n\n")

    # Key Findings
    f.write("## Key Findings\n")
    f.write(f"- **Total anomalies detected:** {num_anomalies}\n\n")

    f.write("### Anomalous Event Types\n")
    for event, count in anomaly_event_counts.items():
        f.write(f"- {event}: {count}\n")

    f.write("\n### Top Extracted Entities (Labels)\n")
    for label, count in top_entity_labels.items():
        f.write(f"- {label}: {count}\n")

    f.write("\n### Top Extracted Entities (Texts)\n")
    for text, count in top_entity_texts.items():
        f.write(f"- {text}: {count}\n")

    # Visualizations
    f.write("\n## Visualizations\n")
    f.write("Below are visualizations generated from the analysis:\n\n")
    f.write("### Timeline of Anomalous Events\n")
    f.write("![Anomalous Events Timeline](anomalous_events_timeline.png)\n\n")
    f.write("### Distribution of Entity Labels\n")
    f.write("![Entity Distribution](entity_distribution.png)\n")

print("✅ Forensic report generated with timeline-based anomalies chart: forensic_report.md, anomalous_events_timeline.png, and entity_distribution.png")
