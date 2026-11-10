#!/usr/bin/env python3
"""PackList - generate a travel packing checklist.

Builds a sectioned packing checklist from trip length, trip type and
weather. Python standard library only.
"""

import argparse


def build_sections(days, trip_type, weather):
    sections = []

    essentials = [
        ("Passport or ID", 1),
        ("Phone charger", 1),
        ("Wallet and cards", 1),
        ("Medicines", 1),
        ("Toiletries bag", 1),
    ]
    sections.append(("Essentials", essentials))

    clothing = [
        ("Tops", min(days + 1, 7)),
        ("Bottoms", min(days // 2 + 1, 4)),
        ("Underwear", min(days + 1, 10)),
        ("Socks", min(days + 1, 10)),
        ("Sleepwear", 1),
    ]
    if weather == "warm":
        clothing += [("Light jacket", 1), ("Shorts", 2)]
    elif weather == "cold":
        clothing += [
            ("Warm coat", 1),
            ("Gloves", 1),
            ("Scarf", 1),
            ("Thermal layers", 2),
        ]
    elif weather == "mixed":
        clothing += [("Packable jacket", 1), ("Umbrella", 1)]
    sections.append(("Clothing", clothing))

    extras = {
        "beach": (
            "Beach",
            [("Swimwear", 2), ("Sunscreen", 1), ("Towel", 1), ("Sunglasses", 1)],
        ),
        "city": (
            "City",
            [("Comfortable walking shoes", 1), ("Day bag", 1)],
        ),
        "business": (
            "Business",
            [
                ("Formal outfit", 1),
                ("Blazer", 1),
                ("Laptop and charger", 1),
                ("Wrinkle spray", 1),
            ],
        ),
        "mountain": (
            "Mountain",
            [
                ("Hiking boots", 1),
                ("Backpack", 1),
                ("Water bottle", 1),
                ("Torch", 1),
            ],
        ),
    }
    if trip_type in extras:
        sections.append(extras[trip_type])

    return sections


def render(sections):
    blocks = []
    for name, items in sections:
        lines = ["## " + name]
        lines += ["[ ] {} x{}".format(item, qty) for item, qty in items]
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Generate a travel packing checklist."
    )
    parser.add_argument(
        "--days", type=int, required=True, help="Trip length in days"
    )
    parser.add_argument(
        "--type",
        choices=["beach", "city", "business", "mountain", "general"],
        default="general",
        help="Trip type (default: general)",
    )
    parser.add_argument(
        "--weather",
        choices=["warm", "cold", "mixed"],
        default="mixed",
        help="Expected weather (default: mixed)",
    )
    parser.add_argument(
        "--out", help="Also save the checklist to this file path"
    )
    args = parser.parse_args()

    if args.days < 1:
        parser.error("--days must be at least 1")

    text = render(build_sections(args.days, args.type, args.weather))
    print(text, end="")
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("Saved to {}".format(args.out))


if __name__ == "__main__":
    main()
