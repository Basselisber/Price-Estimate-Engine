from abc import abstractmethod, ABC
import enum


class Input(str, enum.Enum):
    A = 'a'
    B = 'b'


class Listener:
    def __init__(self):
        pass

    @abstractmethod
    def output_ready(self, val: int):
        pass


class LogicalGate():
    def __init__(self):
        self.__a = None
        self.__b = None
        self.__c = None
        self.__listeners = []

    def reset(self) -> None:
        self.__a = None
        self.__b = None
        self.__c = None

    def _get_a(self) -> int:
        return self.__a
    def _set_a(self, v: int) -> None:
        self.__a = v
        self.ready()
    a = property(fget=lambda self: self._get_a(),
                 fset=lambda self, v: self._set_a(v))

    def _get_b(self) -> int:
        return self.__b
    def _set_b(self, v: int) -> None:
        self.__b = v
        self.ready()
    b = property(fget=lambda self: self._get_b(),
                 fset=lambda self, v: self._set_b(v))

    def _get_c(self) -> int:
        return self.__c
    def _set_c(self, v: int):
        self.__c = v
    c = property(fget=lambda self: self._get_c())

    def ready(self) -> None:
        if self._is_ready():
            self._compute_output()
            self.__notify_listeners()

    @abstractmethod
    def _is_ready(self) -> bool:
        pass

    @abstractmethod
    def _compute_output(self)-> None:
        pass

    def add_listener(self, lst: Listener) -> None:
        self.__listeners.append(lst)

    def __notify_listeners(self):
        for x in self.__listeners:
            x.output_ready(self.__c)

    @abstractmethod
    def expr(self) -> str:
        pass


class UnaryGate(LogicalGate):
    def __init__(self):
        super().__init__()

    def _set_b(self, v: int) -> None:
        raise Exception("UNARY gates have only one input (a)")

    def _is_ready(self) -> bool:
        return self.a is not None


class NotGate(UnaryGate):
    def __init__(self):
        super().__init__()

    def _compute_output(self)-> None:
        self._set_c(1 if self.a == 0 else 0)

    def expr(self) -> str:
        return f'{chr(256)} = {self.c}'


class BinaryGate(LogicalGate):
    def __init__(self):
        super().__init__()

    def _is_ready(self) -> bool:
        return self.a is not None and self.b is not None


class AndGate(BinaryGate):
    def __init__(self):
        super().__init__()

    def _compute_output(self)-> None:
         self._set_c(1 if self.a == 1 and self.b == 1 else 0)


class OrGate(BinaryGate):
    def __init__(self):
        super().__init__()

    def _compute_output(self)-> None:
        self._set_c(0 if (self.a == 0 and self.b == 0) else 1)


class XOrGate(BinaryGate):
    def __init__(self):
        super().__init__()

    def _compute_output(self)-> None:
        self.c = 0 if self.a == self.b else 1


class Connector(Listener):
    def __init__(self, from_gate: LogicalGate, to_gate: LogicalGate, id_input: Input):
        self.__from_gate = from_gate
        self.__to_gate = to_gate
        self.__input = id_input
        self.__from_gate.add_listener(self)

    @property
    def from_gate(self) -> LogicalGate:
        return self.__from_gate
    
    @from_gate.setter
    def from_gate(self, v: LogicalGate) -> None:
        self.__from_gate = v

    @property
    def to_gate(self) -> LogicalGate:
        return self.__to_gate
    
    @to_gate.setter
    def to_gate(self, v: LogicalGate) -> None:
        self.__to_gate = v

    @property
    def input(self) -> Input:
        return self.__input
    
    @input.setter
    def input(self, v: Input) -> None:
        self.__input = v

    def output_ready(self, val: int):
        if self.__input is Input.A:
            self.__to_gate.a = val
        else:
            self.__to_gate.b = val

# tests
def test_complex():
    ag1 = AndGate()
    ng = NotGate()
    og = OrGate()
    ag2 = AndGate()
    ng2 = NotGate()

    c1 = Connector(ag1, ng, Input.A)
    c2 = Connector(ag1, og, Input.A)
    c3 = Connector(ng, ag2, Input.A)
    c4 = Connector(og, ag2, Input.B)
    c5 = Connector(ag2,ng2, Input.A)

    og.b = 1
    ag1.a = 0
    ag1.b = 1

    print(f'result is {ag2.c}')

test_complex()

