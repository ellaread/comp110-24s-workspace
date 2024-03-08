"""Some functions for my garden plan."""
__author__ = "730487065"


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add a plant to dictionary sorted by kind -- mutate input dict."""
# if the kind is already in the dictionary (flower was already in by kind so i did this.)
    if new_plant_kind in by_kind:  # if the kind is already in the dictionary
        by_kind[new_plant_kind].append(new_plant)

    else:  # if the kind is not already in the dictionary ex fruit 
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)


def add_by_date(by_date: dict[str, list[str]], month: str, new_plant: str) -> None:
    """Add a plant to dictionary sorted by date - mutate input dict."""
    if month in by_date:
        by_date[month].append(new_plant)
    else: 
        by_date[month] = []
        by_date[month].append(new_plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Search both dictionaries and return a list of what types of plants to plant at certain dates."""
    assert kind in plants_by_kind
    assert month in plants_by_date
    kind_lists: list[str] = plants_by_kind[kind]
    month_list: list[str] = plants_by_date[month]
    # go through both lists and find elements that appear in both
    # kind list = marigold, daisy 
    # month list = daisy, rose
    combined_list: list[str] = []
    for plant in kind_lists:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in kind list and month list
                combined_list.append(plant)
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {kind}s to plant in {month}"