#imports
import module_one   as m1
import module_two   as m2
import module_three as m3
import module_four  as m4
from new_feature import showoff


#do stuff in test
def main():
    print('[' + '- '*6 + 'Starting main() in test.py' + ' -'*6 + ']')
    
    m1.report()
    m2.report()
    m3.report()
    m4.report()
    
    showoff()
    
    aa = 0
    
    return aa


if __name__ == "__main__":
    main()
