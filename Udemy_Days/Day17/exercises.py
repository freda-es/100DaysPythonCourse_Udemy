# class User: #the first letter of the name class is Capitalize
#     pass #if you dont want to do enything with this class/function

# user_1  = User() #create an object out of the class
# user_1.id = "001" # adding an attribute to this object /an attribute 
#                 #is a value whitch is associated with this object
#                 #is the same as creating a varibale but attached to an object
# user_1.username = "Freda"
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Dyrkaj"



class User:
    def __init__(self,user_id,username):#init function(method becouse is inside the class) is a special func that python can read it
                        #is used to initialize the attributes, create the strating values for our attributes
                        #user_id, etc inside the func are parametres
            self.id = user_id#initialize the atributes and we can use every name we want, even the same as the prarametres
            self.username = username
            self.followers = 0 # attribute that will change latter on, and we initialize it as a default value
            self.following = 0
 
    def follow (self, user):  #add another method in our class, always want a slef parameter 
                        #we will pass the user that we decide to follow
        user.followers += 1 # eatch account grows by 1 when they follow eatch-other
        self.following += 1
 



user_1 = User("001","Freda")
user_2 = User("002", "Dyrkaj")
user_1.follow(user_2)#user_1 decided to follow user_2
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
