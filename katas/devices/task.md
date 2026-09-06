## Задача

Реализуйте в `solution.py` два класса:

```python
class SimplePrinter:
    def print_doc(self, text: str) -> None: ...


class AllInOnePrinter:
    def print_doc(self, text: str) -> None: ...
    def scan_doc(self) -> str: ...
    def send_fax(self, text: str, number: str) -> None: ...
```

Реальная печать/скан/факс не нужны — методы могут просто ничего не
делать или возвращать заглушечное значение (`scan_doc` — любую строку).
Важно поведение на уровне интерфейса, не результат.

## Требование, которое легко нарушить

**У `SimplePrinter` не должно быть методов `scan_doc` и `send_fax`** —
ни рабочих, ни поднимающих `NotImplementedError`. Если вы объявите один
общий интерфейс `Machine` с методами `print_doc`/`scan_doc`/`send_fax`
и заставите оба класса его реализовывать — `SimplePrinter` окажется
обязан либо притворяться, что умеет сканировать, либо бросать
`NotImplementedError` на вызов метода из своего же интерфейса. Это и
есть нарушение Interface Segregation Principle: класс не должен
зависеть от методов, которые он не использует.

Правильный выход: либо не объявлять общий интерфейс вообще (как в
этом задании), либо разбить его на несколько узких (`Printer`,
`Scanner`, `Fax`) и реализовывать только нужные.
