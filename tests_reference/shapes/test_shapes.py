import pytest

from tests_reference.conftest import import_solution

Rectangle, Square = import_solution("katas.shapes.solution", "Rectangle", "Square")


def test_rectangle_area() -> None:
    rect = Rectangle(3, 4)
    assert rect.area() == 12


def test_rectangle_width_and_height_are_independently_mutable() -> None:
    rect = Rectangle(3, 4)
    rect.width = 5
    rect.height = 10
    assert rect.area() == 50


def test_rectangle_zero_dimension() -> None:
    rect = Rectangle(0, 10)
    assert rect.area() == 0


def test_square_area() -> None:
    assert Square(4).area() == 16


def test_square_area_zero_side() -> None:
    assert Square(0).area() == 0


def test_square_is_not_a_rectangle_subclass() -> None:
    assert not issubclass(Square, Rectangle), (
        "Square не должен наследоваться от Rectangle — см. task.md про LSP"
    )


@pytest.mark.parametrize("side", [1, 2.5, 100])
def test_square_area_matches_side_squared(side: float) -> None:
    assert Square(side).area() == side * side
