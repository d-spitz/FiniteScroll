#!/usr/bin/env python3
"""
Interactive script to add new cards to the database.
"""

import sqlite3
import sys
from pathlib import Path


def add_card():
    """Interactively add a new card."""
    print("Add a new card to Finite Scroll\n")

    slug = input("Slug (unique-id): ").strip()
    if not slug:
        print("Error: Slug is required")
        return False

    title = input("Title: ").strip()
    if not title:
        print("Error: Title is required")
        return False

    description = input("Description: ").strip()
    if not description:
        print("Error: Description is required")
        return False

    link = input("Link URL: ").strip()
    if not link:
        print("Error: Link is required")
        return False

    link_text = input("Link text (Learn/Read/Explore): ").strip()
    if not link_text:
        link_text = "Learn"

    # Connect to database
    db_path = Path(__file__).parent / 'cards.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO cards (slug, title, description, link, link_text)
            VALUES (?, ?, ?, ?, ?)
        ''', (slug, title, description, link, link_text))

        conn.commit()
        print(f"\n✓ Added card: {title}")
        print(f"  Run 'python3 build.py' to rebuild index.html")
        return True

    except sqlite3.IntegrityError:
        print(f"\n✗ Error: A card with slug '{slug}' already exists")
        return False

    finally:
        conn.close()


if __name__ == '__main__':
    success = add_card()
    sys.exit(0 if success else 1)
