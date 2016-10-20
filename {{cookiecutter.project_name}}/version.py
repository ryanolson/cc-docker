from datetime import datetime

openai = datetime(2016, 8, 15, 0, 0, 0)
version = datetime.now() - openai

#print "{0}.{1:05d}".format(version.days, version.seconds)
print version.days
