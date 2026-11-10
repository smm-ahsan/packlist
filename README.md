# PackList

A tiny command-line tool that generates a travel packing checklist based on trip length, trip type and weather.

## Quantity rules

- **Essentials** (always): Passport or ID x1, Phone charger x1, Wallet and cards x1, Medicines x1, Toiletries bag x1.
- **Clothing**:
  - Tops: days + 1, capped at 7
  - Bottoms: days / 2 + 1 (integer division), capped at 4
  - Underwear: days + 1, capped at 10
  - Socks: days + 1, capped at 10
  - Sleepwear: x1
- **Trip type extras**:
  - `beach` adds a Beach section: Swimwear x2, Sunscreen x1, Towel x1, Sunglasses x1
  - `city` adds a City section: Comfortable walking shoes x1, Day bag x1
  - `business` adds a Business section: Formal outfit x1, Blazer x1, Laptop and charger x1, Wrinkle spray x1
  - `mountain` adds a Mountain section: Hiking boots x1, Backpack x1, Water bottle x1, Torch x1
  - `general` adds no extra section
- **Weather extras** (appended to Clothing):
  - `warm`: Light jacket x1, Shorts x2
  - `cold`: Warm coat x1, Gloves x1, Scarf x1, Thermal layers x2
  - `mixed`: Packable jacket x1, Umbrella x1

## Requirements

- Python 3
- Standard library only, nothing to install

## Usage

```bash
python3 packlist.py --days 3 --type beach --weather warm
python3 packlist.py --days 2 --type business --weather cold
```

Options:

- `--days` (required): trip length in days, must be at least 1
- `--type`: `beach`, `city`, `business`, `mountain` or `general` (default: `general`)
- `--weather`: `warm`, `cold` or `mixed` (default: `mixed`)
- `--out`: optional file path; the checklist is also written to that file

See `examples.md` for real captured output.

## License

MIT License, Copyright (c) 2026 Muhammad Ahsan Anwar. See `LICENSE` for the full text.
