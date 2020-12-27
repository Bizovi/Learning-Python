"""Playing around with bit operations, might be useful for specific algorithms

Some interesting resources to dive deeper:
    * David MacKay - Information Theory, Bayesian Inference and Neural Networks
    * SantaFe Complexity Explorer - Introduction to Renormalization

Exercise:
    1. A simple int type in Python can be used to represent a bit string.
    2. Ergonomic wrapper around `int` that can be used generically as a sequence of bits 
    3. Make it iterable and implement __getitem__(). 
    4. Reimplement CompressedGene, using the wrapper.

    This is tricky, if we want to achieve something more than syntactic sugar.
    The main issues are scaling, performance and usability (no mental gymnastics on ints)
    Therefore, we would effectively re-implement BitVector.py or bitarray[C] packages.
    https://stackoverflow.com/questions/1227163/what-are-some-common-uses-for-bitarrays
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
        """Add the bits with or in increasing powers, effectively building up the integer
        The bit representation of integer is effectively out compression representation
        """
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
        """The `>>` operator pushes the bits to the right, eliminates last one
        & is the bitwise and, used to get the last 2 nonzero bits

        An intuition:
            Decompress by starting from the smaller digits (low powers), then reverse
            Because encoding pushed bits to the largest powers
        """
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # use the BitSequence
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
        return f"""
            Decoded: {self.decompress()}; 
            compressed size {getsizeof(self.bit_string)};
            original size {getsizeof(self.decompress())};
        """