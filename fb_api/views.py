# Create your views here.
import sha
import facebook
from webob import Request
from zope.interface import implements
from repoze.who.interfaces import IIdentifier

DEFAULT_FIELDS = ['uid', 'name', 'first_name', 'birthday', 'relationship_status',
                  'proxied_email', 'sex', 'hometown_location',
                  'pic', 'pic_big', 'pic_small', 'pic_square']

class Params(dict):
    def __getattr__(self, attr):
        return self.get(attr, '')
    def __html__(self):
        return repr(self)

class Facebook(object):
    implements(IIdentifier)

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def identify(self, environ):
        req = Request(environ)

# initialize the api object
        fbapi = facebook.Facebook(self.api_key, self.secret_key) # init pyfacebook instance
        if fbapi.check_session(req):
            environ['repoze.who.fb'] = fbapi
            user = fbapi.users.getInfo([fbapi.uid], DEFAULT_FIELDS)[0]

            # we used the proxied_email and a generated password to retriave
            # the user from our DB
            user.update(
                login=user['proxied_email'],
                email=user['proxied_email'],
                password=sha.new('%s%s' % (fbapi.uid, self.secret_key)).hexdigest(),
                )

            # we store the facebook data in environ
            environ['repoze.who.fbuser'] = Params(user.items())
            return user

    def remember(self, environ, identity): pass
    def forget(self, environ, identity): pass