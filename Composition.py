# ---------- Computer Build System: Composition Demonstration ----------

class CPU:
    def __init__(self, brand, cores):
        self.brand = brand
        self.cores = cores

    def specs(self):
        return f"{self.brand} CPU with {self.cores} cores"


class GPU:
    def __init__(self, brand, memory):
        self.brand = brand
        self.memory = memory

    def specs(self):
        return f"{self.brand} GPU with {self.memory}GB VRAM"


class RAM:
    def __init__(self, size):
        self.size = size

    def specs(self):
        return f"{self.size}GB RAM"


class Computer:
    def __init__(self, cpu, gpu, ram):
        # Composition: Computer has CPU, GPU, and RAM
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram

    def system_specs(self):
        print("Computer Specifications:")
        print(self.cpu.specs())
        print(self.gpu.specs())
        print(self.ram.specs())


# ---------- Try It Out Section ----------
cpu1 = CPU("Intel", 8)
gpu1 = GPU("NVIDIA", 6)
ram1 = RAM(16)

my_pc = Computer(cpu1, gpu1, ram1)
my_pc.system_specs()
"""
| Concept           | Where It Appears                            | Meaning                                 |
| ----------------- | ------------------------------------------- | --------------------------------------- |
| **Class**         | `CPU`, `GPU`, `RAM`, `Computer`             | Blueprint for an object                 |
| **Object**        | `cpu1`, `gpu1`, `ram1`, `my_pc`             | Instance of a class                     |
| **Encapsulation** | Attributes like `self.brand` or `self.size` | Data stored inside objects              |
| **Composition**   | `Computer` has `CPU`, `GPU`, `RAM`          | Class contains other class objects      |
| **Delegation**    | `Computer` calls `self.cpu.specs()`         | One class using another’s functionality |
| **Reusability**   | Components can be reused in other systems   | Promotes modular design                 |
"""
