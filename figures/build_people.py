"""Aggregate data/experiments_by_year_tag.csv into figures/data/W01_people.json for the W01 timeline tooltips:
    {"2016": {"total": n, "scientists": [...], "by_category": {...}}, ...}
Uses the same year filter and tag-to-category mapping as W01 (exp_year / exp_category in build_figures.py).
Run from the project root:  python figures/build_people.py
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_figures as bf


def main():
    people = collections.defaultdict(set)
    total = collections.Counter()
    cats = collections.defaultdict(collections.Counter)
    for r in bf.load_experiments():  # already excludes _databases
        y = bf.exp_year(r)
        if not y:
            continue
        total[y] += 1
        cats[y][bf.exp_category(r)] += 1
        if r["scientist"].strip():
            people[y].add(r["scientist"].strip())
    out = {str(y): {"total": total[y], "scientists": sorted(people[y]), "by_category": dict(cats[y])} for y in sorted(total)}
    path = os.path.join(bf.DATA, "W01_people.json")
    json.dump(out, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("wrote", path, f"({len(out)} years, {sum(total.values())} experiments)")


if __name__ == "__main__":
    main()
