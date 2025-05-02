class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        n = len(title)

        for i in range(n):
            if len(title[i]) > 2:
                title[i] = title[i].capitalize()

            else:
                title[i] = title[i].lower()

        return ' '.join(title)