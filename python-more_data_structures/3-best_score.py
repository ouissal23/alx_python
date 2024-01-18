def best_score(a_dictionary):
   if a_dictionary == {} or a_dictionary==None:
       return None
   else:
       biggest_value = max(list(a_dictionary.values()))
       for key in a_dictionary:
           if a_dictionary[key]== biggest_value:
               thebest_score= key 
       return thebest_score       
           


