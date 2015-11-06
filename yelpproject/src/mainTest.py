__author__ = 'Abhishek'
import csv
import sklearn.metrics
from sklearn.metrics import mean_squared_error
reviews = dict()
stars = dict()
def evaluate(ratings_actual,ratings_predicted):
    print "The mean square error is "+mean_squared_error(ratings_actual,ratings_predicted)
def manage_input(csvfile):
    #make dictionary of reviews
    with open(csvfile,'rb') as datacsv:
        yelpreader = csv.reader(datacsv)
        for rows in yelpreader:
            review_id = rows[1]
            text = rows[2]
            reviews[review_id]=text
    #make dictionary of stars
    with open(csvfile,'rb') as datacsv:
        yelpreader = csv.reader(datacsv)
        for rows in yelpreader:
            review_id = rows[1]
            stars = rows[2]
            reviews[review_id] = stars




def main():

    ratings_actual = []
    ratings_predicted = []
    print evaluate(ratings_actual, ratings_predicted)
    print "this is the mean square error"

if __name__ == "__main__": main()