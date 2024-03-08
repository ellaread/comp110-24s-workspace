"""Test my garden functions."""
__author__ = "730487065"
from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_from_empty_kind() -> None:  # Edge Case
    """Add a plant to a plant kind that already exists in by_kind, but is empty."""
    by_kind = {'flower': ['rose', 'tulip'], 'tree': []}
    new_plant_kind = 'tree'
    new_plant = 'oak'
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {'flower': ['rose', 'tulip'], 'tree': ['oak']}


def test_add_new_kind() -> None:  # Expected use case 
    """Test that when a new kind of plant is added the function adds a new kind."""
    by_kind = {'flower': ['rose', 'tulip']}
    new_plant_kind = 'fruit'
    new_plant = 'apple'
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {'flower': ['rose', 'tulip'], 'fruit': ['apple']}


def test_add_new_plant_and_kind() -> None:   # Expected use... adding a new kind and a new plant to the empty string.
    """Add new kinds when the existing dictionary is empty."""
    by_kind = {}
    new_plant_kind = 'tree'
    new_plant = 'oak', 'spruce', 'apple'
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {'tree': [('oak', 'spruce', 'apple')]}


def test_empty_dict_date() -> None:  # Edge case.
    """Function to test functionality when strings are empty."""
    by_date = {}
    month = ""
    new_plant = ""
    add_by_date(by_date, month, new_plant)
    assert by_date == {"": [""]}

   
def test_add_date() -> None:  # Expected use case 
    """Test functionality when adding new date."""
    by_date = {'March': ['zinnia', 'poppy'], 'April': ['daisy', 'daffodil']}
    month = 'May'
    new_plant = 'globe amaranth'
    add_by_date(by_date, month, new_plant)
    assert by_date[month] == ['globe amaranth']


def test_empty_kind_lookup() -> None:  # Edge Case.
    """Test functionality when the plant kind dictionary is empty."""
    plants_by_kind = {'flowers': ['rose', 'lily'], 'tree': ['oak', 'maple']}
    plants_by_date = {'January': ['sunflower', 'daisy'], 'February': ['lily', 'maple']}
    kind = 'flowers'
    month = 'January'
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month) == f"No {kind}s to plant in {month}"


def test_matching_lookup() -> None:  # Expected Use Case.
    """Test that function matches kind and month correctly."""
    plants_by_kind = {'flowers': ['rose', 'petunia', 'lily'], 'tree': ['oak', 'hickory', 'maple']}
    plants_by_date = {'February': ['rose', 'hickory', 'lily'], 'March': ['oak', 'petunia', 'maple', 'magnolia']}
    kind = 'tree'
    month = 'March'
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month) == f"{kind}s to plant in {month}: {['oak', 'maple']}"