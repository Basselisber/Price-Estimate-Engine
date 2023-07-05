from abc import ABC, abstractmethod

class LogicGate(ABC):
    def __init__(self,n,inputs):
        self.label = n
        self.inputs = inputs
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.gateLogic()
        return self.output
    def setInput(self,inputs):
        self.inputs = inputs
    def getInputs(self):
        return self.inputs
    @abstractmethod
    def gateLogic(self):
        pass

class AND_Gate(LogicGate):
    def gateLogic(self):
        if len(self.inputs) == 2:
            a = self.inputs[0]
            b = self.inputs[1]
            return a & b
        else:
            raise ValueError("And Gate requires exactly 2 inputs.")   
class OR_Gate(LogicGate):
    def gateLogic(self):
        if len(self.inputs) == 2:
            a = self.inputs[0]
            b = self.inputs[1]
            return a | b
        else:
            raise ValueError("Or Gate requires exactly 2 inputs.")
class NOT_Gate(LogicGate):
    def gateLogic(self):
        if len(self.inputs) == 1:
            a = self.inputs[0]
            return not a
        else:
            raise ValueError("Not Gate requires exactly 1 input.") 
class XOR_Gate(LogicGate):
    def gateLogic(self):
        if len(self.inputs) == 2:
            a = self.inputs[0]
            b = self.inputs[1]
            return a ^ b
        else:
            raise ValueError("Xor Gate requires exactly 2 inputs.")
class Circuit():
    def __init__(self):
        self.gates = []
    

        
gate1 = AND_Gate("G",[False,True])
gate2 = NOT_Gate("G",[gate1.getOutput()])
# print(gate1.getOutput())
# print(gate1.getInputs())
# gate1.setInput([True,True])
# print(gate1.getOutput())
# print(gate1.getInputs())
# print(gate1.getLabel())
print(gate2.getOutput())
