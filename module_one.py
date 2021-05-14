

def report():
    ORIGINAL_NUM = 0
    
    num = 0
    originality = {True  : 'This is the original number.',
                   False : 'This is NOT the original number. Edits have been made.'}
    b_is_og = (num == ORIGINAL_NUM)    
    print('module_one: Hello!')
    print('    num is {} \n    {}'.format(num, originality[b_is_og]))
    return b_is_og
    
    
    