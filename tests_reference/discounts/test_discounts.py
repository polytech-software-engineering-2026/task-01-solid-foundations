from tests_reference.conftest import import_solution

PercentageDiscount, FixedAmountDiscount = import_solution(
    "katas.discounts.solution", "PercentageDiscount", "FixedAmountDiscount"
)

from katas.discounts.engine import PriceCalculator  # noqa: E402


def test_percentage_discount() -> None:
    calc = PriceCalculator([PercentageDiscount(0.1)])
    assert calc.total_with_discounts(100) == 90


def test_fixed_amount_discount() -> None:
    calc = PriceCalculator([FixedAmountDiscount(20)])
    assert calc.total_with_discounts(100) == 80


def test_no_rules_returns_original_total() -> None:
    calc = PriceCalculator([])
    assert calc.total_with_discounts(100) == 100


def test_combining_two_rules_without_touching_engine() -> None:
    calc = PriceCalculator([PercentageDiscount(0.1), FixedAmountDiscount(5)])
    # 100 -> 90 (percentage) -> 85 (fixed)
    assert calc.total_with_discounts(100) == 85


def test_total_never_goes_negative() -> None:
    calc = PriceCalculator([FixedAmountDiscount(1000)])
    assert calc.total_with_discounts(100) == 0
