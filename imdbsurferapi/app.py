import falcon
from imdbsurferapi.resources import MovieResource


api = application = falcon.API()

mr = MovieResource()
api.add_route('/movies', mr)