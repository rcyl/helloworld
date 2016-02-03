import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = '/text/plain'
		self.repsonse.write('Hello, World!')

app = webapp2.WSGOApplication([ 
	('/', MainPage), 
	],debug=True) 