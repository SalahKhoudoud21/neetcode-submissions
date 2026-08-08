class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "%^&"
        return ",,,".join(strs) if strs else ""
    def decode(self, s: str) -> List[str]:
        if s == "%^&":
            return []
        return s.split(",,,") if s else [""]
