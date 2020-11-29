"""Playing around with bit operations, might be useful for specific algorithms

Some interesting resources to dive deeper:
    * David MacKay - Information Theory, Bayesian Inference and Neural Networks
    * SantaFe Complexity Explorer - Introduction to Renormalization
"""

from sys import getsizeof


class CompressedGene(object):
    """A class for serializing a sequence of nucleotides into bytes. (f"{my_int :08b}")
    
    An intuition for the compression algorithm:
        input: ACG
        steps:
            A: bs = 1,  bs <<= 2 is    0100, |= 0b00 is    0100, bs = 4
            C: bs = 4,  bs <<= 2 is   10000, |= 0b01 is   10001, bs = 17
            G: bs = 17, bs <<= 2 is 1000100, |= 0b10 is 1000110, bs = 70
    """
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left two bits before adding (4 := 0100)
            if nucleotide == "A":  # change the last two bits to (00, 01, 10, 11)
                self.bit_string |= 0b00  # an or operation
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11  # get just the 2 relevant bits
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits: {bits}")
        return gene[::-1]  # reverses the string, slice backwards
    
    def __str__(self) -> str:
        return self.decompress()