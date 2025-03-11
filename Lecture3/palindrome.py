def palindrome(query: str) -> bool:
    '''
    Checks the query string and returns whether
    or not it is a palindrome
    :param query: the query to validate
    :return: whether or not the query was a palindrome
    '''
    cleaned_query = ""
    for letter in query: #adds all letters together, removes spaces
        if letter.isalnum():
            cleaned_query += letter
    normalized_query = cleaned_query.lower
    for index in range(len(normalized_query)): #ask chat?
        left = normalized_query[index]
        right = normalized_query[(len(normalized_query)-1)-index]
        
        if left !=right:
            return False
    return True
    
    