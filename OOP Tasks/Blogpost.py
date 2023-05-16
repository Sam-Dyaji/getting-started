# Create a BlogPost class that has
# an authorName
# a title
# a text
# a publicationDate
# Create a few blog post objects:
# "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
# Lorem ipsum dolor sit amet.
# "Wait but why" titled by Tim Urban posted at "2010.10.10."
# A popular long-form, stick-figure-illustrated blog about almost everything.
# "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
# Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture
# outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.
class Blogpost():
    #initializing method
    def __init__(self, authorName, title, text, publicationDate):
        self.authorName= authorName
        self.title=title
        self.text=text
        self.publicationDate=publicationDate

#Creating objects with the various write ups, authornamr, publication and date
blogpost1=Blogpost("Lorem Ipsum", "John Doe", "Lorem Ipsum dolor sit amet", "2000.05.04")
blogpost2= Blogpost("Wait but why", "Tim Urban", "A popular long-form, stick-figure-illustrated blog about something different", "2010.10.10")
blogpost3= Blogpost("One Enginner is Trying to Get IBM  to Reckon with Trump", "William Turton", "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.","2017.03.28")

# for the first blogpost 
print (blogpost1.authorName)
print (blogpost1.title)
print (blogpost1.text)
print (blogpost1.publicationDate)

# for the seconf blogpost 
print (blogpost2.authorName)
print (blogpost2.title)
print (blogpost2.text)
print (blogpost2.publicationDate)

# for the first blogpost 
print (blogpost3.authorName)
print (blogpost3.title)
print (blogpost3.text)
print (blogpost3.publicationDate)