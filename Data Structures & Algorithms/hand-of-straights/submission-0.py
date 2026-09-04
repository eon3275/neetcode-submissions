class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        for card in sorted(freq):
            if freq[card]>0:
                count = freq[card]
                for next_card in range(card, card+groupSize):
                    if freq[next_card]<count:
                        return False
                    freq[next_card]-=count
        return True