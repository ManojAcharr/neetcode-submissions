class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        boxes = {}
        for s in strs:
            label = "".join(sorted(s))

            if label not in boxes:
                boxes[label] = []
            boxes[label].append(s)
        return list(boxes.values())