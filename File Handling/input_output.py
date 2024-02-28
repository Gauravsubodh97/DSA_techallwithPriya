#open the read/write/append and then close
f =open('sample.txt','w')
f.write('Glory to GOD')
f.close()
f =open('sample.txt','w')
f.write('God is greate')

#multiline write
f=open('sample1.txt','w')
f.write('My God Is Greate')
f.write('\nHe always favors me')
f.close()

#append
f =open('sample1.txt','a')
f.write('\n He always favors me')
f.close()

#multiple list items or mutiple line
#writelines()

l =['Jesus','\nMother Marry','\nFather Joseph','\nMoses']

f=open('sample1.txt','w')
f.writelines(l)
f.close()

h ='''God is greate,\nHe loves me,\nHe saves me.'''

f =open('sample.txt','w')
f.writelines(h)
f.close()

