class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                h_bits = bin(h).count('1')
                m_bits = bin(m).count('1')
                if h_bits + m_bits == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res