class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for dest in path.split("/"):
            if dest == "..":
                if stack: stack.pop()
            elif dest and dest != ".":
                stack.append(dest)
        return "/" + "/".join(stack)
