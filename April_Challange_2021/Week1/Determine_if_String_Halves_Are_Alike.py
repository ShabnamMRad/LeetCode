

class Solution:

    def __init__(self):
        self.vow_ref = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def halvesAreAlike(self, s):

        try:
            str_to_list = list(s)

            if len(str_to_list) < 2 or len(str_to_list) > 1000:
                return "length of string should be 2 <= s.length <= 1000"

            elif int(len(str_to_list)%2) == 0:
                first_half = str_to_list[:int(len(str_to_list) / 2)]
                second_half = str_to_list[int(len(str_to_list) / 2):]

                first_half_vowels_count = 0
                second_half_vowels_count = 0
                for i in range(0, int(len(str_to_list) / 2)):
                    if first_half[i] in self.vow_ref:
                        first_half_vowels_count += 1

                    if second_half[i] in self.vow_ref:
                        second_half_vowels_count += 1

                if first_half_vowels_count == second_half_vowels_count:
                    return True
                else:
                    return False

            else:
                return " length of string in not Even!"

        except TypeError:
            return "s is not a string!"




result = Solution()
print(result.halvesAreAlike("qEEsdABKKK"))



