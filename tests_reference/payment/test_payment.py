import inspect

from tests_reference.conftest import import_solution

OrderService = import_solution("katas.payment.solution", "OrderService")


class FakeGateway:
    def __init__(self, response: str = "txn-1") -> None:
        self.response = response
        self.calls: list[float] = []

    def charge(self, amount: float) -> str:
        self.calls.append(amount)
        return self.response


def test_order_service_delegates_to_injected_gateway() -> None:
    gateway = FakeGateway()
    service = OrderService(gateway)

    result = service.place_order(150.0)

    assert gateway.calls == [150.0]
    assert result == "txn-1"


def test_order_service_uses_whichever_gateway_it_was_given() -> None:
    gateway_a = FakeGateway(response="txn-a")
    gateway_b = FakeGateway(response="txn-b")

    assert OrderService(gateway_a).place_order(10) == "txn-a"
    assert OrderService(gateway_b).place_order(10) == "txn-b"


def test_place_order_can_be_called_multiple_times() -> None:
    gateway = FakeGateway()
    service = OrderService(gateway)

    service.place_order(10)
    service.place_order(20)

    assert gateway.calls == [10, 20]


def test_constructor_accepts_gateway_as_parameter() -> None:
    params = inspect.signature(OrderService.__init__).parameters
    assert "gateway" in params, (
        "OrderService должен принимать gateway через конструктор — см. task.md про DIP"
    )
