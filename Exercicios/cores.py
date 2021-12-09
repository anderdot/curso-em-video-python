from enum import Enum

class cor(Enum):
    reset       = '\033[m'
    branco      = '\033[30m'
    vermelho    = '\033[31m'
    verde       = '\033[32m'
    amarelo     = '\033[33m'
    azul        = '\033[34m'
    roxo        = '\033[35m'
    anil        = '\033[36m'
    cinza       = '\033[37m'

    def __str__(self):
        return self.value
