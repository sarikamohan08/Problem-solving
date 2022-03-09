class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        for l in s:
            if l == "{" or l == "[" or l == "(":
                left.append(l)

            else:
                if len(left) == 0:
                    return False

                else:

                    if l == "}":
                        if left.pop() == "{":
                            continue
                        else:
                            return False

                    if l == "]":
                        if left.pop() == "[":
                            continue
                        else:
                            return False

                    if l == ")":
                        if left.pop() == "(":
                            continue
                        else:
                            return False

        if len(left) == 0:
            return True
        else:
            return False