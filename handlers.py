import tornado.web

from google_search import google_search

class HomeHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("search.html")

class SearchHandler(tornado.web.RequestHandler):
	def get(self):
		searchstr = self.get_argument("search_text")
		page = int(self.get_argument("page"))
		rsz = int(self.get_argument("rsz"))
		print 'searching:', searchstr
		results = google_search(searchstr, page, rsz)
		nextpage = 1
		if len(results) >= 8:
			nextpage = page + 1

		self.render("search_results.html", results=results, searchstr = searchstr, page = page, nextpage = nextpage)