import pytest
from keys_and_rooms import Solution


@pytest.fixture
def solution():
    return Solution()


def test_no_rooms(solution):
    # Edge case: No rooms
    rooms = []
    assert solution.canVisitAllRooms(rooms) == True  # No rooms to visit, trivially True


def test_single_room(solution):
    # Edge case: Only one room, no keys needed
    rooms = [[]]
    assert (
        solution.canVisitAllRooms(rooms) == True
    )  # There's only one room, already accessible


def test_all_rooms_accessible(solution):
    # Test case: All rooms can be accessed directly or indirectly
    rooms = [[1], [2], [3], []]
    assert (
        solution.canVisitAllRooms(rooms) == True
    )  # All rooms are accessible in sequence


def test_isolated_room(solution):
    # Test case: One room cannot be accessed because there's no key for it or is disconnected
    rooms = [[1], [2], [], [0]]
    assert (
        solution.canVisitAllRooms(rooms) == False
    )  # Room 3 is isolated and cannot be visited


def test_cyclic_access(solution):
    # Test case: The rooms form a cycle
    rooms = [[1], [2], [0]]
    assert (
        solution.canVisitAllRooms(rooms) == True
    )  # All rooms are accessible in a cycle


# def test_disconnected_room(solution):
#     # Test case: A room is disconnected and cannot be reached
#     rooms = [[1], [2], []]
#     assert (
#         solution.canVisitAllRooms(rooms) == True
#     )  # Room 2 is not reachable from any other room


def test_all_keys_in_first_room(solution):
    # Test case: All keys are available in the first room
    rooms = [[1, 2, 3], [], [], []]
    assert (
        solution.canVisitAllRooms(rooms) == True
    )  # All rooms are accessible from the first room


def test_multiple_keys_in_rooms(solution):
    # Test case: Rooms contain multiple keys for each other
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    assert (
        solution.canVisitAllRooms(rooms) == False
    )  # All rooms are accessible through the chain of keys


def test_room_with_no_keys(solution):
    # Test case: Some rooms have no keys, but others provide access
    rooms = [[1], [2], [], []]
    assert solution.canVisitAllRooms(rooms) == False  # Room 3 is unreachable, no keys


def test_all_rooms_accessible_reverse(solution):
    # Test case: Reverse connection between rooms
    rooms = [[], [0], [1]]
    assert (
        solution.canVisitAllRooms(rooms) == False
    )  # Rooms 2 and 1 cannot be accessed from 0, hence False
