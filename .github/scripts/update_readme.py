#!/usr/bin/env python3
"""Update README.md with brief descriptions of Jupyter notebook exercises."""

import json
import os
from pathlib import Path


def extract_description(notebook_path):
    """Extract a brief description (max 3 lines) from a Jupyter notebook.

    Prefers markdown cells; falls back to comment lines in code cells.
    """
    with open(notebook_path, encoding="utf-8") as f:
        nb = json.load(f)

    # Prefer markdown cells
    for cell in nb.get("cells", []):
        if cell["cell_type"] == "markdown":
            source = "".join(cell["source"])
            lines = [line for line in source.strip().splitlines() if line.strip()]
            if lines:
                return "\n".join(lines[:3])

    # Fall back to comment lines in code cells
    comments = []
    for cell in nb.get("cells", []):
        if cell["cell_type"] == "code":
            for line in cell["source"]:
                stripped = line.strip()
                if stripped.startswith("#"):
                    comment = stripped[1:].strip()
                    if comment:
                        comments.append(comment)
                if len(comments) >= 3:
                    break
        if len(comments) >= 3:
            break

    if comments:
        return "\n".join(comments[:3])

    return "No description available."


def build_exercises_section(repo_root):
    """Build the exercises section of the README."""
    notebooks_by_folder = {}
    for nb_path in sorted(Path(repo_root).rglob("*.ipynb")):
        parts = nb_path.relative_to(repo_root).parts
        # Skip hidden directories
        if any(p.startswith(".") for p in parts):
            continue
        folder = parts[0] if len(parts) > 1 else "."
        notebooks_by_folder.setdefault(folder, []).append(nb_path)

    if not notebooks_by_folder:
        return ""

    section = "## Exercises\n"
    for folder in sorted(notebooks_by_folder.keys()):
        section += f"\n### {folder}\n"
        for nb_path in sorted(notebooks_by_folder[folder]):
            name = nb_path.stem
            rel_path = nb_path.relative_to(repo_root)
            description = extract_description(nb_path)
            section += f"\n#### [{name}]({rel_path.as_posix()})\n{description}\n"

    return section


def update_readme(repo_root):
    """Update README.md with descriptions of all notebooks."""
    readme_path = Path(repo_root) / "README.md"

    with open(readme_path, encoding="utf-8") as f:
        content = f.read()

    exercises_section = build_exercises_section(repo_root)
    if not exercises_section:
        return

    marker = "## Exercises"
    if marker in content:
        # Replace everything from the marker onwards
        before = content[: content.index(marker)]
        content = before.rstrip() + "\n\n" + exercises_section
    else:
        content = content.rstrip() + "\n\n" + exercises_section

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    repo_root = os.environ.get("GITHUB_WORKSPACE", ".")
    update_readme(repo_root)
