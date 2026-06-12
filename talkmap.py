from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TALKS_DIR = ROOT / "_talks"
STATIC_COORDINATES_PATH = ROOT / "talkmap" / "city_coordinates.json"
TALKS_MAP_PATH = ROOT / "talkmap" / "talks_map.html"


DEFAULT_STATIC_CITY_COORDINATES_RAW = {
    "Banff, Alberta, Canada": {"lat": 51.1784, "lon": -115.5708, "address": "Banff, Alberta, Canada"},
    "Pittsburgh, Pennsylvania, USA": {"lat": 40.4406, "lon": -79.9959, "address": "Pittsburgh, Pennsylvania, USA"},
    "Nanjing, CHINA": {"lat": 32.0603, "lon": 118.7969, "address": "Nanjing, China"},
    "Singapore, SINGAPORE": {"lat": 1.3521, "lon": 103.8198, "address": "Singapore"},
    "Guangzhou, CHINA": {"lat": 23.1291, "lon": 113.2644, "address": "Guangzhou, China"},
    "ShenZhen, CHINA": {"lat": 22.5431, "lon": 114.0579, "address": "Shenzhen, China"},
    "Laramie, WY": {"lat": 41.3114, "lon": -105.5911, "address": "Laramie, Wyoming, USA"},
    "1920 Research Private, Ottawa, Ontario, Canada": {
        "lat": 45.4215,
        "lon": -75.6972,
        "address": "Ottawa, Ontario, Canada",
    },
    "Ottawa, Ontario, Canada": {"lat": 45.4215, "lon": -75.6972, "address": "Ottawa, Ontario, Canada"},
    "Zhuhai, CHINA": {"lat": 22.2710, "lon": 113.5767, "address": "Zhuhai, China"},
}


def _normalize_location(value: str) -> str:
    return ", ".join(part.strip().casefold() for part in value.split(",") if part.strip())


def _coerce_static_city_coordinates(raw_coordinates: dict[str, dict]) -> dict[str, dict[str, float | str]]:
    loaded_coordinates: dict[str, dict[str, float | str]] = {}
    for raw_location, values in raw_coordinates.items():
        loaded_coordinates[_normalize_location(raw_location)] = {
            "lat": float(values["lat"]),
            "lon": float(values["lon"]),
            "address": values.get("address", raw_location),
        }
    return loaded_coordinates


def load_static_city_coordinates(path: Path) -> dict[str, dict[str, float | str]]:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(DEFAULT_STATIC_CITY_COORDINATES_RAW, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        raw_coordinates = DEFAULT_STATIC_CITY_COORDINATES_RAW
    else:
        raw_coordinates = json.loads(path.read_text(encoding="utf-8"))

    return _coerce_static_city_coordinates(raw_coordinates)


STATIC_CITY_COORDINATES = load_static_city_coordinates(STATIC_COORDINATES_PATH)


def _location_candidates(location: str) -> list[str]:
    parts = [part.strip() for part in location.split(",") if part.strip()]
    candidates = [location.strip()]

    if len(parts) >= 3:
        candidates.append(", ".join(parts[-3:]))
    if len(parts) >= 2:
        candidates.append(", ".join(parts[:2]))
    if parts:
        candidates.append(parts[0])

    unique_candidates: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        normalized = _normalize_location(candidate)
        if normalized and normalized not in seen:
            seen.add(normalized)
            unique_candidates.append(candidate)
    return unique_candidates


def _static_location_for(location: str) -> dict[str, float | str] | None:
    for candidate in _location_candidates(location):
        static_location = STATIC_CITY_COORDINATES.get(_normalize_location(candidate))
        if static_location is not None:
            return static_location
    return None


def resolve_location(location: str) -> dict[str, float | str] | None:
    static_location = _static_location_for(location)
    if static_location is not None:
        print(f"Using static city coordinates for '{location}' -> {static_location['address']}")
        return static_location
    return None


def _extract_front_matter_value(text: str, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(?:\"([^\"]+)\"|'([^']+)'|(.+))$", re.MULTILINE)
    match = pattern.search(text)
    if match is None:
        return None

    for group in match.groups():
        if group is not None:
            value = group.strip()
            return value if value else None
    return None


def load_talk_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []

    for path in sorted(TALKS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        location = _extract_front_matter_value(text, "location")
        if not location:
            continue

        title = _extract_front_matter_value(text, "title") or path.stem
        permalink = _extract_front_matter_value(text, "permalink")

        geo_result = resolve_location(location)
        if geo_result is None:
            print(f"No static coordinates found for '{location}'. Add it to talkmap/city_coordinates.json.")
            continue

        records.append(
            {
                "title": title,
                "location": location,
                "permalink": permalink,
                "lat": float(geo_result["lat"]),
                "lon": float(geo_result["lon"]),
                "address": str(geo_result["address"]),
            }
        )

    return records


def _group_records(records: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, float, float], dict[str, object]] = {}
    for record in records:
        key = (str(record["address"]), float(record["lat"]), float(record["lon"]))
        group = grouped.setdefault(
            key,
            {
                "address": str(record["address"]),
                "lat": float(record["lat"]),
                "lon": float(record["lon"]),
                "talks": [],
            },
        )
        group["talks"].append({"title": str(record["title"]), "permalink": record["permalink"]})
    return list(grouped.values())


def _build_hover_html(group: dict[str, object]) -> str:
    talks = group["talks"]
    lines = [f"<b>{html.escape(str(group['address']))}</b>"]
    lines.append(f"Talks: {len(talks)}")
    for talk in talks:
        lines.append(f"- {html.escape(str(talk['title']))}")
    return "<br>".join(lines)


def build_html(records: list[dict[str, object]], output_path: Path) -> None:
    groups = _group_records(records)

    hover_text = [_build_hover_html(group) for group in groups]
    latitudes = [group["lat"] for group in groups]
    longitudes = [group["lon"] for group in groups]
    marker_sizes = [16 + (len(group["talks"]) - 1) * 4 for group in groups]
    labels = [group["address"] for group in groups]

    figure_data = [
        {
            "type": "scattergeo",
            "mode": "markers+text",
            "lat": latitudes,
            "lon": longitudes,
            "text": [str(label).split(",")[0] for label in labels],
            "textposition": "top center",
            "textfont": {"size": 11, "family": "Space Grotesk, sans-serif", "color": "#173042"},
            "hovertemplate": "%{customdata}<extra></extra>",
            "customdata": hover_text,
            "marker": {
                "size": marker_sizes,
                "color": "#d65a31",
                "line": {"color": "#10212b", "width": 1.5},
                "opacity": 0.92,
            },
        }
    ]

    figure_layout = {
        "margin": {"l": 0, "r": 0, "t": 0, "b": 0},
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font": {"family": "Space Grotesk, sans-serif", "color": "#173042"},
        "geo": {
            "scope": "world",
            "projection": {"type": "natural earth"},
            "showland": True,
            "landcolor": "#e7efe8",
            "showocean": True,
            "oceancolor": "#d7e7f0",
            "showlakes": True,
            "lakecolor": "#d7e7f0",
            "showcountries": True,
            "countrycolor": "#93a8a5",
            "coastlinecolor": "#5b7982",
            "bgcolor": "rgba(0,0,0,0)",
        },
    }

    config = {"responsive": True, "displaylogo": False, "scrollZoom": True}
    html_text = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Talk map</title>
  <script src=\"https://cdn.plot.ly/plotly-3.0.1.min.js\"></script>
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
  <link href=\"https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap\" rel=\"stylesheet\" />
  <style>
    :root {{
      color-scheme: light;
      --bg-top: #f8f4ed;
      --bg-bottom: #e7efe8;
      --panel: rgba(255, 255, 255, 0.78);
      --panel-border: rgba(16, 33, 43, 0.12);
      --ink: #173042;
      --muted: #526b72;
      --accent: #d65a31;
    }}

    * {{ box-sizing: border-box; }}

    html, body {{
      margin: 0;
      min-height: 100%;
      background:
        radial-gradient(circle at top left, rgba(214, 90, 49, 0.16), transparent 28%),
        radial-gradient(circle at top right, rgba(83, 133, 109, 0.18), transparent 32%),
        linear-gradient(180deg, var(--bg-top), var(--bg-bottom));
      font-family: \"Space Grotesk\", sans-serif;
      color: var(--ink);
    }}

    body {{ padding: 16px; }}

    .frame {{
      width: min(100%, 1100px);
      margin: 0 auto;
      background: var(--panel);
      border: 1px solid var(--panel-border);
      border-radius: 24px;
      box-shadow: 0 18px 60px rgba(16, 33, 43, 0.12);
      overflow: hidden;
      backdrop-filter: blur(10px);
    }}

    .header {{
      padding: 18px 20px 8px;
    }}

    .eyebrow {{
      margin: 0 0 8px;
      font-size: 12px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--muted);
    }}

    h1 {{
      margin: 0;
      font-size: clamp(1.4rem, 2.4vw, 2rem);
      line-height: 1.1;
    }}

    .subhead {{
      margin: 10px 0 0;
      color: var(--muted);
      line-height: 1.5;
      font-size: 0.95rem;
    }}

    #map {{
      width: 100%;
      height: min(78vh, 720px);
      min-height: 520px;
    }}

    @media (max-width: 720px) {{
      body {{ padding: 8px; }}
      .frame {{ border-radius: 18px; }}
      .header {{ padding: 14px 14px 2px; }}
      #map {{ min-height: 460px; height: 68vh; }}
    }}
  </style>
</head>
<body>
  <main class=\"frame\">
    <header class=\"header\">
      <p class=\"eyebrow\">Academic travel</p>
      <h1>Talk locations</h1>
      <p class=\"subhead\">Hover markers to see talks by city. Drag to pan and use the mouse wheel or trackpad to zoom.</p>
    </header>
    <div id=\"map\"></div>
  </main>
  <script>
    const data = {json.dumps(figure_data, ensure_ascii=False)};
    const layout = {json.dumps(figure_layout, ensure_ascii=False)};
    const config = {json.dumps(config, ensure_ascii=False)};
    Plotly.newPlot('map', data, layout, config);
  </script>
</body>
</html>
"""
    output_path.write_text(html_text, encoding="utf-8")


def main() -> None:
    records = load_talk_records()
    if not records:
        raise SystemExit("No talks with static coordinates were found.")

    TALKS_MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    build_html(records, TALKS_MAP_PATH)
    print(f"Built talks map HTML for {len(records)} talks at {TALKS_MAP_PATH}")


if __name__ == "__main__":
    main()