import sys

def punctuation(text):
	punct = '.!?,:;)'
	for c in punct:
		text = text.replace(c, ' ' + c)
	text = text.replace('(', '( ')
	return text

line = sys.stdin.readline()
while line:
	line = punctuation(line)
	line = line.replace(' ', '\n')
	sys.stdout.write(line)
	line = sys.stdin.readline()