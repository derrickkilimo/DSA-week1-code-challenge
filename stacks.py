def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

