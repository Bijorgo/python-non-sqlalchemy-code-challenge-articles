class Article:
    all = [] # store all articles
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        #else:
            #raise ValueError("Title must be a string")
            #this makes the test fail

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instnace of Author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine")

        
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        pass
        # when an attempt to change name is made
        # original name persists
        # no errors due to test requirements

    def articles(self):
        return [article for article in Article.all if article.author == self]
        # returns a list of all the articles an author has written

    def magazines(self):
        return list({article.magazine for article in self.articles()})
        #returns the magazine object for a given article

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        #creates an instance of Article written by this author

    def topic_areas(self):
        if self.articles():
            return list({magazine.category for magazine in self.magazines()})
        else:
            return None
            # returns a unique list of categories of the magazine an author has contributed to
            # if an author has no articles, return None
    

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and ( 2 <= len(name) <= 16 ):
            self._name = name
        #else:
            #raise ValueError("Name must be a string and 2 to 16 (inclusice) charaters long.")
            # this test doesn't seem to like ValueErrors
        

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        #else:
            #raise ValueError("Category must be a non-empty string.")
        

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        # returns a list of all articles the magazine has published
        # must be of type Article

    def contributors(self):
        return list({article.author for article in self.articles()})
        # returns a unique list of authors who have written for this magazine

    def article_titles(self):
        if self.articles():
            return [article.title for article in self.articles()]
        else: 
            return None
        # returns a list of titles (strings) written for this magazine
        #returns None if the magazine has no articles

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            if author in author_count:
                author_count[author] +=1
            else:
                author_count[author] = 1
        result = []
        for author, count in author_count.items():
            if count > 2:
                result.append(author)
        return result if result else None
        # returns a list of authors who have written more than 2 articles for the magazine 
        # must be of type Author
        # Returns None if the magazine has no authors with more than 2 publications 