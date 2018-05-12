import requests
#z=input()
x='http://api.screenshotlayer.com/api/capture?access_key=  &url=http://apple.com'#&viewport=1440x900&fullpage=1

r = requests.get(x)
open('apple.jpg', 'wb').write(r.content)


