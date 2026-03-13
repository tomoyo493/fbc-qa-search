"""
Q&A JSON → Notion用CSV変換
"""
import json
import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

INPUT_FILE = "qa_pairs.json"
OUTPUT_FILE = "qa_for_notion.csv"


def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        qa_pairs = json.load(f)

    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # Header row matching our Notion DB design
        writer.writerow([
            "質問",          # Title (Name)
            "回答",          # Text
            "質問者",        # Select
            "回答者",        # Select
            "日付",          # Date
            "カテゴリ",      # Select
            "Discord元リンク",  # URL
            "回答数"         # Number
        ])

        for qa in qa_pairs:
            # Truncate question for title (Notion title has limits for readability)
            question_title = qa['question'][:100].replace('\n', ' ')
            if len(qa['question']) > 100:
                question_title += "..."

            # Full answer text
            answer = qa['answer']

            # Answer authors (join with comma)
            answer_authors = ", ".join(qa['answer_authors']) if qa['answer_authors'] else ""

            # Category placeholder (empty for now)
            category = ""

            writer.writerow([
                question_title,
                answer,
                qa['question_author'],
                answer_authors,
                qa['date'],
                category,
                qa['discord_url'],
                qa['reply_count']
            ])

    print(f"CSV exported: {OUTPUT_FILE}")
    print(f"Total rows: {len(qa_pairs)}")


if __name__ == '__main__':
    main()
