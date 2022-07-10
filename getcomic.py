import requests, json, os
comicId = 1421

os.chdir(os.path.dirname(__file__))
episodes = json.loads(requests.get(f"https://terra-historicus.hypergryph.com/api/comic/{comicId}").text)["data"]["episodes"][::-1]
for ep in episodes:
	try:
		os.makedirs(ep["shortTitle"] + '-' + ep["title"])
	except Exception:
		pass
	pageNum = len(json.loads(requests.get(f"https://terra-historicus.hypergryph.com/api/comic/{comicId}/episode/{ep['cid']}").text)["data"]["pageInfos"])
	print(ep["cid"], ep["title"], pageNum)
	for i in range(1, 1 + pageNum):
		picUrl = json.loads(requests.get(f"https://terra-historicus.hypergryph.com/api/comic/{comicId}/episode/{ep['cid']}/page?pageNum={i}").text)["data"]["url"]
		picFile = requests.get(picUrl).content
		with open(ep["shortTitle"] + '-' + ep["title"] + '\\' + str(i).rjust(3, '0') + ".jpg", "wb") as f:
			f.write(picFile)