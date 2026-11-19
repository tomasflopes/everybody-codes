from collections import defaultdict


def count_ingredients(ingredients, recipes, seen):
    count = 0
    for ingredient in ingredients:
        if ingredient in seen:
            continue

        seen.add(ingredient)
        count += 1

        if ingredient in recipes:
            count += count_ingredients(recipes[ingredient], recipes, seen)

    return count


def parse_recipes(data: str) -> dict[str, list[str]]:
    recipes = {}
    for line in data.splitlines():
        item, ingredients = line.split(":", 1)
        recipes[item] = ingredients.split(",")
    return recipes


def part_1(data: str) -> str:
    recipes = parse_recipes(data)
    seen = {"NULL"}
    return count_ingredients(recipes["NULL"], recipes, seen)


def part_2(data: str) -> str:
    recipes = parse_recipes(data)
    users = defaultdict(set)

    for item, ingredients in recipes.items():
        for ingredient in ingredients:
            users[ingredient].add(item)

    affected = set()
    pending = ["NULL"]
    while pending:
        ingredient = pending.pop()
        for item in users[ingredient]:
            if item == "NULL": continue

            if item not in affected:
                affected.add(item)
                pending.append(item)

    return len(affected)


def part_3(data: str) -> str:
    recipes = parse_recipes(data)
    users = defaultdict(set)

    for item, ingredients in recipes.items():
        for ingredient in ingredients:
            users[ingredient].add(item)

    s = defaultdict(int)
    for a in ["NULLv1", "NULLv2", "NULLv3"]:
      affected = set()
      pending = [a]
      while pending:
          ingredient = pending.pop()
          for item in users[ingredient]:
              if item == "NULL": continue

              if item not in affected:
                  affected.add(item)
                  pending.append(item)

      for i in affected:
        s[i] += 1

    return sum(count > 1 for count in s.values())


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
