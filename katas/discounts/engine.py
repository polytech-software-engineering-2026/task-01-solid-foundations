from typing import Protocol


class DiscountRule(Protocol):
    """Контракт правила скидки. Не редактировать — файл защищён."""

    def apply(self, total: float) -> float:
        """Возвращает новую сумму после применения скидки к total."""
        ...


class PriceCalculator:
    """Не редактировать — этот класс закрыт для изменений (OCP).

    Расширяется добавлением новых реализаций DiscountRule в solution.py,
    а не правкой этого файла.
    """

    def __init__(self, rules: list[DiscountRule]) -> None:
        self._rules = rules

    def total_with_discounts(self, base_total: float) -> float:
        total = base_total
        for rule in self._rules:
            total = rule.apply(total)
        return max(total, 0.0)
