s = input('enter: ')
def sl(x):
    for i in x:
	    if ord(u'\u0900') <= ord(i) <= ord(u'\u097F'):
		    return True

if sl(s):
    print('hi')
else:
    print('no')