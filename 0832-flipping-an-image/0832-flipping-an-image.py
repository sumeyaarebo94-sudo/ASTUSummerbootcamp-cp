class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:

            # Flip
            row.reverse()

            # Invert
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0

        return image  