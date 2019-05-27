import re
def convdic(str):
    import re
    import morse_dictionary as dic
    import jaconv
    #英小文字を大文字に
    if re.match(r"[a-z]",str):
        str=list(str.upper())
        lang=dic.eng
    elif re.match(r"[A-Z]",str):
        str=list(str)
        lang=dic.eng
    #ひらがなをカタカナに(濁点・半濁点分かつ)
    elif re.match(r"[あ-ん]",str):
        str=jaconv.h2z(jaconv.hira2hkata(str))
        str=list(jaconv.hira2kata(str))
        lang=dic.jpn
    elif re.match(r"[ア-ン]",str):
        str=jaconv.h2z(str)
        str=list(str)
        lang=dic.jpn
    #モールス(英日の解釈の選択)
    elif re.match(r"[－・]",str):
        str=str.split()
        lang_d={"0":dic.jpn,"1":dic.eng}
        lang=lang_d["0"]#デフォルトは和文モールスで
    return str,lang
#文からモールス
def convm(str,lang):
    ans=[]
    for i in str:
         ans.append(lang[i])
    return "　".join(ans)
#モールスから文
def convs(str,lang):
    ans=[]
    for i in str:
        print(i)
        ans.append([k for k,v in lang.items() if v==i][0])
    return "".join(ans)

#main()
str=convdic(input())
if re.match(r"[－・]","".join(str[0])):
    print(convs(str[0],str[1]))
else:
    print(convm(str[0],str[1]))