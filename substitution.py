#Substitution cipher decrypt
import math
cipher='lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb'
cipher=cipher.upper()
cipher=cipher.replace(" ","")

cipher_dict=dict(((chr(i+65),0.0) for i in range (26)))
freq_dict=dict((('A',0.08167),('B',0.01492),('C',0.02782),('D',0.04253),('E',0.12702),('F',0.02228),('G',0.02015),('H',0.06094),('I',0.06966),('J',0.00153),('K',0.00772),('L',0.04025),('M',0.02406),('N',0.06749),('O',0.07507),('P',0.01929),('Q',0.00095),('R',0.05987),('S',0.06327),('T',0.09056),('U',0.02758),('V',0.00978),('W',0.02360),('X',0.00150),('Y',0.01974),('Z',0.00074)))
map_dict=dict(((chr(i+65),[]) for i in range (26)))

sta_dev=dict(((chr(i+65),(math.ceil(len(cipher)*freq_dict[chr(i+65)]-3*math.sqrt(len(cipher)*freq_dict[chr(i+65)]*(1-freq_dict[chr(i+65)]))),math.ceil(len(cipher)*freq_dict[chr(i+65)]+3*math.sqrt(len(cipher)*freq_dict[chr(i+65)]*(1-freq_dict[chr(i+65)]))))) for i in range (26)))

for i in range(len(cipher)):
	cipher_dict[cipher[i]]+=1
for i in range(26):
	for j in range(26):
		if (cipher_dict[chr(i+65)]>=sta_dev[chr(j+65)][0] and cipher_dict[chr(i+65)]<=sta_dev[chr(j+65)][1]):
			map_dict[chr(i+65)].append(chr(j+65))

for i in range(26):
	print(chr(i+65),map_dict[chr(i+65)])
