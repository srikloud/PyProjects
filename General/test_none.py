class test():
    def test_none(self):
        #something = 'something'
        something = None
        #something = ' '

        #not = None, 0, '', [],{},(), False, list(), set(), dict(), bytearray(), bytes()
        if not something:
            print('not -- something is None')

        if something == None:
            print('== -- something is None')

        if something is None:
            print('is --something is None')




t = test()
t.test_none()

