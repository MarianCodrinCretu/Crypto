import numpy
import math
def DFTStatisticalTest(sequence, confidence=0.95, decisionLevel=0.01):
    sequence = [2*int(x)-1 for x in sequence]

    n=len(sequence)

    dftSequence = numpy.fft.fft(sequence)
    sprim = dftSequence[: int(n/2+0.5)]

    m = numpy.abs(sprim)

    T = numpy.sqrt(n*numpy.log(1/(1-confidence)))

    N0 = confidence*n/2

    N1 = len(m[m < T])

    d = (N1-N0)/numpy.sqrt(n*confidence*(1-confidence)/4)

    pValue= math.erfc(numpy.abs(d)/numpy.sqrt(2))
    # return True if we have no clue that the sequence is not random
    # if pValue is less than decisionLevel, then we will return False
    print(pValue)
    return pValue >= decisionLevel

print(DFTStatisticalTest("1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"))

