class Solution:
    def generateTag(self, caption: str) -> str:
        captions = caption.split()
        n = len(captions)
        if n == 0:
            return "#"
            
        tag = "#" + captions[0].lower()
        
        for i in range(1, n):
            tag += captions[i].capitalize()

        return tag[:100]