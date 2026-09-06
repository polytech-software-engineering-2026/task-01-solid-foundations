from typing import Protocol


class PaymentGateway(Protocol):
    """Контракт платёжного шлюза. Не редактировать — этот файл защищён."""

    def charge(self, amount: float) -> str:
        """Списывает amount, возвращает идентификатор транзакции."""
        ...
