class News:
    '''
    News class to define news Objects
    '''

    def __init__(self,id,name,description,category,url):
        self.id =id
        self.name = name
        self.description = description
        self.category=category
        self.url=url