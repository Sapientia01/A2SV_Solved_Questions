class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ocurence = {}
        result = []
        place_holder = 0
        seeker = 0
        for i,char in enumerate(s):
            last_ocurence[char] = i

        for i ,char in enumerate(s):
            seeker = max(seeker,last_ocurence[char])

            if seeker == i:
                result.append(seeker-place_holder+1)
                place_holder= seeker+ 1

        return  result