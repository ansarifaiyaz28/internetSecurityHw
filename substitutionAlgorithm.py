



strin="hzsrnqc klyy wqc flo mflwf ol zqdn nsoznj wskn lj xzsrbjnf, wzsxz gqv zqhhnf ol ozn glco zlfnco hnlhrn; nsoznj jnrqosdnc lj fnqj kjsnfbc, wzsxz sc xnjoqsfrv gljn efeceqr. zn rsdnb qrlfn sf zsc zlecn sf cqdsrrn jlw, wzsoznj flfn hnfnojqonb. q csfyrn blgncosx cekksxnb ol cnjdn zsg. zn pjnqmkqconb qfb bsfnb qo ozn xrep, qo zlejc gqozngqosxqrrv ksanb, sf ozn cqgn jllg, qo ozn cqgn oqprn, fndnj oqmsfy zsc gnqrc wsoz loznj gngpnjc, gexz rncc pjsfysfy q yenco wsoz zsg; qfb wnfo zlgn qo naqxorv gsbfsyzo, lfrv ol jnosjn qo lfxn ol pnb. zn fndnj ecnb ozn xlcv xzqgpnjc wzsxz ozn jnkljg hjldsbnc klj soc  kqdlejnb gngpnjc. zn hqccnb onf zlejc leo lk ozn ownfov-klej sf cqdsrrn jlw, nsoznj sf crnnhsfy lj gqmsfy zsc olsrno."
dic = {'a':"j", 'c':"s", 'd':"v", 'e':"u", 'n':"e", 'o':"t", 's':"i", 'z':"h", 'q':"a", 'l':"o", 'j':"r",
       'f':"n", 'r':"l", 'g':"m", 'x':"c", 'w':"w", 'k':"f", 'y':"g", 'h':"p", 'p':"b", 'v':"y", 'm':"k", 'b':"d"}
plainText = ""
for i in strin:
    if ord(i)>96:
        plainText = plainText + dic[i]
    else:
        plainText = plainText + i
    #print(dic[chr(i)])
print(plainText)