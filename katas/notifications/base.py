from typing import Protocol


class Notifier(Protocol):
    """Контракт отправки уведомления. Не редактировать — этот файл защищён."""

    def send(self, message: str, recipient: str) -> bool:
        """Отправляет message получателю recipient.

        Возвращает True, если отправка прошла успешно, False — если не
        удалось (это ожидаемый исход, не ошибка). Бросает ValueError,
        если message или recipient пустые.
        """
        ...
