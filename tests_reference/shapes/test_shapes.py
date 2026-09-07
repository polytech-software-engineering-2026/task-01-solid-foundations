import pytest

from tests_reference.conftest import import_solution

Rectangle, Square, ColoredRectangle = import_solution(
    "katas.shapes.solution", "Rectangle", "Square", "ColoredRectangle"
)


def _make_rectangle_like(cls: type, width: float, height: float):
    if cls is ColoredRectangle:
        return cls(width, height, color="red")
    return cls(width, height)


# Rectangle и ColoredRectangle проходят ОДНИ И ТЕ ЖЕ тесты: ColoredRectangle
# ничего не переопределяет, только добавляет поле color — вот так выглядит
# наследование, не нарушающее LSP.
RECTANGLE_LIKE = [Rectangle, ColoredRectangle]


@pytest.mark.parametrize("cls", RECTANGLE_LIKE)
def test_rectangle_contract_area(cls: type) -> None:
    assert _make_rectangle_like(cls, 3, 4).area() == 12


@pytest.mark.parametrize("cls", RECTANGLE_LIKE)
def test_rectangle_contract_width_and_height_are_independently_mutable(cls: type) -> None:
    rect = _make_rectangle_like(cls, 3, 4)
    rect.width = 5
    rect.height = 10
    assert rect.area() == 50


@pytest.mark.parametrize("cls", RECTANGLE_LIKE)
def test_rectangle_contract_zero_dimension(cls: type) -> None:
    assert _make_rectangle_like(cls, 0, 10).area() == 0


def test_colored_rectangle_keeps_its_own_field() -> None:
    rect = ColoredRectangle(3, 4, color="blue")
    assert rect.color == "blue"
    assert rect.area() == 12


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
