alp=input()
if(alp>='a'and alp<='z') or (alp>='A' and alp<='Z'):
  if(alp=='A' or alp=='a' or alp=='E' or alp=='e' or alp=='I'
    or alp=='i' or alp=='O' or alp=='o' or alp=='U' or alp=='u'):
     print("Vowel")
  else:
     print("Consonant")
else:
  print("invalid")
