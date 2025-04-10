class india ():
    def capital (self):
        print("New delhi is the capital of india.")
    def language (self):
        print("Hindi is the most spoken.")    
class usa ():
    def capital (self):
        print("washington is the capital of usa.")
    def language (self):
        print("English is the most spoken.")    
obj_ind=india()
obj_usa=usa()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
