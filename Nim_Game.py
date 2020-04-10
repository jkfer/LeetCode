# https://leetcode.com/problems/nim-game/
# 292


class Solution:
    def canWinNim(self, n):
        # referred solution
        """
        if the scenario is 4 stones remaining and your turn
        you will lose. SO we must make sure we dont get this scenario
        This scenario can only be created if n%4 == 0
        if n > 0 and n% == 0, since it is your turn and your partner is equally strong,
        you can losesince partner can guide you to have last 4 and your turn
        """
        if n%4 == 0:
            return False
        else:
            return True
