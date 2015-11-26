__author__ = 'Abhishek'
import csv
import sys
import sklearn.metrics
from sklearn.metrics import mean_squared_error
reviews = dict()
stars = dict()
def evaluate(ratings_actual,ratings_predicted):
    print "The mean square error is "+str(mean_squared_error(ratings_actual,ratings_predicted))
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
def predict_ratings_userwise(trainingfile):
    user_count = {}
    user_average_rating = {}
    with open(trainingfile) as trainingcsv:
        trainingreader = csv.reader(trainingcsv)
        for row in trainingreader:
            user_id = row[0]
            user_rating = row[4]
            if not user_average_rating.has_key(user_id):
                user_average_rating[user_id] = 0
                user_count[user_id] = 0
            user_average_rating[user_id] += int(user_rating)
            user_count[user_id] += 1
        for user_id in user_average_rating.keys():
            user_average_rating[user_id] = int(user_average_rating[user_id]/user_count[user_id])
        return user_average_rating







def predict_ratings_businesswise(trainingfile,business_avg_rating_file):
    business_count = {}
    business_average_rating = {}
    with open(trainingfile) as trainingcsv:
        trainingreader = csv.reader(trainingcsv)
        for row in trainingreader:
            business_id = row[3]
            business_rating = row[4]
            if not business_average_rating.has_key(business_id):
                business_average_rating[business_id] = 0
                business_count[business_id] = 0
            business_average_rating[business_id] += int(business_rating)
            business_count[business_id] += 1
        for business_id in business_average_rating.keys():
            business_average_rating[business_id] = int(business_average_rating[business_id]/business_count[business_id])
        """with open(business_avg_rating_file,"wb") as outputfile:
            writer = csv.writer(outputfile)
            for business_id,business_rating in business_average_rating.items():
                writer.writerows([business_id,str(business_rating)])"""
        return business_average_rating


def main(argv):
    trainingfile = argv[0]
    testfile = argv[1]
    business_average_rating_file = argv[2]
    ratings_actual = []
    ratings_predicted = []
    predicted_business_rating = predict_ratings_businesswise(trainingfile,business_average_rating_file)
    templist = []
    with open(testfile,"rU") as testcsvfile:
        testfilereader = csv.reader(testcsvfile)
        for row in testfilereader:
            business_id = row[3]
            templist.append(business_id)
            if(predicted_business_rating.has_key(business_id)):
                ratings_predicted.append(int(predicted_business_rating[business_id]))
            else:
                ratings_predicted.append(4)
            ratings_actual.append(int(row[4]))
        a = predicted_business_rating.keys()
        b = templist
        print "The common businesses are " + str(len(set(a) & set(b)))


    evaluate(ratings_actual, ratings_predicted)
    #print "this is the mean square error"

if __name__ == "__main__":
    main((sys.argv[1:]))
    """ 1st argument is trainingfile 2nd argument is testfile
        trainingfile = "C:\\Users\\Abhishek\\PycharmProjects\\yelpproject\\src\\Restaurantstraining.csv"
        business_average_rating_file = "C:\\Users\\Abhishek\\PycharmProjects\\yelpproject\\src\\business.csv"
        testfile = "C:\\Users\\Abhishek\\PycharmProjects\\yelpproject\\src\\Restaurantstest.csv"
    """
