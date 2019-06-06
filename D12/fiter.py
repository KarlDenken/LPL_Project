import re

def main():
    purify_pattern = '[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔'
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purifed = re.sub(pattern=purify_pattern, repl='*', string=sentence, flags=re.IGNORECASE)
    print(purifed)


if __name__ == '__main__':
    main()
