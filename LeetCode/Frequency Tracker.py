# Question  link: https://leetcode.com/problems/frequency-tracker/description/
class FrequencyTracker:

    def __init__(self):
        self.data = {}
        self.freq = {}


    def changeFreq(self, prev_freq: int, cur_freq: int,) -> None:
        if cur_freq in self.freq:
            self.freq[cur_freq] += 1
        else:
            self.freq[cur_freq] = 1

        if prev_freq in self.freq:
            if self.freq[prev_freq] > 1:
                self.freq[prev_freq] -= 1
            else:
               del self.freq[prev_freq]
  

    def add(self, number: int) -> None:
        prev_freq = 0
        cur_freq = 1
        if number in self.data:
            prev_freq = self.data[number]
            cur_freq = prev_freq + 1
            self.data[number] += 1
        else:
            self.data[number] = 1

        self.changeFreq(prev_freq, cur_freq)
        

    def deleteOne(self, number: int) -> None:
        prev_freq = 0
        cur_freq = 0
        if number in self.data:
            prev_freq = self.data[number]
            if self.data[number] > 1:
                cur_freq = prev_freq - 1
                self.data[number] -= 1
            else:
               del self.data[number]

            self.changeFreq(prev_freq, cur_freq)


    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq