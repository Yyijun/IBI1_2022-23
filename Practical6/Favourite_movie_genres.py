#creat a dictionary to record data
movie = {'Comedy':73, 'Action':42, 'Romance':38, 'Fantasy':28, 'Science-fiction':22, 'Horror':19, 'Crime':18, 'Documentary':12, 'History':8, 'War':7}
print(movie)
#import module
import matplotlib.pyplot as plt
#basic data for pie chart
labels = list(movie.keys()) #list the keys in movie and name the list "labels" 
sizes = list(movie.values()) #list the values in movie and name the list "sizes"
#set some arguments ( to prevent labels from overlapping, put all lables outside the pie chart)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', pctdistance=1.1, labeldistance=1.3, shadow=False, startangle=90)
#equal aspect ratio
plt.axis('equal')
plt.show()

movie_genre = 'Comedy' #the variable of the requested genre
print(movie[movie_genre])
