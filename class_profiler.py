#Q2
#Make a data profiler class that takes as params on the _init_ a list of data. 
#Include the followingmethods:
#•get_summary_stats: should calculate the mean, minand max.No parameters are needed in this methodexcept self.
#min_max_scale: converts the array to 0-1 values.
#•zscore_scale: converts the array to zscores.
#Be sure to bind the summary stats and normalized data using self
#Test your class on the below list


b = [1,2,3,4,5,6,7,8,9,10]


class Profiler_class:
    
    def __init__(self, data):
        self.data = []
        for item in data:
            self.data.append(item)
        
    
    def get_summary_stats(self):
        #calc mean, min and max, no params except self
        
        mean_data = sum(self.data)/len(self.data)
        min_data = min(self.data)
        max_data = max(self.data)
        
        return mean_data, min_data, max_data
        
        
    def min_max_scale(self):
        #retrieve mean_data from other method
        mean_data, min_data, max_data = self.get_summary_stats()
        
        #calcuate max-min for array calcuation and make empty list to store data
        max_min = max_data - min_data
        array_list = []
        
        #iterate over list and perform calculation, append to list
        for item in self.data:
            array_list.append((item - min_data)/max_min)
        return array_list
            
        #converts array to 0-1 values
        
        
    def zscore_scale(self):
        #retrieve mean_data from other method
        mean_data, min_data, max_data = self.get_summary_stats()
        
        #calc stdev first, make empty list so that stdev can be calculated, iterate for population stdev 
        stdev_list = []
        for item in self.data:
            stdev_item = (item - mean_data)**2
            stdev_list.append(stdev_item)
         
        mean_stdev = sum(stdev_list)/len(self.data)
        stdev = mean_stdev**(1/2)
        print("stdev:", stdev)
        
        #iterate to make final zscore calulation
        zscore = []
        for item in self.data:
            zscore_item = ((item - mean_data)/stdev)
            zscore.append(zscore_item)
        return zscore
   
    
test = Profiler_class(b)
print("Class test:", test)

values = test.get_summary_stats()
print("Get Summary stats:", values)

test2 = test.min_max_scale()
print("Array:", test2)

test3 = test.zscore_scale()
print("zscore:", test3)


amean, amin, amax = values
#assert(amean == values[0])
