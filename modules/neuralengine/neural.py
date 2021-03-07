import wolframalpha

class Neural(object):

    def __init__(self,access_key='8REQUG-YQ7JGY96T8'):
        self.access_key = access_key
        self.client = wolframalpha.Client(access_key)                       # Initialize and Authenticate
        try:
            test = self.client.query('Test/Attempt')
        except:
            print("Some error occured in nueral engine")
            raise

    def query(self, message):
        try:
            result = self.client.query(message)
            return next(result.results).text

        except:
            print("Some error occured in nueral engine")
            raise
