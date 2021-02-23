def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{": 
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balance = False
                    break
            index += 1
            
        if s.is_empty() and is_balanced:
            return True
        else:
            return False