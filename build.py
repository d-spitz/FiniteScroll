#!/usr/bin/env python3
"""
Build script for Finite Scroll.
Generates index.html from index.tmpl and cards.db.
No external dependencies required.
"""

import sqlite3
from pathlib import Path


def generate_card_html(card):
    """Generate HTML for a single card."""
    slug, title, description, link, link_text = card

    return f'''<article class="card" id="{slug}">
        <h2>{title} <a href="#{slug}" class="share-link">🔗</a></h2>
        <p>{description}</p>
        <a href="{link}" target="_blank" rel="noopener noreferrer">→ {link_text}</a>
      </article>'''


def build():
    """Build index.html from template and card data."""
    # Connect to database
    db_path = Path(__file__).parent / 'cards.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read card data
    cursor.execute('SELECT slug, title, description, link, link_text FROM cards ORDER BY id')
    cards = cursor.fetchall()
    conn.close()

    # Generate HTML for all cards
    cards_html = '\n\n'.join(generate_card_html(card) for card in cards)

    # Read template
    template_path = Path(__file__).parent / 'index.tmpl'
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Replace placeholder with cards
    output = template.replace('{{CARDS}}', cards_html)

    # Write output
    output_path = Path(__file__).parent / 'index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f'✓ Built index.html with {len(cards)} cards')


if __name__ == '__main__':
    build()
