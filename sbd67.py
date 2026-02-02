#storing objects into list
class Movie(object):
    def __init__(self,title,mins,hero):
        self.title=title
        self.runtime=mins
        self.hero=hero

    def printer(self):
        print(f"title is : {self.title}\nruntime is: {self.runtime}\nhero is : {self.hero}")
list_of_movies=[]
while True:
    title=input("enter the title of movie:")
    mins=input("enter the runtime of movie:")
    hero=input("enter the name of hero of movie:")
    obj=Movie(title,mins,hero)
    list_of_movies.append(obj)
    print("Movie added into the list")
    ans=input("Do you want to add another movie(y/n)")
    if ans!='y':
         break
    
print("all movies information:")
for obj in list_of_movies:
    obj.printer()