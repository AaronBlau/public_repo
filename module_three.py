def report():
    ORIGINAL_NUM = 0
    
    
    
    num = 0
    
    originality = {True  : 'This is the original number.',
                   False : 'This is NOT the original number. Edits have been made.'}
    b_is_og = (num == ORIGINAL_NUM)    
    print('module_three: Why hello there!')
    print('    num is {} \n    {}'.format(num, originality[b_is_og]))
    print("    Also, I used to have a typo. Now I don't.")
    return b_is_og
