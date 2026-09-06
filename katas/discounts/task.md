## Задача

`engine.py` содержит готовый и **закрытый для изменений** `PriceCalculator`
(получает список правил `DiscountRule` и применяет их по очереди) и
интерфейс `DiscountRule`. Файл защищён: даже если вы его отредактируете
локально, в CI он пересобирается из шаблона — рассчитывайте только на
добавление новых классов в `solution.py`.

Реализуйте в `solution.py` два правила:

```python
class PercentageDiscount:
    def __init__(self, rate: float) -> None: ...  # rate в диапазоне (0, 1)
    def apply(self, total: float) -> float: ...    # total * (1 - rate)


class FixedAmountDiscount:
    def __init__(self, amount: float) -> None: ...
    def apply(self, total: float) -> float: ...    # total - amount
```

## Зачем

`PriceCalculator` не знает заранее, какие скидки к нему подключат —
он работает через интерфейс `DiscountRule`. Добавление нового вида
скидки не требует правки `PriceCalculator` (класс **открыт для
расширения, закрыт для изменения** — Open/Closed Principle). Проверьте
сами: чтобы добавить `FixedAmountDiscount` после `PercentageDiscount`,
вам не понадобилось ни строчки менять в `engine.py`.
