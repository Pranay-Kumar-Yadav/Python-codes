#create threads by extending thread class
#constuctor
from time import sleep
from threading import Thread
videos = ['OOP Syllabus','constructor','destructor','file handling']

class Myclass(Thread):
    def __init__(self, val):
        print("constructor called")
        self.temp = 10
        Thread.__init__(self)

        def compression(self):
            print("Video compression code")

        def run(self):
            a=10
            b=20
            self.compression()
            if self.kid:
                print("Suitable for kids")
            for vid in videos:
                print(f"{vid} started uploading...")
                sleep(1)
                print(f"{vid} uploaded.")
            self.temp=a+b    
t1=Myclass(False)
t1.start()
print("result is", t1.temp)
